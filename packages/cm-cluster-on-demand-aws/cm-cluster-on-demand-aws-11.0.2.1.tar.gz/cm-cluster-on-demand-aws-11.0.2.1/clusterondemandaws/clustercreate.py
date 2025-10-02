# Copyright (c) 2004-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import collections
import logging
from datetime import datetime

import netaddr
from botocore.exceptions import ClientError

import clusterondemand.clustercreate
import clusterondemand.inbound_traffic_rule as inbound_traffic_rule
from clusterondemand import utils
from clusterondemand.cidr import cidr, must_be_within_cidr
from clusterondemand.clustercreate import validate_inbound_rules
from clusterondemand.clusternameprefix import must_start_with_cod_prefix
from clusterondemand.exceptions import CODException
from clusterondemand.node_definition import NodeDefinition
from clusterondemand.ssh_key import validate_ssh_pub_key
from clusterondemand.summary import SummaryType
from clusterondemand.tags import tags_ns
from clusterondemand.wait_helpers import clusterwaiters_ns, wait_for_cluster
from clusterondemandaws.base import ClusterCommandBase
from clusterondemandaws.summary import AwsSummaryGenerator
from clusterondemandaws.vpc import get_aws_tag
from clusterondemandconfig import ConfigNamespace, config
from clusterondemandconfig.configuration_validation import (
    if_disabled_require_other_paramaters_to_be_disabled,
    if_not_set_requires_other_parameters_to_be_set,
    requires_other_parameters_to_be_set
)

from .awsconnection import create_aws_service_resource
from .cluster import Cluster
from .configuration import awscommon_ns, wait_timeout_ns
from .images import AWSImageSource, findimages_ns
from .vpc import create_in_existing_vpc, create_vpc

log = logging.getLogger("cluster-on-demand")

DEFAULT_DISK_SETUP = """
<diskSetup xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>
  <device>
    <blockdev>/dev/vdb</blockdev>
    <blockdev>/dev/sda</blockdev>
    <blockdev mode='cloud'>/dev/sdb</blockdev>
    <blockdev mode='cloud'>/dev/hdb</blockdev>
    <blockdev mode='cloud'>/dev/vdb</blockdev>
    <blockdev mode='cloud'>/dev/xvdb</blockdev>
    <blockdev mode='cloud'>/dev/xvdf</blockdev>
    <blockdev mode='cloud'>/dev/nvme1n1</blockdev>
    <partition id='a2'>
      <size>max</size>
      <type>linux</type>
      <filesystem>xfs</filesystem>
      <mountPoint>/</mountPoint>
      <mountOptions>defaults,noatime,nodiratime</mountOptions>
    </partition>
  </device>
</diskSetup>
"""

DEFAULT_DISK_SETUP_10_AND_ABOVE = """
<diskSetup xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>
  <device>
    <blockdev>/dev/vdb</blockdev>
    <blockdev>/dev/sda</blockdev>
    <blockdev mode='cloud'>/dev/sdb</blockdev>
    <blockdev mode='cloud'>/dev/hdb</blockdev>
    <blockdev mode='cloud'>/dev/vdb</blockdev>
    <blockdev mode='cloud'>/dev/xvdf</blockdev>
    <partition id='a2'>
      <size>max</size>
      <type>linux</type>
      <filesystem>xfs</filesystem>
      <mountPoint>/</mountPoint>
      <mountOptions>defaults,noatime,nodiratime</mountOptions>
    </partition>
  </device>
</diskSetup>
"""

HR = "---------------------------------------------------------------------"

config_ns = ConfigNamespace("aws.cluster.create", "cluster creation parameters")
config_ns.import_namespace(awscommon_ns)
config_ns.import_namespace(findimages_ns)
config_ns.import_namespace(clusterwaiters_ns)
config_ns.override_imported_parameter("version", default="11.0")
config_ns.import_namespace(clusterondemand.configuration.clustercreate_ns)
config_ns.import_namespace(clusterondemand.configuration.clustercreatename_ns)
config_ns.import_namespace(clusterondemand.configuration.cmd_debug_ns)
config_ns.import_namespace(clusterondemand.configuration.timezone_ns)
config_ns.import_namespace(wait_timeout_ns)
config_ns.import_namespace(tags_ns)
config_ns.override_imported_parameter(
    "head_node_type",
    default="t3.medium",
    help="The instance type must exist in the region you use.")
config_ns.override_imported_parameter(
    "head_node_root_volume_size",
    default=42,
    help="Head node root disk size in GB. Should be bigger than the AMI size.")
