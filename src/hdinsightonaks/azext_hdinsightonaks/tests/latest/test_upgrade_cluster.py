# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

import os
from .testUtil import authorization_info
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class TestUpdateCluster(ScenarioTest):
    location = 'westus3'
    resourceGroup = "hilocli-test"
    clusterPoolName = "hilopool11"

    def test_upgrade_cluster(self):
        self.kwargs.update({
            "rg": self.resourceGroup,
            "loc": self.location,
            "poolName": self.clusterPoolName,
            "clusterName": "cluster2024314152356",
            "clusterType": "Spark",
            # Create a cluster node-profile object.
            "computeNodeProfile": self.cmd('az hdinsight-on-aks cluster node-profile create --count 5 --node-type Worker --vm-size Standard_D16a_v4').get_output_in_json(),
        })

        # If there is no existing cluster to test, use the following code to create the cluster.
        # spark_versions = self.cmd('az hdinsight-on-aks list-available-cluster-version -l {loc} --query "[?clusterType==\'Spark\']"').get_output_in_json()
        # create_command = 'az hdinsight-on-aks cluster create -n {clusterName} --cluster-pool-name {poolName} -g {rg} -l {loc} --cluster-type {clusterType} --spark-storage-url abfs://testspark@yuchenhilostorage.dfs.core.windows.net/ --cluster-version ' + spark_versions[0]["clusterVersion"] + ' --oss-version ' + spark_versions[0]["ossVersion"] + ' --nodes ' + '{computeNodeProfile}' +' '+ authorization_info()
        # self.cmd(create_command)

        # Test list a clusterpool's available upgrades.
        upgrades = self.cmd(
            'az hdinsight-on-aks clusterpool upgrade list --cluster-pool-name {poolName} -g {rg}').get_output_in_json()
        assert upgrades[0]["name"] == "AKSPatchUpgrade"

        # Test list a cluster's available upgrades.
        upgrades = self.cmd(
            'az hdinsight-on-aks cluster upgrade list --cluster-pool-name {poolName} -g {rg} --cluster-name {clusterName}').get_output_in_json()
        assert upgrades[0]["upgradeType"] == "HotfixUpgrade"

        # Test upgrade a clusterpool.
        self.cmd(
            'az hdinsight-on-aks clusterpool upgrade run --cluster-pool-name {poolName} -g {rg} --upgrade-profile target-aks-version=1.27.9 upgrade-clusters=false upgrade-cluster-pool=true')

        # Test upgrade a cluster.(There is currently no upgradeable version, but need to test it later)
        # self.cmd('az hdinsight-on-aks cluster upgrade run --cluster-pool-name {poolName} -g {rg} --cluster-name {clusterName} --hotfix-upgrade component-name=' + upgrades[0]["componentName"] + ' target-build-number='+upgrades[0]["targetBuildNumber"] +' target-cluster-version='+upgrades[0]["targetClusterVersion"] +' target-oss-version='+ upgrades[0]["targetOssVersion"])
