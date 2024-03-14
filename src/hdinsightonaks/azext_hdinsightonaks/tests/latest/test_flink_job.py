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


class TestRunFlinkJob(ScenarioTest):
    location = 'westus3'
    resourceGroup = "hilocli-test"
    clusterPoolName = "hilopool"

    def test_flink_job(self):
        self.kwargs.update({
            "rg": self.resourceGroup,
            "loc": self.location,
            "poolName": self.clusterPoolName,
            "clusterName": "cluster2024311163924",
            "clusterType": "Flink",
            "computeNodeProfile": self.cmd('az hdinsight-on-aks cluster node-profile create --count 5 --node-type Worker --vm-size Standard_D16a_v4').get_output_in_json(),
            "storageUri": "abfs://testflinkjob@hiloclistorage.dfs.core.windows.net",
        })

        # Create a Flink cluster.
        # flink_versions = self.cmd('az hdinsight-on-aks list-available-cluster-version -l {loc} --query "[?clusterType==\'Flink\']"').get_output_in_json()

        # create_command = 'az hdinsight-on-aks cluster create  -n {clusterName} --cluster-pool-name {poolName} -g {rg} -l {loc} --cluster-type {clusterType} --cluster-version ' \
        #       + flink_versions[0]["clusterVersion"] + ' --oss-version ' + flink_versions[0]["ossVersion"] + ' --nodes ' + '{computeNodeProfile}' \
        #         +' '+ authorization_info() + " " + flink_config_str() + ' --flink-storage-uri {storageUri}'

        # self.cmd(create_command,checks=[
        #     self.check("name", '{clusterName}'),
        #     self.check("location", '{loc}'),
        # ])

        # Run a job on a Flink cluster.
        # self.cmd('az hdinsight-on-aks cluster job run --cluster-name {clusterName} --cluster-pool-name {poolName} -g {rg} --flink-job job-name="test" action="DELETE"')
        # List a cluster job list.
        self.cmd(
            'az hdinsight-on-aks cluster job list --cluster-name {clusterName} --cluster-pool-name {poolName} -g {rg}')