config_ns.add_switch_parameter(
    "validate_parameters",
    default=True,
    help=(
        "Validate parameters before creation. This involves doing API calls to the AWS API. "
        "It can be disabled with --no-validate-parameters (use with care)"
    )
)
config_ns.remove_imported_parameter("name")
config_ns.add_enumeration_parameter(
    "name",
    default=[],
    help="Name of the cluster (VPC) to create",
    validation=must_start_with_cod_prefix
)
config_ns.override_imported_parameter(
    "on_error",
    default="ask",
    choices=["ask", "retry", "cleanup", "undo", "abort"],
    help_choices={
        "retry": "try again",
        "cleanup": "destroy only failed clusters",
        "undo": "destroy all clusters (failed and created)",
        "abort": "do nothing and exit"
    }
)
config_ns.add_parameter(
    "store_head_node_ip",
    help_varname="PATH_TO_FILE",
    help=("Once the cluster has been created, store the IP of the headnode in a file."
          " Useful for automation.")
)
config_ns.add_parameter(
    "store_head_node_id",
    help_varname="PATH_TO_FILE",
    help=("Once the cluster has been created, store the instance-id of the headnode in a file."
          " Useful for automation.")
)
config_ns.add_parameter(
    "ssh_key_pair",
    help=("Name of the AWS key pair used to access the headnode; must exist in your "
          "AWS account in the used region."),
    help_section=clusterondemand.configuration.clustercreatepassword_ns.help_section,
    help_varname="NAME",
)
config_ns.override_imported_parameter(
    "ingress_icmp",
    help="CIDR from which to allow ingress ICMP traffic to the head node."
         "Specify 'none' to disable ICMP altogether. Note that you also need to specify "
         "the ICMP rule in the --inbound-network-acl-rule parameter.",
)
config_ns.add_parameter(
    "head_node_image",
    help=("ID of the AMI to use. This value is determined automatically to latest, if"
          " not specified."),
    help_varname="ID"
)
config_ns.add_parameter(
    "head_node_root_volume_type",
    default="gp2",
    help="Head node root volume type"
)
config_ns.add_parameter(
    "head_node_root_volume_iops",
    default=1000,
    help=("IOPS for head node root volume. Should only be used when requesting io1 or io2 volume. AWS can impose a"
          " maximum based on the volume size. Also affects AWS pricing.")
)
config_ns.override_imported_parameter("node_type", default="t3.medium")
config_ns.override_imported_parameter(
    "ssh_pub_key_path", validation=lambda p, c: validate_ssh_pub_key(p, c, allowed_types=None)
)
config_ns.add_parameter(
    "vpc_cidr",
    advanced=True,
    default=cidr("10.0.0.0/16"),
    help=("CIDR range of the VPC. The VPC Subnets must fall within this range. "
          "The widest allowed range is /16."),
    help_varname="CIDR",
    parser=cidr
)
config_ns.add_parameter(
    "public_subnet_cidr",
    advanced=True,
    default=cidr("10.0.0.0/17"),
    help="Must be within the range of 'vpc_cidr'",
    help_varname="CIDR",
    parser=cidr,
    validation=must_be_within_cidr("vpc_cidr")
)
config_ns.add_parameter(
    "private_subnet_cidr",
    advanced=True,
    default=cidr("10.0.128.0/17"),
    help="Must be within the range of 'vpc-cidr'",
    help_varname="CIDR",
    parser=cidr,
    validation=must_be_within_cidr("vpc_cidr")
)

config_ns.add_parameter(
    "clusters",
    default=1,
    help="The amount of clusters to create. Each cluster requires one dedicated VPC.",
)
config_ns.add_parameter(
    "node_disk_setup",
    default=DEFAULT_DISK_SETUP)
