# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_securitylake import type_defs as bs_td


class SECURITYLAKECaster:

    def create_aws_log_source(
        self,
        res: "bs_td.CreateAwsLogSourceResponseTypeDef",
    ) -> "dc_td.CreateAwsLogSourceResponse":
        return dc_td.CreateAwsLogSourceResponse.make_one(res)

    def create_custom_log_source(
        self,
        res: "bs_td.CreateCustomLogSourceResponseTypeDef",
    ) -> "dc_td.CreateCustomLogSourceResponse":
        return dc_td.CreateCustomLogSourceResponse.make_one(res)

    def create_data_lake(
        self,
        res: "bs_td.CreateDataLakeResponseTypeDef",
    ) -> "dc_td.CreateDataLakeResponse":
        return dc_td.CreateDataLakeResponse.make_one(res)

    def create_subscriber(
        self,
        res: "bs_td.CreateSubscriberResponseTypeDef",
    ) -> "dc_td.CreateSubscriberResponse":
        return dc_td.CreateSubscriberResponse.make_one(res)

    def create_subscriber_notification(
        self,
        res: "bs_td.CreateSubscriberNotificationResponseTypeDef",
    ) -> "dc_td.CreateSubscriberNotificationResponse":
        return dc_td.CreateSubscriberNotificationResponse.make_one(res)

    def delete_aws_log_source(
        self,
        res: "bs_td.DeleteAwsLogSourceResponseTypeDef",
    ) -> "dc_td.DeleteAwsLogSourceResponse":
        return dc_td.DeleteAwsLogSourceResponse.make_one(res)

    def get_data_lake_exception_subscription(
        self,
        res: "bs_td.GetDataLakeExceptionSubscriptionResponseTypeDef",
    ) -> "dc_td.GetDataLakeExceptionSubscriptionResponse":
        return dc_td.GetDataLakeExceptionSubscriptionResponse.make_one(res)

    def get_data_lake_organization_configuration(
        self,
        res: "bs_td.GetDataLakeOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.GetDataLakeOrganizationConfigurationResponse":
        return dc_td.GetDataLakeOrganizationConfigurationResponse.make_one(res)

    def get_data_lake_sources(
        self,
        res: "bs_td.GetDataLakeSourcesResponseTypeDef",
    ) -> "dc_td.GetDataLakeSourcesResponse":
        return dc_td.GetDataLakeSourcesResponse.make_one(res)

    def get_subscriber(
        self,
        res: "bs_td.GetSubscriberResponseTypeDef",
    ) -> "dc_td.GetSubscriberResponse":
        return dc_td.GetSubscriberResponse.make_one(res)

    def list_data_lake_exceptions(
        self,
        res: "bs_td.ListDataLakeExceptionsResponseTypeDef",
    ) -> "dc_td.ListDataLakeExceptionsResponse":
        return dc_td.ListDataLakeExceptionsResponse.make_one(res)

    def list_data_lakes(
        self,
        res: "bs_td.ListDataLakesResponseTypeDef",
    ) -> "dc_td.ListDataLakesResponse":
        return dc_td.ListDataLakesResponse.make_one(res)

    def list_log_sources(
        self,
        res: "bs_td.ListLogSourcesResponseTypeDef",
    ) -> "dc_td.ListLogSourcesResponse":
        return dc_td.ListLogSourcesResponse.make_one(res)

    def list_subscribers(
        self,
        res: "bs_td.ListSubscribersResponseTypeDef",
    ) -> "dc_td.ListSubscribersResponse":
        return dc_td.ListSubscribersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_data_lake(
        self,
        res: "bs_td.UpdateDataLakeResponseTypeDef",
    ) -> "dc_td.UpdateDataLakeResponse":
        return dc_td.UpdateDataLakeResponse.make_one(res)

    def update_subscriber(
        self,
        res: "bs_td.UpdateSubscriberResponseTypeDef",
    ) -> "dc_td.UpdateSubscriberResponse":
        return dc_td.UpdateSubscriberResponse.make_one(res)

    def update_subscriber_notification(
        self,
        res: "bs_td.UpdateSubscriberNotificationResponseTypeDef",
    ) -> "dc_td.UpdateSubscriberNotificationResponse":
        return dc_td.UpdateSubscriberNotificationResponse.make_one(res)


securitylake_caster = SECURITYLAKECaster()
