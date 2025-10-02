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

import logging

from clusterondemand.clusternameprefix import clusterprefix_ns, ensure_cod_prefix
from clusterondemand.utils import confirm, confirm_ns, log_no_clusters_found, multithread_run
from clusterondemandaws.base import ClusterCommandBase
from clusterondemandconfig import ConfigNamespace, config

from .cluster import Cluster
from .configuration import awscommon_ns

log = logging.getLogger("cluster-on-demand")


def run_command():
    return ClusterStop().run()


config_ns = ConfigNamespace("aws.cluster.stop")
config_ns.import_namespace(awscommon_ns)
config_ns.import_namespace(clusterprefix_ns)
config_ns.import_namespace(confirm_ns)
config_ns.add_repeating_positional_parameter(
    "filters",
    require_value=True,
    help="Cluster names or patterns. Wildcards are supported (e.g: \\*)",
)
config_ns.add_switch_parameter(
    "release_eip",
    default=True,
    help=(
        "Release elastic IP(s) associated with the instances that are being stopped"
    )
)


class ClusterStop(ClusterCommandBase):

    def _validate_params(self):
        self._validate_aws_access_credentials()

    def run(self):
        self._validate_params()

        names = [ensure_cod_prefix(name) for name in config["filters"]]
        clusters = list(Cluster.find(names))

        if not clusters:
            log_no_clusters_found("stop")
            return

        if not confirm(f"This will stop clusters {' '.join([c.name for c in clusters])} continue?"):
            return

        log.info(f"Stopping nodes for clusters {' '.join(c.name for c in clusters)}.")

        release_eip = config["release_eip"]
        if release_eip:
            log.info("The elastic IP(s) will be released as part of the stop process in order to reduce costs. "
                     "The next time the cluster is started, it will have a different IP. "
                     "Use --no-release-eip to retain the same IP(s) in between stop/start operations.")

        multithread_run(lambda cluster: cluster.stop(release_eip), clusters, config["max_threads"])