config_ns.add_parameter(
    "aws_availability_zone",
    env="AWS_AVAILABILITY_ZONE",
    help=("Name of the AWS availability zone in which the subnet, and all of the VMs,"
          " will be created. When not specified, a random availability zone will be used."
          " Useful when your chosen VM type is not available in all availability zones.")
)
config_ns.add_enumeration_parameter(
    "inbound_network_acl_rule",
    help=("One or several inbound network acl rules for the cluster's head node in one of the following format: "
          f"[src_cidr,]dst_port:{inbound_traffic_rule.TRANSPORT_PROTOCOL},{inbound_traffic_rule.RULE_ACTION},rule_num' "
          f"or '[src_cidr,]{inbound_traffic_rule.ICMP_AND_ALL_PROTOCOL},{inbound_traffic_rule.RULE_ACTION},rule_num', "
          "where port can be a single port or a dash separated range. Supported rule_num: 1 to 32766, "
          f"but {inbound_traffic_rule.RESERVED_NETWORK_ACL_RULE_NUM} is reserved for communication inside a VPC. "
          f"Note: a special variable {inbound_traffic_rule.CLIENT_IP} can be used to substitute src_cidr, in which "
          "case COD client's public IP will be detected and used. Examples: '11.0.0.0/24,20-23:TCP,ALLOW,100' "
          "'443:TCP,ALLOW,200' 'ICMP,ALLOW,500' '10.0.0.0/16,ALL,ALLOW,500' {CLIENT_IP},22:tcp,ALLOW,101 "
          "Empty src_cidr is replaced by 0.0.0.0/0. A DENY all traffic is always existed at the end of all rules. "
          "It is recommended to allow ports 22:TCP, 80:TCP, 443:TCP, 8081:TCP, as well as ephemeral 32768-65535:tcp"),
    type=[inbound_traffic_rule.InboundNetworkACLRule],
)


#################################################################
# Extra documentation for the 'existing-vpc' scenario:
#################################################################
# Some scenarios we're attempting to cover here:
#
# A) Create cluster in a new VPC, and configure internet connectivity in that vpc:
#    this is the traditional cod-aws scenario - creating everything from scratch.
# B) Create cluster in a new VPC, but don't configure Internet connectivity:
#    The user will use e.g. Direct Connect to access the VPC, and doesn't want us
#    to mess with networking (or does not have policy permissions).
#
# C) Create cluster in an **EXISTING** VPC, don't configure the Internet connectivity.
#    The user already has a VPC they want to use. In such case, they typically also already have
#    some sort of connectivity into that VPC, and they don't want us to mess with it.
# D) Create cluster in an **EXISTING** VPC, and configure Internet connectivity in that VPC.
#    Theoretical use case: someone having AWS credentials, the security policy of which which allows them to
#    do anything they want with a VPC they've been allocated by their cloud networking team, EXCEPT for allowing them
#    to create new VPCs.
#    Except for the use case above, it's pretty hard to imagine someone already having
#    a production VPC they want to create a cluster in, but at the same time allowing cod-aws to tweak
#    Internet Connectivity of that VPC.
#    Since this scenario is risky, we have an extra flag user must use to confirm this is what they want.
#
# In all of the above described scenarios "configure Internet connectivity" can be further
# broken down into the following two:
#  - creating and configuring IGW in the VPC (and altering the routes)
#  - assigning the public IP to the head node
# In most cases, both will be either enabled, or disabled, but to cover all the bases, we allow to switch those
# separately.

config_ns.add_parameter(
    "existing_vpc_id",
    advanced=True,
    help="AWS VPC ID of an already existing VPC (format: 'vpc-....'). "
         "When specified, the COD-AWS cluster will be created within this VPC. "
         "Must be used in conjunction with '--existing-subnet-id' flag "
         "(the tool will not be creating any VPC subnets). "
         "Related flags: --existing-subnet-id, --head-node-assign-public-ip, "
         "--configure-igw-in-existing-vpc ",
    help_varname="VPC_ID",
    validation=requires_other_parameters_to_be_set(["existing_subnet_id"])
)

config_ns.add_enumeration_parameter(
    "existing_subnet_id",
    advanced=True,
    help="One or more already existing VPC subnet IDs (format: 'subnet-....'). "
         "The specified subnet(s) must exist within the VPC specified with --existing-vpc-id. "
         "The existing VPC can have one or more subnets. Of those, "
         "at least one subnet must be specified using this flag. "
         "All specified VPC subnets will be configured as Network entities within the BCM cluster "
         "(i.e. it will be possible to create cloud nodes on them). "
         "Subnets not specified at cluster-create-time can be added later on by manually "
         "creating new Network entities. "
         "The first specified VPC subnet will be the one hosting the head node (you cannot change this later). "
         "Compute nodes can be assigned to a different subnet by changing the Network entity of their NIC; this should "
         "be done before first-time powering on (creating) a compute node VM instance.",
    help_varname="SUBNET_ID",
    validation=requires_other_parameters_to_be_set(["existing_vpc_id"])
)

