# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

import os
from .testUtil import *
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class TestCreateClusterWithCataLog(ScenarioTest):
    location = 'westus3'
    resourceGroup = "hilocli-test"
    clusterPoolName = "hilopool"

    # Set your hive catalog config.
    secretName = "sqlpassword"
    catalogName = "hilocli"
    metastoreDbConnectionURL = "jdbc:sqlserver://yuchensqlserver.database.windows.net:1433;database=clidata;encrypt=true;trustServerCertificate=true;loginTimeout=30;"
    metastoreDbUserName = "hdi"
    metastoreDbPasswordSecret = secretName
    metastoreWarehouseDir = "abfs://clitesta@flinkdemo125stuoi.dfs.core.windows.net/"
    keyVaultResourceId = "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/Group/providers/Microsoft.KeyVault/vaults/yuchensqlpass"

    # @ResourceGroupPreparer(name_prefix='hilocli-', location=location, random_name_length=12)
    # def test_create_cluster_with_catalog(self):
    #     self.kwargs.update({
    #             "loc": self.location,
    #             "rg": self.resourceGroup,
    #             "poolName": self.clusterPoolName,
    #             "clusterName": self.create_random_name(prefix='hilo-', length=18),
    #             "clusterType": "Trino",
    #             "computeNodeProfile": self.cmd('az hdinsight-on-aks cluster node-profile create --count 5 --node-type Worker --vm-size Standard_D16a_v4').get_output_in_json(),    # Create a cluster node-profile object.

    #             "keyVaultResourceId": self.keyVaultResourceId,
    #             "trinoHiveCatalogOption": self.cmd('az hdinsight-on-aks cluster trino-hive-catalog create --catalog-name ' + self.catalogName \
    #                                                             + ' --metastore-db-connection-url ' + self.metastoreDbConnectionURL + ' --metastore-db-connection-user-name ' + self.metastoreDbUserName \
    #                                                             + ' --metastore-db-connection-password-secret ' + self.metastoreDbPasswordSecret + ' --metastore-warehouse-dir ' + self.metastoreWarehouseDir).get_output_in_json(),

    #             "secret_reference": self.cmd('az hdinsight-on-aks cluster secret create --secret-name ' + self.secretName + ' --reference-name ' +  self.secretName).get_output_in_json()
    #         })
    #     # Get trino cluster version and ossVersion.
    #     trino_versions = self.cmd('az hdinsight-on-aks list-available-cluster-version -l {loc} --query "[?clusterType==\'Trino\']"').get_output_in_json()

    #     # Create a Trino cluster.
    #     create_command = 'az hdinsight-on-aks cluster create  -n {clusterName} --cluster-pool-name {poolName} -g {rg} -l {loc} --cluster-type {clusterType} --cluster-version ' \
    #           + trino_versions[1]["clusterVersion"] + ' --oss-version ' + trino_versions[1]["ossVersion"] + ' --nodes ' + '{computeNodeProfile}' \
    #             +' '+ authorization_info() + ' --secret-reference {secret_reference} --key-vault-id {keyVaultResourceId}' + ' --trino-hive-catalog {trinoHiveCatalogOption}'

    #     self.cmd(create_command,checks=[
    #         self.check("name", '{clusterName}'),
    #         self.check("location", '{loc}'),
    #     ])
