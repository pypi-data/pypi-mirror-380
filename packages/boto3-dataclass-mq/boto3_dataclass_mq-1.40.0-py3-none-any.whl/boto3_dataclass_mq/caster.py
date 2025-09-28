# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mq import type_defs as bs_td


class MQCaster:

    def create_broker(
        self,
        res: "bs_td.CreateBrokerResponseTypeDef",
    ) -> "dc_td.CreateBrokerResponse":
        return dc_td.CreateBrokerResponse.make_one(res)

    def create_configuration(
        self,
        res: "bs_td.CreateConfigurationResponseTypeDef",
    ) -> "dc_td.CreateConfigurationResponse":
        return dc_td.CreateConfigurationResponse.make_one(res)

    def create_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_broker(
        self,
        res: "bs_td.DeleteBrokerResponseTypeDef",
    ) -> "dc_td.DeleteBrokerResponse":
        return dc_td.DeleteBrokerResponse.make_one(res)

    def delete_configuration(
        self,
        res: "bs_td.DeleteConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteConfigurationResponse":
        return dc_td.DeleteConfigurationResponse.make_one(res)

    def delete_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_broker(
        self,
        res: "bs_td.DescribeBrokerResponseTypeDef",
    ) -> "dc_td.DescribeBrokerResponse":
        return dc_td.DescribeBrokerResponse.make_one(res)

    def describe_broker_engine_types(
        self,
        res: "bs_td.DescribeBrokerEngineTypesResponseTypeDef",
    ) -> "dc_td.DescribeBrokerEngineTypesResponse":
        return dc_td.DescribeBrokerEngineTypesResponse.make_one(res)

    def describe_broker_instance_options(
        self,
        res: "bs_td.DescribeBrokerInstanceOptionsResponseTypeDef",
    ) -> "dc_td.DescribeBrokerInstanceOptionsResponse":
        return dc_td.DescribeBrokerInstanceOptionsResponse.make_one(res)

    def describe_configuration(
        self,
        res: "bs_td.DescribeConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationResponse":
        return dc_td.DescribeConfigurationResponse.make_one(res)

    def describe_configuration_revision(
        self,
        res: "bs_td.DescribeConfigurationRevisionResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationRevisionResponse":
        return dc_td.DescribeConfigurationRevisionResponse.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResponseTypeDef",
    ) -> "dc_td.DescribeUserResponse":
        return dc_td.DescribeUserResponse.make_one(res)

    def list_brokers(
        self,
        res: "bs_td.ListBrokersResponseTypeDef",
    ) -> "dc_td.ListBrokersResponse":
        return dc_td.ListBrokersResponse.make_one(res)

    def list_configuration_revisions(
        self,
        res: "bs_td.ListConfigurationRevisionsResponseTypeDef",
    ) -> "dc_td.ListConfigurationRevisionsResponse":
        return dc_td.ListConfigurationRevisionsResponse.make_one(res)

    def list_configurations(
        self,
        res: "bs_td.ListConfigurationsResponseTypeDef",
    ) -> "dc_td.ListConfigurationsResponse":
        return dc_td.ListConfigurationsResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def promote(
        self,
        res: "bs_td.PromoteResponseTypeDef",
    ) -> "dc_td.PromoteResponse":
        return dc_td.PromoteResponse.make_one(res)

    def update_broker(
        self,
        res: "bs_td.UpdateBrokerResponseTypeDef",
    ) -> "dc_td.UpdateBrokerResponse":
        return dc_td.UpdateBrokerResponse.make_one(res)

    def update_configuration(
        self,
        res: "bs_td.UpdateConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateConfigurationResponse":
        return dc_td.UpdateConfigurationResponse.make_one(res)


mq_caster = MQCaster()