config_ns.add_parameter(
    # Technically, AWS calls those "Private IP". But I think in some other places (e.g. cod-os) we call those
    # internal IPs. So, maybe it makes sense to deviate from using per-provider terminology here
    "head_node_internal_ip",
    advanced=True,
    help="The internal/private IP address of the head node on the VPC subnet. "
         "If not specified, the cloud provider will pick this IP address. ",
    help_varname="HEAD_NODE_IP",
    # TODO(cloud-team): validate early that the IP is within the CIDR (otherwise it will fail later)
    #                   (a bit tricky to do when using existing VPC -- you'll have to get CIDR from existing subnet).

)


config_ns.add_switch_parameter(
    "head_node_assign_public_ip",
    default=True,
    advanced=True,
    help="Whether or not the head node will have a public IP address assigned. Enabled by default. "
         "Note that with this flag disabled, it will not be possible out of the box to reach the head node "
         "over the Internet. "
         "Therefore, this flag should only be disabled if there exists some other means to reach "
         "the head node, e.g. via a dedicated "
         "link into the VPC which can be used to access the head node via its internal/private IP address. "
         "Assigning the public IP is not required for the cluster creation to be successful, but not assigning it "
         "in some cases might cause the COD client to time out when waiting for cloud-init to finish. Thus, consider "
         "using '--wait-ssh=0' when disabling this flag. "
         "Related flags: --configure-igw-in-existing-vpc, --configure-igw, --wait-ssh, --wait-cmdaemon"
)


def _validate_user_confirmed_igw():
    def validate(parameter, configuration):
        item = configuration.get_item_for_key(parameter.name)
        if item.value and not configuration.get_item_for_key("i_know_configuring_igw_is_risky").value:
            raise CODException(
                "ATTENTION: Selected configuration asks for creating and configuring an Internet Gateway in an "
                "already existing VPC! This is risky and can break networking in the existing VPC. "
                "E.g. it will alter the routes in the existing VPC, which is rarely desirable. "
                "If you know what you're doing, and you're sure you want to proceed "
                "regardless, please add '--i-know-configuring-igw-is-risky' flag to the CLI. "
                "Alternatively, to not configure the IGW in the existing VPC, make sure that "
                "--configure-igw-in-existing-vpc is not set.")
    return validate


config_ns.add_switch_parameter(
    "configure_igw_in_existing_vpc",
    default=False,
    advanced=True,
    # not adding 'i_know_configuring_igw_is_risky' into the "requires_other..." validation so that we can print more
    # using a custom validation instead
    validation=[
        requires_other_parameters_to_be_set(["existing_vpc_id"]),
        _validate_user_confirmed_igw(),  # we want a dedicated error message here
    ],
    help="By default, when creating the cluster in an existing VPC, the cod-aws tool will "
         "not attempt to configure the Internet access in that VPC by creating and configuring an IGW. "
         "This flag can be used to change this behavior. It may only be used in conjunction with '--existing-vpc-id'. "
)

config_ns.add_switch_parameter(
    "i_know_configuring_igw_is_risky",
    default=False,
    advanced=True,
    validation=requires_other_parameters_to_be_set(["existing_vpc_id", "configure_igw_in_existing_vpc"]),
    help="This flag should be used with caution. "
         "Can only be used with '--existing-vpc-id'. "
         "Must be used with '--configure-igw-in-existing-vpc' to confirm that the user is aware that "
         "allowing cod-aws client to create and configure IGW in "
         "an existing VPC is risky can cause issues. Configuring IGW might result in altering the routes in the VPC, "
         "potentially breaking existing networking connectivity in the VPC, and affecting other existing resources. "
)

config_ns.add_switch_parameter(
    "configure_igw",
    default=True,
    advanced=True,
    help="By default, when creating the cluster in a new VPC, the cod-aws tool will "
         "configure the Internet access in that VPC by creating and configuring an IGW. "
         "Disabling this flag will change this behavior by not creating/configuring any IGW. "
         "The flag should be only be disabled if there exist some other means of accessing the head node's "
         "private IP, e.g. a VPN or a Direct Connect link. "
         "The value of this flag has no effect when creating the cluster in an existing VPC. "
         "Must be used along with '--no-head-node-assign-public-ip'.",
    # There's no point in trying to assign a public IP if we know for a fact there won't be any IGW.
    # Thus, we require the user to explicitly acknowledge that no public IP will be assigned
    validation=if_disabled_require_other_paramaters_to_be_disabled(["head_node_assign_public_ip"])
)

config_ns.add_switch_parameter(
    "configure_nat_gateway",
    default=False,
    advanced=True,
    help="By default, HA clusters will create and route traffic through a NAT gateway for the private subnet. "
         "However, non-HA clusters will use their head node as the gateway for the private subnet. Enabling this "
         "option will require non-HA clusters to also create and route traffic through a NAT gateway for the private"
         " subnet."
)

