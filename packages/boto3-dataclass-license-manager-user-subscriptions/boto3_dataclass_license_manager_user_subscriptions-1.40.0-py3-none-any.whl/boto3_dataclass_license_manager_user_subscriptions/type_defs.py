# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_license_manager_user_subscriptions import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class DomainNetworkSettingsOutput:
    boto3_raw_data: "type_defs.DomainNetworkSettingsOutputTypeDef" = dataclasses.field()

    Subnets = field("Subnets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainNetworkSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNetworkSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNetworkSettings:
    boto3_raw_data: "type_defs.DomainNetworkSettingsTypeDef" = dataclasses.field()

    Subnets = field("Subnets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainNetworkSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNetworkSettingsTypeDef"]
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
class SecretsManagerCredentialsProvider:
    boto3_raw_data: "type_defs.SecretsManagerCredentialsProviderTypeDef" = (
        dataclasses.field()
    )

    SecretId = field("SecretId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecretsManagerCredentialsProviderTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecretsManagerCredentialsProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseServerEndpointRequest:
    boto3_raw_data: "type_defs.DeleteLicenseServerEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseServerEndpointArn = field("LicenseServerEndpointArn")
    ServerType = field("ServerType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLicenseServerEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseServerEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    Operation = field("Operation")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SettingsOutput:
    boto3_raw_data: "type_defs.SettingsOutputTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    SecurityGroupId = field("SecurityGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseServer:
    boto3_raw_data: "type_defs.LicenseServerTypeDef" = dataclasses.field()

    ProvisioningStatus = field("ProvisioningStatus")
    HealthStatus = field("HealthStatus")
    Ipv4Address = field("Ipv4Address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicenseServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicenseServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerEndpoint:
    boto3_raw_data: "type_defs.ServerEndpointTypeDef" = dataclasses.field()

    Endpoint = field("Endpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerEndpointTypeDef"]],
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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class Settings:
    boto3_raw_data: "type_defs.SettingsTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    SecurityGroupId = field("SecurityGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class UpdateSettings:
    boto3_raw_data: "type_defs.UpdateSettingsTypeDef" = dataclasses.field()

    AddSubnets = field("AddSubnets")
    RemoveSubnets = field("RemoveSubnets")
    SecurityGroupId = field("SecurityGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseServerEndpointResponse:
    boto3_raw_data: "type_defs.CreateLicenseServerEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityProviderArn = field("IdentityProviderArn")
    LicenseServerEndpointArn = field("LicenseServerEndpointArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseServerEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseServerEndpointResponseTypeDef"]
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

    Tags = field("Tags")

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
class CredentialsProvider:
    boto3_raw_data: "type_defs.CredentialsProviderTypeDef" = dataclasses.field()

    @cached_property
    def SecretsManagerCredentialsProvider(self):  # pragma: no cover
        return SecretsManagerCredentialsProvider.make_one(
            self.boto3_raw_data["SecretsManagerCredentialsProvider"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CredentialsProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CredentialsProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersRequest:
    boto3_raw_data: "type_defs.ListIdentityProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityProvidersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequest:
    boto3_raw_data: "type_defs.ListInstancesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseServerEndpointsRequest:
    boto3_raw_data: "type_defs.ListLicenseServerEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseServerEndpointsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseServerEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseServerEndpoint:
    boto3_raw_data: "type_defs.LicenseServerEndpointTypeDef" = dataclasses.field()

    IdentityProviderArn = field("IdentityProviderArn")
    ServerType = field("ServerType")

    @cached_property
    def ServerEndpoint(self):  # pragma: no cover
        return ServerEndpoint.make_one(self.boto3_raw_data["ServerEndpoint"])

    StatusMessage = field("StatusMessage")
    LicenseServerEndpointId = field("LicenseServerEndpointId")
    LicenseServerEndpointArn = field("LicenseServerEndpointArn")
    LicenseServerEndpointProvisioningStatus = field(
        "LicenseServerEndpointProvisioningStatus"
    )

    @cached_property
    def LicenseServers(self):  # pragma: no cover
        return LicenseServer.make_many(self.boto3_raw_data["LicenseServers"])

    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseServerEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseServerEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersRequestPaginate:
    boto3_raw_data: "type_defs.ListIdentityProvidersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityProvidersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseServerEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListLicenseServerEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseServerEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseServerEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveDirectorySettingsOutput:
    boto3_raw_data: "type_defs.ActiveDirectorySettingsOutputTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    DomainIpv4List = field("DomainIpv4List")

    @cached_property
    def DomainCredentialsProvider(self):  # pragma: no cover
        return CredentialsProvider.make_one(
            self.boto3_raw_data["DomainCredentialsProvider"]
        )

    @cached_property
    def DomainNetworkSettings(self):  # pragma: no cover
        return DomainNetworkSettingsOutput.make_one(
            self.boto3_raw_data["DomainNetworkSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActiveDirectorySettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveDirectorySettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveDirectorySettings:
    boto3_raw_data: "type_defs.ActiveDirectorySettingsTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DomainIpv4List = field("DomainIpv4List")

    @cached_property
    def DomainCredentialsProvider(self):  # pragma: no cover
        return CredentialsProvider.make_one(
            self.boto3_raw_data["DomainCredentialsProvider"]
        )

    @cached_property
    def DomainNetworkSettings(self):  # pragma: no cover
        return DomainNetworkSettings.make_one(
            self.boto3_raw_data["DomainNetworkSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActiveDirectorySettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveDirectorySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsSalSettings:
    boto3_raw_data: "type_defs.RdsSalSettingsTypeDef" = dataclasses.field()

    @cached_property
    def RdsSalCredentialsProvider(self):  # pragma: no cover
        return CredentialsProvider.make_one(
            self.boto3_raw_data["RdsSalCredentialsProvider"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsSalSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RdsSalSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseServerEndpointResponse:
    boto3_raw_data: "type_defs.DeleteLicenseServerEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LicenseServerEndpoint(self):  # pragma: no cover
        return LicenseServerEndpoint.make_one(
            self.boto3_raw_data["LicenseServerEndpoint"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLicenseServerEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseServerEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseServerEndpointsResponse:
    boto3_raw_data: "type_defs.ListLicenseServerEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LicenseServerEndpoints(self):  # pragma: no cover
        return LicenseServerEndpoint.make_many(
            self.boto3_raw_data["LicenseServerEndpoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseServerEndpointsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseServerEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveDirectoryIdentityProviderOutput:
    boto3_raw_data: "type_defs.ActiveDirectoryIdentityProviderOutputTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @cached_property
    def ActiveDirectorySettings(self):  # pragma: no cover
        return ActiveDirectorySettingsOutput.make_one(
            self.boto3_raw_data["ActiveDirectorySettings"]
        )

    ActiveDirectoryType = field("ActiveDirectoryType")
    IsSharedActiveDirectory = field("IsSharedActiveDirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActiveDirectoryIdentityProviderOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveDirectoryIdentityProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveDirectoryIdentityProvider:
    boto3_raw_data: "type_defs.ActiveDirectoryIdentityProviderTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @cached_property
    def ActiveDirectorySettings(self):  # pragma: no cover
        return ActiveDirectorySettings.make_one(
            self.boto3_raw_data["ActiveDirectorySettings"]
        )

    ActiveDirectoryType = field("ActiveDirectoryType")
    IsSharedActiveDirectory = field("IsSharedActiveDirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActiveDirectoryIdentityProviderTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveDirectoryIdentityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSettings:
    boto3_raw_data: "type_defs.ServerSettingsTypeDef" = dataclasses.field()

    @cached_property
    def RdsSalSettings(self):  # pragma: no cover
        return RdsSalSettings.make_one(self.boto3_raw_data["RdsSalSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderOutput:
    boto3_raw_data: "type_defs.IdentityProviderOutputTypeDef" = dataclasses.field()

    @cached_property
    def ActiveDirectoryIdentityProvider(self):  # pragma: no cover
        return ActiveDirectoryIdentityProviderOutput.make_one(
            self.boto3_raw_data["ActiveDirectoryIdentityProvider"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProvider:
    boto3_raw_data: "type_defs.IdentityProviderTypeDef" = dataclasses.field()

    @cached_property
    def ActiveDirectoryIdentityProvider(self):  # pragma: no cover
        return ActiveDirectoryIdentityProvider.make_one(
            self.boto3_raw_data["ActiveDirectoryIdentityProvider"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseServerSettings:
    boto3_raw_data: "type_defs.LicenseServerSettingsTypeDef" = dataclasses.field()

    ServerType = field("ServerType")

    @cached_property
    def ServerSettings(self):  # pragma: no cover
        return ServerSettings.make_one(self.boto3_raw_data["ServerSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseServerSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseServerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderSummary:
    boto3_raw_data: "type_defs.IdentityProviderSummaryTypeDef" = dataclasses.field()

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderOutput.make_one(self.boto3_raw_data["IdentityProvider"])

    @cached_property
    def Settings(self):  # pragma: no cover
        return SettingsOutput.make_one(self.boto3_raw_data["Settings"])

    Product = field("Product")
    Status = field("Status")
    IdentityProviderArn = field("IdentityProviderArn")
    FailureMessage = field("FailureMessage")
    OwnerAccountId = field("OwnerAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceSummary:
    boto3_raw_data: "type_defs.InstanceSummaryTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Status = field("Status")
    Products = field("Products")
    LastStatusCheckDate = field("LastStatusCheckDate")
    StatusMessage = field("StatusMessage")
    OwnerAccountId = field("OwnerAccountId")

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderOutput.make_one(self.boto3_raw_data["IdentityProvider"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceUserSummary:
    boto3_raw_data: "type_defs.InstanceUserSummaryTypeDef" = dataclasses.field()

    Username = field("Username")
    InstanceId = field("InstanceId")

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderOutput.make_one(self.boto3_raw_data["IdentityProvider"])

    Status = field("Status")
    InstanceUserArn = field("InstanceUserArn")
    StatusMessage = field("StatusMessage")
    Domain = field("Domain")
    AssociationDate = field("AssociationDate")
    DisassociationDate = field("DisassociationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceUserSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceUserSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductUserSummary:
    boto3_raw_data: "type_defs.ProductUserSummaryTypeDef" = dataclasses.field()

    Username = field("Username")
    Product = field("Product")

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderOutput.make_one(self.boto3_raw_data["IdentityProvider"])

    Status = field("Status")
    ProductUserArn = field("ProductUserArn")
    StatusMessage = field("StatusMessage")
    Domain = field("Domain")
    SubscriptionStartDate = field("SubscriptionStartDate")
    SubscriptionEndDate = field("SubscriptionEndDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductUserSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductUserSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseServerEndpointRequest:
    boto3_raw_data: "type_defs.CreateLicenseServerEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityProviderArn = field("IdentityProviderArn")

    @cached_property
    def LicenseServerSettings(self):  # pragma: no cover
        return LicenseServerSettings.make_one(
            self.boto3_raw_data["LicenseServerSettings"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseServerEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseServerEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterIdentityProviderResponse:
    boto3_raw_data: "type_defs.DeregisterIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProviderSummary(self):  # pragma: no cover
        return IdentityProviderSummary.make_one(
            self.boto3_raw_data["IdentityProviderSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterIdentityProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersResponse:
    boto3_raw_data: "type_defs.ListIdentityProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProviderSummaries(self):  # pragma: no cover
        return IdentityProviderSummary.make_many(
            self.boto3_raw_data["IdentityProviderSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentityProvidersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterIdentityProviderResponse:
    boto3_raw_data: "type_defs.RegisterIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProviderSummary(self):  # pragma: no cover
        return IdentityProviderSummary.make_one(
            self.boto3_raw_data["IdentityProviderSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterIdentityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentityProviderSettingsResponse:
    boto3_raw_data: "type_defs.UpdateIdentityProviderSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProviderSummary(self):  # pragma: no cover
        return IdentityProviderSummary.make_one(
            self.boto3_raw_data["IdentityProviderSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIdentityProviderSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentityProviderSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesResponse:
    boto3_raw_data: "type_defs.ListInstancesResponseTypeDef" = dataclasses.field()

    @cached_property
    def InstanceSummaries(self):  # pragma: no cover
        return InstanceSummary.make_many(self.boto3_raw_data["InstanceSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserResponse:
    boto3_raw_data: "type_defs.AssociateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def InstanceUserSummary(self):  # pragma: no cover
        return InstanceUserSummary.make_one(self.boto3_raw_data["InstanceUserSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateUserResponse:
    boto3_raw_data: "type_defs.DisassociateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def InstanceUserSummary(self):  # pragma: no cover
        return InstanceUserSummary.make_one(self.boto3_raw_data["InstanceUserSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserAssociationsResponse:
    boto3_raw_data: "type_defs.ListUserAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceUserSummaries(self):  # pragma: no cover
        return InstanceUserSummary.make_many(
            self.boto3_raw_data["InstanceUserSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserAssociationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProductSubscriptionsResponse:
    boto3_raw_data: "type_defs.ListProductSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProductUserSummaries(self):  # pragma: no cover
        return ProductUserSummary.make_many(self.boto3_raw_data["ProductUserSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProductSubscriptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProductSubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProductSubscriptionResponse:
    boto3_raw_data: "type_defs.StartProductSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProductUserSummary(self):  # pragma: no cover
        return ProductUserSummary.make_one(self.boto3_raw_data["ProductUserSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartProductSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProductSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopProductSubscriptionResponse:
    boto3_raw_data: "type_defs.StopProductSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProductUserSummary(self):  # pragma: no cover
        return ProductUserSummary.make_one(self.boto3_raw_data["ProductUserSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopProductSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopProductSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserRequest:
    boto3_raw_data: "type_defs.AssociateUserRequestTypeDef" = dataclasses.field()

    Username = field("Username")
    InstanceId = field("InstanceId")
    IdentityProvider = field("IdentityProvider")
    Domain = field("Domain")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterIdentityProviderRequest:
    boto3_raw_data: "type_defs.DeregisterIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityProvider = field("IdentityProvider")
    Product = field("Product")
    IdentityProviderArn = field("IdentityProviderArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterIdentityProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateUserRequest:
    boto3_raw_data: "type_defs.DisassociateUserRequestTypeDef" = dataclasses.field()

    Username = field("Username")
    InstanceId = field("InstanceId")
    IdentityProvider = field("IdentityProvider")
    InstanceUserArn = field("InstanceUserArn")
    Domain = field("Domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProductSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListProductSubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    IdentityProvider = field("IdentityProvider")
    Product = field("Product")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProductSubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProductSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProductSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListProductSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityProvider = field("IdentityProvider")
    Product = field("Product")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProductSubscriptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProductSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListUserAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    IdentityProvider = field("IdentityProvider")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUserAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserAssociationsRequest:
    boto3_raw_data: "type_defs.ListUserAssociationsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    IdentityProvider = field("IdentityProvider")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserAssociationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterIdentityProviderRequest:
    boto3_raw_data: "type_defs.RegisterIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityProvider = field("IdentityProvider")
    Product = field("Product")
    Settings = field("Settings")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProductSubscriptionRequest:
    boto3_raw_data: "type_defs.StartProductSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    IdentityProvider = field("IdentityProvider")
    Product = field("Product")
    Domain = field("Domain")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartProductSubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProductSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopProductSubscriptionRequest:
    boto3_raw_data: "type_defs.StopProductSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    IdentityProvider = field("IdentityProvider")
    Product = field("Product")
    ProductUserArn = field("ProductUserArn")
    Domain = field("Domain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopProductSubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopProductSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentityProviderSettingsRequest:
    boto3_raw_data: "type_defs.UpdateIdentityProviderSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UpdateSettings(self):  # pragma: no cover
        return UpdateSettings.make_one(self.boto3_raw_data["UpdateSettings"])

    IdentityProvider = field("IdentityProvider")
    Product = field("Product")
    IdentityProviderArn = field("IdentityProviderArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIdentityProviderSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentityProviderSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
