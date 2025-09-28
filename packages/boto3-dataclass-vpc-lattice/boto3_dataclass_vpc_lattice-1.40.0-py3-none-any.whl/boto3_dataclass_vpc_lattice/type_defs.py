# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_vpc_lattice import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessLogSubscriptionSummary:
    boto3_raw_data: "type_defs.AccessLogSubscriptionSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    destinationArn = field("destinationArn")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    resourceArn = field("resourceArn")
    resourceId = field("resourceId")
    serviceNetworkLogType = field("serviceNetworkLogType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessLogSubscriptionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessLogSubscriptionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArnResource:
    boto3_raw_data: "type_defs.ArnResourceTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArnResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArnResourceTypeDef"]]
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
class RuleUpdateFailure:
    boto3_raw_data: "type_defs.RuleUpdateFailureTypeDef" = dataclasses.field()

    failureCode = field("failureCode")
    failureMessage = field("failureMessage")
    ruleIdentifier = field("ruleIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleUpdateFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleUpdateFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessLogSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateAccessLogSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    destinationArn = field("destinationArn")
    resourceIdentifier = field("resourceIdentifier")
    clientToken = field("clientToken")
    serviceNetworkLogType = field("serviceNetworkLogType")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessLogSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessLogSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceGatewayRequest:
    boto3_raw_data: "type_defs.CreateResourceGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    subnetIds = field("subnetIds")
    vpcIdentifier = field("vpcIdentifier")
    clientToken = field("clientToken")
    ipAddressType = field("ipAddressType")
    securityGroupIds = field("securityGroupIds")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharingConfig:
    boto3_raw_data: "type_defs.SharingConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SharingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SharingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkResourceAssociationRequest:
    boto3_raw_data: (
        "type_defs.CreateServiceNetworkResourceAssociationRequestTypeDef"
    ) = dataclasses.field()

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceNetworkResourceAssociationRequestTypeDef"
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
                "type_defs.CreateServiceNetworkResourceAssociationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkServiceAssociationRequest:
    boto3_raw_data: "type_defs.CreateServiceNetworkServiceAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceIdentifier = field("serviceIdentifier")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceNetworkServiceAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceNetworkServiceAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsEntry:
    boto3_raw_data: "type_defs.DnsEntryTypeDef" = dataclasses.field()

    domainName = field("domainName")
    hostedZoneId = field("hostedZoneId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DnsEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DnsEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkVpcAssociationRequest:
    boto3_raw_data: "type_defs.CreateServiceNetworkVpcAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceNetworkIdentifier = field("serviceNetworkIdentifier")
    vpcIdentifier = field("vpcIdentifier")
    clientToken = field("clientToken")
    securityGroupIds = field("securityGroupIds")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceNetworkVpcAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceNetworkVpcAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceRequest:
    boto3_raw_data: "type_defs.CreateServiceRequestTypeDef" = dataclasses.field()

    name = field("name")
    authType = field("authType")
    certificateArn = field("certificateArn")
    clientToken = field("clientToken")
    customDomainName = field("customDomainName")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessLogSubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteAccessLogSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    accessLogSubscriptionIdentifier = field("accessLogSubscriptionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessLogSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessLogSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuthPolicyRequest:
    boto3_raw_data: "type_defs.DeleteAuthPolicyRequestTypeDef" = dataclasses.field()

    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAuthPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuthPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteListenerRequest:
    boto3_raw_data: "type_defs.DeleteListenerRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteResourceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResourceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceEndpointAssociationRequest:
    boto3_raw_data: "type_defs.DeleteResourceEndpointAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceEndpointAssociationIdentifier = field(
        "resourceEndpointAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResourceEndpointAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceEndpointAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceGatewayRequest:
    boto3_raw_data: "type_defs.DeleteResourceGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    resourceGatewayIdentifier = field("resourceGatewayIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleRequest:
    boto3_raw_data: "type_defs.DeleteRuleRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    ruleIdentifier = field("ruleIdentifier")
    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkRequest:
    boto3_raw_data: "type_defs.DeleteServiceNetworkRequestTypeDef" = dataclasses.field()

    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkResourceAssociationRequest:
    boto3_raw_data: (
        "type_defs.DeleteServiceNetworkResourceAssociationRequestTypeDef"
    ) = dataclasses.field()

    serviceNetworkResourceAssociationIdentifier = field(
        "serviceNetworkResourceAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceNetworkResourceAssociationRequestTypeDef"
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
                "type_defs.DeleteServiceNetworkResourceAssociationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkServiceAssociationRequest:
    boto3_raw_data: "type_defs.DeleteServiceNetworkServiceAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceNetworkServiceAssociationIdentifier = field(
        "serviceNetworkServiceAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceNetworkServiceAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceNetworkServiceAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkVpcAssociationRequest:
    boto3_raw_data: "type_defs.DeleteServiceNetworkVpcAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceNetworkVpcAssociationIdentifier = field(
        "serviceNetworkVpcAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceNetworkVpcAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceNetworkVpcAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceRequest:
    boto3_raw_data: "type_defs.DeleteServiceRequestTypeDef" = dataclasses.field()

    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTargetGroupRequest:
    boto3_raw_data: "type_defs.DeleteTargetGroupRequestTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTargetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTargetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    id = field("id")
    port = field("port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetFailure:
    boto3_raw_data: "type_defs.TargetFailureTypeDef" = dataclasses.field()

    failureCode = field("failureCode")
    failureMessage = field("failureMessage")
    id = field("id")
    port = field("port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetFailureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsResource:
    boto3_raw_data: "type_defs.DnsResourceTypeDef" = dataclasses.field()

    domainName = field("domainName")
    ipAddressType = field("ipAddressType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DnsResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DnsResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedResponseAction:
    boto3_raw_data: "type_defs.FixedResponseActionTypeDef" = dataclasses.field()

    statusCode = field("statusCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FixedResponseActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedResponseActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeightedTargetGroup:
    boto3_raw_data: "type_defs.WeightedTargetGroupTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")
    weight = field("weight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WeightedTargetGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WeightedTargetGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessLogSubscriptionRequest:
    boto3_raw_data: "type_defs.GetAccessLogSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    accessLogSubscriptionIdentifier = field("accessLogSubscriptionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessLogSubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessLogSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthPolicyRequest:
    boto3_raw_data: "type_defs.GetAuthPolicyRequestTypeDef" = dataclasses.field()

    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListenerRequest:
    boto3_raw_data: "type_defs.GetListenerRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceConfigurationRequest:
    boto3_raw_data: "type_defs.GetResourceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceGatewayRequest:
    boto3_raw_data: "type_defs.GetResourceGatewayRequestTypeDef" = dataclasses.field()

    resourceGatewayIdentifier = field("resourceGatewayIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleRequest:
    boto3_raw_data: "type_defs.GetRuleRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    ruleIdentifier = field("ruleIdentifier")
    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRuleRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkRequest:
    boto3_raw_data: "type_defs.GetServiceNetworkRequestTypeDef" = dataclasses.field()

    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkResourceAssociationRequest:
    boto3_raw_data: "type_defs.GetServiceNetworkResourceAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceNetworkResourceAssociationIdentifier = field(
        "serviceNetworkResourceAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceNetworkResourceAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkResourceAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkServiceAssociationRequest:
    boto3_raw_data: "type_defs.GetServiceNetworkServiceAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceNetworkServiceAssociationIdentifier = field(
        "serviceNetworkServiceAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceNetworkServiceAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkServiceAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkVpcAssociationRequest:
    boto3_raw_data: "type_defs.GetServiceNetworkVpcAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    serviceNetworkVpcAssociationIdentifier = field(
        "serviceNetworkVpcAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceNetworkVpcAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkVpcAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceRequest:
    boto3_raw_data: "type_defs.GetServiceRequestTypeDef" = dataclasses.field()

    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServiceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTargetGroupRequest:
    boto3_raw_data: "type_defs.GetTargetGroupRequestTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTargetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTargetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderMatchType:
    boto3_raw_data: "type_defs.HeaderMatchTypeTypeDef" = dataclasses.field()

    contains = field("contains")
    exact = field("exact")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeaderMatchTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeaderMatchTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Matcher:
    boto3_raw_data: "type_defs.MatcherTypeDef" = dataclasses.field()

    httpCode = field("httpCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatcherTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatcherTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpResource:
    boto3_raw_data: "type_defs.IpResourceTypeDef" = dataclasses.field()

    ipAddress = field("ipAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpResourceTypeDef"]]
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
class ListAccessLogSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListAccessLogSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessLogSubscriptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessLogSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListListenersRequest:
    boto3_raw_data: "type_defs.ListListenersRequestTypeDef" = dataclasses.field()

    serviceIdentifier = field("serviceIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListListenersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListListenersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerSummary:
    boto3_raw_data: "type_defs.ListenerSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    port = field("port")
    protocol = field("protocol")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceConfigurationsRequest:
    boto3_raw_data: "type_defs.ListResourceConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    resourceConfigurationGroupIdentifier = field("resourceConfigurationGroupIdentifier")
    resourceGatewayIdentifier = field("resourceGatewayIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceConfigurationSummary:
    boto3_raw_data: "type_defs.ResourceConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    amazonManaged = field("amazonManaged")
    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    resourceConfigurationGroupId = field("resourceConfigurationGroupId")
    resourceGatewayId = field("resourceGatewayId")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceEndpointAssociationsRequest:
    boto3_raw_data: "type_defs.ListResourceEndpointAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    resourceEndpointAssociationIdentifier = field(
        "resourceEndpointAssociationIdentifier"
    )
    vpcEndpointId = field("vpcEndpointId")
    vpcEndpointOwner = field("vpcEndpointOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceEndpointAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceEndpointAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceEndpointAssociationSummary:
    boto3_raw_data: "type_defs.ResourceEndpointAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    id = field("id")
    resourceConfigurationArn = field("resourceConfigurationArn")
    resourceConfigurationId = field("resourceConfigurationId")
    resourceConfigurationName = field("resourceConfigurationName")
    vpcEndpointId = field("vpcEndpointId")
    vpcEndpointOwner = field("vpcEndpointOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceEndpointAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceEndpointAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceGatewaysRequest:
    boto3_raw_data: "type_defs.ListResourceGatewaysRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceGatewaysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceGatewaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceGatewaySummary:
    boto3_raw_data: "type_defs.ResourceGatewaySummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    ipAddressType = field("ipAddressType")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    subnetIds = field("subnetIds")
    vpcIdentifier = field("vpcIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceGatewaySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceGatewaySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequest:
    boto3_raw_data: "type_defs.ListRulesRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    serviceIdentifier = field("serviceIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleSummary:
    boto3_raw_data: "type_defs.RuleSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    isDefault = field("isDefault")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    priority = field("priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkResourceAssociationsRequest:
    boto3_raw_data: "type_defs.ListServiceNetworkResourceAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkResourceAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworkResourceAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkServiceAssociationsRequest:
    boto3_raw_data: "type_defs.ListServiceNetworkServiceAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    serviceIdentifier = field("serviceIdentifier")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkServiceAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworkServiceAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkVpcAssociationsRequest:
    boto3_raw_data: "type_defs.ListServiceNetworkVpcAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")
    vpcIdentifier = field("vpcIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkVpcAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworkVpcAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNetworkVpcAssociationSummary:
    boto3_raw_data: "type_defs.ServiceNetworkVpcAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    serviceNetworkArn = field("serviceNetworkArn")
    serviceNetworkId = field("serviceNetworkId")
    serviceNetworkName = field("serviceNetworkName")
    status = field("status")
    vpcId = field("vpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNetworkVpcAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNetworkVpcAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkVpcEndpointAssociationsRequest:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkVpcEndpointAssociationsRequestTypeDef"
    ) = dataclasses.field()

    serviceNetworkIdentifier = field("serviceNetworkIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkVpcEndpointAssociationsRequestTypeDef"
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
                "type_defs.ListServiceNetworkVpcEndpointAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNetworkEndpointAssociation:
    boto3_raw_data: "type_defs.ServiceNetworkEndpointAssociationTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    id = field("id")
    serviceNetworkArn = field("serviceNetworkArn")
    state = field("state")
    vpcEndpointId = field("vpcEndpointId")
    vpcEndpointOwnerId = field("vpcEndpointOwnerId")
    vpcId = field("vpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNetworkEndpointAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNetworkEndpointAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworksRequest:
    boto3_raw_data: "type_defs.ListServiceNetworksRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceNetworksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNetworkSummary:
    boto3_raw_data: "type_defs.ServiceNetworkSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    numberOfAssociatedResourceConfigurations = field(
        "numberOfAssociatedResourceConfigurations"
    )
    numberOfAssociatedServices = field("numberOfAssociatedServices")
    numberOfAssociatedVPCs = field("numberOfAssociatedVPCs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceNetworkSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNetworkSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequest:
    boto3_raw_data: "type_defs.ListServicesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestTypeDef"]
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
class ListTargetGroupsRequest:
    boto3_raw_data: "type_defs.ListTargetGroupsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    targetGroupType = field("targetGroupType")
    vpcIdentifier = field("vpcIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupSummary:
    boto3_raw_data: "type_defs.TargetGroupSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    ipAddressType = field("ipAddressType")
    lambdaEventStructureVersion = field("lambdaEventStructureVersion")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    port = field("port")
    protocol = field("protocol")
    serviceArns = field("serviceArns")
    status = field("status")
    type = field("type")
    vpcIdentifier = field("vpcIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetSummary:
    boto3_raw_data: "type_defs.TargetSummaryTypeDef" = dataclasses.field()

    id = field("id")
    port = field("port")
    reasonCode = field("reasonCode")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathMatchType:
    boto3_raw_data: "type_defs.PathMatchTypeTypeDef" = dataclasses.field()

    exact = field("exact")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathMatchTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathMatchTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAuthPolicyRequest:
    boto3_raw_data: "type_defs.PutAuthPolicyRequestTypeDef" = dataclasses.field()

    policy = field("policy")
    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAuthPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAuthPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    policy = field("policy")
    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
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
    tags = field("tags")

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
class UpdateAccessLogSubscriptionRequest:
    boto3_raw_data: "type_defs.UpdateAccessLogSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    accessLogSubscriptionIdentifier = field("accessLogSubscriptionIdentifier")
    destinationArn = field("destinationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessLogSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessLogSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceGatewayRequest:
    boto3_raw_data: "type_defs.UpdateResourceGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    resourceGatewayIdentifier = field("resourceGatewayIdentifier")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceNetworkRequest:
    boto3_raw_data: "type_defs.UpdateServiceNetworkRequestTypeDef" = dataclasses.field()

    authType = field("authType")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceNetworkVpcAssociationRequest:
    boto3_raw_data: "type_defs.UpdateServiceNetworkVpcAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    securityGroupIds = field("securityGroupIds")
    serviceNetworkVpcAssociationIdentifier = field(
        "serviceNetworkVpcAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceNetworkVpcAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceNetworkVpcAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceRequest:
    boto3_raw_data: "type_defs.UpdateServiceRequestTypeDef" = dataclasses.field()

    serviceIdentifier = field("serviceIdentifier")
    authType = field("authType")
    certificateArn = field("certificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessLogSubscriptionResponse:
    boto3_raw_data: "type_defs.CreateAccessLogSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    destinationArn = field("destinationArn")
    id = field("id")
    resourceArn = field("resourceArn")
    resourceId = field("resourceId")
    serviceNetworkLogType = field("serviceNetworkLogType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessLogSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessLogSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceGatewayResponse:
    boto3_raw_data: "type_defs.CreateResourceGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    ipAddressType = field("ipAddressType")
    name = field("name")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    subnetIds = field("subnetIds")
    vpcIdentifier = field("vpcIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkResourceAssociationResponse:
    boto3_raw_data: (
        "type_defs.CreateServiceNetworkResourceAssociationResponseTypeDef"
    ) = dataclasses.field()

    arn = field("arn")
    createdBy = field("createdBy")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceNetworkResourceAssociationResponseTypeDef"
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
                "type_defs.CreateServiceNetworkResourceAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkVpcAssociationResponse:
    boto3_raw_data: "type_defs.CreateServiceNetworkVpcAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdBy = field("createdBy")
    id = field("id")
    securityGroupIds = field("securityGroupIds")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceNetworkVpcAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceNetworkVpcAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceEndpointAssociationResponse:
    boto3_raw_data: "type_defs.DeleteResourceEndpointAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    resourceConfigurationArn = field("resourceConfigurationArn")
    resourceConfigurationId = field("resourceConfigurationId")
    vpcEndpointId = field("vpcEndpointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResourceEndpointAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceEndpointAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceGatewayResponse:
    boto3_raw_data: "type_defs.DeleteResourceGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResourceGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkResourceAssociationResponse:
    boto3_raw_data: (
        "type_defs.DeleteServiceNetworkResourceAssociationResponseTypeDef"
    ) = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceNetworkResourceAssociationResponseTypeDef"
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
                "type_defs.DeleteServiceNetworkResourceAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkServiceAssociationResponse:
    boto3_raw_data: (
        "type_defs.DeleteServiceNetworkServiceAssociationResponseTypeDef"
    ) = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceNetworkServiceAssociationResponseTypeDef"
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
                "type_defs.DeleteServiceNetworkServiceAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceNetworkVpcAssociationResponse:
    boto3_raw_data: "type_defs.DeleteServiceNetworkVpcAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceNetworkVpcAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceNetworkVpcAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceResponse:
    boto3_raw_data: "type_defs.DeleteServiceResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTargetGroupResponse:
    boto3_raw_data: "type_defs.DeleteTargetGroupResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTargetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTargetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessLogSubscriptionResponse:
    boto3_raw_data: "type_defs.GetAccessLogSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    destinationArn = field("destinationArn")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    resourceArn = field("resourceArn")
    resourceId = field("resourceId")
    serviceNetworkLogType = field("serviceNetworkLogType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessLogSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessLogSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthPolicyResponse:
    boto3_raw_data: "type_defs.GetAuthPolicyResponseTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    policy = field("policy")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceGatewayResponse:
    boto3_raw_data: "type_defs.GetResourceGatewayResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    ipAddressType = field("ipAddressType")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    subnetIds = field("subnetIds")
    vpcId = field("vpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkVpcAssociationResponse:
    boto3_raw_data: "type_defs.GetServiceNetworkVpcAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    failureCode = field("failureCode")
    failureMessage = field("failureMessage")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    securityGroupIds = field("securityGroupIds")
    serviceNetworkArn = field("serviceNetworkArn")
    serviceNetworkId = field("serviceNetworkId")
    serviceNetworkName = field("serviceNetworkName")
    status = field("status")
    vpcId = field("vpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceNetworkVpcAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkVpcAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessLogSubscriptionsResponse:
    boto3_raw_data: "type_defs.ListAccessLogSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return AccessLogSubscriptionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessLogSubscriptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessLogSubscriptionsResponseTypeDef"]
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

    tags = field("tags")

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
class PutAuthPolicyResponse:
    boto3_raw_data: "type_defs.PutAuthPolicyResponseTypeDef" = dataclasses.field()

    policy = field("policy")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAuthPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAuthPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessLogSubscriptionResponse:
    boto3_raw_data: "type_defs.UpdateAccessLogSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    destinationArn = field("destinationArn")
    id = field("id")
    resourceArn = field("resourceArn")
    resourceId = field("resourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessLogSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessLogSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceGatewayResponse:
    boto3_raw_data: "type_defs.UpdateResourceGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    ipAddressType = field("ipAddressType")
    name = field("name")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    subnetIds = field("subnetIds")
    vpcId = field("vpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResourceGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceNetworkResponse:
    boto3_raw_data: "type_defs.UpdateServiceNetworkResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    authType = field("authType")
    id = field("id")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceNetworkVpcAssociationResponse:
    boto3_raw_data: "type_defs.UpdateServiceNetworkVpcAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdBy = field("createdBy")
    id = field("id")
    securityGroupIds = field("securityGroupIds")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceNetworkVpcAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceNetworkVpcAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceResponse:
    boto3_raw_data: "type_defs.UpdateServiceResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    authType = field("authType")
    certificateArn = field("certificateArn")
    customDomainName = field("customDomainName")
    id = field("id")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkRequest:
    boto3_raw_data: "type_defs.CreateServiceNetworkRequestTypeDef" = dataclasses.field()

    name = field("name")
    authType = field("authType")
    clientToken = field("clientToken")

    @cached_property
    def sharingConfig(self):  # pragma: no cover
        return SharingConfig.make_one(self.boto3_raw_data["sharingConfig"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkResponse:
    boto3_raw_data: "type_defs.CreateServiceNetworkResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    authType = field("authType")
    id = field("id")
    name = field("name")

    @cached_property
    def sharingConfig(self):  # pragma: no cover
        return SharingConfig.make_one(self.boto3_raw_data["sharingConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkResponse:
    boto3_raw_data: "type_defs.GetServiceNetworkResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    authType = field("authType")
    createdAt = field("createdAt")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    numberOfAssociatedServices = field("numberOfAssociatedServices")
    numberOfAssociatedVPCs = field("numberOfAssociatedVPCs")

    @cached_property
    def sharingConfig(self):  # pragma: no cover
        return SharingConfig.make_one(self.boto3_raw_data["sharingConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceNetworkServiceAssociationResponse:
    boto3_raw_data: (
        "type_defs.CreateServiceNetworkServiceAssociationResponseTypeDef"
    ) = dataclasses.field()

    arn = field("arn")
    createdBy = field("createdBy")
    customDomainName = field("customDomainName")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceNetworkServiceAssociationResponseTypeDef"
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
                "type_defs.CreateServiceNetworkServiceAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceResponse:
    boto3_raw_data: "type_defs.CreateServiceResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    authType = field("authType")
    certificateArn = field("certificateArn")
    customDomainName = field("customDomainName")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkResourceAssociationResponse:
    boto3_raw_data: "type_defs.GetServiceNetworkResourceAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    failureCode = field("failureCode")
    failureReason = field("failureReason")
    id = field("id")
    isManagedAssociation = field("isManagedAssociation")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def privateDnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["privateDnsEntry"])

    resourceConfigurationArn = field("resourceConfigurationArn")
    resourceConfigurationId = field("resourceConfigurationId")
    resourceConfigurationName = field("resourceConfigurationName")
    serviceNetworkArn = field("serviceNetworkArn")
    serviceNetworkId = field("serviceNetworkId")
    serviceNetworkName = field("serviceNetworkName")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceNetworkResourceAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkResourceAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceNetworkServiceAssociationResponse:
    boto3_raw_data: "type_defs.GetServiceNetworkServiceAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    customDomainName = field("customDomainName")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    failureCode = field("failureCode")
    failureMessage = field("failureMessage")
    id = field("id")
    serviceArn = field("serviceArn")
    serviceId = field("serviceId")
    serviceName = field("serviceName")
    serviceNetworkArn = field("serviceNetworkArn")
    serviceNetworkId = field("serviceNetworkId")
    serviceNetworkName = field("serviceNetworkName")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceNetworkServiceAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceNetworkServiceAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceResponse:
    boto3_raw_data: "type_defs.GetServiceResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    authType = field("authType")
    certificateArn = field("certificateArn")
    createdAt = field("createdAt")
    customDomainName = field("customDomainName")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    failureCode = field("failureCode")
    failureMessage = field("failureMessage")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNetworkResourceAssociationSummary:
    boto3_raw_data: "type_defs.ServiceNetworkResourceAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    failureCode = field("failureCode")
    id = field("id")
    isManagedAssociation = field("isManagedAssociation")

    @cached_property
    def privateDnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["privateDnsEntry"])

    resourceConfigurationArn = field("resourceConfigurationArn")
    resourceConfigurationId = field("resourceConfigurationId")
    resourceConfigurationName = field("resourceConfigurationName")
    serviceNetworkArn = field("serviceNetworkArn")
    serviceNetworkId = field("serviceNetworkId")
    serviceNetworkName = field("serviceNetworkName")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNetworkResourceAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNetworkResourceAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNetworkServiceAssociationSummary:
    boto3_raw_data: "type_defs.ServiceNetworkServiceAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    customDomainName = field("customDomainName")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    id = field("id")
    serviceArn = field("serviceArn")
    serviceId = field("serviceId")
    serviceName = field("serviceName")
    serviceNetworkArn = field("serviceNetworkArn")
    serviceNetworkId = field("serviceNetworkId")
    serviceNetworkName = field("serviceNetworkName")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNetworkServiceAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNetworkServiceAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSummary:
    boto3_raw_data: "type_defs.ServiceSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    customDomainName = field("customDomainName")

    @cached_property
    def dnsEntry(self):  # pragma: no cover
        return DnsEntry.make_one(self.boto3_raw_data["dnsEntry"])

    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTargetsRequest:
    boto3_raw_data: "type_defs.DeregisterTargetsRequestTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")

    @cached_property
    def targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["targets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsRequest:
    boto3_raw_data: "type_defs.ListTargetsRequestTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["targets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTargetsRequest:
    boto3_raw_data: "type_defs.RegisterTargetsRequestTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")

    @cached_property
    def targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["targets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTargetsResponse:
    boto3_raw_data: "type_defs.DeregisterTargetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def successful(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["successful"])

    @cached_property
    def unsuccessful(self):  # pragma: no cover
        return TargetFailure.make_many(self.boto3_raw_data["unsuccessful"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTargetsResponse:
    boto3_raw_data: "type_defs.RegisterTargetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def successful(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["successful"])

    @cached_property
    def unsuccessful(self):  # pragma: no cover
        return TargetFailure.make_many(self.boto3_raw_data["unsuccessful"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardActionOutput:
    boto3_raw_data: "type_defs.ForwardActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def targetGroups(self):  # pragma: no cover
        return WeightedTargetGroup.make_many(self.boto3_raw_data["targetGroups"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForwardActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForwardActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardAction:
    boto3_raw_data: "type_defs.ForwardActionTypeDef" = dataclasses.field()

    @cached_property
    def targetGroups(self):  # pragma: no cover
        return WeightedTargetGroup.make_many(self.boto3_raw_data["targetGroups"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForwardActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ForwardActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderMatch:
    boto3_raw_data: "type_defs.HeaderMatchTypeDef" = dataclasses.field()

    @cached_property
    def match(self):  # pragma: no cover
        return HeaderMatchType.make_one(self.boto3_raw_data["match"])

    name = field("name")
    caseSensitive = field("caseSensitive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeaderMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeaderMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckConfig:
    boto3_raw_data: "type_defs.HealthCheckConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")
    healthCheckIntervalSeconds = field("healthCheckIntervalSeconds")
    healthCheckTimeoutSeconds = field("healthCheckTimeoutSeconds")
    healthyThresholdCount = field("healthyThresholdCount")

    @cached_property
    def matcher(self):  # pragma: no cover
        return Matcher.make_one(self.boto3_raw_data["matcher"])

    path = field("path")
    port = field("port")
    protocol = field("protocol")
    protocolVersion = field("protocolVersion")
    unhealthyThresholdCount = field("unhealthyThresholdCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceConfigurationDefinition:
    boto3_raw_data: "type_defs.ResourceConfigurationDefinitionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def arnResource(self):  # pragma: no cover
        return ArnResource.make_one(self.boto3_raw_data["arnResource"])

    @cached_property
    def dnsResource(self):  # pragma: no cover
        return DnsResource.make_one(self.boto3_raw_data["dnsResource"])

    @cached_property
    def ipResource(self):  # pragma: no cover
        return IpResource.make_one(self.boto3_raw_data["ipResource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResourceConfigurationDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceConfigurationDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessLogSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessLogSubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessLogSubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessLogSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListListenersRequestPaginate:
    boto3_raw_data: "type_defs.ListListenersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    serviceIdentifier = field("serviceIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListListenersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListListenersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceConfigurationGroupIdentifier = field("resourceConfigurationGroupIdentifier")
    resourceGatewayIdentifier = field("resourceGatewayIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceEndpointAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListResourceEndpointAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")
    resourceEndpointAssociationIdentifier = field(
        "resourceEndpointAssociationIdentifier"
    )
    vpcEndpointId = field("vpcEndpointId")
    vpcEndpointOwner = field("vpcEndpointOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceEndpointAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListResourceEndpointAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceGatewaysRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceGatewaysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceGatewaysRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceGatewaysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListRulesRequestPaginateTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    serviceIdentifier = field("serviceIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkResourceAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkResourceAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkResourceAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListServiceNetworkResourceAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkServiceAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkServiceAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    serviceIdentifier = field("serviceIdentifier")
    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkServiceAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListServiceNetworkServiceAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkVpcAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkVpcAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    serviceNetworkIdentifier = field("serviceNetworkIdentifier")
    vpcIdentifier = field("vpcIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkVpcAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListServiceNetworkVpcAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkVpcEndpointAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    serviceNetworkIdentifier = field("serviceNetworkIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworksRequestPaginate:
    boto3_raw_data: "type_defs.ListServiceNetworksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequestPaginate:
    boto3_raw_data: "type_defs.ListServicesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListTargetGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    targetGroupType = field("targetGroupType")
    vpcIdentifier = field("vpcIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTargetGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsRequestPaginate:
    boto3_raw_data: "type_defs.ListTargetsRequestPaginateTypeDef" = dataclasses.field()

    targetGroupIdentifier = field("targetGroupIdentifier")

    @cached_property
    def targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["targets"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListListenersResponse:
    boto3_raw_data: "type_defs.ListListenersResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ListenerSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListListenersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListListenersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceConfigurationsResponse:
    boto3_raw_data: "type_defs.ListResourceConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ResourceConfigurationSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceEndpointAssociationsResponse:
    boto3_raw_data: "type_defs.ListResourceEndpointAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ResourceEndpointAssociationSummary.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceEndpointAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceEndpointAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceGatewaysResponse:
    boto3_raw_data: "type_defs.ListResourceGatewaysResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ResourceGatewaySummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceGatewaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceGatewaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesResponse:
    boto3_raw_data: "type_defs.ListRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return RuleSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkVpcAssociationsResponse:
    boto3_raw_data: "type_defs.ListServiceNetworkVpcAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ServiceNetworkVpcAssociationSummary.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkVpcAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworkVpcAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkVpcEndpointAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkVpcEndpointAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ServiceNetworkEndpointAssociation.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkVpcEndpointAssociationsResponseTypeDef"
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
                "type_defs.ListServiceNetworkVpcEndpointAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworksResponse:
    boto3_raw_data: "type_defs.ListServiceNetworksResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ServiceNetworkSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceNetworksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetGroupsResponse:
    boto3_raw_data: "type_defs.ListTargetGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return TargetGroupSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsResponse:
    boto3_raw_data: "type_defs.ListTargetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return TargetSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathMatch:
    boto3_raw_data: "type_defs.PathMatchTypeDef" = dataclasses.field()

    @cached_property
    def match(self):  # pragma: no cover
        return PathMatchType.make_one(self.boto3_raw_data["match"])

    caseSensitive = field("caseSensitive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkResourceAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListServiceNetworkResourceAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ServiceNetworkResourceAssociationSummary.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkResourceAssociationsResponseTypeDef"
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
                "type_defs.ListServiceNetworkResourceAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceNetworkServiceAssociationsResponse:
    boto3_raw_data: "type_defs.ListServiceNetworkServiceAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ServiceNetworkServiceAssociationSummary.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceNetworkServiceAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceNetworkServiceAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesResponse:
    boto3_raw_data: "type_defs.ListServicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ServiceSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleActionOutput:
    boto3_raw_data: "type_defs.RuleActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def fixedResponse(self):  # pragma: no cover
        return FixedResponseAction.make_one(self.boto3_raw_data["fixedResponse"])

    @cached_property
    def forward(self):  # pragma: no cover
        return ForwardActionOutput.make_one(self.boto3_raw_data["forward"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupConfig:
    boto3_raw_data: "type_defs.TargetGroupConfigTypeDef" = dataclasses.field()

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return HealthCheckConfig.make_one(self.boto3_raw_data["healthCheck"])

    ipAddressType = field("ipAddressType")
    lambdaEventStructureVersion = field("lambdaEventStructureVersion")
    port = field("port")
    protocol = field("protocol")
    protocolVersion = field("protocolVersion")
    vpcIdentifier = field("vpcIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetGroupConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTargetGroupRequest:
    boto3_raw_data: "type_defs.UpdateTargetGroupRequestTypeDef" = dataclasses.field()

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return HealthCheckConfig.make_one(self.boto3_raw_data["healthCheck"])

    targetGroupIdentifier = field("targetGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTargetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTargetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceConfigurationRequest:
    boto3_raw_data: "type_defs.CreateResourceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    allowAssociationToShareableServiceNetwork = field(
        "allowAssociationToShareableServiceNetwork"
    )
    clientToken = field("clientToken")
    portRanges = field("portRanges")
    protocol = field("protocol")

    @cached_property
    def resourceConfigurationDefinition(self):  # pragma: no cover
        return ResourceConfigurationDefinition.make_one(
            self.boto3_raw_data["resourceConfigurationDefinition"]
        )

    resourceConfigurationGroupIdentifier = field("resourceConfigurationGroupIdentifier")
    resourceGatewayIdentifier = field("resourceGatewayIdentifier")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceConfigurationResponse:
    boto3_raw_data: "type_defs.CreateResourceConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    allowAssociationToShareableServiceNetwork = field(
        "allowAssociationToShareableServiceNetwork"
    )
    arn = field("arn")
    createdAt = field("createdAt")
    failureReason = field("failureReason")
    id = field("id")
    name = field("name")
    portRanges = field("portRanges")
    protocol = field("protocol")

    @cached_property
    def resourceConfigurationDefinition(self):  # pragma: no cover
        return ResourceConfigurationDefinition.make_one(
            self.boto3_raw_data["resourceConfigurationDefinition"]
        )

    resourceConfigurationGroupId = field("resourceConfigurationGroupId")
    resourceGatewayId = field("resourceGatewayId")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourceConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceConfigurationResponse:
    boto3_raw_data: "type_defs.GetResourceConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    allowAssociationToShareableServiceNetwork = field(
        "allowAssociationToShareableServiceNetwork"
    )
    amazonManaged = field("amazonManaged")
    arn = field("arn")
    createdAt = field("createdAt")
    customDomainName = field("customDomainName")
    failureReason = field("failureReason")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    portRanges = field("portRanges")
    protocol = field("protocol")

    @cached_property
    def resourceConfigurationDefinition(self):  # pragma: no cover
        return ResourceConfigurationDefinition.make_one(
            self.boto3_raw_data["resourceConfigurationDefinition"]
        )

    resourceConfigurationGroupId = field("resourceConfigurationGroupId")
    resourceGatewayId = field("resourceGatewayId")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateResourceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceConfigurationIdentifier = field("resourceConfigurationIdentifier")
    allowAssociationToShareableServiceNetwork = field(
        "allowAssociationToShareableServiceNetwork"
    )
    portRanges = field("portRanges")

    @cached_property
    def resourceConfigurationDefinition(self):  # pragma: no cover
        return ResourceConfigurationDefinition.make_one(
            self.boto3_raw_data["resourceConfigurationDefinition"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResourceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateResourceConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    allowAssociationToShareableServiceNetwork = field(
        "allowAssociationToShareableServiceNetwork"
    )
    arn = field("arn")
    id = field("id")
    name = field("name")
    portRanges = field("portRanges")
    protocol = field("protocol")

    @cached_property
    def resourceConfigurationDefinition(self):  # pragma: no cover
        return ResourceConfigurationDefinition.make_one(
            self.boto3_raw_data["resourceConfigurationDefinition"]
        )

    resourceConfigurationGroupId = field("resourceConfigurationGroupId")
    resourceGatewayId = field("resourceGatewayId")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResourceConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpMatchOutput:
    boto3_raw_data: "type_defs.HttpMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def headerMatches(self):  # pragma: no cover
        return HeaderMatch.make_many(self.boto3_raw_data["headerMatches"])

    method = field("method")

    @cached_property
    def pathMatch(self):  # pragma: no cover
        return PathMatch.make_one(self.boto3_raw_data["pathMatch"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpMatchOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpMatchOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpMatch:
    boto3_raw_data: "type_defs.HttpMatchTypeDef" = dataclasses.field()

    @cached_property
    def headerMatches(self):  # pragma: no cover
        return HeaderMatch.make_many(self.boto3_raw_data["headerMatches"])

    method = field("method")

    @cached_property
    def pathMatch(self):  # pragma: no cover
        return PathMatch.make_one(self.boto3_raw_data["pathMatch"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListenerResponse:
    boto3_raw_data: "type_defs.CreateListenerResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def defaultAction(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["defaultAction"])

    id = field("id")
    name = field("name")
    port = field("port")
    protocol = field("protocol")
    serviceArn = field("serviceArn")
    serviceId = field("serviceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListenerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListenerResponse:
    boto3_raw_data: "type_defs.GetListenerResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def defaultAction(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["defaultAction"])

    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    port = field("port")
    protocol = field("protocol")
    serviceArn = field("serviceArn")
    serviceId = field("serviceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetListenerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateListenerResponse:
    boto3_raw_data: "type_defs.UpdateListenerResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def defaultAction(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["defaultAction"])

    id = field("id")
    name = field("name")
    port = field("port")
    protocol = field("protocol")
    serviceArn = field("serviceArn")
    serviceId = field("serviceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateListenerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateListenerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleAction:
    boto3_raw_data: "type_defs.RuleActionTypeDef" = dataclasses.field()

    @cached_property
    def fixedResponse(self):  # pragma: no cover
        return FixedResponseAction.make_one(self.boto3_raw_data["fixedResponse"])

    forward = field("forward")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTargetGroupRequest:
    boto3_raw_data: "type_defs.CreateTargetGroupRequestTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    clientToken = field("clientToken")

    @cached_property
    def config(self):  # pragma: no cover
        return TargetGroupConfig.make_one(self.boto3_raw_data["config"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTargetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTargetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTargetGroupResponse:
    boto3_raw_data: "type_defs.CreateTargetGroupResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def config(self):  # pragma: no cover
        return TargetGroupConfig.make_one(self.boto3_raw_data["config"])

    id = field("id")
    name = field("name")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTargetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTargetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTargetGroupResponse:
    boto3_raw_data: "type_defs.GetTargetGroupResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def config(self):  # pragma: no cover
        return TargetGroupConfig.make_one(self.boto3_raw_data["config"])

    createdAt = field("createdAt")
    failureCode = field("failureCode")
    failureMessage = field("failureMessage")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    serviceArns = field("serviceArns")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTargetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTargetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTargetGroupResponse:
    boto3_raw_data: "type_defs.UpdateTargetGroupResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def config(self):  # pragma: no cover
        return TargetGroupConfig.make_one(self.boto3_raw_data["config"])

    id = field("id")
    name = field("name")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTargetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTargetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleMatchOutput:
    boto3_raw_data: "type_defs.RuleMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def httpMatch(self):  # pragma: no cover
        return HttpMatchOutput.make_one(self.boto3_raw_data["httpMatch"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleMatchOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleMatchOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleResponse:
    boto3_raw_data: "type_defs.CreateRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["action"])

    arn = field("arn")
    id = field("id")

    @cached_property
    def match(self):  # pragma: no cover
        return RuleMatchOutput.make_one(self.boto3_raw_data["match"])

    name = field("name")
    priority = field("priority")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleResponse:
    boto3_raw_data: "type_defs.GetRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["action"])

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    isDefault = field("isDefault")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def match(self):  # pragma: no cover
        return RuleMatchOutput.make_one(self.boto3_raw_data["match"])

    name = field("name")
    priority = field("priority")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRuleResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleUpdateSuccess:
    boto3_raw_data: "type_defs.RuleUpdateSuccessTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["action"])

    arn = field("arn")
    id = field("id")
    isDefault = field("isDefault")

    @cached_property
    def match(self):  # pragma: no cover
        return RuleMatchOutput.make_one(self.boto3_raw_data["match"])

    name = field("name")
    priority = field("priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleUpdateSuccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleUpdateSuccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleResponse:
    boto3_raw_data: "type_defs.UpdateRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["action"])

    arn = field("arn")
    id = field("id")
    isDefault = field("isDefault")

    @cached_property
    def match(self):  # pragma: no cover
        return RuleMatchOutput.make_one(self.boto3_raw_data["match"])

    name = field("name")
    priority = field("priority")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleMatch:
    boto3_raw_data: "type_defs.RuleMatchTypeDef" = dataclasses.field()

    httpMatch = field("httpMatch")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleMatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListenerRequest:
    boto3_raw_data: "type_defs.CreateListenerRequestTypeDef" = dataclasses.field()

    defaultAction = field("defaultAction")
    name = field("name")
    protocol = field("protocol")
    serviceIdentifier = field("serviceIdentifier")
    clientToken = field("clientToken")
    port = field("port")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateListenerRequest:
    boto3_raw_data: "type_defs.UpdateListenerRequestTypeDef" = dataclasses.field()

    defaultAction = field("defaultAction")
    listenerIdentifier = field("listenerIdentifier")
    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateListenerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateListenerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRuleResponse:
    boto3_raw_data: "type_defs.BatchUpdateRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def successful(self):  # pragma: no cover
        return RuleUpdateSuccess.make_many(self.boto3_raw_data["successful"])

    @cached_property
    def unsuccessful(self):  # pragma: no cover
        return RuleUpdateFailure.make_many(self.boto3_raw_data["unsuccessful"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleRequest:
    boto3_raw_data: "type_defs.CreateRuleRequestTypeDef" = dataclasses.field()

    action = field("action")
    listenerIdentifier = field("listenerIdentifier")
    match = field("match")
    name = field("name")
    priority = field("priority")
    serviceIdentifier = field("serviceIdentifier")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleUpdate:
    boto3_raw_data: "type_defs.RuleUpdateTypeDef" = dataclasses.field()

    ruleIdentifier = field("ruleIdentifier")
    action = field("action")
    match = field("match")
    priority = field("priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleUpdateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleRequest:
    boto3_raw_data: "type_defs.UpdateRuleRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")
    ruleIdentifier = field("ruleIdentifier")
    serviceIdentifier = field("serviceIdentifier")
    action = field("action")
    match = field("match")
    priority = field("priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRuleRequest:
    boto3_raw_data: "type_defs.BatchUpdateRuleRequestTypeDef" = dataclasses.field()

    listenerIdentifier = field("listenerIdentifier")

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleUpdate.make_many(self.boto3_raw_data["rules"])

    serviceIdentifier = field("serviceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