config_ns.add_parameter(
    "head_node_sg_id",
    advanced=True,
    help_varname="HEAD_NODE_SEC_GROUP_ID",
    help="By default the security group for the head node is created by cod-aws tool. "
         "This optional parameter can be used to change this behavior by providing a pre-created security group ID. "
         "When specifying it, make sure to allow bidirectional access between the head node's SG and node's SG. "
         "If you want to tweak the sec. groups created by the cod-aws tool, use --ingress-rules. "
         "Related parameters: --node-sg-id, --wait-ssh, --wait-cmdaemon",
    validation=requires_other_parameters_to_be_set(["node_sg_id"])
)

config_ns.add_parameter(
    "node_sg_id",
    advanced=True,
    help_varname="NODE_SEC_GROUP_ID",
    help="By default the security group for the compute nodes is created by cm-cod-aws tool. "
         "This optional parameter can be used to change this behavior by providing a pre-created security group ID. "
         "Make sure to allow bidirectional access between the head node's SG and node's SG. "
         "Related parameter: --head-node-sg-id",
    validation=requires_other_parameters_to_be_set(["node_sg_id"])
)
config_ns.add_parameter(
    "head_node_pg_name",
    advanced=True,
    help="Name of the placement group for the head node."
)
config_ns.add_parameter(
    "headnode_instance_profile",
    help_varname="PROFILE",
    help="Instance profile to assign to the head node. Can be specified as short name or full ARN. The cluster will be "
         "configured to obtain credentials from the meta-data endpoint. The values of the --aws-access-key-id and "
         "--aws-secret-key settings will not be used by the head node CMDaemon.",
    validation=if_not_set_requires_other_parameters_to_be_set(["aws_access_key_id", "aws_secret_key"]),
)


def run_command():
    ClusterCreate().run()


def _validate_head_node_ip_in_cidr(ip_orig: str, cidr: str):
    """
    ref: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
    """
    net = netaddr.IPNetwork(cidr)
    ip = netaddr.IPAddress(ip_orig)

    if (ip == net.broadcast) or (ip == net.network):
        raise CODException("The head node IP cannot be neither the network, nor the broadcast address.")

    if ip in [net.network + 1, net.network + 2, net.network + 3]:
        raise CODException(f"The first 3 usable IPs (in this case"
                           f" {[net.network + 1, net.network + 2, net.network + 3]}) of every subnet "
                           f"are reserved by AWS, and cannot be used as a head node IP.")

    if ip not in net:
        raise CODException(f"The specified head node IP {ip_orig} is not within the {cidr} CIDR.")

    return ip in net


