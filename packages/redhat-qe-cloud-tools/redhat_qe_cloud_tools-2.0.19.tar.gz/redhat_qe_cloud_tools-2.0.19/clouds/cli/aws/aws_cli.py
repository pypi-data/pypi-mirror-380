from __future__ import annotations
import multiprocessing
import re
import shlex
from multiprocessing import Queue
from typing import List

from ocp_utilities.utils import run_command
from simple_logger.logger import get_logger

from clouds.aws.aws_utils import (
    delete_all_objects_from_s3_folder,
    delete_bucket,
)
from clouds.aws.session_clients import ec2_client, iam_client, rds_client, s3_client

LOGGER = get_logger(name="aws-nuke-cli")
MAX_ITEMS: int = 1000


def delete_rds_instances(region_name: str) -> bool:
    db_instances = rds_client(region_name=region_name).describe_db_instances()["DBInstances"]
    for db_instance_identifier in db_instances:
        LOGGER.warning(f"DB instance identifier: {db_instance_identifier}")
        # TODO: once we have the contents of db_instance_identifier, update code to delete it update return value
        # aws rds modify-db-instance --no-deletion-protection --db-instance-identifier "${rds}"

    return False


def delete_vpc_peering_connections(region_name: str) -> bool:
    for conn in ec2_client(region_name=region_name).describe_vpc_peering_connections()["VpcPeeringConnections"]:
        LOGGER.warning(f"VPC peering connection: {conn}")
        # TODO: once we have the contents of conn, update code to delete it update return value
        # aws ec2 delete-vpc-peering-connection --vpc-peering-connection-id "${pc}"

    return False


def delete_open_id_connect_providers(region_name: str) -> bool:
    LOGGER.info("Executing delete_open_id_connect_provider")
    _iam_client = iam_client(region_name=region_name)
    for conn in _iam_client.list_open_id_connect_providers()["OpenIDConnectProviderList"]:
        conn_name = conn["Arn"]
        LOGGER.info(f"Delete open id connection provider {conn_name}")
        _iam_client.delete_open_id_connect_provider(OpenIDConnectProviderArn=conn_name)

    return True


def delete_instance_profiles(region_name: str) -> bool:
    LOGGER.info("Executing delete_instance_profiles")
    _iam_client = iam_client(region_name=region_name)
    instance_profiles_dict = _iam_client.list_instance_profiles(MaxItems=MAX_ITEMS)
    for profile in instance_profiles_dict["InstanceProfiles"]:
        profile_name = profile["InstanceProfileName"]
        for role in _iam_client.get_instance_profile(InstanceProfileName=profile_name)["InstanceProfile"]["Roles"]:
            role_name = role["RoleName"]
            LOGGER.info(f"Remove role {role_name} from instance profile {profile_name}")
            _iam_client.remove_role_from_instance_profile(InstanceProfileName=profile_name, RoleName=role_name)
        LOGGER.info(f"Delete Profile {profile_name}")
        _iam_client.delete_instance_profile(InstanceProfileName=profile_name)

    return instance_profiles_dict["IsTruncated"]


def delete_roles(region_name: str) -> bool:
    LOGGER.info("Executing delete_roles")
    _iam_client = iam_client(region_name=region_name)
    roles_dict = _iam_client.list_roles(MaxItems=MAX_ITEMS)
    attached_role_policies_dict = {}
    detached_policy_names_dict = {}
    for role in roles_dict["Roles"]:
        role_name = role["RoleName"]
        if not re.search(
            r"ManagedOpenShift|AWS|OrganizationAccountAccessRole|pco-|RedHatIT|RH-",
            role_name,
        ):
            # Need to iterate over both list_attached_role_policies and list_role_policies
            # For attached policies, we need to detach them using ARN
            attached_role_policies_dict = _iam_client.list_attached_role_policies(RoleName=role_name, MaxItems=1000)
            for attached_policy in attached_role_policies_dict["AttachedPolicies"]:
                attached_policy_name = attached_policy["PolicyName"]
                LOGGER.info(f"Detach policy {attached_policy_name} for role {role_name}")
                _iam_client.detach_role_policy(RoleName=role_name, PolicyArn=attached_policy["PolicyArn"])

            # For detached policies, we need to delete them by name
            detached_policy_names_dict = _iam_client.list_role_policies(RoleName=role_name, MaxItems=1000)
            for detached_policy_name in detached_policy_names_dict["PolicyNames"]:
                LOGGER.info(f"Delete policy {detached_policy_name} for role {role_name}")
                _iam_client.delete_role_policy(RoleName=role_name, PolicyName=detached_policy_name)

            LOGGER.info(f"Delete role {role_name}")
            _iam_client.delete_role(RoleName=role_name)

    return any([
        roles_dict["IsTruncated"],
        attached_role_policies_dict.get("IsTruncated"),
        detached_policy_names_dict.get("IsTruncated"),
    ])


def delete_buckets(region_name: str) -> bool:
    LOGGER.info("Executing delete_buckets")
    _s3_client = s3_client(region_name=region_name)
    buckets_dict = _s3_client.list_buckets(MaxItems=MAX_ITEMS)
    for bucket in buckets_dict["Buckets"]:
        delete_all_objects_from_s3_folder(bucket_name=bucket["Name"], boto_client=_s3_client)
        delete_bucket(bucket_name=bucket["Name"], boto_client=_s3_client)

    return buckets_dict.get("IsTruncated")


def clean_aws_resources(aws_regions: List[str]) -> None:
    rerun_cleanup_regions_list = []
    jobs = []
    cleanup_queue: Queue[str] = multiprocessing.Queue()

    for region in aws_regions:
        job = multiprocessing.Process(
            name=f"--- Clean up {region} ---",
            target=clean_aws_region,
            kwargs={"aws_region": region, "queue": cleanup_queue},
        )
        jobs.append(job)
        job.start()

    while not cleanup_queue.empty():
        rerun_cleanup_regions_list.append(cleanup_queue.get())

    for _job in jobs:
        _job.join()

    if rerun_cleanup_regions_list:
        clean_aws_resources(aws_regions=rerun_cleanup_regions_list)


def clean_aws_region(aws_region: str, queue: Queue[str]) -> None:
    """Deletes AWS resources.

    Deletes open id connector providers, instance profiles and roles.
    (calls rds instances and vpc peerings connections - currently to only log data).
    Runs `cloud-nuke` utility - https://github.com/gruntwork-io/cloud-nuke
    Deletes S2 buckets.
    Adds aws_region to queue in case additional cleanup is needed.

    Args:
        aws_region (str): AWS region name
        queue (Queue): multiprocessing queue to pass result

    """
    LOGGER.info(f"Deleting resources in region {aws_region}")
    rerun_results: List[bool] = [
        delete_rds_instances(region_name=aws_region),
        delete_vpc_peering_connections(region_name=aws_region),
        delete_open_id_connect_providers(region_name=aws_region),
        delete_instance_profiles(region_name=aws_region),
        delete_roles(region_name=aws_region),
    ]
    run_command(command=shlex.split(f"cloud-nuke aws --region {aws_region} --force"))
    rerun_results.append(delete_buckets(region_name=aws_region))

    if any(rerun_results):
        queue.put(aws_region)
