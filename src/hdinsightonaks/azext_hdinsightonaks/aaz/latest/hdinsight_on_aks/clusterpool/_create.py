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
    "hdinsight-on-aks clusterpool create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create a cluster pool.

    :example: Create a cluster pool.
        az hdinsight-on-aks clusterpool create -g RG -n poolName -l westus3 --workernode-size Standard_E4s_v3 --version 1.1
    """

    _aaz_info = {
        "version": "2023-11-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.hdinsight/clusterpools/{}", "2023-11-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_pool_name = AAZStrArg(
            options=["-n", "--name", "--cluster-pool-name"],
            help="The name of the cluster pool.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ClusterPool"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="ClusterPool",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="ClusterPool",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "ClusterPoolProfile"

        _args_schema = cls._args_schema
        _args_schema.cluster_pool_version = AAZStrArg(
            options=["--version", "--cluster-pool-version"],
            arg_group="ClusterPoolProfile",
            help="Cluster pool version is a 2-part version.",
            fmt=AAZStrArgFormat(
                pattern="^(0|[1-9][0-9]{0,18})\.(0|[1-9][0-9]{0,18})$",
            ),
        )

        # define Arg Group "ComputeProfile"

        _args_schema = cls._args_schema
        _args_schema.workernode_size = AAZStrArg(
            options=["--workernode-size"],
            arg_group="ComputeProfile",
            help="The virtual machine SKU.",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9_\-]{0,256}$",
            ),
        )

        # define Arg Group "LogAnalyticsProfile"

        _args_schema = cls._args_schema
        _args_schema.enable_log_analytics = AAZBoolArg(
            options=["--enable-log-analytics"],
            arg_group="LogAnalyticsProfile",
            help="True if log analytics is enabled for cluster pool, otherwise false.",
        )
        _args_schema.log_analytic_workspace_id = AAZResourceIdArg(
            options=["--la-workspace-id", "--log-analytic-workspace-id"],
            arg_group="LogAnalyticsProfile",
            help="Log analytics workspace to associate with the OMS agent.",
        )

        # define Arg Group "NetworkProfile"

        _args_schema = cls._args_schema
        _args_schema.api_server_authorized_ip_ranges = AAZListArg(
            options=["--api-server-authorized-ip-ranges"],
            arg_group="NetworkProfile",
            help="IP ranges are specified in CIDR format, e.g. 137.117.106.88/29. This feature is not compatible with private AKS clusters. So you cannot set enablePrivateApiServer to true and apiServerAuthorizedIpRanges at the same time.",
        )
        _args_schema.enable_private_api_server = AAZBoolArg(
            options=["--enable-private-api-server"],
            arg_group="NetworkProfile",
            help="ClusterPool is based on AKS cluster. AKS cluster exposes the API server to public internet by default. If you set this property to true, a private AKS cluster will be created, and it will use private apiserver, which is not exposed to public internet.",
        )
        _args_schema.outbound_type = AAZStrArg(
            options=["--outbound-type"],
            arg_group="NetworkProfile",
            help="This can only be set at cluster pool creation time and cannot be changed later.",
            enum={"loadBalancer": "loadBalancer", "userDefinedRouting": "userDefinedRouting"},
        )
        _args_schema.subnet_id = AAZResourceIdArg(
            options=["--subnet-id"],
            arg_group="NetworkProfile",
            help="Cluster pool subnet resource id.",
        )

        api_server_authorized_ip_ranges = cls._args_schema.api_server_authorized_ip_ranges
        api_server_authorized_ip_ranges.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.managed_rg_name = AAZStrArg(
            options=["--managed-rg-name"],
            arg_group="Properties",
            help="A resource group created by RP, to hold the resources created by RP on-behalf of customers. It will also be used to generate aksManagedResourceGroupName by pattern: MC_{managedResourceGroupName}_{clusterPoolName}_{region}. Please make sure it meets resource group name restriction.",
            fmt=AAZStrArgFormat(
                max_length=40,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ClusterPoolsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClusterPoolsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusterpools/{clusterPoolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2023-11-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("clusterPoolProfile", AAZObjectType)
                properties.set_prop("computeProfile", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("logAnalyticsProfile", AAZObjectType)
                properties.set_prop("managedResourceGroupName", AAZStrType, ".managed_rg_name")
                properties.set_prop("networkProfile", AAZObjectType)

            cluster_pool_profile = _builder.get(".properties.clusterPoolProfile")
            if cluster_pool_profile is not None:
                cluster_pool_profile.set_prop("clusterPoolVersion", AAZStrType, ".cluster_pool_version", typ_kwargs={"flags": {"required": True}})

            compute_profile = _builder.get(".properties.computeProfile")
            if compute_profile is not None:
                compute_profile.set_prop("vmSize", AAZStrType, ".workernode_size", typ_kwargs={"flags": {"required": True}})

            log_analytics_profile = _builder.get(".properties.logAnalyticsProfile")
            if log_analytics_profile is not None:
                log_analytics_profile.set_prop("enabled", AAZBoolType, ".enable_log_analytics", typ_kwargs={"flags": {"required": True}})
                log_analytics_profile.set_prop("workspaceId", AAZStrType, ".log_analytic_workspace_id")

            network_profile = _builder.get(".properties.networkProfile")
            if network_profile is not None:
                network_profile.set_prop("apiServerAuthorizedIpRanges", AAZListType, ".api_server_authorized_ip_ranges")
                network_profile.set_prop("enablePrivateApiServer", AAZBoolType, ".enable_private_api_server")
                network_profile.set_prop("outboundType", AAZStrType, ".outbound_type")
                network_profile.set_prop("subnetId", AAZStrType, ".subnet_id", typ_kwargs={"flags": {"required": True}})

            api_server_authorized_ip_ranges = _builder.get(".properties.networkProfile.apiServerAuthorizedIpRanges")
            if api_server_authorized_ip_ranges is not None:
                api_server_authorized_ip_ranges.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.aks_cluster_profile = AAZObjectType(
                serialized_name="aksClusterProfile",
                flags={"read_only": True},
            )
            properties.aks_managed_resource_group_name = AAZStrType(
                serialized_name="aksManagedResourceGroupName",
                flags={"read_only": True},
            )
            properties.cluster_pool_profile = AAZObjectType(
                serialized_name="clusterPoolProfile",
            )
            properties.compute_profile = AAZObjectType(
                serialized_name="computeProfile",
                flags={"required": True},
            )
            properties.deployment_id = AAZStrType(
                serialized_name="deploymentId",
                flags={"read_only": True},
            )
            properties.log_analytics_profile = AAZObjectType(
                serialized_name="logAnalyticsProfile",
            )
            properties.managed_resource_group_name = AAZStrType(
                serialized_name="managedResourceGroupName",
            )
            properties.network_profile = AAZObjectType(
                serialized_name="networkProfile",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )

            aks_cluster_profile = cls._schema_on_200_201.properties.aks_cluster_profile
            aks_cluster_profile.aks_cluster_agent_pool_identity_profile = AAZObjectType(
                serialized_name="aksClusterAgentPoolIdentityProfile",
            )
            aks_cluster_profile.aks_cluster_resource_id = AAZStrType(
                serialized_name="aksClusterResourceId",
            )
            aks_cluster_profile.aks_version = AAZStrType(
                serialized_name="aksVersion",
                flags={"read_only": True},
            )

            aks_cluster_agent_pool_identity_profile = cls._schema_on_200_201.properties.aks_cluster_profile.aks_cluster_agent_pool_identity_profile
            aks_cluster_agent_pool_identity_profile.msi_client_id = AAZStrType(
                serialized_name="msiClientId",
                flags={"required": True},
            )
            aks_cluster_agent_pool_identity_profile.msi_object_id = AAZStrType(
                serialized_name="msiObjectId",
                flags={"required": True},
            )
            aks_cluster_agent_pool_identity_profile.msi_resource_id = AAZStrType(
                serialized_name="msiResourceId",
                flags={"required": True},
            )

            cluster_pool_profile = cls._schema_on_200_201.properties.cluster_pool_profile
            cluster_pool_profile.cluster_pool_version = AAZStrType(
                serialized_name="clusterPoolVersion",
                flags={"required": True},
            )

            compute_profile = cls._schema_on_200_201.properties.compute_profile
            compute_profile.count = AAZIntType(
                flags={"read_only": True},
            )
            compute_profile.vm_size = AAZStrType(
                serialized_name="vmSize",
                flags={"required": True},
            )

            log_analytics_profile = cls._schema_on_200_201.properties.log_analytics_profile
            log_analytics_profile.enabled = AAZBoolType(
                flags={"required": True},
            )
            log_analytics_profile.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )

            network_profile = cls._schema_on_200_201.properties.network_profile
            network_profile.api_server_authorized_ip_ranges = AAZListType(
                serialized_name="apiServerAuthorizedIpRanges",
            )
            network_profile.enable_private_api_server = AAZBoolType(
                serialized_name="enablePrivateApiServer",
            )
            network_profile.outbound_type = AAZStrType(
                serialized_name="outboundType",
            )
            network_profile.subnet_id = AAZStrType(
                serialized_name="subnetId",
                flags={"required": True},
            )

            api_server_authorized_ip_ranges = cls._schema_on_200_201.properties.network_profile.api_server_authorized_ip_ranges
            api_server_authorized_ip_ranges.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