class ClusterCreate(ClusterCommandBase):

    def _validate_params(self, names, ec2):
        if config["validate_parameters"]:
            if config["head_node_assign_public_ip"] and not config["head_node_sg_id"]:
                validate_inbound_rules(inbound_rules=config["inbound_rule"])
            self._validate_inbound_network_acl_rule(
                inbound_acl_rules=config["inbound_network_acl_rule"],
                configure_acl_rules=not config["existing_vpc_id"] and config["head_node_assign_public_ip"]
            )
            self._validate_cluster_names_len_and_regex(names)
            self._validate_aws_access_credentials()
            self._validate_instance_types()
            self._validate_instance_types_arch()
            self._validate_volume_types()
        else:
            log.warning("Ignoring parameter validation. Use --validate-parameters to enable it.")

        # We do NOT want this validation to be gated by 'config["validate_parameters"]'
        # The validation here is too important for this (code is touching existing/production VPCs of the customer).
        if config["existing_vpc_id"]:
            self._validate_params_existing_vpc(ec2)

    @classmethod
    def _generate_cluster_names(cls, names, cluster_count):
        if (cluster_count > 1 and len(names) != 1) or not names:
            raise CODException("You need to either specify one name, one name and --clusters <number>, "
                               "or a list of names.")

        if cluster_count and cluster_count > 1:
            base_cluster_name = names[0]
            names = [f"{base_cluster_name}-{i + 1:02}" for i in range(cluster_count)]  # [cluster-01, cluster-02, ...]

        name_counter = collections.Counter(names)
        duplicate_names = [name for name, name_count in name_counter.items() if name_count > 1]
        if duplicate_names:
            raise CODException(f"Duplicate cluster names: {' '.join(duplicate_names)}")

        conflicting_names = {cluster.name for cluster in Cluster.find(names)}
        if conflicting_names:
            raise CODException(f"Cluster(s) with conflicting name(s) already exists: {' '.join(conflicting_names)}")

        return names

    def _validate_params_existing_vpc(self, ec2):
        log.debug("Reusing existing VPC - validating parameters")
        assert config["existing_vpc_id"]

        if config["clusters"] > 1:
            raise CODException("Can only create one cluster when using an existing VPC.")

        vpc = ec2.Vpc(config["existing_vpc_id"])
        try:
            vpc.load()
        except ClientError:
            raise CODException(
                f"Failed to find VPC {config['existing_vpc_id']} in region {config['aws_region']}")

        vpc_name = get_aws_tag(vpc.tags, "Name", "<name not set>")
        log.debug(f"VPC '{config['existing_vpc_id']}' exists, good. Name: '{vpc_name}'.")

        # Confirm that specified subnets exist in the vpc
        assert len(config["existing_subnet_id"])
        vpc_subnet_ids = {subnet.id for subnet in vpc.subnets.all()}
        for subnet_id in config["existing_subnet_id"]:
            if subnet_id not in vpc_subnet_ids:
                raise CODException(f"User specified subnet '{subnet_id}' was not found in VPC '{vpc.id}' "
                                   f"in region '{config['aws_region']}'")

        log.debug(f"All user specified subnets {config['existing_subnet_id']} were found in the VPC, good.")

        if config["head_node_internal_ip"]:
            head_node_subnet_id = config["existing_subnet_id"][0]
            head_node_subnet = None
            for subnet in vpc.subnets.all():
                if subnet.id == head_node_subnet_id:
                    head_node_subnet = subnet

            _validate_head_node_ip_in_cidr(config["head_node_internal_ip"], head_node_subnet.cidr_block)

    def _get_existing_vpc_details(self, ec2):
        """Get information necessary for displaying information about existing VPCs"""
        if not config["existing_vpc_id"]:
            return (None, None, None, [])

        vpc = ec2.Vpc(config["existing_vpc_id"])
        vpc.load()

        head_node_subnet_id = config["existing_subnet_id"][0]
        head_node_subnet = next(
            (subnet for subnet in vpc.subnets.all() if subnet.id == head_node_subnet_id),
            None)

        vpc_name = get_aws_tag(vpc.tags, "Name", "<name not set>")
        vpc_id = config["existing_vpc_id"]
        vpc_cidr_block = vpc.cidr_block
        all_subnets_texts = []

        for subnet in vpc.subnets.all():
            all_subnets_texts += [
                f"CIDR: {subnet.cidr_block}, "
                f"name: {get_aws_tag(subnet.tags, 'Name', '<name not set>')}, "
                f"AZ: {subnet.availability_zone}, ID: {subnet.id}"]
            if subnet.id == head_node_subnet.id:
                all_subnets_texts[-1] = all_subnets_texts[-1] + " <Head node>"
            if subnet.id in config["existing_subnet_id"]:
                all_subnets_texts[-1] = all_subnets_texts[-1] + " (*)"

        return (vpc_name, vpc_id, vpc_cidr_block, all_subnets_texts)

    def run(self):
        ec2 = create_aws_service_resource(service_name="ec2")
        names = self._generate_cluster_names(config["name"], config["clusters"])

        self._validate_params(names, ec2)

        head_node_image = AWSImageSource.pick_head_node_image_using_options(config)
        if not head_node_image.version and config["run_cm_bright_setup"]:
            log.warning(
                f"Using custom image: {head_node_image.uuid} with parameter run_cm_bright_setup set to 'yes'."
                f" Probably it was set by mistake because a custom image might not have necessary files"
                f" to run cm-bright-setup. Consider using --run-cm-bright-setup=no to "
            )

        requested = [
            Cluster(name, head_node_image)
            for name in names
        ]

        def print_overview(requested_clusters):
            vpc_name, vpc_id, vpc_cidr_block, subnet_texts = self._get_existing_vpc_details(ec2)
            head_node_definition = NodeDefinition(len(requested_clusters), config["head_node_type"])
            node_definition = NodeDefinition(config["nodes"], config["node_type"])
            generator = AwsSummaryGenerator(requested_clusters,
                                            SummaryType.Proposal,
                                            config,
                                            head_node_definition,
                                            head_node_image,
                                            node_definition,
                                            vpc_name,
                                            vpc_id,
                                            vpc_cidr_block,
                                            subnet_texts)
            generator.print_summary(log.info)

        # TODO(cloud-team): move to a proper validation stage, add unit tests
        if len(requested) > 1 and config["head_node_internal_ip"]:
            raise CODException("--head-node-internal-ip can only be used when creating only one head node.")

        print_overview(requested)
        if config["ask_to_confirm_cluster_creation"]:
            utils.confirm_cluster_creation(num_clusters=len(requested))

        cluster_creator = ClusterCreator(requested)
        cluster_creator.run()

        if config["store_head_node_ip"]:
            number_of_stored_ips = 0
            with open(config["store_head_node_ip"], "w") as f:
                for cluster in requested:
                    if not cluster.primary_head_node:
                        continue
                    ip = (cluster.primary_head_node.public_ip_address if config["head_node_assign_public_ip"] else
                          cluster.primary_head_node.private_ip_address)
                    if ip:
                        number_of_stored_ips += 1
                        f.write(f"{ip} {cluster.name}\n")
            log.info("Stored %s IP(s) in %s" %
                     (number_of_stored_ips, config["store_head_node_ip"]))
        if config["store_head_node_id"]:
            number_of_stored_ids = 0
            with open(config["store_head_node_id"], "w") as f:
                for cluster in requested:
                    if cluster.primary_head_node and cluster.primary_head_node.id:
                        number_of_stored_ids += 1
                        f.write(cluster.primary_head_node.id + " " + cluster.name + "\n")
            log.info("Stored %s ID(s) in %s" %
                     (number_of_stored_ids, config["store_head_node_id"]))
        if cluster_creator.failed:
            if len(cluster_creator.failed) == 1:
                details = cluster_creator.failed[0].error_message
                raise CODException(f"Cluster creation failed. Details: {details}")

            details = "\n\n".join([c.error_message for c in cluster_creator.failed])
            raise CODException(f"Cluster creation failed. \n\nDetails:\n{details}")

        return


