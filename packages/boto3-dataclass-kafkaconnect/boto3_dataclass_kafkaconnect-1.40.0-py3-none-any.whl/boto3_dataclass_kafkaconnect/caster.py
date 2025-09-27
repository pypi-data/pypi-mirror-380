# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kafkaconnect import type_defs as bs_td


class KAFKACONNECTCaster:

    def create_connector(
        self,
        res: "bs_td.CreateConnectorResponseTypeDef",
    ) -> "dc_td.CreateConnectorResponse":
        return dc_td.CreateConnectorResponse.make_one(res)

    def create_custom_plugin(
        self,
        res: "bs_td.CreateCustomPluginResponseTypeDef",
    ) -> "dc_td.CreateCustomPluginResponse":
        return dc_td.CreateCustomPluginResponse.make_one(res)

    def create_worker_configuration(
        self,
        res: "bs_td.CreateWorkerConfigurationResponseTypeDef",
    ) -> "dc_td.CreateWorkerConfigurationResponse":
        return dc_td.CreateWorkerConfigurationResponse.make_one(res)

    def delete_connector(
        self,
        res: "bs_td.DeleteConnectorResponseTypeDef",
    ) -> "dc_td.DeleteConnectorResponse":
        return dc_td.DeleteConnectorResponse.make_one(res)

    def delete_custom_plugin(
        self,
        res: "bs_td.DeleteCustomPluginResponseTypeDef",
    ) -> "dc_td.DeleteCustomPluginResponse":
        return dc_td.DeleteCustomPluginResponse.make_one(res)

    def delete_worker_configuration(
        self,
        res: "bs_td.DeleteWorkerConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteWorkerConfigurationResponse":
        return dc_td.DeleteWorkerConfigurationResponse.make_one(res)

    def describe_connector(
        self,
        res: "bs_td.DescribeConnectorResponseTypeDef",
    ) -> "dc_td.DescribeConnectorResponse":
        return dc_td.DescribeConnectorResponse.make_one(res)

    def describe_connector_operation(
        self,
        res: "bs_td.DescribeConnectorOperationResponseTypeDef",
    ) -> "dc_td.DescribeConnectorOperationResponse":
        return dc_td.DescribeConnectorOperationResponse.make_one(res)

    def describe_custom_plugin(
        self,
        res: "bs_td.DescribeCustomPluginResponseTypeDef",
    ) -> "dc_td.DescribeCustomPluginResponse":
        return dc_td.DescribeCustomPluginResponse.make_one(res)

    def describe_worker_configuration(
        self,
        res: "bs_td.DescribeWorkerConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeWorkerConfigurationResponse":
        return dc_td.DescribeWorkerConfigurationResponse.make_one(res)

    def list_connector_operations(
        self,
        res: "bs_td.ListConnectorOperationsResponseTypeDef",
    ) -> "dc_td.ListConnectorOperationsResponse":
        return dc_td.ListConnectorOperationsResponse.make_one(res)

    def list_connectors(
        self,
        res: "bs_td.ListConnectorsResponseTypeDef",
    ) -> "dc_td.ListConnectorsResponse":
        return dc_td.ListConnectorsResponse.make_one(res)

    def list_custom_plugins(
        self,
        res: "bs_td.ListCustomPluginsResponseTypeDef",
    ) -> "dc_td.ListCustomPluginsResponse":
        return dc_td.ListCustomPluginsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_worker_configurations(
        self,
        res: "bs_td.ListWorkerConfigurationsResponseTypeDef",
    ) -> "dc_td.ListWorkerConfigurationsResponse":
        return dc_td.ListWorkerConfigurationsResponse.make_one(res)

    def update_connector(
        self,
        res: "bs_td.UpdateConnectorResponseTypeDef",
    ) -> "dc_td.UpdateConnectorResponse":
        return dc_td.UpdateConnectorResponse.make_one(res)


kafkaconnect_caster = KAFKACONNECTCaster()
