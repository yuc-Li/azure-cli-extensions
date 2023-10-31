# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "hdinsightonaks cluster wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.hdinsight/clusterpools/{}/clusters/{}", "2023-06-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the HDInsight cluster.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.cluster_pool_name = AAZStrArg(
            options=["--cluster-pool-name"],
            help="The name of the cluster pool.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ClustersGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class ClustersGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusterpools/{clusterPoolName}/clusters/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "clusterPoolName", self.ctx.args.cluster_pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.cluster_profile = AAZObjectType(
                serialized_name="clusterProfile",
                flags={"required": True},
            )
            properties.cluster_type = AAZStrType(
                serialized_name="clusterType",
                flags={"required": True},
            )
            properties.compute_profile = AAZObjectType(
                serialized_name="computeProfile",
                flags={"required": True},
            )
            properties.deployment_id = AAZStrType(
                serialized_name="deploymentId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )

            cluster_profile = cls._schema_on_200.properties.cluster_profile
            cluster_profile.authorization_profile = AAZObjectType(
                serialized_name="authorizationProfile",
                flags={"required": True},
            )
            cluster_profile.autoscale_profile = AAZObjectType(
                serialized_name="autoscaleProfile",
            )
            cluster_profile.cluster_version = AAZStrType(
                serialized_name="clusterVersion",
                flags={"required": True},
            )
            cluster_profile.components = AAZListType(
                flags={"read_only": True},
            )
            cluster_profile.connectivity_profile = AAZObjectType(
                serialized_name="connectivityProfile",
                flags={"read_only": True},
            )
            cluster_profile.flink_profile = AAZObjectType(
                serialized_name="flinkProfile",
            )
            cluster_profile.identity_profile = AAZObjectType(
                serialized_name="identityProfile",
                flags={"required": True},
            )
            cluster_profile.kafka_profile = AAZFreeFormDictType(
                serialized_name="kafkaProfile",
            )
            cluster_profile.llap_profile = AAZFreeFormDictType(
                serialized_name="llapProfile",
            )
            cluster_profile.log_analytics_profile = AAZObjectType(
                serialized_name="logAnalyticsProfile",
            )
            cluster_profile.oss_version = AAZStrType(
                serialized_name="ossVersion",
                flags={"required": True},
            )
            cluster_profile.prometheus_profile = AAZObjectType(
                serialized_name="prometheusProfile",
            )
            cluster_profile.script_action_profiles = AAZListType(
                serialized_name="scriptActionProfiles",
            )
            cluster_profile.secrets_profile = AAZObjectType(
                serialized_name="secretsProfile",
            )
            cluster_profile.service_configs_profiles = AAZListType(
                serialized_name="serviceConfigsProfiles",
            )
            cluster_profile.spark_profile = AAZObjectType(
                serialized_name="sparkProfile",
            )
            cluster_profile.ssh_profile = AAZObjectType(
                serialized_name="sshProfile",
            )
            cluster_profile.stub_profile = AAZFreeFormDictType(
                serialized_name="stubProfile",
            )
            cluster_profile.trino_profile = AAZObjectType(
                serialized_name="trinoProfile",
            )

            authorization_profile = cls._schema_on_200.properties.cluster_profile.authorization_profile
            authorization_profile.group_ids = AAZListType(
                serialized_name="groupIds",
            )
            authorization_profile.user_ids = AAZListType(
                serialized_name="userIds",
            )

            group_ids = cls._schema_on_200.properties.cluster_profile.authorization_profile.group_ids
            group_ids.Element = AAZStrType()

            user_ids = cls._schema_on_200.properties.cluster_profile.authorization_profile.user_ids
            user_ids.Element = AAZStrType()

            autoscale_profile = cls._schema_on_200.properties.cluster_profile.autoscale_profile
            autoscale_profile.autoscale_type = AAZStrType(
                serialized_name="autoscaleType",
            )
            autoscale_profile.enabled = AAZBoolType(
                flags={"required": True},
            )
            autoscale_profile.graceful_decommission_timeout = AAZIntType(
                serialized_name="gracefulDecommissionTimeout",
            )
            autoscale_profile.load_based_config = AAZObjectType(
                serialized_name="loadBasedConfig",
            )
            autoscale_profile.schedule_based_config = AAZObjectType(
                serialized_name="scheduleBasedConfig",
            )

            load_based_config = cls._schema_on_200.properties.cluster_profile.autoscale_profile.load_based_config
            load_based_config.cooldown_period = AAZIntType(
                serialized_name="cooldownPeriod",
            )
            load_based_config.max_nodes = AAZIntType(
                serialized_name="maxNodes",
                flags={"required": True},
            )
            load_based_config.min_nodes = AAZIntType(
                serialized_name="minNodes",
                flags={"required": True},
            )
            load_based_config.poll_interval = AAZIntType(
                serialized_name="pollInterval",
            )
            load_based_config.scaling_rules = AAZListType(
                serialized_name="scalingRules",
                flags={"required": True},
            )

            scaling_rules = cls._schema_on_200.properties.cluster_profile.autoscale_profile.load_based_config.scaling_rules
            scaling_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.autoscale_profile.load_based_config.scaling_rules.Element
            _element.action_type = AAZStrType(
                serialized_name="actionType",
                flags={"required": True},
            )
            _element.comparison_rule = AAZObjectType(
                serialized_name="comparisonRule",
                flags={"required": True},
            )
            _element.evaluation_count = AAZIntType(
                serialized_name="evaluationCount",
                flags={"required": True},
            )
            _element.scaling_metric = AAZStrType(
                serialized_name="scalingMetric",
                flags={"required": True},
            )

            comparison_rule = cls._schema_on_200.properties.cluster_profile.autoscale_profile.load_based_config.scaling_rules.Element.comparison_rule
            comparison_rule.operator = AAZStrType(
                flags={"required": True},
            )
            comparison_rule.threshold = AAZFloatType(
                flags={"required": True},
            )

            schedule_based_config = cls._schema_on_200.properties.cluster_profile.autoscale_profile.schedule_based_config
            schedule_based_config.default_count = AAZIntType(
                serialized_name="defaultCount",
                flags={"required": True},
            )
            schedule_based_config.schedules = AAZListType(
                flags={"required": True},
            )
            schedule_based_config.time_zone = AAZStrType(
                serialized_name="timeZone",
                flags={"required": True},
            )

            schedules = cls._schema_on_200.properties.cluster_profile.autoscale_profile.schedule_based_config.schedules
            schedules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.autoscale_profile.schedule_based_config.schedules.Element
            _element.count = AAZIntType(
                flags={"required": True},
            )
            _element.days = AAZListType(
                flags={"required": True},
            )
            _element.end_time = AAZStrType(
                serialized_name="endTime",
                flags={"required": True},
            )
            _element.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"required": True},
            )

            days = cls._schema_on_200.properties.cluster_profile.autoscale_profile.schedule_based_config.schedules.Element.days
            days.Element = AAZStrType()

            components = cls._schema_on_200.properties.cluster_profile.components
            components.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.components.Element
            _element.name = AAZStrType()
            _element.version = AAZStrType()

            connectivity_profile = cls._schema_on_200.properties.cluster_profile.connectivity_profile
            connectivity_profile.ssh = AAZListType()
            connectivity_profile.web = AAZObjectType(
                flags={"required": True},
            )

            ssh = cls._schema_on_200.properties.cluster_profile.connectivity_profile.ssh
            ssh.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.connectivity_profile.ssh.Element
            _element.endpoint = AAZStrType(
                flags={"required": True},
            )

            web = cls._schema_on_200.properties.cluster_profile.connectivity_profile.web
            web.fqdn = AAZStrType(
                flags={"required": True},
            )

            flink_profile = cls._schema_on_200.properties.cluster_profile.flink_profile
            flink_profile.catalog_options = AAZObjectType(
                serialized_name="catalogOptions",
            )
            flink_profile.history_server = AAZObjectType(
                serialized_name="historyServer",
            )
            _WaitHelper._build_schema_compute_resource_definition_read(flink_profile.history_server)
            flink_profile.job_manager = AAZObjectType(
                serialized_name="jobManager",
                flags={"required": True},
            )
            _WaitHelper._build_schema_compute_resource_definition_read(flink_profile.job_manager)
            flink_profile.num_replicas = AAZIntType(
                serialized_name="numReplicas",
            )
            flink_profile.storage = AAZObjectType(
                flags={"required": True},
            )
            flink_profile.task_manager = AAZObjectType(
                serialized_name="taskManager",
                flags={"required": True},
            )
            _WaitHelper._build_schema_compute_resource_definition_read(flink_profile.task_manager)

            catalog_options = cls._schema_on_200.properties.cluster_profile.flink_profile.catalog_options
            catalog_options.hive = AAZObjectType()

            hive = cls._schema_on_200.properties.cluster_profile.flink_profile.catalog_options.hive
            hive.metastore_db_connection_password_secret = AAZStrType(
                serialized_name="metastoreDbConnectionPasswordSecret",
                flags={"required": True},
            )
            hive.metastore_db_connection_url = AAZStrType(
                serialized_name="metastoreDbConnectionURL",
                flags={"required": True},
            )
            hive.metastore_db_connection_user_name = AAZStrType(
                serialized_name="metastoreDbConnectionUserName",
                flags={"required": True},
            )

            storage = cls._schema_on_200.properties.cluster_profile.flink_profile.storage
            storage.storage_uri = AAZStrType(
                serialized_name="storageUri",
                flags={"required": True},
            )
            storage.storagekey = AAZStrType(
                flags={"secret": True},
            )

            identity_profile = cls._schema_on_200.properties.cluster_profile.identity_profile
            identity_profile.msi_client_id = AAZStrType(
                serialized_name="msiClientId",
                flags={"required": True},
            )
            identity_profile.msi_object_id = AAZStrType(
                serialized_name="msiObjectId",
                flags={"required": True},
            )
            identity_profile.msi_resource_id = AAZStrType(
                serialized_name="msiResourceId",
                flags={"required": True},
            )

            log_analytics_profile = cls._schema_on_200.properties.cluster_profile.log_analytics_profile
            log_analytics_profile.application_logs = AAZObjectType(
                serialized_name="applicationLogs",
            )
            log_analytics_profile.enabled = AAZBoolType(
                flags={"required": True},
            )
            log_analytics_profile.metrics_enabled = AAZBoolType(
                serialized_name="metricsEnabled",
            )

            application_logs = cls._schema_on_200.properties.cluster_profile.log_analytics_profile.application_logs
            application_logs.std_error_enabled = AAZBoolType(
                serialized_name="stdErrorEnabled",
            )
            application_logs.std_out_enabled = AAZBoolType(
                serialized_name="stdOutEnabled",
            )

            prometheus_profile = cls._schema_on_200.properties.cluster_profile.prometheus_profile
            prometheus_profile.enabled = AAZBoolType(
                flags={"required": True},
            )

            script_action_profiles = cls._schema_on_200.properties.cluster_profile.script_action_profiles
            script_action_profiles.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.script_action_profiles.Element
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.parameters = AAZStrType()
            _element.services = AAZListType(
                flags={"required": True},
            )
            _element.should_persist = AAZBoolType(
                serialized_name="shouldPersist",
            )
            _element.timeout_in_minutes = AAZIntType(
                serialized_name="timeoutInMinutes",
            )
            _element.type = AAZStrType(
                flags={"required": True},
            )
            _element.url = AAZStrType(
                flags={"required": True},
            )

            services = cls._schema_on_200.properties.cluster_profile.script_action_profiles.Element.services
            services.Element = AAZStrType()

            secrets_profile = cls._schema_on_200.properties.cluster_profile.secrets_profile
            secrets_profile.key_vault_resource_id = AAZStrType(
                serialized_name="keyVaultResourceId",
                flags={"required": True},
            )
            secrets_profile.secrets = AAZListType()

            secrets = cls._schema_on_200.properties.cluster_profile.secrets_profile.secrets
            secrets.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.secrets_profile.secrets.Element
            _element.key_vault_object_name = AAZStrType(
                serialized_name="keyVaultObjectName",
                flags={"required": True},
            )
            _element.reference_name = AAZStrType(
                serialized_name="referenceName",
                flags={"required": True},
            )
            _element.type = AAZStrType(
                flags={"required": True},
            )
            _element.version = AAZStrType()

            service_configs_profiles = cls._schema_on_200.properties.cluster_profile.service_configs_profiles
            service_configs_profiles.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.service_configs_profiles.Element
            _element.configs = AAZListType(
                flags={"required": True},
            )
            _element.service_name = AAZStrType(
                serialized_name="serviceName",
                flags={"required": True},
            )

            configs = cls._schema_on_200.properties.cluster_profile.service_configs_profiles.Element.configs
            configs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.service_configs_profiles.Element.configs.Element
            _element.component = AAZStrType(
                flags={"required": True},
            )
            _element.files = AAZListType(
                flags={"required": True},
            )

            files = cls._schema_on_200.properties.cluster_profile.service_configs_profiles.Element.configs.Element.files
            files.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.service_configs_profiles.Element.configs.Element.files.Element
            _element.content = AAZStrType()
            _element.encoding = AAZStrType()
            _element.file_name = AAZStrType(
                serialized_name="fileName",
                flags={"required": True},
            )
            _element.path = AAZStrType()
            _element.values = AAZDictType()

            values = cls._schema_on_200.properties.cluster_profile.service_configs_profiles.Element.configs.Element.files.Element.values
            values.Element = AAZStrType()

            spark_profile = cls._schema_on_200.properties.cluster_profile.spark_profile
            spark_profile.default_storage_url = AAZStrType(
                serialized_name="defaultStorageUrl",
            )
            spark_profile.metastore_spec = AAZObjectType(
                serialized_name="metastoreSpec",
            )
            spark_profile.user_plugins_spec = AAZObjectType(
                serialized_name="userPluginsSpec",
            )

            metastore_spec = cls._schema_on_200.properties.cluster_profile.spark_profile.metastore_spec
            metastore_spec.db_name = AAZStrType(
                serialized_name="dbName",
                flags={"required": True},
            )
            metastore_spec.db_password_secret_name = AAZStrType(
                serialized_name="dbPasswordSecretName",
                flags={"required": True},
            )
            metastore_spec.db_server_host = AAZStrType(
                serialized_name="dbServerHost",
                flags={"required": True},
            )
            metastore_spec.db_user_name = AAZStrType(
                serialized_name="dbUserName",
                flags={"required": True},
            )
            metastore_spec.key_vault_id = AAZStrType(
                serialized_name="keyVaultId",
                flags={"required": True},
            )
            metastore_spec.thrift_url = AAZStrType(
                serialized_name="thriftUrl",
            )

            user_plugins_spec = cls._schema_on_200.properties.cluster_profile.spark_profile.user_plugins_spec
            user_plugins_spec.plugins = AAZListType()

            plugins = cls._schema_on_200.properties.cluster_profile.spark_profile.user_plugins_spec.plugins
            plugins.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.spark_profile.user_plugins_spec.plugins.Element
            _element.path = AAZStrType(
                flags={"required": True},
            )

            ssh_profile = cls._schema_on_200.properties.cluster_profile.ssh_profile
            ssh_profile.count = AAZIntType(
                flags={"required": True},
            )
            ssh_profile.pod_prefix = AAZStrType(
                serialized_name="podPrefix",
                flags={"read_only": True},
            )

            trino_profile = cls._schema_on_200.properties.cluster_profile.trino_profile
            trino_profile.catalog_options = AAZObjectType(
                serialized_name="catalogOptions",
            )
            trino_profile.coordinator = AAZObjectType()
            trino_profile.user_plugins_spec = AAZObjectType(
                serialized_name="userPluginsSpec",
            )
            trino_profile.user_telemetry_spec = AAZObjectType(
                serialized_name="userTelemetrySpec",
            )
            trino_profile.worker = AAZObjectType()

            catalog_options = cls._schema_on_200.properties.cluster_profile.trino_profile.catalog_options
            catalog_options.hive = AAZListType()

            hive = cls._schema_on_200.properties.cluster_profile.trino_profile.catalog_options.hive
            hive.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.trino_profile.catalog_options.hive.Element
            _element.catalog_name = AAZStrType(
                serialized_name="catalogName",
                flags={"required": True},
            )
            _element.metastore_db_connection_password_secret = AAZStrType(
                serialized_name="metastoreDbConnectionPasswordSecret",
                flags={"required": True},
            )
            _element.metastore_db_connection_url = AAZStrType(
                serialized_name="metastoreDbConnectionURL",
                flags={"required": True},
            )
            _element.metastore_db_connection_user_name = AAZStrType(
                serialized_name="metastoreDbConnectionUserName",
                flags={"required": True},
            )
            _element.metastore_warehouse_dir = AAZStrType(
                serialized_name="metastoreWarehouseDir",
                flags={"required": True},
            )

            coordinator = cls._schema_on_200.properties.cluster_profile.trino_profile.coordinator
            coordinator.debug = AAZObjectType(
                flags={"client_flatten": True},
            )
            _WaitHelper._build_schema_trino_debug_config_read(coordinator.debug)
            coordinator.high_availability_enabled = AAZBoolType(
                serialized_name="highAvailabilityEnabled",
            )

            user_plugins_spec = cls._schema_on_200.properties.cluster_profile.trino_profile.user_plugins_spec
            user_plugins_spec.plugins = AAZListType()

            plugins = cls._schema_on_200.properties.cluster_profile.trino_profile.user_plugins_spec.plugins
            plugins.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cluster_profile.trino_profile.user_plugins_spec.plugins.Element
            _element.enabled = AAZBoolType()
            _element.name = AAZStrType()
            _element.path = AAZStrType()

            user_telemetry_spec = cls._schema_on_200.properties.cluster_profile.trino_profile.user_telemetry_spec
            user_telemetry_spec.storage = AAZObjectType()

            storage = cls._schema_on_200.properties.cluster_profile.trino_profile.user_telemetry_spec.storage
            storage.hivecatalog_name = AAZStrType(
                serialized_name="hivecatalogName",
            )
            storage.hivecatalog_schema = AAZStrType(
                serialized_name="hivecatalogSchema",
            )
            storage.partition_retention_in_days = AAZIntType(
                serialized_name="partitionRetentionInDays",
            )
            storage.path = AAZStrType()

            worker = cls._schema_on_200.properties.cluster_profile.trino_profile.worker
            worker.debug = AAZObjectType(
                flags={"client_flatten": True},
            )
            _WaitHelper._build_schema_trino_debug_config_read(worker.debug)

            compute_profile = cls._schema_on_200.properties.compute_profile
            compute_profile.nodes = AAZListType(
                flags={"required": True},
            )

            nodes = cls._schema_on_200.properties.compute_profile.nodes
            nodes.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.compute_profile.nodes.Element
            _element.count = AAZIntType(
                flags={"required": True},
            )
            _element.type = AAZStrType(
                flags={"required": True},
            )
            _element.vm_size = AAZStrType(
                serialized_name="vmSize",
                flags={"required": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_compute_resource_definition_read = None

    @classmethod
    def _build_schema_compute_resource_definition_read(cls, _schema):
        if cls._schema_compute_resource_definition_read is not None:
            _schema.cpu = cls._schema_compute_resource_definition_read.cpu
            _schema.memory = cls._schema_compute_resource_definition_read.memory
            return

        cls._schema_compute_resource_definition_read = _schema_compute_resource_definition_read = AAZObjectType()

        compute_resource_definition_read = _schema_compute_resource_definition_read
        compute_resource_definition_read.cpu = AAZFloatType(
            flags={"required": True},
        )
        compute_resource_definition_read.memory = AAZIntType(
            flags={"required": True},
        )

        _schema.cpu = cls._schema_compute_resource_definition_read.cpu
        _schema.memory = cls._schema_compute_resource_definition_read.memory

    _schema_trino_debug_config_read = None

    @classmethod
    def _build_schema_trino_debug_config_read(cls, _schema):
        if cls._schema_trino_debug_config_read is not None:
            _schema.enable = cls._schema_trino_debug_config_read.enable
            _schema.port = cls._schema_trino_debug_config_read.port
            _schema.suspend = cls._schema_trino_debug_config_read.suspend
            return

        cls._schema_trino_debug_config_read = _schema_trino_debug_config_read = AAZObjectType()

        trino_debug_config_read = _schema_trino_debug_config_read
        trino_debug_config_read.enable = AAZBoolType()
        trino_debug_config_read.port = AAZIntType()
        trino_debug_config_read.suspend = AAZBoolType()

        _schema.enable = cls._schema_trino_debug_config_read.enable
        _schema.port = cls._schema_trino_debug_config_read.port
        _schema.suspend = cls._schema_trino_debug_config_read.suspend


__all__ = ["Wait"]
