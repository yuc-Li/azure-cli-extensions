# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements


def load_arguments(self, _):  # pylint: disable=unused-argument
    with self.argument_context('hdinsight-on-aks cluster trino-hive-catalog create') as c:
        c.argument('catalog_name',
                   help='Name of trino catalog which should use specified hive metastore.')
        c.argument('metastore_db_connection_url', options_list=['--metastore-db-connection-url', '--url'],
                   help='Connection string for hive metastore database.', required=True)
        c.argument('metastore_db_connection_user_name', options_list=['--metastore-db-connection-user-name', '--user'],
                   help='User name for hive metastore database.', required=True)
        c.argument('metastore_db_connection_password_secret',
                   options_list=['--metastore-db-connection-password-secret', '--secret'],
                   help='Password secret for hive metastore database.', required=True)
        c.argument('metastore_warehouse_dir', options_list=['--metastore-warehouse-dir', '--warehouse-dir'],
                   help='Warehouse directory for hive metastore database.')

    with self.argument_context('hdinsight-on-aks cluster node-profile create') as c:
        c.argument('count',
                   help='The number of virtual machines.', required=True)
        c.argument('node_type',
                   help='The node type.', required=True)
        c.argument('vm_size',
                   help='The virtual machine SKU.', required=True)

    with self.argument_context('hdinsight-on-aks cluster secret create') as c:
        c.argument('secret_name',
                   help='The secret name in the key vault.', required=True)
        c.argument('reference_name',
                   help='The reference name of the secret to be used in service configs.', required=True)
        c.argument('version',
                   help='The version of the secret in key vault.')

    with self.argument_context('hdinsight-on-aks cluster flink-job create') as c:
        c.argument('job_name',
                   help='The name of the Flink job.', required=True)
        c.argument('action',
                   help='The reference name of the secret to be used in service configs.', required=True)
        c.argument('job_jar_directory',
                   help='A string property that specifies the directory where the job JAR is located.')
        c.argument('jar_name',
                   help='A string property that represents the name of the job JAR')
        c.argument('entry_class',
                   help='A string property that specifies the entry class for the Flink job.')
        c.argument('args',
                   help='A string property representing additional JVM arguments for the Flink job. '
                   + 'It should be space separated value.')
        c.argument('save_point_name',
                   help='A string property that represents the name of the savepoint for the Flink job.')
        c.argument('flink_configuration',
                   help='Additional properties used to configure Flink jobs. It allows users to set properties '
                   + 'such as parallelism and jobSavePointDirectory. It accepts additional key-value pairs as '
                   + 'properties, where the keys are strings and the values are strings as well.')
