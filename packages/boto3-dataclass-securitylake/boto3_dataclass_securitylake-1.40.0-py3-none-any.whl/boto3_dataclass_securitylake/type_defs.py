# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_securitylake import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AwsIdentity:
    boto3_raw_data: "type_defs.AwsIdentityTypeDef" = dataclasses.field()

    externalId = field("externalId")
    principal = field("principal")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsIdentityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsLogSourceConfiguration:
    boto3_raw_data: "type_defs.AwsLogSourceConfigurationTypeDef" = dataclasses.field()

    regions = field("regions")
    sourceName = field("sourceName")
    accounts = field("accounts")
    sourceVersion = field("sourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsLogSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsLogSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsLogSourceResource:
    boto3_raw_data: "type_defs.AwsLogSourceResourceTypeDef" = dataclasses.field()

    sourceName = field("sourceName")
    sourceVersion = field("sourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsLogSourceResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsLogSourceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeExceptionSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateDataLakeExceptionSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    notificationEndpoint = field("notificationEndpoint")
    subscriptionProtocol = field("subscriptionProtocol")
    exceptionTimeToLive = field("exceptionTimeToLive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataLakeExceptionSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeExceptionSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLogSourceAttributes:
    boto3_raw_data: "type_defs.CustomLogSourceAttributesTypeDef" = dataclasses.field()

    crawlerArn = field("crawlerArn")
    databaseArn = field("databaseArn")
    tableArn = field("tableArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLogSourceAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLogSourceAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLogSourceCrawlerConfiguration:
    boto3_raw_data: "type_defs.CustomLogSourceCrawlerConfigurationTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomLogSourceCrawlerConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLogSourceCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLogSourceProvider:
    boto3_raw_data: "type_defs.CustomLogSourceProviderTypeDef" = dataclasses.field()

    location = field("location")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLogSourceProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLogSourceProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeEncryptionConfiguration:
    boto3_raw_data: "type_defs.DataLakeEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataLakeEncryptionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeException:
    boto3_raw_data: "type_defs.DataLakeExceptionTypeDef" = dataclasses.field()

    exception = field("exception")
    region = field("region")
    remediation = field("remediation")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakeExceptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeLifecycleExpiration:
    boto3_raw_data: "type_defs.DataLakeLifecycleExpirationTypeDef" = dataclasses.field()

    days = field("days")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeLifecycleExpirationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeLifecycleExpirationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeLifecycleTransition:
    boto3_raw_data: "type_defs.DataLakeLifecycleTransitionTypeDef" = dataclasses.field()

    days = field("days")
    storageClass = field("storageClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeLifecycleTransitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeLifecycleTransitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeReplicationConfigurationOutput:
    boto3_raw_data: "type_defs.DataLakeReplicationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    regions = field("regions")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataLakeReplicationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeReplicationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeReplicationConfiguration:
    boto3_raw_data: "type_defs.DataLakeReplicationConfigurationTypeDef" = (
        dataclasses.field()
    )

    regions = field("regions")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataLakeReplicationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeSourceStatus:
    boto3_raw_data: "type_defs.DataLakeSourceStatusTypeDef" = dataclasses.field()

    resource = field("resource")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeSourceStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeSourceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeUpdateException:
    boto3_raw_data: "type_defs.DataLakeUpdateExceptionTypeDef" = dataclasses.field()

    code = field("code")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeUpdateExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeUpdateExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomLogSourceRequest:
    boto3_raw_data: "type_defs.DeleteCustomLogSourceRequestTypeDef" = (
        dataclasses.field()
    )

    sourceName = field("sourceName")
    sourceVersion = field("sourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomLogSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomLogSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataLakeRequest:
    boto3_raw_data: "type_defs.DeleteDataLakeRequestTypeDef" = dataclasses.field()

    regions = field("regions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataLakeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataLakeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriberNotificationRequest:
    boto3_raw_data: "type_defs.DeleteSubscriberNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    subscriberId = field("subscriberId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSubscriberNotificationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriberNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriberRequest:
    boto3_raw_data: "type_defs.DeleteSubscriberRequestTypeDef" = dataclasses.field()

    subscriberId = field("subscriberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeSourcesRequest:
    boto3_raw_data: "type_defs.GetDataLakeSourcesRequestTypeDef" = dataclasses.field()

    accounts = field("accounts")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriberRequest:
    boto3_raw_data: "type_defs.GetSubscriberRequestTypeDef" = dataclasses.field()

    subscriberId = field("subscriberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpsNotificationConfiguration:
    boto3_raw_data: "type_defs.HttpsNotificationConfigurationTypeDef" = (
        dataclasses.field()
    )

    endpoint = field("endpoint")
    targetRoleArn = field("targetRoleArn")
    authorizationApiKeyName = field("authorizationApiKeyName")
    authorizationApiKeyValue = field("authorizationApiKeyValue")
    httpMethod = field("httpMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpsNotificationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpsNotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeExceptionsRequest:
    boto3_raw_data: "type_defs.ListDataLakeExceptionsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    regions = field("regions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataLakeExceptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeExceptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakesRequest:
    boto3_raw_data: "type_defs.ListDataLakesRequestTypeDef" = dataclasses.field()

    regions = field("regions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataLakesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscribersRequest:
    boto3_raw_data: "type_defs.ListSubscribersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscribersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscribersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDataLakeDelegatedAdministratorRequest:
    boto3_raw_data: "type_defs.RegisterDataLakeDelegatedAdministratorRequestTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterDataLakeDelegatedAdministratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDataLakeDelegatedAdministratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataLakeExceptionSubscriptionRequest:
    boto3_raw_data: "type_defs.UpdateDataLakeExceptionSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    notificationEndpoint = field("notificationEndpoint")
    subscriptionProtocol = field("subscriptionProtocol")
    exceptionTimeToLive = field("exceptionTimeToLive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataLakeExceptionSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeExceptionSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAwsLogSourceRequest:
    boto3_raw_data: "type_defs.CreateAwsLogSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def sources(self):  # pragma: no cover
        return AwsLogSourceConfiguration.make_many(self.boto3_raw_data["sources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAwsLogSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAwsLogSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAwsLogSourceRequest:
    boto3_raw_data: "type_defs.DeleteAwsLogSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def sources(self):  # pragma: no cover
        return AwsLogSourceConfiguration.make_many(self.boto3_raw_data["sources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAwsLogSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAwsLogSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeAutoEnableNewAccountConfigurationOutput:
    boto3_raw_data: (
        "type_defs.DataLakeAutoEnableNewAccountConfigurationOutputTypeDef"
    ) = dataclasses.field()

    region = field("region")

    @cached_property
    def sources(self):  # pragma: no cover
        return AwsLogSourceResource.make_many(self.boto3_raw_data["sources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataLakeAutoEnableNewAccountConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DataLakeAutoEnableNewAccountConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeAutoEnableNewAccountConfiguration:
    boto3_raw_data: "type_defs.DataLakeAutoEnableNewAccountConfigurationTypeDef" = (
        dataclasses.field()
    )

    region = field("region")

    @cached_property
    def sources(self):  # pragma: no cover
        return AwsLogSourceResource.make_many(self.boto3_raw_data["sources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataLakeAutoEnableNewAccountConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeAutoEnableNewAccountConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAwsLogSourceResponse:
    boto3_raw_data: "type_defs.CreateAwsLogSourceResponseTypeDef" = dataclasses.field()

    failed = field("failed")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAwsLogSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAwsLogSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriberNotificationResponse:
    boto3_raw_data: "type_defs.CreateSubscriberNotificationResponseTypeDef" = (
        dataclasses.field()
    )

    subscriberEndpoint = field("subscriberEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSubscriberNotificationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriberNotificationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAwsLogSourceResponse:
    boto3_raw_data: "type_defs.DeleteAwsLogSourceResponseTypeDef" = dataclasses.field()

    failed = field("failed")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAwsLogSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAwsLogSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeExceptionSubscriptionResponse:
    boto3_raw_data: "type_defs.GetDataLakeExceptionSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    exceptionTimeToLive = field("exceptionTimeToLive")
    notificationEndpoint = field("notificationEndpoint")
    subscriptionProtocol = field("subscriptionProtocol")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataLakeExceptionSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeExceptionSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriberNotificationResponse:
    boto3_raw_data: "type_defs.UpdateSubscriberNotificationResponseTypeDef" = (
        dataclasses.field()
    )

    subscriberEndpoint = field("subscriberEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriberNotificationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriberNotificationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLogSourceConfiguration:
    boto3_raw_data: "type_defs.CustomLogSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return CustomLogSourceCrawlerConfiguration.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @cached_property
    def providerIdentity(self):  # pragma: no cover
        return AwsIdentity.make_one(self.boto3_raw_data["providerIdentity"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLogSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLogSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLogSourceResource:
    boto3_raw_data: "type_defs.CustomLogSourceResourceTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return CustomLogSourceAttributes.make_one(self.boto3_raw_data["attributes"])

    @cached_property
    def provider(self):  # pragma: no cover
        return CustomLogSourceProvider.make_one(self.boto3_raw_data["provider"])

    sourceName = field("sourceName")
    sourceVersion = field("sourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLogSourceResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLogSourceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeExceptionsResponse:
    boto3_raw_data: "type_defs.ListDataLakeExceptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def exceptions(self):  # pragma: no cover
        return DataLakeException.make_many(self.boto3_raw_data["exceptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataLakeExceptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeExceptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeLifecycleConfigurationOutput:
    boto3_raw_data: "type_defs.DataLakeLifecycleConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def expiration(self):  # pragma: no cover
        return DataLakeLifecycleExpiration.make_one(self.boto3_raw_data["expiration"])

    @cached_property
    def transitions(self):  # pragma: no cover
        return DataLakeLifecycleTransition.make_many(self.boto3_raw_data["transitions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataLakeLifecycleConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeLifecycleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeLifecycleConfiguration:
    boto3_raw_data: "type_defs.DataLakeLifecycleConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def expiration(self):  # pragma: no cover
        return DataLakeLifecycleExpiration.make_one(self.boto3_raw_data["expiration"])

    @cached_property
    def transitions(self):  # pragma: no cover
        return DataLakeLifecycleTransition.make_many(self.boto3_raw_data["transitions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataLakeLifecycleConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeLifecycleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeSource:
    boto3_raw_data: "type_defs.DataLakeSourceTypeDef" = dataclasses.field()

    account = field("account")
    eventClasses = field("eventClasses")
    sourceName = field("sourceName")

    @cached_property
    def sourceStatuses(self):  # pragma: no cover
        return DataLakeSourceStatus.make_many(self.boto3_raw_data["sourceStatuses"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakeSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataLakeSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeUpdateStatus:
    boto3_raw_data: "type_defs.DataLakeUpdateStatusTypeDef" = dataclasses.field()

    @cached_property
    def exception(self):  # pragma: no cover
        return DataLakeUpdateException.make_one(self.boto3_raw_data["exception"])

    requestId = field("requestId")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeUpdateStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeUpdateStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeSourcesRequestPaginate:
    boto3_raw_data: "type_defs.GetDataLakeSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accounts = field("accounts")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataLakeSourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeExceptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataLakeExceptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    regions = field("regions")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataLakeExceptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeExceptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscribersRequestPaginate:
    boto3_raw_data: "type_defs.ListSubscribersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSubscribersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscribersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def httpsNotificationConfiguration(self):  # pragma: no cover
        return HttpsNotificationConfiguration.make_one(
            self.boto3_raw_data["httpsNotificationConfiguration"]
        )

    sqsNotificationConfiguration = field("sqsNotificationConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeOrganizationConfigurationResponse:
    boto3_raw_data: "type_defs.GetDataLakeOrganizationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def autoEnableNewAccount(self):  # pragma: no cover
        return DataLakeAutoEnableNewAccountConfigurationOutput.make_many(
            self.boto3_raw_data["autoEnableNewAccount"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataLakeOrganizationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeOrganizationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomLogSourceRequest:
    boto3_raw_data: "type_defs.CreateCustomLogSourceRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return CustomLogSourceConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    sourceName = field("sourceName")
    eventClasses = field("eventClasses")
    sourceVersion = field("sourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomLogSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomLogSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomLogSourceResponse:
    boto3_raw_data: "type_defs.CreateCustomLogSourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def source(self):  # pragma: no cover
        return CustomLogSourceResource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCustomLogSourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomLogSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSourceResource:
    boto3_raw_data: "type_defs.LogSourceResourceTypeDef" = dataclasses.field()

    @cached_property
    def awsLogSource(self):  # pragma: no cover
        return AwsLogSourceResource.make_one(self.boto3_raw_data["awsLogSource"])

    @cached_property
    def customLogSource(self):  # pragma: no cover
        return CustomLogSourceResource.make_one(self.boto3_raw_data["customLogSource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogSourceResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogSourceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeSourcesResponse:
    boto3_raw_data: "type_defs.GetDataLakeSourcesResponseTypeDef" = dataclasses.field()

    dataLakeArn = field("dataLakeArn")

    @cached_property
    def dataLakeSources(self):  # pragma: no cover
        return DataLakeSource.make_many(self.boto3_raw_data["dataLakeSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeResource:
    boto3_raw_data: "type_defs.DataLakeResourceTypeDef" = dataclasses.field()

    dataLakeArn = field("dataLakeArn")
    region = field("region")
    createStatus = field("createStatus")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return DataLakeEncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def lifecycleConfiguration(self):  # pragma: no cover
        return DataLakeLifecycleConfigurationOutput.make_one(
            self.boto3_raw_data["lifecycleConfiguration"]
        )

    @cached_property
    def replicationConfiguration(self):  # pragma: no cover
        return DataLakeReplicationConfigurationOutput.make_one(
            self.boto3_raw_data["replicationConfiguration"]
        )

    s3BucketArn = field("s3BucketArn")

    @cached_property
    def updateStatus(self):  # pragma: no cover
        return DataLakeUpdateStatus.make_one(self.boto3_raw_data["updateStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakeResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriberNotificationRequest:
    boto3_raw_data: "type_defs.CreateSubscriberNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(self.boto3_raw_data["configuration"])

    subscriberId = field("subscriberId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSubscriberNotificationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriberNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriberNotificationRequest:
    boto3_raw_data: "type_defs.UpdateSubscriberNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(self.boto3_raw_data["configuration"])

    subscriberId = field("subscriberId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriberNotificationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriberNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeOrganizationConfigurationRequest:
    boto3_raw_data: (
        "type_defs.CreateDataLakeOrganizationConfigurationRequestTypeDef"
    ) = dataclasses.field()

    autoEnableNewAccount = field("autoEnableNewAccount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataLakeOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateDataLakeOrganizationConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataLakeOrganizationConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteDataLakeOrganizationConfigurationRequestTypeDef"
    ) = dataclasses.field()

    autoEnableNewAccount = field("autoEnableNewAccount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataLakeOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteDataLakeOrganizationConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriberRequest:
    boto3_raw_data: "type_defs.CreateSubscriberRequestTypeDef" = dataclasses.field()

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSourceResource.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def subscriberIdentity(self):  # pragma: no cover
        return AwsIdentity.make_one(self.boto3_raw_data["subscriberIdentity"])

    subscriberName = field("subscriberName")
    accessTypes = field("accessTypes")
    subscriberDescription = field("subscriberDescription")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogSourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListLogSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accounts = field("accounts")
    regions = field("regions")

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSourceResource.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLogSourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogSourcesRequest:
    boto3_raw_data: "type_defs.ListLogSourcesRequestTypeDef" = dataclasses.field()

    accounts = field("accounts")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    regions = field("regions")

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSourceResource.make_many(self.boto3_raw_data["sources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSource:
    boto3_raw_data: "type_defs.LogSourceTypeDef" = dataclasses.field()

    account = field("account")
    region = field("region")

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSourceResource.make_many(self.boto3_raw_data["sources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriberResource:
    boto3_raw_data: "type_defs.SubscriberResourceTypeDef" = dataclasses.field()

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSourceResource.make_many(self.boto3_raw_data["sources"])

    subscriberArn = field("subscriberArn")
    subscriberId = field("subscriberId")

    @cached_property
    def subscriberIdentity(self):  # pragma: no cover
        return AwsIdentity.make_one(self.boto3_raw_data["subscriberIdentity"])

    subscriberName = field("subscriberName")
    accessTypes = field("accessTypes")
    createdAt = field("createdAt")
    resourceShareArn = field("resourceShareArn")
    resourceShareName = field("resourceShareName")
    roleArn = field("roleArn")
    s3BucketArn = field("s3BucketArn")
    subscriberDescription = field("subscriberDescription")
    subscriberEndpoint = field("subscriberEndpoint")
    subscriberStatus = field("subscriberStatus")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriberResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriberResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriberRequest:
    boto3_raw_data: "type_defs.UpdateSubscriberRequestTypeDef" = dataclasses.field()

    subscriberId = field("subscriberId")

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSourceResource.make_many(self.boto3_raw_data["sources"])

    subscriberDescription = field("subscriberDescription")

    @cached_property
    def subscriberIdentity(self):  # pragma: no cover
        return AwsIdentity.make_one(self.boto3_raw_data["subscriberIdentity"])

    subscriberName = field("subscriberName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeConfiguration:
    boto3_raw_data: "type_defs.DataLakeConfigurationTypeDef" = dataclasses.field()

    region = field("region")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return DataLakeEncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    lifecycleConfiguration = field("lifecycleConfiguration")
    replicationConfiguration = field("replicationConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeResponse:
    boto3_raw_data: "type_defs.CreateDataLakeResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataLakes(self):  # pragma: no cover
        return DataLakeResource.make_many(self.boto3_raw_data["dataLakes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataLakeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakesResponse:
    boto3_raw_data: "type_defs.ListDataLakesResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataLakes(self):  # pragma: no cover
        return DataLakeResource.make_many(self.boto3_raw_data["dataLakes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataLakesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataLakeResponse:
    boto3_raw_data: "type_defs.UpdateDataLakeResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataLakes(self):  # pragma: no cover
        return DataLakeResource.make_many(self.boto3_raw_data["dataLakes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataLakeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogSourcesResponse:
    boto3_raw_data: "type_defs.ListLogSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def sources(self):  # pragma: no cover
        return LogSource.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriberResponse:
    boto3_raw_data: "type_defs.CreateSubscriberResponseTypeDef" = dataclasses.field()

    @cached_property
    def subscriber(self):  # pragma: no cover
        return SubscriberResource.make_one(self.boto3_raw_data["subscriber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubscriberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriberResponse:
    boto3_raw_data: "type_defs.GetSubscriberResponseTypeDef" = dataclasses.field()

    @cached_property
    def subscriber(self):  # pragma: no cover
        return SubscriberResource.make_one(self.boto3_raw_data["subscriber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscribersResponse:
    boto3_raw_data: "type_defs.ListSubscribersResponseTypeDef" = dataclasses.field()

    @cached_property
    def subscribers(self):  # pragma: no cover
        return SubscriberResource.make_many(self.boto3_raw_data["subscribers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscribersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscribersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriberResponse:
    boto3_raw_data: "type_defs.UpdateSubscriberResponseTypeDef" = dataclasses.field()

    @cached_property
    def subscriber(self):  # pragma: no cover
        return SubscriberResource.make_one(self.boto3_raw_data["subscriber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubscriberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeRequest:
    boto3_raw_data: "type_defs.CreateDataLakeRequestTypeDef" = dataclasses.field()

    @cached_property
    def configurations(self):  # pragma: no cover
        return DataLakeConfiguration.make_many(self.boto3_raw_data["configurations"])

    metaStoreManagerRoleArn = field("metaStoreManagerRoleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataLakeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataLakeRequest:
    boto3_raw_data: "type_defs.UpdateDataLakeRequestTypeDef" = dataclasses.field()

    @cached_property
    def configurations(self):  # pragma: no cover
        return DataLakeConfiguration.make_many(self.boto3_raw_data["configurations"])

    metaStoreManagerRoleArn = field("metaStoreManagerRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataLakeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
