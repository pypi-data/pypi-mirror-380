# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_outposts import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    ContactName = field("ContactName")
    ContactPhoneNumber = field("ContactPhoneNumber")
    AddressLine1 = field("AddressLine1")
    City = field("City")
    StateOrRegion = field("StateOrRegion")
    PostalCode = field("PostalCode")
    CountryCode = field("CountryCode")
    AddressLine2 = field("AddressLine2")
    AddressLine3 = field("AddressLine3")
    DistrictOrCounty = field("DistrictOrCounty")
    Municipality = field("Municipality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetLocation:
    boto3_raw_data: "type_defs.AssetLocationTypeDef" = dataclasses.field()

    RackElevation = field("RackElevation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetInstanceTypeCapacity:
    boto3_raw_data: "type_defs.AssetInstanceTypeCapacityTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    Count = field("Count")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetInstanceTypeCapacityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetInstanceTypeCapacityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetInstance:
    boto3_raw_data: "type_defs.AssetInstanceTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    InstanceType = field("InstanceType")
    AssetId = field("AssetId")
    AccountId = field("AccountId")
    AwsServiceName = field("AwsServiceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockingInstance:
    boto3_raw_data: "type_defs.BlockingInstanceTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    AccountId = field("AccountId")
    AwsServiceName = field("AwsServiceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockingInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockingInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelCapacityTaskInput:
    boto3_raw_data: "type_defs.CancelCapacityTaskInputTypeDef" = dataclasses.field()

    CapacityTaskId = field("CapacityTaskId")
    OutpostIdentifier = field("OutpostIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelCapacityTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelCapacityTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelOrderInput:
    boto3_raw_data: "type_defs.CancelOrderInputTypeDef" = dataclasses.field()

    OrderId = field("OrderId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelOrderInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelOrderInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityTaskFailure:
    boto3_raw_data: "type_defs.CapacityTaskFailureTypeDef" = dataclasses.field()

    Reason = field("Reason")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityTaskFailureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityTaskFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityTaskSummary:
    boto3_raw_data: "type_defs.CapacityTaskSummaryTypeDef" = dataclasses.field()

    CapacityTaskId = field("CapacityTaskId")
    OutpostId = field("OutpostId")
    OrderId = field("OrderId")
    AssetId = field("AssetId")
    CapacityTaskStatus = field("CapacityTaskStatus")
    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityTaskSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2Capacity:
    boto3_raw_data: "type_defs.EC2CapacityTypeDef" = dataclasses.field()

    Family = field("Family")
    MaxSize = field("MaxSize")
    Quantity = field("Quantity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2CapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EC2CapacityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionDetails:
    boto3_raw_data: "type_defs.ConnectionDetailsTypeDef" = dataclasses.field()

    ClientPublicKey = field("ClientPublicKey")
    ServerPublicKey = field("ServerPublicKey")
    ServerEndpoint = field("ServerEndpoint")
    ClientTunnelAddress = field("ClientTunnelAddress")
    ServerTunnelAddress = field("ServerTunnelAddress")
    AllowedIps = field("AllowedIps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItemRequest:
    boto3_raw_data: "type_defs.LineItemRequestTypeDef" = dataclasses.field()

    CatalogItemId = field("CatalogItemId")
    Quantity = field("Quantity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineItemRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineItemRequestTypeDef"]],
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
class CreateOutpostInput:
    boto3_raw_data: "type_defs.CreateOutpostInputTypeDef" = dataclasses.field()

    Name = field("Name")
    SiteId = field("SiteId")
    Description = field("Description")
    AvailabilityZone = field("AvailabilityZone")
    AvailabilityZoneId = field("AvailabilityZoneId")
    Tags = field("Tags")
    SupportedHardwareType = field("SupportedHardwareType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOutpostInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOutpostInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Outpost:
    boto3_raw_data: "type_defs.OutpostTypeDef" = dataclasses.field()

    OutpostId = field("OutpostId")
    OwnerId = field("OwnerId")
    OutpostArn = field("OutpostArn")
    SiteId = field("SiteId")
    Name = field("Name")
    Description = field("Description")
    LifeCycleStatus = field("LifeCycleStatus")
    AvailabilityZone = field("AvailabilityZone")
    AvailabilityZoneId = field("AvailabilityZoneId")
    Tags = field("Tags")
    SiteArn = field("SiteArn")
    SupportedHardwareType = field("SupportedHardwareType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutpostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutpostTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RackPhysicalProperties:
    boto3_raw_data: "type_defs.RackPhysicalPropertiesTypeDef" = dataclasses.field()

    PowerDrawKva = field("PowerDrawKva")
    PowerPhase = field("PowerPhase")
    PowerConnector = field("PowerConnector")
    PowerFeedDrop = field("PowerFeedDrop")
    UplinkGbps = field("UplinkGbps")
    UplinkCount = field("UplinkCount")
    FiberOpticCableType = field("FiberOpticCableType")
    OpticalStandard = field("OpticalStandard")
    MaximumSupportedWeightLbs = field("MaximumSupportedWeightLbs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RackPhysicalPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RackPhysicalPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutpostInput:
    boto3_raw_data: "type_defs.DeleteOutpostInputTypeDef" = dataclasses.field()

    OutpostId = field("OutpostId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOutpostInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOutpostInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSiteInput:
    boto3_raw_data: "type_defs.DeleteSiteInputTypeDef" = dataclasses.field()

    SiteId = field("SiteId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteSiteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteSiteInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapacityTaskInput:
    boto3_raw_data: "type_defs.GetCapacityTaskInputTypeDef" = dataclasses.field()

    CapacityTaskId = field("CapacityTaskId")
    OutpostIdentifier = field("OutpostIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCapacityTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapacityTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTypeCapacity:
    boto3_raw_data: "type_defs.InstanceTypeCapacityTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    Count = field("Count")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeCapacityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeCapacityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancesToExcludeOutput:
    boto3_raw_data: "type_defs.InstancesToExcludeOutputTypeDef" = dataclasses.field()

    Instances = field("Instances")
    AccountIds = field("AccountIds")
    Services = field("Services")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancesToExcludeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancesToExcludeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCatalogItemInput:
    boto3_raw_data: "type_defs.GetCatalogItemInputTypeDef" = dataclasses.field()

    CatalogItemId = field("CatalogItemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCatalogItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCatalogItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionRequest:
    boto3_raw_data: "type_defs.GetConnectionRequestTypeDef" = dataclasses.field()

    ConnectionId = field("ConnectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrderInput:
    boto3_raw_data: "type_defs.GetOrderInputTypeDef" = dataclasses.field()

    OrderId = field("OrderId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOrderInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetOrderInputTypeDef"]],
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
class GetOutpostBillingInformationInput:
    boto3_raw_data: "type_defs.GetOutpostBillingInformationInputTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifier = field("OutpostIdentifier")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostBillingInformationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostBillingInformationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subscription:
    boto3_raw_data: "type_defs.SubscriptionTypeDef" = dataclasses.field()

    SubscriptionId = field("SubscriptionId")
    SubscriptionType = field("SubscriptionType")
    SubscriptionStatus = field("SubscriptionStatus")
    OrderIds = field("OrderIds")
    BeginDate = field("BeginDate")
    EndDate = field("EndDate")
    MonthlyRecurringPrice = field("MonthlyRecurringPrice")
    UpfrontPrice = field("UpfrontPrice")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubscriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostInput:
    boto3_raw_data: "type_defs.GetOutpostInputTypeDef" = dataclasses.field()

    OutpostId = field("OutpostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOutpostInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetOutpostInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostInstanceTypesInput:
    boto3_raw_data: "type_defs.GetOutpostInstanceTypesInputTypeDef" = (
        dataclasses.field()
    )

    OutpostId = field("OutpostId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOutpostInstanceTypesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostInstanceTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTypeItem:
    boto3_raw_data: "type_defs.InstanceTypeItemTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    VCPUs = field("VCPUs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostSupportedInstanceTypesInput:
    boto3_raw_data: "type_defs.GetOutpostSupportedInstanceTypesInputTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifier = field("OutpostIdentifier")
    OrderId = field("OrderId")
    AssetId = field("AssetId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostSupportedInstanceTypesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostSupportedInstanceTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSiteAddressInput:
    boto3_raw_data: "type_defs.GetSiteAddressInputTypeDef" = dataclasses.field()

    SiteId = field("SiteId")
    AddressType = field("AddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSiteAddressInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSiteAddressInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSiteInput:
    boto3_raw_data: "type_defs.GetSiteInputTypeDef" = dataclasses.field()

    SiteId = field("SiteId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSiteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSiteInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancesToExclude:
    boto3_raw_data: "type_defs.InstancesToExcludeTypeDef" = dataclasses.field()

    Instances = field("Instances")
    AccountIds = field("AccountIds")
    Services = field("Services")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancesToExcludeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancesToExcludeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItemAssetInformation:
    boto3_raw_data: "type_defs.LineItemAssetInformationTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    MacAddressList = field("MacAddressList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineItemAssetInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineItemAssetInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShipmentInformation:
    boto3_raw_data: "type_defs.ShipmentInformationTypeDef" = dataclasses.field()

    ShipmentTrackingNumber = field("ShipmentTrackingNumber")
    ShipmentCarrier = field("ShipmentCarrier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShipmentInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShipmentInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetInstancesInput:
    boto3_raw_data: "type_defs.ListAssetInstancesInputTypeDef" = dataclasses.field()

    OutpostIdentifier = field("OutpostIdentifier")
    AssetIdFilter = field("AssetIdFilter")
    InstanceTypeFilter = field("InstanceTypeFilter")
    AccountIdFilter = field("AccountIdFilter")
    AwsServiceFilter = field("AwsServiceFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetsInput:
    boto3_raw_data: "type_defs.ListAssetsInputTypeDef" = dataclasses.field()

    OutpostIdentifier = field("OutpostIdentifier")
    HostIdFilter = field("HostIdFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    StatusFilter = field("StatusFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAssetsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAssetsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBlockingInstancesForCapacityTaskInput:
    boto3_raw_data: "type_defs.ListBlockingInstancesForCapacityTaskInputTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifier = field("OutpostIdentifier")
    CapacityTaskId = field("CapacityTaskId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBlockingInstancesForCapacityTaskInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBlockingInstancesForCapacityTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapacityTasksInput:
    boto3_raw_data: "type_defs.ListCapacityTasksInputTypeDef" = dataclasses.field()

    OutpostIdentifierFilter = field("OutpostIdentifierFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    CapacityTaskStatusFilter = field("CapacityTaskStatusFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCapacityTasksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapacityTasksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCatalogItemsInput:
    boto3_raw_data: "type_defs.ListCatalogItemsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ItemClassFilter = field("ItemClassFilter")
    SupportedStorageFilter = field("SupportedStorageFilter")
    EC2FamilyFilter = field("EC2FamilyFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCatalogItemsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCatalogItemsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrdersInput:
    boto3_raw_data: "type_defs.ListOrdersInputTypeDef" = dataclasses.field()

    OutpostIdentifierFilter = field("OutpostIdentifierFilter")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListOrdersInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListOrdersInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderSummary:
    boto3_raw_data: "type_defs.OrderSummaryTypeDef" = dataclasses.field()

    OutpostId = field("OutpostId")
    OrderId = field("OrderId")
    OrderType = field("OrderType")
    Status = field("Status")
    LineItemCountsByStatus = field("LineItemCountsByStatus")
    OrderSubmissionDate = field("OrderSubmissionDate")
    OrderFulfilledDate = field("OrderFulfilledDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrderSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrderSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutpostsInput:
    boto3_raw_data: "type_defs.ListOutpostsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    LifeCycleStatusFilter = field("LifeCycleStatusFilter")
    AvailabilityZoneFilter = field("AvailabilityZoneFilter")
    AvailabilityZoneIdFilter = field("AvailabilityZoneIdFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListOutpostsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutpostsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSitesInput:
    boto3_raw_data: "type_defs.ListSitesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    OperatingAddressCountryCodeFilter = field("OperatingAddressCountryCodeFilter")
    OperatingAddressStateOrRegionFilter = field("OperatingAddressStateOrRegionFilter")
    OperatingAddressCityFilter = field("OperatingAddressCityFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSitesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListSitesInputTypeDef"]],
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
class StartConnectionRequest:
    boto3_raw_data: "type_defs.StartConnectionRequestTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    ClientPublicKey = field("ClientPublicKey")
    NetworkInterfaceDeviceIndex = field("NetworkInterfaceDeviceIndex")
    DeviceSerialNumber = field("DeviceSerialNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConnectionRequestTypeDef"]
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
class UpdateOutpostInput:
    boto3_raw_data: "type_defs.UpdateOutpostInputTypeDef" = dataclasses.field()

    OutpostId = field("OutpostId")
    Name = field("Name")
    Description = field("Description")
    SupportedHardwareType = field("SupportedHardwareType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOutpostInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOutpostInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteInput:
    boto3_raw_data: "type_defs.UpdateSiteInputTypeDef" = dataclasses.field()

    SiteId = field("SiteId")
    Name = field("Name")
    Description = field("Description")
    Notes = field("Notes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateSiteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateSiteInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteRackPhysicalPropertiesInput:
    boto3_raw_data: "type_defs.UpdateSiteRackPhysicalPropertiesInputTypeDef" = (
        dataclasses.field()
    )

    SiteId = field("SiteId")
    PowerDrawKva = field("PowerDrawKva")
    PowerPhase = field("PowerPhase")
    PowerConnector = field("PowerConnector")
    PowerFeedDrop = field("PowerFeedDrop")
    UplinkGbps = field("UplinkGbps")
    UplinkCount = field("UplinkCount")
    FiberOpticCableType = field("FiberOpticCableType")
    OpticalStandard = field("OpticalStandard")
    MaximumSupportedWeightLbs = field("MaximumSupportedWeightLbs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSiteRackPhysicalPropertiesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteRackPhysicalPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteAddressInput:
    boto3_raw_data: "type_defs.UpdateSiteAddressInputTypeDef" = dataclasses.field()

    SiteId = field("SiteId")
    AddressType = field("AddressType")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSiteAddressInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteAddressInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeAttributes:
    boto3_raw_data: "type_defs.ComputeAttributesTypeDef" = dataclasses.field()

    HostId = field("HostId")
    State = field("State")
    InstanceFamilies = field("InstanceFamilies")

    @cached_property
    def InstanceTypeCapacities(self):  # pragma: no cover
        return AssetInstanceTypeCapacity.make_many(
            self.boto3_raw_data["InstanceTypeCapacities"]
        )

    MaxVcpus = field("MaxVcpus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CatalogItem:
    boto3_raw_data: "type_defs.CatalogItemTypeDef" = dataclasses.field()

    CatalogItemId = field("CatalogItemId")
    ItemStatus = field("ItemStatus")

    @cached_property
    def EC2Capacities(self):  # pragma: no cover
        return EC2Capacity.make_many(self.boto3_raw_data["EC2Capacities"])

    PowerKva = field("PowerKva")
    WeightLbs = field("WeightLbs")
    SupportedUplinkGbps = field("SupportedUplinkGbps")
    SupportedStorage = field("SupportedStorage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CatalogItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CatalogItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOrderInput:
    boto3_raw_data: "type_defs.CreateOrderInputTypeDef" = dataclasses.field()

    OutpostIdentifier = field("OutpostIdentifier")

    @cached_property
    def LineItems(self):  # pragma: no cover
        return LineItemRequest.make_many(self.boto3_raw_data["LineItems"])

    PaymentOption = field("PaymentOption")
    PaymentTerm = field("PaymentTerm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateOrderInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOrderInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionResponse:
    boto3_raw_data: "type_defs.GetConnectionResponseTypeDef" = dataclasses.field()

    ConnectionId = field("ConnectionId")

    @cached_property
    def ConnectionDetails(self):  # pragma: no cover
        return ConnectionDetails.make_one(self.boto3_raw_data["ConnectionDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSiteAddressOutput:
    boto3_raw_data: "type_defs.GetSiteAddressOutputTypeDef" = dataclasses.field()

    SiteId = field("SiteId")
    AddressType = field("AddressType")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSiteAddressOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSiteAddressOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetInstancesOutput:
    boto3_raw_data: "type_defs.ListAssetInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def AssetInstances(self):  # pragma: no cover
        return AssetInstance.make_many(self.boto3_raw_data["AssetInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBlockingInstancesForCapacityTaskOutput:
    boto3_raw_data: "type_defs.ListBlockingInstancesForCapacityTaskOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlockingInstances(self):  # pragma: no cover
        return BlockingInstance.make_many(self.boto3_raw_data["BlockingInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBlockingInstancesForCapacityTaskOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBlockingInstancesForCapacityTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapacityTasksOutput:
    boto3_raw_data: "type_defs.ListCapacityTasksOutputTypeDef" = dataclasses.field()

    @cached_property
    def CapacityTasks(self):  # pragma: no cover
        return CapacityTaskSummary.make_many(self.boto3_raw_data["CapacityTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCapacityTasksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapacityTasksOutputTypeDef"]
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
class StartConnectionResponse:
    boto3_raw_data: "type_defs.StartConnectionResponseTypeDef" = dataclasses.field()

    ConnectionId = field("ConnectionId")
    UnderlayIpAddress = field("UnderlayIpAddress")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteAddressOutput:
    boto3_raw_data: "type_defs.UpdateSiteAddressOutputTypeDef" = dataclasses.field()

    AddressType = field("AddressType")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSiteAddressOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteAddressOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOutpostOutput:
    boto3_raw_data: "type_defs.CreateOutpostOutputTypeDef" = dataclasses.field()

    @cached_property
    def Outpost(self):  # pragma: no cover
        return Outpost.make_one(self.boto3_raw_data["Outpost"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOutpostOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOutpostOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostOutput:
    boto3_raw_data: "type_defs.GetOutpostOutputTypeDef" = dataclasses.field()

    @cached_property
    def Outpost(self):  # pragma: no cover
        return Outpost.make_one(self.boto3_raw_data["Outpost"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOutpostOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutpostsOutput:
    boto3_raw_data: "type_defs.ListOutpostsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Outposts(self):  # pragma: no cover
        return Outpost.make_many(self.boto3_raw_data["Outposts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOutpostsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutpostsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOutpostOutput:
    boto3_raw_data: "type_defs.UpdateOutpostOutputTypeDef" = dataclasses.field()

    @cached_property
    def Outpost(self):  # pragma: no cover
        return Outpost.make_one(self.boto3_raw_data["Outpost"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOutpostOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOutpostOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSiteInput:
    boto3_raw_data: "type_defs.CreateSiteInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Notes = field("Notes")
    Tags = field("Tags")

    @cached_property
    def OperatingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["OperatingAddress"])

    @cached_property
    def ShippingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["ShippingAddress"])

    @cached_property
    def RackPhysicalProperties(self):  # pragma: no cover
        return RackPhysicalProperties.make_one(
            self.boto3_raw_data["RackPhysicalProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateSiteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateSiteInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Site:
    boto3_raw_data: "type_defs.SiteTypeDef" = dataclasses.field()

    SiteId = field("SiteId")
    AccountId = field("AccountId")
    Name = field("Name")
    Description = field("Description")
    Tags = field("Tags")
    SiteArn = field("SiteArn")
    Notes = field("Notes")
    OperatingAddressCountryCode = field("OperatingAddressCountryCode")
    OperatingAddressStateOrRegion = field("OperatingAddressStateOrRegion")
    OperatingAddressCity = field("OperatingAddressCity")

    @cached_property
    def RackPhysicalProperties(self):  # pragma: no cover
        return RackPhysicalProperties.make_one(
            self.boto3_raw_data["RackPhysicalProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SiteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SiteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapacityTaskOutput:
    boto3_raw_data: "type_defs.GetCapacityTaskOutputTypeDef" = dataclasses.field()

    CapacityTaskId = field("CapacityTaskId")
    OutpostId = field("OutpostId")
    OrderId = field("OrderId")
    AssetId = field("AssetId")

    @cached_property
    def RequestedInstancePools(self):  # pragma: no cover
        return InstanceTypeCapacity.make_many(
            self.boto3_raw_data["RequestedInstancePools"]
        )

    @cached_property
    def InstancesToExclude(self):  # pragma: no cover
        return InstancesToExcludeOutput.make_one(
            self.boto3_raw_data["InstancesToExclude"]
        )

    DryRun = field("DryRun")
    CapacityTaskStatus = field("CapacityTaskStatus")

    @cached_property
    def Failed(self):  # pragma: no cover
        return CapacityTaskFailure.make_one(self.boto3_raw_data["Failed"])

    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    LastModifiedDate = field("LastModifiedDate")
    TaskActionOnBlockingInstances = field("TaskActionOnBlockingInstances")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCapacityTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapacityTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCapacityTaskOutput:
    boto3_raw_data: "type_defs.StartCapacityTaskOutputTypeDef" = dataclasses.field()

    CapacityTaskId = field("CapacityTaskId")
    OutpostId = field("OutpostId")
    OrderId = field("OrderId")
    AssetId = field("AssetId")

    @cached_property
    def RequestedInstancePools(self):  # pragma: no cover
        return InstanceTypeCapacity.make_many(
            self.boto3_raw_data["RequestedInstancePools"]
        )

    @cached_property
    def InstancesToExclude(self):  # pragma: no cover
        return InstancesToExcludeOutput.make_one(
            self.boto3_raw_data["InstancesToExclude"]
        )

    DryRun = field("DryRun")
    CapacityTaskStatus = field("CapacityTaskStatus")

    @cached_property
    def Failed(self):  # pragma: no cover
        return CapacityTaskFailure.make_one(self.boto3_raw_data["Failed"])

    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    LastModifiedDate = field("LastModifiedDate")
    TaskActionOnBlockingInstances = field("TaskActionOnBlockingInstances")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCapacityTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCapacityTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostBillingInformationInputPaginate:
    boto3_raw_data: "type_defs.GetOutpostBillingInformationInputPaginateTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifier = field("OutpostIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostBillingInformationInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostBillingInformationInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostInstanceTypesInputPaginate:
    boto3_raw_data: "type_defs.GetOutpostInstanceTypesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    OutpostId = field("OutpostId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostInstanceTypesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostInstanceTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostSupportedInstanceTypesInputPaginate:
    boto3_raw_data: "type_defs.GetOutpostSupportedInstanceTypesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifier = field("OutpostIdentifier")
    OrderId = field("OrderId")
    AssetId = field("AssetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostSupportedInstanceTypesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostSupportedInstanceTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListAssetInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifier = field("OutpostIdentifier")
    AssetIdFilter = field("AssetIdFilter")
    InstanceTypeFilter = field("InstanceTypeFilter")
    AccountIdFilter = field("AccountIdFilter")
    AwsServiceFilter = field("AwsServiceFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetInstancesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetsInputPaginate:
    boto3_raw_data: "type_defs.ListAssetsInputPaginateTypeDef" = dataclasses.field()

    OutpostIdentifier = field("OutpostIdentifier")
    HostIdFilter = field("HostIdFilter")
    StatusFilter = field("StatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBlockingInstancesForCapacityTaskInputPaginate:
    boto3_raw_data: (
        "type_defs.ListBlockingInstancesForCapacityTaskInputPaginateTypeDef"
    ) = dataclasses.field()

    OutpostIdentifier = field("OutpostIdentifier")
    CapacityTaskId = field("CapacityTaskId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBlockingInstancesForCapacityTaskInputPaginateTypeDef"
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
                "type_defs.ListBlockingInstancesForCapacityTaskInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapacityTasksInputPaginate:
    boto3_raw_data: "type_defs.ListCapacityTasksInputPaginateTypeDef" = (
        dataclasses.field()
    )

    OutpostIdentifierFilter = field("OutpostIdentifierFilter")
    CapacityTaskStatusFilter = field("CapacityTaskStatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCapacityTasksInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapacityTasksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCatalogItemsInputPaginate:
    boto3_raw_data: "type_defs.ListCatalogItemsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ItemClassFilter = field("ItemClassFilter")
    SupportedStorageFilter = field("SupportedStorageFilter")
    EC2FamilyFilter = field("EC2FamilyFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCatalogItemsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCatalogItemsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrdersInputPaginate:
    boto3_raw_data: "type_defs.ListOrdersInputPaginateTypeDef" = dataclasses.field()

    OutpostIdentifierFilter = field("OutpostIdentifierFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOrdersInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrdersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutpostsInputPaginate:
    boto3_raw_data: "type_defs.ListOutpostsInputPaginateTypeDef" = dataclasses.field()

    LifeCycleStatusFilter = field("LifeCycleStatusFilter")
    AvailabilityZoneFilter = field("AvailabilityZoneFilter")
    AvailabilityZoneIdFilter = field("AvailabilityZoneIdFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOutpostsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutpostsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSitesInputPaginate:
    boto3_raw_data: "type_defs.ListSitesInputPaginateTypeDef" = dataclasses.field()

    OperatingAddressCountryCodeFilter = field("OperatingAddressCountryCodeFilter")
    OperatingAddressStateOrRegionFilter = field("OperatingAddressStateOrRegionFilter")
    OperatingAddressCityFilter = field("OperatingAddressCityFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSitesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSitesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostBillingInformationOutput:
    boto3_raw_data: "type_defs.GetOutpostBillingInformationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["Subscriptions"])

    ContractEndDate = field("ContractEndDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostBillingInformationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostBillingInformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostInstanceTypesOutput:
    boto3_raw_data: "type_defs.GetOutpostInstanceTypesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceTypes(self):  # pragma: no cover
        return InstanceTypeItem.make_many(self.boto3_raw_data["InstanceTypes"])

    OutpostId = field("OutpostId")
    OutpostArn = field("OutpostArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOutpostInstanceTypesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostInstanceTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostSupportedInstanceTypesOutput:
    boto3_raw_data: "type_defs.GetOutpostSupportedInstanceTypesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceTypes(self):  # pragma: no cover
        return InstanceTypeItem.make_many(self.boto3_raw_data["InstanceTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOutpostSupportedInstanceTypesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostSupportedInstanceTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItem:
    boto3_raw_data: "type_defs.LineItemTypeDef" = dataclasses.field()

    CatalogItemId = field("CatalogItemId")
    LineItemId = field("LineItemId")
    Quantity = field("Quantity")
    Status = field("Status")

    @cached_property
    def ShipmentInformation(self):  # pragma: no cover
        return ShipmentInformation.make_one(self.boto3_raw_data["ShipmentInformation"])

    @cached_property
    def AssetInformationList(self):  # pragma: no cover
        return LineItemAssetInformation.make_many(
            self.boto3_raw_data["AssetInformationList"]
        )

    PreviousLineItemId = field("PreviousLineItemId")
    PreviousOrderId = field("PreviousOrderId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrdersOutput:
    boto3_raw_data: "type_defs.ListOrdersOutputTypeDef" = dataclasses.field()

    @cached_property
    def Orders(self):  # pragma: no cover
        return OrderSummary.make_many(self.boto3_raw_data["Orders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListOrdersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrdersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetInfo:
    boto3_raw_data: "type_defs.AssetInfoTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    RackId = field("RackId")
    AssetType = field("AssetType")

    @cached_property
    def ComputeAttributes(self):  # pragma: no cover
        return ComputeAttributes.make_one(self.boto3_raw_data["ComputeAttributes"])

    @cached_property
    def AssetLocation(self):  # pragma: no cover
        return AssetLocation.make_one(self.boto3_raw_data["AssetLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCatalogItemOutput:
    boto3_raw_data: "type_defs.GetCatalogItemOutputTypeDef" = dataclasses.field()

    @cached_property
    def CatalogItem(self):  # pragma: no cover
        return CatalogItem.make_one(self.boto3_raw_data["CatalogItem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCatalogItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCatalogItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCatalogItemsOutput:
    boto3_raw_data: "type_defs.ListCatalogItemsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CatalogItems(self):  # pragma: no cover
        return CatalogItem.make_many(self.boto3_raw_data["CatalogItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCatalogItemsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCatalogItemsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSiteOutput:
    boto3_raw_data: "type_defs.CreateSiteOutputTypeDef" = dataclasses.field()

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateSiteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSiteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSiteOutput:
    boto3_raw_data: "type_defs.GetSiteOutputTypeDef" = dataclasses.field()

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSiteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSiteOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSitesOutput:
    boto3_raw_data: "type_defs.ListSitesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Sites(self):  # pragma: no cover
        return Site.make_many(self.boto3_raw_data["Sites"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSitesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListSitesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteOutput:
    boto3_raw_data: "type_defs.UpdateSiteOutputTypeDef" = dataclasses.field()

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateSiteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSiteRackPhysicalPropertiesOutput:
    boto3_raw_data: "type_defs.UpdateSiteRackPhysicalPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Site(self):  # pragma: no cover
        return Site.make_one(self.boto3_raw_data["Site"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSiteRackPhysicalPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSiteRackPhysicalPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCapacityTaskInput:
    boto3_raw_data: "type_defs.StartCapacityTaskInputTypeDef" = dataclasses.field()

    OutpostIdentifier = field("OutpostIdentifier")

    @cached_property
    def InstancePools(self):  # pragma: no cover
        return InstanceTypeCapacity.make_many(self.boto3_raw_data["InstancePools"])

    OrderId = field("OrderId")
    AssetId = field("AssetId")
    InstancesToExclude = field("InstancesToExclude")
    DryRun = field("DryRun")
    TaskActionOnBlockingInstances = field("TaskActionOnBlockingInstances")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCapacityTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCapacityTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Order:
    boto3_raw_data: "type_defs.OrderTypeDef" = dataclasses.field()

    OutpostId = field("OutpostId")
    OrderId = field("OrderId")
    Status = field("Status")

    @cached_property
    def LineItems(self):  # pragma: no cover
        return LineItem.make_many(self.boto3_raw_data["LineItems"])

    PaymentOption = field("PaymentOption")
    OrderSubmissionDate = field("OrderSubmissionDate")
    OrderFulfilledDate = field("OrderFulfilledDate")
    PaymentTerm = field("PaymentTerm")
    OrderType = field("OrderType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetsOutput:
    boto3_raw_data: "type_defs.ListAssetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return AssetInfo.make_many(self.boto3_raw_data["Assets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAssetsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOrderOutput:
    boto3_raw_data: "type_defs.CreateOrderOutputTypeDef" = dataclasses.field()

    @cached_property
    def Order(self):  # pragma: no cover
        return Order.make_one(self.boto3_raw_data["Order"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateOrderOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOrderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrderOutput:
    boto3_raw_data: "type_defs.GetOrderOutputTypeDef" = dataclasses.field()

    @cached_property
    def Order(self):  # pragma: no cover
        return Order.make_one(self.boto3_raw_data["Order"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOrderOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetOrderOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
