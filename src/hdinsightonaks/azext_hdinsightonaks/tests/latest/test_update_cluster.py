# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

import os
from .testUtil import *
from azure.cli.testsdk import *
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class TestUpdateCluster(ScenarioTest):
    location = 'westus3'
    resourceGroup = "hilocli-test"
    clusterPoolName = "hilopool"

    def test_update_cluster(self):
        self.kwargs.update({
            "rg": self.resourceGroup,
            "loc": self.location,
            "poolName": self.clusterPoolName,
            "clusterName": "hilo-vjkn4d55e7cby",
            "clusterType": "Spark",
            'config_path': os.path.join(TEST_DIR, 'config.json'),
            # Create a cluster node-profile object.
            "computeNodeProfile": self.cmd('az hdinsight-on-aks cluster node-profile create --count 5 --node-type Worker --vm-size Standard_D16a_v4').get_output_in_json(),
        })

        # Get spark cluster version and ossVersion.
        spark_versions = self.cmd(
            'az hdinsight-on-aks list-available-cluster-version -l {loc} --query "[?clusterType==\'Spark\']"').get_output_in_json()

        # # Create a spark cluster.
        # create_command = 'az hdinsight-on-aks cluster create -n {clusterName} --cluster-pool-name {poolName} -g {rg} -l {loc} --cluster-type {clusterType} --spark-storage-url abfs://testspark@yuchenhilostorage.dfs.core.windows.net/ --cluster-version ' + spark_versions[0]["clusterVersion"] + ' --oss-version ' + spark_versions[0]["ossVersion"] + ' --nodes ' + '{computeNodeProfile}' +' '+ authorization_info()

        # self.cmd(create_command,checks=[
        #     self.check("name", '{clusterName}'),
        #     self.check("location", '{loc}'),
        #     self.check("computeProfile.nodes[1].count", 5)

        # ])
        # Test update a cluster's service config.
        self.cmd('az hdinsight-on-aks cluster update -n {clusterName} --cluster-pool-name {poolName} -g {rg} --service-configs-profiles @"{config_path}"', checks=[
            self.check("clusterProfile.serviceConfigsProfiles[0].serviceName", "yarn-service"),
            self.check("clusterProfile.serviceConfigsProfiles[0].configs[0].component", "hadoop-config"),
            self.check("clusterProfile.serviceConfigsProfiles[0].configs[0].files[0].fileName", "core-site.xml"),
        ])

        # Test list service config.
        self.cmd(
            'az hdinsight-on-aks cluster list-service-config --cluster-name {clusterName} --cluster-pool-name {poolName} -g {rg}')

        # Test update a cluster's autoscale config.
        # self.cmd('az hdinsight-on-aks cluster update -n {clusterName} --cluster-pool-name {poolName} -g {rg} ' + autoScale_config_str(), checks=[
        #     self.check("clusterProfile.autoscaleProfile.enable", True),
        #     self.check("clusterProfile.autoscaleProfile.autoscaleType", "ScheduleBased"),
        #     self.check("clusterProfile.autoscaleProfile.scheduleBasedConfig.defaultCount", 5),
        # ])