class ClusterCreator:
    Choice = collections.namedtuple("Choice", ["method", "name", "description"])

    def __init__(self, requested):
        self.requested = requested

        if config["existing_vpc_id"]:
            # TODO(cloud-team): CM-32516: Ideally we would like to remove the resources that we created,
            #  but nothing else. Note that the vpc might have non-bright VMs in it.
            self.on_error_choices = collections.OrderedDict([
                ("a", self.Choice(None,
                                  "(a)bort",
                                  "Terminate cm-cod-aws in place. Any resources created in AWS will "
                                  "have to be cleaned up manually by the user.")),
            ])
        else:
            self.on_error_choices = collections.OrderedDict([
                ("c", self.Choice(self.cleanup,
                                  "(c)leanup",
                                  "Destroy resources for failed clusters")),
                ("u", self.Choice(self.undo,
                                  "(u)ndo",
                                  "Destroy resources for all requested clusters" +
                                  " (including succeeded ones)")),
                ("a", self.Choice(None,
                                  "(a)bort",
                                  "Terminate cm-cluster-on-demand create in place")),
            ])

    def cleanup(self):
        utils.multithread_run(lambda cluster: cluster.destroy(), self.failed, config["max_threads"])

    def undo(self):
        utils.multithread_run(lambda cluster: cluster.destroy(), self.requested, config["max_threads"])

    def run(self):
        to_create_names = [c.name for c in self.requested]

        start = datetime.now()

        log.debug("Running Cluster creation")

        to_setup = []
        failed_create = []

        for cluster in self.requested:
            try:
                # cluster.vpc and cluster.primary_head_node will be written in this call
                if config["existing_vpc_id"]:
                    create_in_existing_vpc(cluster)
                else:
                    create_vpc(cluster)
            except ClientError as e:
                failed_create.append(cluster)
                if e.response["Error"]["Code"] == "VpcLimitExceeded":
                    cluster.error_message = str(e.response["Error"]["Message"])
                    raise CODException(str(e.response["Error"]))

                cluster.error_message = str(e.response["Error"]["Message"])
                log.error("VPC Creation failed for cluster %s: %s", cluster.name, str(e))
            except Exception as e:
                log.exception("Create VPC failed for %s: %s", cluster.name, str(e))
                cluster.error_message = str(e)
                failed_create.append(cluster)
            else:
                to_setup.append(cluster)

        if len(self.requested) > 1 and failed_create:
            #  if we fail during setup, dont bother running bright-setup
            log.debug(f"Failed to create clusters {' '.join([cluster.name for cluster in failed_create])}, "
                      f"undoing all progress")
            self.failed = failed_create
            self.undo()
        else:
            failed_setup = []
            if to_setup:
                failed_setup = start_headnodes(to_setup)

            self.failed = failed_create + failed_setup
            if self.failed:
                log.warning("Setup failed for clusters %s",
                            " ".join([c.name for c in self.failed]))

                choice = self.prompt_for_choice()

                if choice.method:
                    choice.method()

        failed_names = [c.name for c in self.failed]

        delta = datetime.now() - start
        delta_string = "%02d:%02d" % ((delta.seconds // 60), (delta.seconds % 60))

        log.info("Script completed.")
        log.info(HR)
        log.info("Time it took:   %s" % delta_string)

        if len(to_create_names) == 1 and len(failed_names) == 0 and self.requested[0].primary_head_node:
            """ One cluster OK """
            head_node_ip = None
            if config["head_node_assign_public_ip"]:
                head_node_ip = self.requested[0].primary_head_node.public_ip_address
            else:
                head_node_ip = self.requested[0].primary_head_node.private_ip_address
            log.info(f"  SSH string:   'ssh root@{head_node_ip}'")
        else:
            log.info("   to create:   %s" % len(to_create_names))
            log.info("     created:   %s" % len([cluster for cluster in self.requested
                                                 if cluster.primary_head_node]))
            if len(self.failed):
                log.info("      failed:   %s" % len(self.failed))

        for r in self.requested:
            if r.primary_head_node:
                # Print in hosts format (easy copy/paste)
                print("%s  %s" % (r.primary_head_node.public_ip_address, r.name))
                log.info("Head node ID:   %s" % r.primary_head_node.id)
            else:
                pass
        if config["log_cluster_password"]:
            log.info("Cluster password:   %s" % config["cluster_password"])

    def prompt_for_choice(self):
        for choice in self.on_error_choices.values():

            log.info("   %s: %s" % (choice.name, choice.description))
        choice_codes = "/".join(self.on_error_choices)

        if config["on_error"] == "ask":
            log.info("Please select [%s]" % choice_codes)
            response = input()
        else:
            get_first_letter = 0
            response = config["on_error"][get_first_letter]

        while True:
            code = response.strip().lower()
            choice = self.on_error_choices.get(code)
            if choice:
                return choice
            log.info('Invalid choice "%s", please select [%s]' %
                     (response, choice_codes))
            response = input()
            continue


def start_headnodes(clusters):

    utils.cod_log(log, f"Starting the head node{'s' if len(clusters) > 1 else ''}", 22)

    # it looks like newly create VMs get started by default anyway. It's just a matter of waiting for them to be running
    # Not sure why we have this "start" code here. We should consider removing it.
    for cluster in clusters:
        cluster.primary_head_node.start()

    ip_assignment_failures = []

    utils.cod_log(log, f"Waiting for the head node{'s' if len(clusters) > 1 else ''} to start", 30)

    for cluster in clusters[:]:
        cluster.primary_head_node.wait_until_running()

        try:
            if config["head_node_assign_public_ip"]:
                utils.cod_log(log,
                              "Assigning public IP to the head node "
                              "(use '--no-head-node-assign-public-ip' to skip)",
                              32)
                if config["existing_vpc_id"] and not config["configure_igw_in_existing_vpc"]:
                    log.info("Note that you're creating a cluster in an existing VPC, while at the same time "
                             "not ensuring that IGW exists. There's a risk assigning a public IP might fail.")

                cluster.attach_eips_to_head_nodes()
            else:
                utils.cod_log(log,
                              "Will not assign a public IP to the head node "
                              "(use '--head-node-assign-public-ip' to change this)",
                              32)
        except ClientError as e:
            ip_assignment_failures.append(cluster)
            clusters.remove(cluster)
            cluster.error_message = str(e.response["Error"]["Message"])
            if e.response["Error"]["Code"] == "AddressLimitExceeded":
                cluster.error_message = "IP Address limit exceeded!"
                raise CODException("IP Address limit exceeded!")
        except Exception as e:
            log.warning("Failed to assign IP for cluster %s: %s", cluster.name, e)
            cluster.error_message = str(e)
            ip_assignment_failures.append(cluster)
            clusters.remove(cluster)

    results = utils.multithread_iter(
        function=lambda cluster: wait_for_cluster(
            config=config,
            host=cluster.primary_head_node.public_ip_address,
        ),
        args_list=clusters,
        max_threads=config["max_threads"],
        reraise=False
    )

    wait_operation_failures = []
    for r in results:
        if isinstance(r[1], utils.MultithreadRunError):
            r[0].error_message = str(r[1].exception)
            wait_operation_failures.append(r[0])

    return ip_assignment_failures + wait_operation_failures
