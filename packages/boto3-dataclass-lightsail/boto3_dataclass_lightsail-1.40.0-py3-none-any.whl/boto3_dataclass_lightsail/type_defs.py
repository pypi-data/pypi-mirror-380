# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lightsail import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessKeyLastUsed:
    boto3_raw_data: "type_defs.AccessKeyLastUsedTypeDef" = dataclasses.field()

    lastUsedDate = field("lastUsedDate")
    region = field("region")
    serviceName = field("serviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyLastUsedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessKeyLastUsedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessRules:
    boto3_raw_data: "type_defs.AccessRulesTypeDef" = dataclasses.field()

    getObject = field("getObject")
    allowPublicOverrides = field("allowPublicOverrides")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessRulesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessRulesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLevelBpaSync:
    boto3_raw_data: "type_defs.AccountLevelBpaSyncTypeDef" = dataclasses.field()

    status = field("status")
    lastSyncedAt = field("lastSyncedAt")
    message = field("message")
    bpaImpactsLightsail = field("bpaImpactsLightsail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountLevelBpaSyncTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountLevelBpaSyncTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoSnapshotAddOnRequest:
    boto3_raw_data: "type_defs.AutoSnapshotAddOnRequestTypeDef" = dataclasses.field()

    snapshotTimeOfDay = field("snapshotTimeOfDay")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoSnapshotAddOnRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoSnapshotAddOnRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInstanceOnIdleRequest:
    boto3_raw_data: "type_defs.StopInstanceOnIdleRequestTypeDef" = dataclasses.field()

    threshold = field("threshold")
    duration = field("duration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopInstanceOnIdleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInstanceOnIdleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddOn:
    boto3_raw_data: "type_defs.AddOnTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")
    snapshotTimeOfDay = field("snapshotTimeOfDay")
    nextSnapshotTimeOfDay = field("nextSnapshotTimeOfDay")
    threshold = field("threshold")
    duration = field("duration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddOnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddOnTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoredResourceInfo:
    boto3_raw_data: "type_defs.MonitoredResourceInfoTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoredResourceInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoredResourceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceLocation:
    boto3_raw_data: "type_defs.ResourceLocationTypeDef" = dataclasses.field()

    availabilityZone = field("availabilityZone")
    regionName = field("regionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocateStaticIpRequest:
    boto3_raw_data: "type_defs.AllocateStaticIpRequestTypeDef" = dataclasses.field()

    staticIpName = field("staticIpName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllocateStaticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocateStaticIpRequestTypeDef"]
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
class AttachCertificateToDistributionRequest:
    boto3_raw_data: "type_defs.AttachCertificateToDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    distributionName = field("distributionName")
    certificateName = field("certificateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachCertificateToDistributionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachCertificateToDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachDiskRequest:
    boto3_raw_data: "type_defs.AttachDiskRequestTypeDef" = dataclasses.field()

    diskName = field("diskName")
    instanceName = field("instanceName")
    diskPath = field("diskPath")
    autoMounting = field("autoMounting")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachDiskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachDiskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachInstancesToLoadBalancerRequest:
    boto3_raw_data: "type_defs.AttachInstancesToLoadBalancerRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    instanceNames = field("instanceNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachInstancesToLoadBalancerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachInstancesToLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachLoadBalancerTlsCertificateRequest:
    boto3_raw_data: "type_defs.AttachLoadBalancerTlsCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    certificateName = field("certificateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachLoadBalancerTlsCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachLoadBalancerTlsCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachStaticIpRequest:
    boto3_raw_data: "type_defs.AttachStaticIpRequestTypeDef" = dataclasses.field()

    staticIpName = field("staticIpName")
    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachStaticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachStaticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachedDisk:
    boto3_raw_data: "type_defs.AttachedDiskTypeDef" = dataclasses.field()

    path = field("path")
    sizeInGb = field("sizeInGb")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachedDiskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachedDiskTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZone:
    boto3_raw_data: "type_defs.AvailabilityZoneTypeDef" = dataclasses.field()

    zoneName = field("zoneName")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Blueprint:
    boto3_raw_data: "type_defs.BlueprintTypeDef" = dataclasses.field()

    blueprintId = field("blueprintId")
    name = field("name")
    group = field("group")
    type = field("type")
    description = field("description")
    isActive = field("isActive")
    minPower = field("minPower")
    version = field("version")
    versionCode = field("versionCode")
    productUrl = field("productUrl")
    licenseUrl = field("licenseUrl")
    platform = field("platform")
    appCategory = field("appCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlueprintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlueprintTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketAccessLogConfig:
    boto3_raw_data: "type_defs.BucketAccessLogConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")
    destination = field("destination")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketAccessLogConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketAccessLogConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketBundle:
    boto3_raw_data: "type_defs.BucketBundleTypeDef" = dataclasses.field()

    bundleId = field("bundleId")
    name = field("name")
    price = field("price")
    storagePerMonthInGb = field("storagePerMonthInGb")
    transferPerMonthInGb = field("transferPerMonthInGb")
    isActive = field("isActive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketBundleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketBundleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketState:
    boto3_raw_data: "type_defs.BucketStateTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceReceivingAccess:
    boto3_raw_data: "type_defs.ResourceReceivingAccessTypeDef" = dataclasses.field()

    name = field("name")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceReceivingAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceReceivingAccessTypeDef"]
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
class Bundle:
    boto3_raw_data: "type_defs.BundleTypeDef" = dataclasses.field()

    price = field("price")
    cpuCount = field("cpuCount")
    diskSizeInGb = field("diskSizeInGb")
    bundleId = field("bundleId")
    instanceType = field("instanceType")
    isActive = field("isActive")
    name = field("name")
    power = field("power")
    ramSizeInGb = field("ramSizeInGb")
    transferPerMonthInGb = field("transferPerMonthInGb")
    supportedPlatforms = field("supportedPlatforms")
    supportedAppCategories = field("supportedAppCategories")
    publicIpv4AddressCount = field("publicIpv4AddressCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BundleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BundleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheBehaviorPerPath:
    boto3_raw_data: "type_defs.CacheBehaviorPerPathTypeDef" = dataclasses.field()

    path = field("path")
    behavior = field("behavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheBehaviorPerPathTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheBehaviorPerPathTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheBehavior:
    boto3_raw_data: "type_defs.CacheBehaviorTypeDef" = dataclasses.field()

    behavior = field("behavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheBehaviorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheBehaviorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieObjectOutput:
    boto3_raw_data: "type_defs.CookieObjectOutputTypeDef" = dataclasses.field()

    option = field("option")
    cookiesAllowList = field("cookiesAllowList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CookieObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderObjectOutput:
    boto3_raw_data: "type_defs.HeaderObjectOutputTypeDef" = dataclasses.field()

    option = field("option")
    headersAllowList = field("headersAllowList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeaderObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeaderObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringObjectOutput:
    boto3_raw_data: "type_defs.QueryStringObjectOutputTypeDef" = dataclasses.field()

    option = field("option")
    queryStringsAllowList = field("queryStringsAllowList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStringObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieObject:
    boto3_raw_data: "type_defs.CookieObjectTypeDef" = dataclasses.field()

    option = field("option")
    cookiesAllowList = field("cookiesAllowList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CookieObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CookieObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderObject:
    boto3_raw_data: "type_defs.HeaderObjectTypeDef" = dataclasses.field()

    option = field("option")
    headersAllowList = field("headersAllowList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeaderObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeaderObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringObject:
    boto3_raw_data: "type_defs.QueryStringObjectTypeDef" = dataclasses.field()

    option = field("option")
    queryStringsAllowList = field("queryStringsAllowList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryStringObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortInfo:
    boto3_raw_data: "type_defs.PortInfoTypeDef" = dataclasses.field()

    fromPort = field("fromPort")
    toPort = field("toPort")
    protocol = field("protocol")
    cidrs = field("cidrs")
    ipv6Cidrs = field("ipv6Cidrs")
    cidrListAliases = field("cidrListAliases")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationStackRecordSourceInfo:
    boto3_raw_data: "type_defs.CloudFormationStackRecordSourceInfoTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    name = field("name")
    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudFormationStackRecordSourceInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationStackRecordSourceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationInfo:
    boto3_raw_data: "type_defs.DestinationInfoTypeDef" = dataclasses.field()

    id = field("id")
    service = field("service")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerImage:
    boto3_raw_data: "type_defs.ContainerImageTypeDef" = dataclasses.field()

    image = field("image")
    digest = field("digest")
    createdAt = field("createdAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerImageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerOutput:
    boto3_raw_data: "type_defs.ContainerOutputTypeDef" = dataclasses.field()

    image = field("image")
    command = field("command")
    environment = field("environment")
    ports = field("ports")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceECRImagePullerRoleRequest:
    boto3_raw_data: "type_defs.ContainerServiceECRImagePullerRoleRequestTypeDef" = (
        dataclasses.field()
    )

    isActive = field("isActive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerServiceECRImagePullerRoleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceECRImagePullerRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceECRImagePullerRole:
    boto3_raw_data: "type_defs.ContainerServiceECRImagePullerRoleTypeDef" = (
        dataclasses.field()
    )

    isActive = field("isActive")
    principalArn = field("principalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerServiceECRImagePullerRoleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceECRImagePullerRoleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceHealthCheckConfig:
    boto3_raw_data: "type_defs.ContainerServiceHealthCheckConfigTypeDef" = (
        dataclasses.field()
    )

    healthyThreshold = field("healthyThreshold")
    unhealthyThreshold = field("unhealthyThreshold")
    timeoutSeconds = field("timeoutSeconds")
    intervalSeconds = field("intervalSeconds")
    path = field("path")
    successCodes = field("successCodes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerServiceHealthCheckConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceHealthCheckConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceLogEvent:
    boto3_raw_data: "type_defs.ContainerServiceLogEventTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerServiceLogEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceLogEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServicePower:
    boto3_raw_data: "type_defs.ContainerServicePowerTypeDef" = dataclasses.field()

    powerId = field("powerId")
    price = field("price")
    cpuCount = field("cpuCount")
    ramSizeInGb = field("ramSizeInGb")
    name = field("name")
    isActive = field("isActive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerServicePowerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServicePowerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceRegistryLogin:
    boto3_raw_data: "type_defs.ContainerServiceRegistryLoginTypeDef" = (
        dataclasses.field()
    )

    username = field("username")
    password = field("password")
    expiresAt = field("expiresAt")
    registry = field("registry")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContainerServiceRegistryLoginTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceRegistryLoginTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceStateDetail:
    boto3_raw_data: "type_defs.ContainerServiceStateDetailTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerServiceStateDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceStateDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Container:
    boto3_raw_data: "type_defs.ContainerTypeDef" = dataclasses.field()

    image = field("image")
    command = field("command")
    environment = field("environment")
    ports = field("ports")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotRequest:
    boto3_raw_data: "type_defs.CopySnapshotRequestTypeDef" = dataclasses.field()

    targetSnapshotName = field("targetSnapshotName")
    sourceRegion = field("sourceRegion")
    sourceSnapshotName = field("sourceSnapshotName")
    sourceResourceName = field("sourceResourceName")
    restoreDate = field("restoreDate")
    useLatestRestorableAutoSnapshot = field("useLatestRestorableAutoSnapshot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketAccessKeyRequest:
    boto3_raw_data: "type_defs.CreateBucketAccessKeyRequestTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketAccessKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketAccessKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceEntry:
    boto3_raw_data: "type_defs.InstanceEntryTypeDef" = dataclasses.field()

    sourceName = field("sourceName")
    instanceType = field("instanceType")
    portInfoSource = field("portInfoSource")
    availabilityZone = field("availabilityZone")
    userData = field("userData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactMethodRequest:
    boto3_raw_data: "type_defs.CreateContactMethodRequestTypeDef" = dataclasses.field()

    protocol = field("protocol")
    contactEndpoint = field("contactEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactMethodRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputOrigin:
    boto3_raw_data: "type_defs.InputOriginTypeDef" = dataclasses.field()

    name = field("name")
    regionName = field("regionName")
    protocolPolicy = field("protocolPolicy")
    responseTimeout = field("responseTimeout")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputOriginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputOriginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGUISessionAccessDetailsRequest:
    boto3_raw_data: "type_defs.CreateGUISessionAccessDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGUISessionAccessDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGUISessionAccessDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    name = field("name")
    url = field("url")
    isPrimary = field("isPrimary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiskMap:
    boto3_raw_data: "type_defs.DiskMapTypeDef" = dataclasses.field()

    originalDiskPath = field("originalDiskPath")
    newDiskName = field("newDiskName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskMapTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiskMapTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAlarmRequest:
    boto3_raw_data: "type_defs.DeleteAlarmRequestTypeDef" = dataclasses.field()

    alarmName = field("alarmName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAlarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAlarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutoSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteAutoSnapshotRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")
    date = field("date")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAutoSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutoSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketAccessKeyRequest:
    boto3_raw_data: "type_defs.DeleteBucketAccessKeyRequestTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    accessKeyId = field("accessKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketAccessKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketAccessKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketRequest:
    boto3_raw_data: "type_defs.DeleteBucketRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    forceDelete = field("forceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateRequest:
    boto3_raw_data: "type_defs.DeleteCertificateRequestTypeDef" = dataclasses.field()

    certificateName = field("certificateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactMethodRequest:
    boto3_raw_data: "type_defs.DeleteContactMethodRequestTypeDef" = dataclasses.field()

    protocol = field("protocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactMethodRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContainerImageRequest:
    boto3_raw_data: "type_defs.DeleteContainerImageRequestTypeDef" = dataclasses.field()

    serviceName = field("serviceName")
    image = field("image")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContainerImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContainerImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContainerServiceRequest:
    boto3_raw_data: "type_defs.DeleteContainerServiceRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteContainerServiceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContainerServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDiskRequest:
    boto3_raw_data: "type_defs.DeleteDiskRequestTypeDef" = dataclasses.field()

    diskName = field("diskName")
    forceDeleteAddOns = field("forceDeleteAddOns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteDiskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDiskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDiskSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteDiskSnapshotRequestTypeDef" = dataclasses.field()

    diskSnapshotName = field("diskSnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDiskSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDiskSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDistributionRequest:
    boto3_raw_data: "type_defs.DeleteDistributionRequestTypeDef" = dataclasses.field()

    distributionName = field("distributionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceRequest:
    boto3_raw_data: "type_defs.DeleteInstanceRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    forceDeleteAddOns = field("forceDeleteAddOns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteInstanceSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    instanceSnapshotName = field("instanceSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInstanceSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyPairRequest:
    boto3_raw_data: "type_defs.DeleteKeyPairRequestTypeDef" = dataclasses.field()

    keyPairName = field("keyPairName")
    expectedFingerprint = field("expectedFingerprint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyPairRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeyPairRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnownHostKeysRequest:
    boto3_raw_data: "type_defs.DeleteKnownHostKeysRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKnownHostKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnownHostKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerRequest:
    boto3_raw_data: "type_defs.DeleteLoadBalancerRequestTypeDef" = dataclasses.field()

    loadBalancerName = field("loadBalancerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLoadBalancerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerTlsCertificateRequest:
    boto3_raw_data: "type_defs.DeleteLoadBalancerTlsCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    certificateName = field("certificateName")
    force = field("force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLoadBalancerTlsCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerTlsCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.DeleteRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    skipFinalSnapshot = field("skipFinalSnapshot")
    finalRelationalDatabaseSnapshotName = field("finalRelationalDatabaseSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRelationalDatabaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRelationalDatabaseSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteRelationalDatabaseSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseSnapshotName = field("relationalDatabaseSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRelationalDatabaseSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRelationalDatabaseSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachCertificateFromDistributionRequest:
    boto3_raw_data: "type_defs.DetachCertificateFromDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    distributionName = field("distributionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachCertificateFromDistributionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachCertificateFromDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachDiskRequest:
    boto3_raw_data: "type_defs.DetachDiskRequestTypeDef" = dataclasses.field()

    diskName = field("diskName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetachDiskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachDiskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachInstancesFromLoadBalancerRequest:
    boto3_raw_data: "type_defs.DetachInstancesFromLoadBalancerRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    instanceNames = field("instanceNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachInstancesFromLoadBalancerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachInstancesFromLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachStaticIpRequest:
    boto3_raw_data: "type_defs.DetachStaticIpRequestTypeDef" = dataclasses.field()

    staticIpName = field("staticIpName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachStaticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachStaticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableAddOnRequest:
    boto3_raw_data: "type_defs.DisableAddOnRequestTypeDef" = dataclasses.field()

    addOnType = field("addOnType")
    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableAddOnRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableAddOnRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiskInfo:
    boto3_raw_data: "type_defs.DiskInfoTypeDef" = dataclasses.field()

    name = field("name")
    path = field("path")
    sizeInGb = field("sizeInGb")
    isSystemDisk = field("isSystemDisk")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiskInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiskSnapshotInfo:
    boto3_raw_data: "type_defs.DiskSnapshotInfoTypeDef" = dataclasses.field()

    sizeInGb = field("sizeInGb")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskSnapshotInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiskSnapshotInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionBundle:
    boto3_raw_data: "type_defs.DistributionBundleTypeDef" = dataclasses.field()

    bundleId = field("bundleId")
    name = field("name")
    price = field("price")
    transferPerMonthInGb = field("transferPerMonthInGb")
    isActive = field("isActive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionBundleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionBundleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsRecordCreationState:
    boto3_raw_data: "type_defs.DnsRecordCreationStateTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DnsRecordCreationStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsRecordCreationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEntryOutput:
    boto3_raw_data: "type_defs.DomainEntryOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    target = field("target")
    isAlias = field("isAlias")
    type = field("type")
    options = field("options")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainEntryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEntry:
    boto3_raw_data: "type_defs.DomainEntryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    target = field("target")
    isAlias = field("isAlias")
    type = field("type")
    options = field("options")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceRecord:
    boto3_raw_data: "type_defs.ResourceRecordTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimePeriod:
    boto3_raw_data: "type_defs.TimePeriodTypeDef" = dataclasses.field()

    start = field("start")
    end = field("end")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimePeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimePeriodTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSnapshotRequest:
    boto3_raw_data: "type_defs.ExportSnapshotRequestTypeDef" = dataclasses.field()

    sourceSnapshotName = field("sourceSnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSnapshotRequestTypeDef"]
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
class GetActiveNamesRequest:
    boto3_raw_data: "type_defs.GetActiveNamesRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetActiveNamesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActiveNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAlarmsRequest:
    boto3_raw_data: "type_defs.GetAlarmsRequestTypeDef" = dataclasses.field()

    alarmName = field("alarmName")
    pageToken = field("pageToken")
    monitoredResourceName = field("monitoredResourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAlarmsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAlarmsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoSnapshotsRequest:
    boto3_raw_data: "type_defs.GetAutoSnapshotsRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAutoSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlueprintsRequest:
    boto3_raw_data: "type_defs.GetBlueprintsRequestTypeDef" = dataclasses.field()

    includeInactive = field("includeInactive")
    pageToken = field("pageToken")
    appCategory = field("appCategory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlueprintsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlueprintsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketAccessKeysRequest:
    boto3_raw_data: "type_defs.GetBucketAccessKeysRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketAccessKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAccessKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketBundlesRequest:
    boto3_raw_data: "type_defs.GetBucketBundlesRequestTypeDef" = dataclasses.field()

    includeInactive = field("includeInactive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketBundlesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketBundlesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDatapoint:
    boto3_raw_data: "type_defs.MetricDatapointTypeDef" = dataclasses.field()

    average = field("average")
    maximum = field("maximum")
    minimum = field("minimum")
    sampleCount = field("sampleCount")
    sum = field("sum")
    timestamp = field("timestamp")
    unit = field("unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDatapointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDatapointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketsRequest:
    boto3_raw_data: "type_defs.GetBucketsRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    pageToken = field("pageToken")
    includeConnectedResources = field("includeConnectedResources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBucketsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBundlesRequest:
    boto3_raw_data: "type_defs.GetBundlesRequestTypeDef" = dataclasses.field()

    includeInactive = field("includeInactive")
    pageToken = field("pageToken")
    appCategory = field("appCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBundlesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBundlesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificatesRequest:
    boto3_raw_data: "type_defs.GetCertificatesRequestTypeDef" = dataclasses.field()

    certificateStatuses = field("certificateStatuses")
    includeCertificateDetails = field("includeCertificateDetails")
    certificateName = field("certificateName")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFormationStackRecordsRequest:
    boto3_raw_data: "type_defs.GetCloudFormationStackRecordsRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFormationStackRecordsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudFormationStackRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactMethodsRequest:
    boto3_raw_data: "type_defs.GetContactMethodsRequestTypeDef" = dataclasses.field()

    protocols = field("protocols")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactMethodsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactMethodsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerImagesRequest:
    boto3_raw_data: "type_defs.GetContainerImagesRequestTypeDef" = dataclasses.field()

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerImagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerImagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerServiceDeploymentsRequest:
    boto3_raw_data: "type_defs.GetContainerServiceDeploymentsRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContainerServiceDeploymentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerServiceDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerServicesRequest:
    boto3_raw_data: "type_defs.GetContainerServicesRequestTypeDef" = dataclasses.field()

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerServicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskRequest:
    boto3_raw_data: "type_defs.GetDiskRequestTypeDef" = dataclasses.field()

    diskName = field("diskName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDiskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDiskRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskSnapshotRequest:
    boto3_raw_data: "type_defs.GetDiskSnapshotRequestTypeDef" = dataclasses.field()

    diskSnapshotName = field("diskSnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDiskSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiskSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskSnapshotsRequest:
    boto3_raw_data: "type_defs.GetDiskSnapshotsRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDiskSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiskSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDisksRequest:
    boto3_raw_data: "type_defs.GetDisksRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDisksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDisksRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionLatestCacheResetRequest:
    boto3_raw_data: "type_defs.GetDistributionLatestCacheResetRequestTypeDef" = (
        dataclasses.field()
    )

    distributionName = field("distributionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDistributionLatestCacheResetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionLatestCacheResetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionsRequest:
    boto3_raw_data: "type_defs.GetDistributionsRequestTypeDef" = dataclasses.field()

    distributionName = field("distributionName")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainRequest:
    boto3_raw_data: "type_defs.GetDomainRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainsRequest:
    boto3_raw_data: "type_defs.GetDomainsRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportSnapshotRecordsRequest:
    boto3_raw_data: "type_defs.GetExportSnapshotRecordsRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExportSnapshotRecordsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportSnapshotRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceAccessDetailsRequest:
    boto3_raw_data: "type_defs.GetInstanceAccessDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceName = field("instanceName")
    protocol = field("protocol")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetInstanceAccessDetailsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceAccessDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstancePortStatesRequest:
    boto3_raw_data: "type_defs.GetInstancePortStatesRequestTypeDef" = (
        dataclasses.field()
    )

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstancePortStatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstancePortStatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancePortState:
    boto3_raw_data: "type_defs.InstancePortStateTypeDef" = dataclasses.field()

    fromPort = field("fromPort")
    toPort = field("toPort")
    protocol = field("protocol")
    state = field("state")
    cidrs = field("cidrs")
    ipv6Cidrs = field("ipv6Cidrs")
    cidrListAliases = field("cidrListAliases")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstancePortStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePortStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceRequest:
    boto3_raw_data: "type_defs.GetInstanceRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceSnapshotRequest:
    boto3_raw_data: "type_defs.GetInstanceSnapshotRequestTypeDef" = dataclasses.field()

    instanceSnapshotName = field("instanceSnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceSnapshotsRequest:
    boto3_raw_data: "type_defs.GetInstanceSnapshotsRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceStateRequest:
    boto3_raw_data: "type_defs.GetInstanceStateRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceState:
    boto3_raw_data: "type_defs.InstanceStateTypeDef" = dataclasses.field()

    code = field("code")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstancesRequest:
    boto3_raw_data: "type_defs.GetInstancesRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPairRequest:
    boto3_raw_data: "type_defs.GetKeyPairRequestTypeDef" = dataclasses.field()

    keyPairName = field("keyPairName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKeyPairRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPairRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPairsRequest:
    boto3_raw_data: "type_defs.GetKeyPairsRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")
    includeDefaultKeyPair = field("includeDefaultKeyPair")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyPairsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPairsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerRequest:
    boto3_raw_data: "type_defs.GetLoadBalancerRequestTypeDef" = dataclasses.field()

    loadBalancerName = field("loadBalancerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoadBalancerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerTlsCertificatesRequest:
    boto3_raw_data: "type_defs.GetLoadBalancerTlsCertificatesRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLoadBalancerTlsCertificatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerTlsCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerTlsPoliciesRequest:
    boto3_raw_data: "type_defs.GetLoadBalancerTlsPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLoadBalancerTlsPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerTlsPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsPolicy:
    boto3_raw_data: "type_defs.LoadBalancerTlsPolicyTypeDef" = dataclasses.field()

    name = field("name")
    isDefault = field("isDefault")
    description = field("description")
    protocols = field("protocols")
    ciphers = field("ciphers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTlsPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerTlsPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancersRequest:
    boto3_raw_data: "type_defs.GetLoadBalancersRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoadBalancersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationRequest:
    boto3_raw_data: "type_defs.GetOperationRequestTypeDef" = dataclasses.field()

    operationId = field("operationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationsForResourceRequest:
    boto3_raw_data: "type_defs.GetOperationsForResourceRequestTypeDef" = (
        dataclasses.field()
    )

    resourceName = field("resourceName")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOperationsForResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationsRequest:
    boto3_raw_data: "type_defs.GetOperationsRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegionsRequest:
    boto3_raw_data: "type_defs.GetRegionsRequestTypeDef" = dataclasses.field()

    includeAvailabilityZones = field("includeAvailabilityZones")
    includeRelationalDatabaseAvailabilityZones = field(
        "includeRelationalDatabaseAvailabilityZones"
    )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRegionsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseBlueprintsRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseBlueprintsRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseBlueprintsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseBlueprintsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseBlueprint:
    boto3_raw_data: "type_defs.RelationalDatabaseBlueprintTypeDef" = dataclasses.field()

    blueprintId = field("blueprintId")
    engine = field("engine")
    engineVersion = field("engineVersion")
    engineDescription = field("engineDescription")
    engineVersionDescription = field("engineVersionDescription")
    isEngineDefault = field("isEngineDefault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseBlueprintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseBlueprintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseBundlesRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseBundlesRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")
    includeInactive = field("includeInactive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseBundlesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseBundlesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseBundle:
    boto3_raw_data: "type_defs.RelationalDatabaseBundleTypeDef" = dataclasses.field()

    bundleId = field("bundleId")
    name = field("name")
    price = field("price")
    ramSizeInGb = field("ramSizeInGb")
    diskSizeInGb = field("diskSizeInGb")
    transferPerMonthInGb = field("transferPerMonthInGb")
    cpuCount = field("cpuCount")
    isEncrypted = field("isEncrypted")
    isActive = field("isActive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseBundleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseBundleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseEventsRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseEventsRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    durationInMinutes = field("durationInMinutes")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseEventsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseEvent:
    boto3_raw_data: "type_defs.RelationalDatabaseEventTypeDef" = dataclasses.field()

    resource = field("resource")
    createdAt = field("createdAt")
    message = field("message")
    eventCategories = field("eventCategories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogEvent:
    boto3_raw_data: "type_defs.LogEventTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseLogStreamsRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseLogStreamsRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseLogStreamsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseLogStreamsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseMasterUserPasswordRequest:
    boto3_raw_data: (
        "type_defs.GetRelationalDatabaseMasterUserPasswordRequestTypeDef"
    ) = dataclasses.field()

    relationalDatabaseName = field("relationalDatabaseName")
    passwordVersion = field("passwordVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseMasterUserPasswordRequestTypeDef"
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
                "type_defs.GetRelationalDatabaseMasterUserPasswordRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseParametersRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseParametersRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseParametersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseParameter:
    boto3_raw_data: "type_defs.RelationalDatabaseParameterTypeDef" = dataclasses.field()

    allowedValues = field("allowedValues")
    applyMethod = field("applyMethod")
    applyType = field("applyType")
    dataType = field("dataType")
    description = field("description")
    isModifiable = field("isModifiable")
    parameterName = field("parameterName")
    parameterValue = field("parameterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRelationalDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseSnapshotRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseSnapshotName = field("relationalDatabaseSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseSnapshotsRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseSnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseSnapshotsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabasesRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabasesRequestTypeDef" = (
        dataclasses.field()
    )

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRelationalDatabasesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSetupHistoryRequest:
    boto3_raw_data: "type_defs.GetSetupHistoryRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSetupHistoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSetupHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticIpRequest:
    boto3_raw_data: "type_defs.GetStaticIpRequestTypeDef" = dataclasses.field()

    staticIpName = field("staticIpName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStaticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticIpsRequest:
    boto3_raw_data: "type_defs.GetStaticIpsRequestTypeDef" = dataclasses.field()

    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStaticIpsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticIpsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostKeyAttributes:
    boto3_raw_data: "type_defs.HostKeyAttributesTypeDef" = dataclasses.field()

    algorithm = field("algorithm")
    publicKey = field("publicKey")
    witnessedAt = field("witnessedAt")
    fingerprintSHA1 = field("fingerprintSHA1")
    fingerprintSHA256 = field("fingerprintSHA256")
    notValidBefore = field("notValidBefore")
    notValidAfter = field("notValidAfter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostKeyAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostKeyAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyPairRequest:
    boto3_raw_data: "type_defs.ImportKeyPairRequestTypeDef" = dataclasses.field()

    keyPairName = field("keyPairName")
    publicKeyBase64 = field("publicKeyBase64")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportKeyPairRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportKeyPairRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PasswordData:
    boto3_raw_data: "type_defs.PasswordDataTypeDef" = dataclasses.field()

    ciphertext = field("ciphertext")
    keyPairName = field("keyPairName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PasswordDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PasswordDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceHealthSummary:
    boto3_raw_data: "type_defs.InstanceHealthSummaryTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    instanceHealth = field("instanceHealth")
    instanceHealthReason = field("instanceHealthReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceHealthSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceHealthSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMetadataOptions:
    boto3_raw_data: "type_defs.InstanceMetadataOptionsTypeDef" = dataclasses.field()

    state = field("state")
    httpTokens = field("httpTokens")
    httpEndpoint = field("httpEndpoint")
    httpPutResponseHopLimit = field("httpPutResponseHopLimit")
    httpProtocolIpv6 = field("httpProtocolIpv6")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceMetadataOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMetadataOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancePortInfo:
    boto3_raw_data: "type_defs.InstancePortInfoTypeDef" = dataclasses.field()

    fromPort = field("fromPort")
    toPort = field("toPort")
    protocol = field("protocol")
    accessFrom = field("accessFrom")
    accessType = field("accessType")
    commonName = field("commonName")
    accessDirection = field("accessDirection")
    cidrs = field("cidrs")
    ipv6Cidrs = field("ipv6Cidrs")
    cidrListAliases = field("cidrListAliases")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstancePortInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePortInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonthlyTransfer:
    boto3_raw_data: "type_defs.MonthlyTransferTypeDef" = dataclasses.field()

    gbPerMonthAllocated = field("gbPerMonthAllocated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonthlyTransferTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonthlyTransferTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Origin:
    boto3_raw_data: "type_defs.OriginTypeDef" = dataclasses.field()

    name = field("name")
    resourceType = field("resourceType")
    regionName = field("regionName")
    protocolPolicy = field("protocolPolicy")
    responseTimeout = field("responseTimeout")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsCertificateDnsRecordCreationState:
    boto3_raw_data: (
        "type_defs.LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef"
    ) = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef"
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
                "type_defs.LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsCertificateDomainValidationOption:
    boto3_raw_data: (
        "type_defs.LoadBalancerTlsCertificateDomainValidationOptionTypeDef"
    ) = dataclasses.field()

    domainName = field("domainName")
    validationStatus = field("validationStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoadBalancerTlsCertificateDomainValidationOptionTypeDef"
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
                "type_defs.LoadBalancerTlsCertificateDomainValidationOptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsCertificateSummary:
    boto3_raw_data: "type_defs.LoadBalancerTlsCertificateSummaryTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    isAttached = field("isAttached")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoadBalancerTlsCertificateSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerTlsCertificateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NameServersUpdateState:
    boto3_raw_data: "type_defs.NameServersUpdateStateTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NameServersUpdateStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NameServersUpdateStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingMaintenanceAction:
    boto3_raw_data: "type_defs.PendingMaintenanceActionTypeDef" = dataclasses.field()

    action = field("action")
    description = field("description")
    currentApplyDate = field("currentApplyDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingMaintenanceActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingModifiedRelationalDatabaseValues:
    boto3_raw_data: "type_defs.PendingModifiedRelationalDatabaseValuesTypeDef" = (
        dataclasses.field()
    )

    masterUserPassword = field("masterUserPassword")
    engineVersion = field("engineVersion")
    backupRetentionEnabled = field("backupRetentionEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PendingModifiedRelationalDatabaseValuesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingModifiedRelationalDatabaseValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAlarmRequest:
    boto3_raw_data: "type_defs.PutAlarmRequestTypeDef" = dataclasses.field()

    alarmName = field("alarmName")
    metricName = field("metricName")
    monitoredResourceName = field("monitoredResourceName")
    comparisonOperator = field("comparisonOperator")
    threshold = field("threshold")
    evaluationPeriods = field("evaluationPeriods")
    datapointsToAlarm = field("datapointsToAlarm")
    treatMissingData = field("treatMissingData")
    contactProtocols = field("contactProtocols")
    notificationTriggers = field("notificationTriggers")
    notificationEnabled = field("notificationEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutAlarmRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutAlarmRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class R53HostedZoneDeletionState:
    boto3_raw_data: "type_defs.R53HostedZoneDeletionStateTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.R53HostedZoneDeletionStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.R53HostedZoneDeletionStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootInstanceRequest:
    boto3_raw_data: "type_defs.RebootInstanceRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.RebootRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RebootRelationalDatabaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterContainerImageRequest:
    boto3_raw_data: "type_defs.RegisterContainerImageRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    label = field("label")
    digest = field("digest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterContainerImageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterContainerImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseEndpoint:
    boto3_raw_data: "type_defs.RelationalDatabaseEndpointTypeDef" = dataclasses.field()

    port = field("port")
    address = field("address")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseHardware:
    boto3_raw_data: "type_defs.RelationalDatabaseHardwareTypeDef" = dataclasses.field()

    cpuCount = field("cpuCount")
    diskSizeInGb = field("diskSizeInGb")
    ramSizeInGb = field("ramSizeInGb")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseHardwareTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseHardwareTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseStaticIpRequest:
    boto3_raw_data: "type_defs.ReleaseStaticIpRequestTypeDef" = dataclasses.field()

    staticIpName = field("staticIpName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleaseStaticIpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseStaticIpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetDistributionCacheRequest:
    boto3_raw_data: "type_defs.ResetDistributionCacheRequestTypeDef" = (
        dataclasses.field()
    )

    distributionName = field("distributionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResetDistributionCacheRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDistributionCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendContactMethodVerificationRequest:
    boto3_raw_data: "type_defs.SendContactMethodVerificationRequestTypeDef" = (
        dataclasses.field()
    )

    protocol = field("protocol")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendContactMethodVerificationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendContactMethodVerificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIpAddressTypeRequest:
    boto3_raw_data: "type_defs.SetIpAddressTypeRequestTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceName = field("resourceName")
    ipAddressType = field("ipAddressType")
    acceptBundleUpdate = field("acceptBundleUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetIpAddressTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIpAddressTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetResourceAccessForBucketRequest:
    boto3_raw_data: "type_defs.SetResourceAccessForBucketRequestTypeDef" = (
        dataclasses.field()
    )

    resourceName = field("resourceName")
    bucketName = field("bucketName")
    access = field("access")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetResourceAccessForBucketRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetResourceAccessForBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetupExecutionDetails:
    boto3_raw_data: "type_defs.SetupExecutionDetailsTypeDef" = dataclasses.field()

    command = field("command")
    dateTime = field("dateTime")
    name = field("name")
    status = field("status")
    standardError = field("standardError")
    standardOutput = field("standardOutput")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetupExecutionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetupExecutionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetupRequest:
    boto3_raw_data: "type_defs.SetupRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    domainNames = field("domainNames")
    certificateProvider = field("certificateProvider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SetupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetupInstanceHttpsRequest:
    boto3_raw_data: "type_defs.SetupInstanceHttpsRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    emailAddress = field("emailAddress")
    domainNames = field("domainNames")
    certificateProvider = field("certificateProvider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetupInstanceHttpsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetupInstanceHttpsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGUISessionRequest:
    boto3_raw_data: "type_defs.StartGUISessionRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartGUISessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGUISessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceRequest:
    boto3_raw_data: "type_defs.StartInstanceRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.StartRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRelationalDatabaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopGUISessionRequest:
    boto3_raw_data: "type_defs.StopGUISessionRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopGUISessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopGUISessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInstanceRequest:
    boto3_raw_data: "type_defs.StopInstanceRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.StopRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    relationalDatabaseSnapshotName = field("relationalDatabaseSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopRelationalDatabaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestAlarmRequest:
    boto3_raw_data: "type_defs.TestAlarmRequestTypeDef" = dataclasses.field()

    alarmName = field("alarmName")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestAlarmRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestAlarmRequestTypeDef"]
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

    resourceName = field("resourceName")
    tagKeys = field("tagKeys")
    resourceArn = field("resourceArn")

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
class UpdateBucketBundleRequest:
    boto3_raw_data: "type_defs.UpdateBucketBundleRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    bundleId = field("bundleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBucketBundleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBucketBundleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionBundleRequest:
    boto3_raw_data: "type_defs.UpdateDistributionBundleRequestTypeDef" = (
        dataclasses.field()
    )

    distributionName = field("distributionName")
    bundleId = field("bundleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDistributionBundleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionBundleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceMetadataOptionsRequest:
    boto3_raw_data: "type_defs.UpdateInstanceMetadataOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceName = field("instanceName")
    httpTokens = field("httpTokens")
    httpEndpoint = field("httpEndpoint")
    httpPutResponseHopLimit = field("httpPutResponseHopLimit")
    httpProtocolIpv6 = field("httpProtocolIpv6")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateInstanceMetadataOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceMetadataOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLoadBalancerAttributeRequest:
    boto3_raw_data: "type_defs.UpdateLoadBalancerAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    attributeName = field("attributeName")
    attributeValue = field("attributeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLoadBalancerAttributeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoadBalancerAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.UpdateRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    masterUserPassword = field("masterUserPassword")
    rotateMasterUserPassword = field("rotateMasterUserPassword")
    preferredBackupWindow = field("preferredBackupWindow")
    preferredMaintenanceWindow = field("preferredMaintenanceWindow")
    enableBackupRetention = field("enableBackupRetention")
    disableBackupRetention = field("disableBackupRetention")
    publiclyAccessible = field("publiclyAccessible")
    applyImmediately = field("applyImmediately")
    caCertificateIdentifier = field("caCertificateIdentifier")
    relationalDatabaseBlueprintId = field("relationalDatabaseBlueprintId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRelationalDatabaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessKey:
    boto3_raw_data: "type_defs.AccessKeyTypeDef" = dataclasses.field()

    accessKeyId = field("accessKeyId")
    secretAccessKey = field("secretAccessKey")
    status = field("status")
    createdAt = field("createdAt")

    @cached_property
    def lastUsed(self):  # pragma: no cover
        return AccessKeyLastUsed.make_one(self.boto3_raw_data["lastUsed"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddOnRequest:
    boto3_raw_data: "type_defs.AddOnRequestTypeDef" = dataclasses.field()

    addOnType = field("addOnType")

    @cached_property
    def autoSnapshotAddOnRequest(self):  # pragma: no cover
        return AutoSnapshotAddOnRequest.make_one(
            self.boto3_raw_data["autoSnapshotAddOnRequest"]
        )

    @cached_property
    def stopInstanceOnIdleRequest(self):  # pragma: no cover
        return StopInstanceOnIdleRequest.make_one(
            self.boto3_raw_data["stopInstanceOnIdleRequest"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddOnRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddOnRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")
    supportCode = field("supportCode")

    @cached_property
    def monitoredResourceInfo(self):  # pragma: no cover
        return MonitoredResourceInfo.make_one(
            self.boto3_raw_data["monitoredResourceInfo"]
        )

    comparisonOperator = field("comparisonOperator")
    evaluationPeriods = field("evaluationPeriods")
    period = field("period")
    threshold = field("threshold")
    datapointsToAlarm = field("datapointsToAlarm")
    treatMissingData = field("treatMissingData")
    statistic = field("statistic")
    metricName = field("metricName")
    state = field("state")
    unit = field("unit")
    contactProtocols = field("contactProtocols")
    notificationTriggers = field("notificationTriggers")
    notificationEnabled = field("notificationEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactMethod:
    boto3_raw_data: "type_defs.ContactMethodTypeDef" = dataclasses.field()

    contactEndpoint = field("contactEndpoint")
    status = field("status")
    protocol = field("protocol")
    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")
    supportCode = field("supportCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactMethodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactMethodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Operation:
    boto3_raw_data: "type_defs.OperationTypeDef" = dataclasses.field()

    id = field("id")
    resourceName = field("resourceName")
    resourceType = field("resourceType")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    isTerminal = field("isTerminal")
    operationDetails = field("operationDetails")
    operationType = field("operationType")
    status = field("status")
    statusChangedAt = field("statusChangedAt")
    errorCode = field("errorCode")
    errorDetails = field("errorDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetupHistoryResource:
    boto3_raw_data: "type_defs.SetupHistoryResourceTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetupHistoryResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetupHistoryResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticIp:
    boto3_raw_data: "type_defs.StaticIpTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")
    ipAddress = field("ipAddress")
    attachedTo = field("attachedTo")
    isAttached = field("isAttached")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StaticIpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StaticIpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DownloadDefaultKeyPairResult:
    boto3_raw_data: "type_defs.DownloadDefaultKeyPairResultTypeDef" = (
        dataclasses.field()
    )

    publicKeyBase64 = field("publicKeyBase64")
    privateKeyBase64 = field("privateKeyBase64")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DownloadDefaultKeyPairResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DownloadDefaultKeyPairResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActiveNamesResult:
    boto3_raw_data: "type_defs.GetActiveNamesResultTypeDef" = dataclasses.field()

    activeNames = field("activeNames")
    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetActiveNamesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActiveNamesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerAPIMetadataResult:
    boto3_raw_data: "type_defs.GetContainerAPIMetadataResultTypeDef" = (
        dataclasses.field()
    )

    metadata = field("metadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetContainerAPIMetadataResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerAPIMetadataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionLatestCacheResetResult:
    boto3_raw_data: "type_defs.GetDistributionLatestCacheResetResultTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    createTime = field("createTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDistributionLatestCacheResetResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionLatestCacheResetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseLogStreamsResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseLogStreamsResultTypeDef" = (
        dataclasses.field()
    )

    logStreams = field("logStreams")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseLogStreamsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseLogStreamsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseMasterUserPasswordResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseMasterUserPasswordResultTypeDef" = (
        dataclasses.field()
    )

    masterUserPassword = field("masterUserPassword")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseMasterUserPasswordResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseMasterUserPasswordResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsVpcPeeredResult:
    boto3_raw_data: "type_defs.IsVpcPeeredResultTypeDef" = dataclasses.field()

    isPeered = field("isPeered")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsVpcPeeredResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsVpcPeeredResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoSnapshotDetails:
    boto3_raw_data: "type_defs.AutoSnapshotDetailsTypeDef" = dataclasses.field()

    date = field("date")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def fromAttachedDisks(self):  # pragma: no cover
        return AttachedDisk.make_many(self.boto3_raw_data["fromAttachedDisks"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoSnapshotDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoSnapshotDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Region:
    boto3_raw_data: "type_defs.RegionTypeDef" = dataclasses.field()

    continentCode = field("continentCode")
    description = field("description")
    displayName = field("displayName")
    name = field("name")

    @cached_property
    def availabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["availabilityZones"])

    @cached_property
    def relationalDatabaseAvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(
            self.boto3_raw_data["relationalDatabaseAvailabilityZones"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlueprintsResult:
    boto3_raw_data: "type_defs.GetBlueprintsResultTypeDef" = dataclasses.field()

    @cached_property
    def blueprints(self):  # pragma: no cover
        return Blueprint.make_many(self.boto3_raw_data["blueprints"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlueprintsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlueprintsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBucketRequest:
    boto3_raw_data: "type_defs.UpdateBucketRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")

    @cached_property
    def accessRules(self):  # pragma: no cover
        return AccessRules.make_one(self.boto3_raw_data["accessRules"])

    versioning = field("versioning")
    readonlyAccessAccounts = field("readonlyAccessAccounts")

    @cached_property
    def accessLogConfig(self):  # pragma: no cover
        return BucketAccessLogConfig.make_one(self.boto3_raw_data["accessLogConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketBundlesResult:
    boto3_raw_data: "type_defs.GetBucketBundlesResultTypeDef" = dataclasses.field()

    @cached_property
    def bundles(self):  # pragma: no cover
        return BucketBundle.make_many(self.boto3_raw_data["bundles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketBundlesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketBundlesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bucket:
    boto3_raw_data: "type_defs.BucketTypeDef" = dataclasses.field()

    resourceType = field("resourceType")

    @cached_property
    def accessRules(self):  # pragma: no cover
        return AccessRules.make_one(self.boto3_raw_data["accessRules"])

    arn = field("arn")
    bundleId = field("bundleId")
    createdAt = field("createdAt")
    url = field("url")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    name = field("name")
    supportCode = field("supportCode")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    objectVersioning = field("objectVersioning")
    ableToUpdateBundle = field("ableToUpdateBundle")
    readonlyAccessAccounts = field("readonlyAccessAccounts")

    @cached_property
    def resourcesReceivingAccess(self):  # pragma: no cover
        return ResourceReceivingAccess.make_many(
            self.boto3_raw_data["resourcesReceivingAccess"]
        )

    @cached_property
    def state(self):  # pragma: no cover
        return BucketState.make_one(self.boto3_raw_data["state"])

    @cached_property
    def accessLogConfig(self):  # pragma: no cover
        return BucketAccessLogConfig.make_one(self.boto3_raw_data["accessLogConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketRequest:
    boto3_raw_data: "type_defs.CreateBucketRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    bundleId = field("bundleId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    enableObjectVersioning = field("enableObjectVersioning")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateRequest:
    boto3_raw_data: "type_defs.CreateCertificateRequestTypeDef" = dataclasses.field()

    certificateName = field("certificateName")
    domainName = field("domainName")
    subjectAlternativeNames = field("subjectAlternativeNames")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDiskSnapshotRequest:
    boto3_raw_data: "type_defs.CreateDiskSnapshotRequestTypeDef" = dataclasses.field()

    diskSnapshotName = field("diskSnapshotName")
    diskName = field("diskName")
    instanceName = field("instanceName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDiskSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDiskSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceSnapshotRequest:
    boto3_raw_data: "type_defs.CreateInstanceSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    instanceSnapshotName = field("instanceSnapshotName")
    instanceName = field("instanceName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInstanceSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyPairRequest:
    boto3_raw_data: "type_defs.CreateKeyPairRequestTypeDef" = dataclasses.field()

    keyPairName = field("keyPairName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyPairRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyPairRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerRequest:
    boto3_raw_data: "type_defs.CreateLoadBalancerRequestTypeDef" = dataclasses.field()

    loadBalancerName = field("loadBalancerName")
    instancePort = field("instancePort")
    healthCheckPath = field("healthCheckPath")
    certificateName = field("certificateName")
    certificateDomainName = field("certificateDomainName")
    certificateAlternativeNames = field("certificateAlternativeNames")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    ipAddressType = field("ipAddressType")
    tlsPolicyName = field("tlsPolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLoadBalancerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerTlsCertificateRequest:
    boto3_raw_data: "type_defs.CreateLoadBalancerTlsCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    certificateName = field("certificateName")
    certificateDomainName = field("certificateDomainName")
    certificateAlternativeNames = field("certificateAlternativeNames")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLoadBalancerTlsCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerTlsCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelationalDatabaseRequest:
    boto3_raw_data: "type_defs.CreateRelationalDatabaseRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    relationalDatabaseBlueprintId = field("relationalDatabaseBlueprintId")
    relationalDatabaseBundleId = field("relationalDatabaseBundleId")
    masterDatabaseName = field("masterDatabaseName")
    masterUsername = field("masterUsername")
    availabilityZone = field("availabilityZone")
    masterUserPassword = field("masterUserPassword")
    preferredBackupWindow = field("preferredBackupWindow")
    preferredMaintenanceWindow = field("preferredMaintenanceWindow")
    publiclyAccessible = field("publiclyAccessible")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRelationalDatabaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelationalDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelationalDatabaseSnapshotRequest:
    boto3_raw_data: "type_defs.CreateRelationalDatabaseSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    relationalDatabaseSnapshotName = field("relationalDatabaseSnapshotName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRelationalDatabaseSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelationalDatabaseSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiskSnapshot:
    boto3_raw_data: "type_defs.DiskSnapshotTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    sizeInGb = field("sizeInGb")
    state = field("state")
    progress = field("progress")
    fromDiskName = field("fromDiskName")
    fromDiskArn = field("fromDiskArn")
    fromInstanceName = field("fromInstanceName")
    fromInstanceArn = field("fromInstanceArn")
    isFromAutoSnapshot = field("isFromAutoSnapshot")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiskSnapshotTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Disk:
    boto3_raw_data: "type_defs.DiskTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def addOns(self):  # pragma: no cover
        return AddOn.make_many(self.boto3_raw_data["addOns"])

    sizeInGb = field("sizeInGb")
    isSystemDisk = field("isSystemDisk")
    iops = field("iops")
    path = field("path")
    state = field("state")
    attachedTo = field("attachedTo")
    isAttached = field("isAttached")
    attachmentState = field("attachmentState")
    gbInUse = field("gbInUse")
    autoMountStatus = field("autoMountStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyPair:
    boto3_raw_data: "type_defs.KeyPairTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    fingerprint = field("fingerprint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyPairTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseSnapshot:
    boto3_raw_data: "type_defs.RelationalDatabaseSnapshotTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    engine = field("engine")
    engineVersion = field("engineVersion")
    sizeInGb = field("sizeInGb")
    state = field("state")
    fromRelationalDatabaseName = field("fromRelationalDatabaseName")
    fromRelationalDatabaseArn = field("fromRelationalDatabaseArn")
    fromRelationalDatabaseBundleId = field("fromRelationalDatabaseBundleId")
    fromRelationalDatabaseBlueprintId = field("fromRelationalDatabaseBlueprintId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseSnapshotTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseSnapshotTypeDef"]
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

    resourceName = field("resourceName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    resourceArn = field("resourceArn")

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
class GetBundlesResult:
    boto3_raw_data: "type_defs.GetBundlesResultTypeDef" = dataclasses.field()

    @cached_property
    def bundles(self):  # pragma: no cover
        return Bundle.make_many(self.boto3_raw_data["bundles"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBundlesResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBundlesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSettingsOutput:
    boto3_raw_data: "type_defs.CacheSettingsOutputTypeDef" = dataclasses.field()

    defaultTTL = field("defaultTTL")
    minimumTTL = field("minimumTTL")
    maximumTTL = field("maximumTTL")
    allowedHTTPMethods = field("allowedHTTPMethods")
    cachedHTTPMethods = field("cachedHTTPMethods")

    @cached_property
    def forwardedCookies(self):  # pragma: no cover
        return CookieObjectOutput.make_one(self.boto3_raw_data["forwardedCookies"])

    @cached_property
    def forwardedHeaders(self):  # pragma: no cover
        return HeaderObjectOutput.make_one(self.boto3_raw_data["forwardedHeaders"])

    @cached_property
    def forwardedQueryStrings(self):  # pragma: no cover
        return QueryStringObjectOutput.make_one(
            self.boto3_raw_data["forwardedQueryStrings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSettings:
    boto3_raw_data: "type_defs.CacheSettingsTypeDef" = dataclasses.field()

    defaultTTL = field("defaultTTL")
    minimumTTL = field("minimumTTL")
    maximumTTL = field("maximumTTL")
    allowedHTTPMethods = field("allowedHTTPMethods")
    cachedHTTPMethods = field("cachedHTTPMethods")

    @cached_property
    def forwardedCookies(self):  # pragma: no cover
        return CookieObject.make_one(self.boto3_raw_data["forwardedCookies"])

    @cached_property
    def forwardedHeaders(self):  # pragma: no cover
        return HeaderObject.make_one(self.boto3_raw_data["forwardedHeaders"])

    @cached_property
    def forwardedQueryStrings(self):  # pragma: no cover
        return QueryStringObject.make_one(self.boto3_raw_data["forwardedQueryStrings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloseInstancePublicPortsRequest:
    boto3_raw_data: "type_defs.CloseInstancePublicPortsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def portInfo(self):  # pragma: no cover
        return PortInfo.make_one(self.boto3_raw_data["portInfo"])

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloseInstancePublicPortsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloseInstancePublicPortsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenInstancePublicPortsRequest:
    boto3_raw_data: "type_defs.OpenInstancePublicPortsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def portInfo(self):  # pragma: no cover
        return PortInfo.make_one(self.boto3_raw_data["portInfo"])

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenInstancePublicPortsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenInstancePublicPortsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInstancePublicPortsRequest:
    boto3_raw_data: "type_defs.PutInstancePublicPortsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def portInfos(self):  # pragma: no cover
        return PortInfo.make_many(self.boto3_raw_data["portInfos"])

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutInstancePublicPortsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInstancePublicPortsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationStackRecord:
    boto3_raw_data: "type_defs.CloudFormationStackRecordTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")
    state = field("state")

    @cached_property
    def sourceInfo(self):  # pragma: no cover
        return CloudFormationStackRecordSourceInfo.make_many(
            self.boto3_raw_data["sourceInfo"]
        )

    @cached_property
    def destinationInfo(self):  # pragma: no cover
        return DestinationInfo.make_one(self.boto3_raw_data["destinationInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationStackRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationStackRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerImagesResult:
    boto3_raw_data: "type_defs.GetContainerImagesResultTypeDef" = dataclasses.field()

    @cached_property
    def containerImages(self):  # pragma: no cover
        return ContainerImage.make_many(self.boto3_raw_data["containerImages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerImagesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerImagesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterContainerImageResult:
    boto3_raw_data: "type_defs.RegisterContainerImageResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerImage(self):  # pragma: no cover
        return ContainerImage.make_one(self.boto3_raw_data["containerImage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterContainerImageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterContainerImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateRegistryAccessRequest:
    boto3_raw_data: "type_defs.PrivateRegistryAccessRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ecrImagePullerRole(self):  # pragma: no cover
        return ContainerServiceECRImagePullerRoleRequest.make_one(
            self.boto3_raw_data["ecrImagePullerRole"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateRegistryAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateRegistryAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateRegistryAccess:
    boto3_raw_data: "type_defs.PrivateRegistryAccessTypeDef" = dataclasses.field()

    @cached_property
    def ecrImagePullerRole(self):  # pragma: no cover
        return ContainerServiceECRImagePullerRole.make_one(
            self.boto3_raw_data["ecrImagePullerRole"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateRegistryAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateRegistryAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceEndpoint:
    boto3_raw_data: "type_defs.ContainerServiceEndpointTypeDef" = dataclasses.field()

    containerName = field("containerName")
    containerPort = field("containerPort")

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return ContainerServiceHealthCheckConfig.make_one(
            self.boto3_raw_data["healthCheck"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerServiceEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointRequest:
    boto3_raw_data: "type_defs.EndpointRequestTypeDef" = dataclasses.field()

    containerName = field("containerName")
    containerPort = field("containerPort")

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return ContainerServiceHealthCheckConfig.make_one(
            self.boto3_raw_data["healthCheck"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerLogResult:
    boto3_raw_data: "type_defs.GetContainerLogResultTypeDef" = dataclasses.field()

    @cached_property
    def logEvents(self):  # pragma: no cover
        return ContainerServiceLogEvent.make_many(self.boto3_raw_data["logEvents"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerLogResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerLogResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerServicePowersResult:
    boto3_raw_data: "type_defs.GetContainerServicePowersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def powers(self):  # pragma: no cover
        return ContainerServicePower.make_many(self.boto3_raw_data["powers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetContainerServicePowersResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerServicePowersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerServiceRegistryLoginResult:
    boto3_raw_data: "type_defs.CreateContainerServiceRegistryLoginResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def registryLogin(self):  # pragma: no cover
        return ContainerServiceRegistryLogin.make_one(
            self.boto3_raw_data["registryLogin"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContainerServiceRegistryLoginResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerServiceRegistryLoginResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFormationStackRequest:
    boto3_raw_data: "type_defs.CreateCloudFormationStackRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instances(self):  # pragma: no cover
        return InstanceEntry.make_many(self.boto3_raw_data["instances"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCloudFormationStackRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFormationStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGUISessionAccessDetailsResult:
    boto3_raw_data: "type_defs.CreateGUISessionAccessDetailsResultTypeDef" = (
        dataclasses.field()
    )

    resourceName = field("resourceName")
    status = field("status")
    percentageComplete = field("percentageComplete")
    failureReason = field("failureReason")

    @cached_property
    def sessions(self):  # pragma: no cover
        return Session.make_many(self.boto3_raw_data["sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGUISessionAccessDetailsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGUISessionAccessDetailsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelationalDatabaseFromSnapshotRequest:
    boto3_raw_data: "type_defs.CreateRelationalDatabaseFromSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    availabilityZone = field("availabilityZone")
    publiclyAccessible = field("publiclyAccessible")
    relationalDatabaseSnapshotName = field("relationalDatabaseSnapshotName")
    relationalDatabaseBundleId = field("relationalDatabaseBundleId")
    sourceRelationalDatabaseName = field("sourceRelationalDatabaseName")
    restoreTime = field("restoreTime")
    useLatestRestorableTime = field("useLatestRestorableTime")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRelationalDatabaseFromSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelationalDatabaseFromSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetricDataRequest:
    boto3_raw_data: "type_defs.GetBucketMetricDataRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    metricName = field("metricName")
    startTime = field("startTime")
    endTime = field("endTime")
    period = field("period")
    statistics = field("statistics")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketMetricDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerLogRequest:
    boto3_raw_data: "type_defs.GetContainerLogRequestTypeDef" = dataclasses.field()

    serviceName = field("serviceName")
    containerName = field("containerName")
    startTime = field("startTime")
    endTime = field("endTime")
    filterPattern = field("filterPattern")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerLogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerLogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerServiceMetricDataRequest:
    boto3_raw_data: "type_defs.GetContainerServiceMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    metricName = field("metricName")
    startTime = field("startTime")
    endTime = field("endTime")
    period = field("period")
    statistics = field("statistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContainerServiceMetricDataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerServiceMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostEstimateRequest:
    boto3_raw_data: "type_defs.GetCostEstimateRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionMetricDataRequest:
    boto3_raw_data: "type_defs.GetDistributionMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    distributionName = field("distributionName")
    metricName = field("metricName")
    startTime = field("startTime")
    endTime = field("endTime")
    period = field("period")
    unit = field("unit")
    statistics = field("statistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDistributionMetricDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceMetricDataRequest:
    boto3_raw_data: "type_defs.GetInstanceMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    instanceName = field("instanceName")
    metricName = field("metricName")
    period = field("period")
    startTime = field("startTime")
    endTime = field("endTime")
    unit = field("unit")
    statistics = field("statistics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceMetricDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerMetricDataRequest:
    boto3_raw_data: "type_defs.GetLoadBalancerMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    loadBalancerName = field("loadBalancerName")
    metricName = field("metricName")
    period = field("period")
    startTime = field("startTime")
    endTime = field("endTime")
    unit = field("unit")
    statistics = field("statistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLoadBalancerMetricDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseLogEventsRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseLogEventsRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    logStreamName = field("logStreamName")
    startTime = field("startTime")
    endTime = field("endTime")
    startFromHead = field("startFromHead")
    pageToken = field("pageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseLogEventsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseLogEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseMetricDataRequest:
    boto3_raw_data: "type_defs.GetRelationalDatabaseMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    metricName = field("metricName")
    period = field("period")
    startTime = field("startTime")
    endTime = field("endTime")
    unit = field("unit")
    statistics = field("statistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseMetricDataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceSnapshotInfo:
    boto3_raw_data: "type_defs.InstanceSnapshotInfoTypeDef" = dataclasses.field()

    fromBundleId = field("fromBundleId")
    fromBlueprintId = field("fromBlueprintId")

    @cached_property
    def fromDiskInfo(self):  # pragma: no cover
        return DiskInfo.make_many(self.boto3_raw_data["fromDiskInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceSnapshotInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceSnapshotInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionBundlesResult:
    boto3_raw_data: "type_defs.GetDistributionBundlesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def bundles(self):  # pragma: no cover
        return DistributionBundle.make_many(self.boto3_raw_data["bundles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionBundlesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionBundlesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainValidationRecord:
    boto3_raw_data: "type_defs.DomainValidationRecordTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @cached_property
    def resourceRecord(self):  # pragma: no cover
        return ResourceRecord.make_one(self.boto3_raw_data["resourceRecord"])

    @cached_property
    def dnsRecordCreationState(self):  # pragma: no cover
        return DnsRecordCreationState.make_one(
            self.boto3_raw_data["dnsRecordCreationState"]
        )

    validationStatus = field("validationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainValidationRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainValidationRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstimateByTime:
    boto3_raw_data: "type_defs.EstimateByTimeTypeDef" = dataclasses.field()

    usageCost = field("usageCost")
    pricingUnit = field("pricingUnit")
    unit = field("unit")
    currency = field("currency")

    @cached_property
    def timePeriod(self):  # pragma: no cover
        return TimePeriod.make_one(self.boto3_raw_data["timePeriod"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EstimateByTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EstimateByTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActiveNamesRequestPaginate:
    boto3_raw_data: "type_defs.GetActiveNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetActiveNamesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActiveNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlueprintsRequestPaginate:
    boto3_raw_data: "type_defs.GetBlueprintsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    includeInactive = field("includeInactive")
    appCategory = field("appCategory")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlueprintsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlueprintsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBundlesRequestPaginate:
    boto3_raw_data: "type_defs.GetBundlesRequestPaginateTypeDef" = dataclasses.field()

    includeInactive = field("includeInactive")
    appCategory = field("appCategory")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBundlesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBundlesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFormationStackRecordsRequestPaginate:
    boto3_raw_data: "type_defs.GetCloudFormationStackRecordsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFormationStackRecordsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudFormationStackRecordsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.GetDiskSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDiskSnapshotsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiskSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDisksRequestPaginate:
    boto3_raw_data: "type_defs.GetDisksRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDisksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDisksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainsRequestPaginate:
    boto3_raw_data: "type_defs.GetDomainsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportSnapshotRecordsRequestPaginate:
    boto3_raw_data: "type_defs.GetExportSnapshotRecordsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetExportSnapshotRecordsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportSnapshotRecordsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.GetInstanceSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInstanceSnapshotsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstancesRequestPaginate:
    boto3_raw_data: "type_defs.GetInstancesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstancesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPairsRequestPaginate:
    boto3_raw_data: "type_defs.GetKeyPairsRequestPaginateTypeDef" = dataclasses.field()

    includeDefaultKeyPair = field("includeDefaultKeyPair")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyPairsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPairsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancersRequestPaginate:
    boto3_raw_data: "type_defs.GetLoadBalancersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLoadBalancersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationsRequestPaginate:
    boto3_raw_data: "type_defs.GetOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseBlueprintsRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetRelationalDatabaseBlueprintsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseBlueprintsRequestPaginateTypeDef"
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
                "type_defs.GetRelationalDatabaseBlueprintsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseBundlesRequestPaginate:
    boto3_raw_data: "type_defs.GetRelationalDatabaseBundlesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    includeInactive = field("includeInactive")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseBundlesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseBundlesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseEventsRequestPaginate:
    boto3_raw_data: "type_defs.GetRelationalDatabaseEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")
    durationInMinutes = field("durationInMinutes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseParametersRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetRelationalDatabaseParametersRequestPaginateTypeDef"
    ) = dataclasses.field()

    relationalDatabaseName = field("relationalDatabaseName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseParametersRequestPaginateTypeDef"
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
                "type_defs.GetRelationalDatabaseParametersRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.GetRelationalDatabaseSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseSnapshotsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabasesRequestPaginate:
    boto3_raw_data: "type_defs.GetRelationalDatabasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticIpsRequestPaginate:
    boto3_raw_data: "type_defs.GetStaticIpsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStaticIpsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticIpsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetricDataResult:
    boto3_raw_data: "type_defs.GetBucketMetricDataResultTypeDef" = dataclasses.field()

    metricName = field("metricName")

    @cached_property
    def metricData(self):  # pragma: no cover
        return MetricDatapoint.make_many(self.boto3_raw_data["metricData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketMetricDataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerServiceMetricDataResult:
    boto3_raw_data: "type_defs.GetContainerServiceMetricDataResultTypeDef" = (
        dataclasses.field()
    )

    metricName = field("metricName")

    @cached_property
    def metricData(self):  # pragma: no cover
        return MetricDatapoint.make_many(self.boto3_raw_data["metricData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContainerServiceMetricDataResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerServiceMetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionMetricDataResult:
    boto3_raw_data: "type_defs.GetDistributionMetricDataResultTypeDef" = (
        dataclasses.field()
    )

    metricName = field("metricName")

    @cached_property
    def metricData(self):  # pragma: no cover
        return MetricDatapoint.make_many(self.boto3_raw_data["metricData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDistributionMetricDataResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionMetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceMetricDataResult:
    boto3_raw_data: "type_defs.GetInstanceMetricDataResultTypeDef" = dataclasses.field()

    metricName = field("metricName")

    @cached_property
    def metricData(self):  # pragma: no cover
        return MetricDatapoint.make_many(self.boto3_raw_data["metricData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceMetricDataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceMetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerMetricDataResult:
    boto3_raw_data: "type_defs.GetLoadBalancerMetricDataResultTypeDef" = (
        dataclasses.field()
    )

    metricName = field("metricName")

    @cached_property
    def metricData(self):  # pragma: no cover
        return MetricDatapoint.make_many(self.boto3_raw_data["metricData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLoadBalancerMetricDataResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerMetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseMetricDataResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseMetricDataResultTypeDef" = (
        dataclasses.field()
    )

    metricName = field("metricName")

    @cached_property
    def metricData(self):  # pragma: no cover
        return MetricDatapoint.make_many(self.boto3_raw_data["metricData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseMetricDataResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseMetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstancePortStatesResult:
    boto3_raw_data: "type_defs.GetInstancePortStatesResultTypeDef" = dataclasses.field()

    @cached_property
    def portStates(self):  # pragma: no cover
        return InstancePortState.make_many(self.boto3_raw_data["portStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstancePortStatesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstancePortStatesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceStateResult:
    boto3_raw_data: "type_defs.GetInstanceStateResultTypeDef" = dataclasses.field()

    @cached_property
    def state(self):  # pragma: no cover
        return InstanceState.make_one(self.boto3_raw_data["state"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceStateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceStateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerTlsPoliciesResult:
    boto3_raw_data: "type_defs.GetLoadBalancerTlsPoliciesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tlsPolicies(self):  # pragma: no cover
        return LoadBalancerTlsPolicy.make_many(self.boto3_raw_data["tlsPolicies"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLoadBalancerTlsPoliciesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerTlsPoliciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseBlueprintsResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseBlueprintsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def blueprints(self):  # pragma: no cover
        return RelationalDatabaseBlueprint.make_many(self.boto3_raw_data["blueprints"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseBlueprintsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseBlueprintsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseBundlesResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseBundlesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def bundles(self):  # pragma: no cover
        return RelationalDatabaseBundle.make_many(self.boto3_raw_data["bundles"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseBundlesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseBundlesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseEventsResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseEventsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relationalDatabaseEvents(self):  # pragma: no cover
        return RelationalDatabaseEvent.make_many(
            self.boto3_raw_data["relationalDatabaseEvents"]
        )

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseEventsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseEventsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseLogEventsResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseLogEventsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceLogEvents(self):  # pragma: no cover
        return LogEvent.make_many(self.boto3_raw_data["resourceLogEvents"])

    nextBackwardToken = field("nextBackwardToken")
    nextForwardToken = field("nextForwardToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseLogEventsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseLogEventsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseParametersResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseParametersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def parameters(self):  # pragma: no cover
        return RelationalDatabaseParameter.make_many(self.boto3_raw_data["parameters"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRelationalDatabaseParametersRequest:
    boto3_raw_data: "type_defs.UpdateRelationalDatabaseParametersRequestTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseName = field("relationalDatabaseName")

    @cached_property
    def parameters(self):  # pragma: no cover
        return RelationalDatabaseParameter.make_many(self.boto3_raw_data["parameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRelationalDatabaseParametersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRelationalDatabaseParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAccessDetails:
    boto3_raw_data: "type_defs.InstanceAccessDetailsTypeDef" = dataclasses.field()

    certKey = field("certKey")
    expiresAt = field("expiresAt")
    ipAddress = field("ipAddress")
    ipv6Addresses = field("ipv6Addresses")
    password = field("password")

    @cached_property
    def passwordData(self):  # pragma: no cover
        return PasswordData.make_one(self.boto3_raw_data["passwordData"])

    privateKey = field("privateKey")
    protocol = field("protocol")
    instanceName = field("instanceName")
    username = field("username")

    @cached_property
    def hostKeys(self):  # pragma: no cover
        return HostKeyAttributes.make_many(self.boto3_raw_data["hostKeys"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceAccessDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAccessDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceNetworking:
    boto3_raw_data: "type_defs.InstanceNetworkingTypeDef" = dataclasses.field()

    @cached_property
    def monthlyTransfer(self):  # pragma: no cover
        return MonthlyTransfer.make_one(self.boto3_raw_data["monthlyTransfer"])

    @cached_property
    def ports(self):  # pragma: no cover
        return InstancePortInfo.make_many(self.boto3_raw_data["ports"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceNetworkingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceNetworkingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsCertificateDomainValidationRecord:
    boto3_raw_data: (
        "type_defs.LoadBalancerTlsCertificateDomainValidationRecordTypeDef"
    ) = dataclasses.field()

    name = field("name")
    type = field("type")
    value = field("value")
    validationStatus = field("validationStatus")
    domainName = field("domainName")

    @cached_property
    def dnsRecordCreationState(self):  # pragma: no cover
        return LoadBalancerTlsCertificateDnsRecordCreationState.make_one(
            self.boto3_raw_data["dnsRecordCreationState"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoadBalancerTlsCertificateDomainValidationRecordTypeDef"
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
                "type_defs.LoadBalancerTlsCertificateDomainValidationRecordTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsCertificateRenewalSummary:
    boto3_raw_data: "type_defs.LoadBalancerTlsCertificateRenewalSummaryTypeDef" = (
        dataclasses.field()
    )

    renewalStatus = field("renewalStatus")

    @cached_property
    def domainValidationOptions(self):  # pragma: no cover
        return LoadBalancerTlsCertificateDomainValidationOption.make_many(
            self.boto3_raw_data["domainValidationOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoadBalancerTlsCertificateRenewalSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerTlsCertificateRenewalSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancer:
    boto3_raw_data: "type_defs.LoadBalancerTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    dnsName = field("dnsName")
    state = field("state")
    protocol = field("protocol")
    publicPorts = field("publicPorts")
    healthCheckPath = field("healthCheckPath")
    instancePort = field("instancePort")

    @cached_property
    def instanceHealthSummary(self):  # pragma: no cover
        return InstanceHealthSummary.make_many(
            self.boto3_raw_data["instanceHealthSummary"]
        )

    @cached_property
    def tlsCertificateSummaries(self):  # pragma: no cover
        return LoadBalancerTlsCertificateSummary.make_many(
            self.boto3_raw_data["tlsCertificateSummaries"]
        )

    configurationOptions = field("configurationOptions")
    ipAddressType = field("ipAddressType")
    httpsRedirectionEnabled = field("httpsRedirectionEnabled")
    tlsPolicyName = field("tlsPolicyName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoadBalancerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisteredDomainDelegationInfo:
    boto3_raw_data: "type_defs.RegisteredDomainDelegationInfoTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nameServersUpdateState(self):  # pragma: no cover
        return NameServersUpdateState.make_one(
            self.boto3_raw_data["nameServersUpdateState"]
        )

    @cached_property
    def r53HostedZoneDeletionState(self):  # pragma: no cover
        return R53HostedZoneDeletionState.make_one(
            self.boto3_raw_data["r53HostedZoneDeletionState"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisteredDomainDelegationInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisteredDomainDelegationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabase:
    boto3_raw_data: "type_defs.RelationalDatabaseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    relationalDatabaseBlueprintId = field("relationalDatabaseBlueprintId")
    relationalDatabaseBundleId = field("relationalDatabaseBundleId")
    masterDatabaseName = field("masterDatabaseName")

    @cached_property
    def hardware(self):  # pragma: no cover
        return RelationalDatabaseHardware.make_one(self.boto3_raw_data["hardware"])

    state = field("state")
    secondaryAvailabilityZone = field("secondaryAvailabilityZone")
    backupRetentionEnabled = field("backupRetentionEnabled")

    @cached_property
    def pendingModifiedValues(self):  # pragma: no cover
        return PendingModifiedRelationalDatabaseValues.make_one(
            self.boto3_raw_data["pendingModifiedValues"]
        )

    engine = field("engine")
    engineVersion = field("engineVersion")
    latestRestorableTime = field("latestRestorableTime")
    masterUsername = field("masterUsername")
    parameterApplyStatus = field("parameterApplyStatus")
    preferredBackupWindow = field("preferredBackupWindow")
    preferredMaintenanceWindow = field("preferredMaintenanceWindow")
    publiclyAccessible = field("publiclyAccessible")

    @cached_property
    def masterEndpoint(self):  # pragma: no cover
        return RelationalDatabaseEndpoint.make_one(
            self.boto3_raw_data["masterEndpoint"]
        )

    @cached_property
    def pendingMaintenanceActions(self):  # pragma: no cover
        return PendingMaintenanceAction.make_many(
            self.boto3_raw_data["pendingMaintenanceActions"]
        )

    caCertificateIdentifier = field("caCertificateIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationalDatabaseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketAccessKeysResult:
    boto3_raw_data: "type_defs.GetBucketAccessKeysResultTypeDef" = dataclasses.field()

    @cached_property
    def accessKeys(self):  # pragma: no cover
        return AccessKey.make_many(self.boto3_raw_data["accessKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketAccessKeysResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAccessKeysResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDiskFromSnapshotRequest:
    boto3_raw_data: "type_defs.CreateDiskFromSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    diskName = field("diskName")
    availabilityZone = field("availabilityZone")
    sizeInGb = field("sizeInGb")
    diskSnapshotName = field("diskSnapshotName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def addOns(self):  # pragma: no cover
        return AddOnRequest.make_many(self.boto3_raw_data["addOns"])

    sourceDiskName = field("sourceDiskName")
    restoreDate = field("restoreDate")
    useLatestRestorableAutoSnapshot = field("useLatestRestorableAutoSnapshot")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDiskFromSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDiskFromSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDiskRequest:
    boto3_raw_data: "type_defs.CreateDiskRequestTypeDef" = dataclasses.field()

    diskName = field("diskName")
    availabilityZone = field("availabilityZone")
    sizeInGb = field("sizeInGb")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def addOns(self):  # pragma: no cover
        return AddOnRequest.make_many(self.boto3_raw_data["addOns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateDiskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDiskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstancesFromSnapshotRequest:
    boto3_raw_data: "type_defs.CreateInstancesFromSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    instanceNames = field("instanceNames")
    availabilityZone = field("availabilityZone")
    bundleId = field("bundleId")
    attachedDiskMapping = field("attachedDiskMapping")
    instanceSnapshotName = field("instanceSnapshotName")
    userData = field("userData")
    keyPairName = field("keyPairName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def addOns(self):  # pragma: no cover
        return AddOnRequest.make_many(self.boto3_raw_data["addOns"])

    ipAddressType = field("ipAddressType")
    sourceInstanceName = field("sourceInstanceName")
    restoreDate = field("restoreDate")
    useLatestRestorableAutoSnapshot = field("useLatestRestorableAutoSnapshot")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInstancesFromSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstancesFromSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstancesRequest:
    boto3_raw_data: "type_defs.CreateInstancesRequestTypeDef" = dataclasses.field()

    instanceNames = field("instanceNames")
    availabilityZone = field("availabilityZone")
    blueprintId = field("blueprintId")
    bundleId = field("bundleId")
    customImageName = field("customImageName")
    userData = field("userData")
    keyPairName = field("keyPairName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def addOns(self):  # pragma: no cover
        return AddOnRequest.make_many(self.boto3_raw_data["addOns"])

    ipAddressType = field("ipAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableAddOnRequest:
    boto3_raw_data: "type_defs.EnableAddOnRequestTypeDef" = dataclasses.field()

    resourceName = field("resourceName")

    @cached_property
    def addOnRequest(self):  # pragma: no cover
        return AddOnRequest.make_one(self.boto3_raw_data["addOnRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableAddOnRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableAddOnRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAlarmsResult:
    boto3_raw_data: "type_defs.GetAlarmsResultTypeDef" = dataclasses.field()

    @cached_property
    def alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["alarms"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAlarmsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAlarmsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactMethodsResult:
    boto3_raw_data: "type_defs.GetContactMethodsResultTypeDef" = dataclasses.field()

    @cached_property
    def contactMethods(self):  # pragma: no cover
        return ContactMethod.make_many(self.boto3_raw_data["contactMethods"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactMethodsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactMethodsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocateStaticIpResult:
    boto3_raw_data: "type_defs.AllocateStaticIpResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllocateStaticIpResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocateStaticIpResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachCertificateToDistributionResult:
    boto3_raw_data: "type_defs.AttachCertificateToDistributionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachCertificateToDistributionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachCertificateToDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachDiskResult:
    boto3_raw_data: "type_defs.AttachDiskResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachDiskResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachDiskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachInstancesToLoadBalancerResult:
    boto3_raw_data: "type_defs.AttachInstancesToLoadBalancerResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachInstancesToLoadBalancerResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachInstancesToLoadBalancerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachLoadBalancerTlsCertificateResult:
    boto3_raw_data: "type_defs.AttachLoadBalancerTlsCertificateResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachLoadBalancerTlsCertificateResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachLoadBalancerTlsCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachStaticIpResult:
    boto3_raw_data: "type_defs.AttachStaticIpResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachStaticIpResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachStaticIpResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloseInstancePublicPortsResult:
    boto3_raw_data: "type_defs.CloseInstancePublicPortsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloseInstancePublicPortsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloseInstancePublicPortsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotResult:
    boto3_raw_data: "type_defs.CopySnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketAccessKeyResult:
    boto3_raw_data: "type_defs.CreateBucketAccessKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def accessKey(self):  # pragma: no cover
        return AccessKey.make_one(self.boto3_raw_data["accessKey"])

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketAccessKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketAccessKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFormationStackResult:
    boto3_raw_data: "type_defs.CreateCloudFormationStackResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCloudFormationStackResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFormationStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactMethodResult:
    boto3_raw_data: "type_defs.CreateContactMethodResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactMethodResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactMethodResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDiskFromSnapshotResult:
    boto3_raw_data: "type_defs.CreateDiskFromSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDiskFromSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDiskFromSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDiskResult:
    boto3_raw_data: "type_defs.CreateDiskResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateDiskResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDiskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDiskSnapshotResult:
    boto3_raw_data: "type_defs.CreateDiskSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDiskSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDiskSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainEntryResult:
    boto3_raw_data: "type_defs.CreateDomainEntryResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainEntryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainEntryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainResult:
    boto3_raw_data: "type_defs.CreateDomainResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceSnapshotResult:
    boto3_raw_data: "type_defs.CreateInstanceSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstancesFromSnapshotResult:
    boto3_raw_data: "type_defs.CreateInstancesFromSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInstancesFromSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstancesFromSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstancesResult:
    boto3_raw_data: "type_defs.CreateInstancesResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstancesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstancesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerResult:
    boto3_raw_data: "type_defs.CreateLoadBalancerResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLoadBalancerResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerTlsCertificateResult:
    boto3_raw_data: "type_defs.CreateLoadBalancerTlsCertificateResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLoadBalancerTlsCertificateResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerTlsCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelationalDatabaseFromSnapshotResult:
    boto3_raw_data: "type_defs.CreateRelationalDatabaseFromSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRelationalDatabaseFromSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelationalDatabaseFromSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelationalDatabaseResult:
    boto3_raw_data: "type_defs.CreateRelationalDatabaseResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRelationalDatabaseResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelationalDatabaseSnapshotResult:
    boto3_raw_data: "type_defs.CreateRelationalDatabaseSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRelationalDatabaseSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelationalDatabaseSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAlarmResult:
    boto3_raw_data: "type_defs.DeleteAlarmResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAlarmResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAlarmResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutoSnapshotResult:
    boto3_raw_data: "type_defs.DeleteAutoSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAutoSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutoSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketAccessKeyResult:
    boto3_raw_data: "type_defs.DeleteBucketAccessKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketAccessKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketAccessKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketResult:
    boto3_raw_data: "type_defs.DeleteBucketResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateResult:
    boto3_raw_data: "type_defs.DeleteCertificateResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCertificateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactMethodResult:
    boto3_raw_data: "type_defs.DeleteContactMethodResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactMethodResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactMethodResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDiskResult:
    boto3_raw_data: "type_defs.DeleteDiskResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteDiskResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDiskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDiskSnapshotResult:
    boto3_raw_data: "type_defs.DeleteDiskSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDiskSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDiskSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDistributionResult:
    boto3_raw_data: "type_defs.DeleteDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainEntryResult:
    boto3_raw_data: "type_defs.DeleteDomainEntryResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainEntryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainEntryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainResult:
    boto3_raw_data: "type_defs.DeleteDomainResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceResult:
    boto3_raw_data: "type_defs.DeleteInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceSnapshotResult:
    boto3_raw_data: "type_defs.DeleteInstanceSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyPairResult:
    boto3_raw_data: "type_defs.DeleteKeyPairResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyPairResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeyPairResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnownHostKeysResult:
    boto3_raw_data: "type_defs.DeleteKnownHostKeysResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKnownHostKeysResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnownHostKeysResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerResult:
    boto3_raw_data: "type_defs.DeleteLoadBalancerResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLoadBalancerResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerTlsCertificateResult:
    boto3_raw_data: "type_defs.DeleteLoadBalancerTlsCertificateResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLoadBalancerTlsCertificateResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerTlsCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRelationalDatabaseResult:
    boto3_raw_data: "type_defs.DeleteRelationalDatabaseResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRelationalDatabaseResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRelationalDatabaseSnapshotResult:
    boto3_raw_data: "type_defs.DeleteRelationalDatabaseSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRelationalDatabaseSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRelationalDatabaseSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachCertificateFromDistributionResult:
    boto3_raw_data: "type_defs.DetachCertificateFromDistributionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachCertificateFromDistributionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachCertificateFromDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachDiskResult:
    boto3_raw_data: "type_defs.DetachDiskResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetachDiskResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachDiskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachInstancesFromLoadBalancerResult:
    boto3_raw_data: "type_defs.DetachInstancesFromLoadBalancerResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachInstancesFromLoadBalancerResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachInstancesFromLoadBalancerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachStaticIpResult:
    boto3_raw_data: "type_defs.DetachStaticIpResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachStaticIpResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachStaticIpResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableAddOnResult:
    boto3_raw_data: "type_defs.DisableAddOnResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableAddOnResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableAddOnResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableAddOnResult:
    boto3_raw_data: "type_defs.EnableAddOnResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableAddOnResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableAddOnResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSnapshotResult:
    boto3_raw_data: "type_defs.ExportSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationResult:
    boto3_raw_data: "type_defs.GetOperationResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationsForResourceResult:
    boto3_raw_data: "type_defs.GetOperationsForResourceResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    nextPageCount = field("nextPageCount")
    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOperationsForResourceResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationsResult:
    boto3_raw_data: "type_defs.GetOperationsResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyPairResult:
    boto3_raw_data: "type_defs.ImportKeyPairResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportKeyPairResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportKeyPairResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenInstancePublicPortsResult:
    boto3_raw_data: "type_defs.OpenInstancePublicPortsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenInstancePublicPortsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenInstancePublicPortsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PeerVpcResult:
    boto3_raw_data: "type_defs.PeerVpcResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PeerVpcResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PeerVpcResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAlarmResult:
    boto3_raw_data: "type_defs.PutAlarmResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutAlarmResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutAlarmResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInstancePublicPortsResult:
    boto3_raw_data: "type_defs.PutInstancePublicPortsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInstancePublicPortsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInstancePublicPortsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootInstanceResult:
    boto3_raw_data: "type_defs.RebootInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootRelationalDatabaseResult:
    boto3_raw_data: "type_defs.RebootRelationalDatabaseResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RebootRelationalDatabaseResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseStaticIpResult:
    boto3_raw_data: "type_defs.ReleaseStaticIpResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleaseStaticIpResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseStaticIpResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetDistributionCacheResult:
    boto3_raw_data: "type_defs.ResetDistributionCacheResultTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    createTime = field("createTime")

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetDistributionCacheResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDistributionCacheResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendContactMethodVerificationResult:
    boto3_raw_data: "type_defs.SendContactMethodVerificationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendContactMethodVerificationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendContactMethodVerificationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIpAddressTypeResult:
    boto3_raw_data: "type_defs.SetIpAddressTypeResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetIpAddressTypeResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIpAddressTypeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetResourceAccessForBucketResult:
    boto3_raw_data: "type_defs.SetResourceAccessForBucketResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetResourceAccessForBucketResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetResourceAccessForBucketResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetupInstanceHttpsResult:
    boto3_raw_data: "type_defs.SetupInstanceHttpsResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetupInstanceHttpsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetupInstanceHttpsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGUISessionResult:
    boto3_raw_data: "type_defs.StartGUISessionResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartGUISessionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGUISessionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceResult:
    boto3_raw_data: "type_defs.StartInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRelationalDatabaseResult:
    boto3_raw_data: "type_defs.StartRelationalDatabaseResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRelationalDatabaseResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopGUISessionResult:
    boto3_raw_data: "type_defs.StopGUISessionResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopGUISessionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopGUISessionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInstanceResult:
    boto3_raw_data: "type_defs.StopInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRelationalDatabaseResult:
    boto3_raw_data: "type_defs.StopRelationalDatabaseResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopRelationalDatabaseResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceResult:
    boto3_raw_data: "type_defs.TagResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestAlarmResult:
    boto3_raw_data: "type_defs.TestAlarmResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestAlarmResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestAlarmResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnpeerVpcResult:
    boto3_raw_data: "type_defs.UnpeerVpcResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnpeerVpcResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnpeerVpcResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceResult:
    boto3_raw_data: "type_defs.UntagResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBucketBundleResult:
    boto3_raw_data: "type_defs.UpdateBucketBundleResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBucketBundleResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBucketBundleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionBundleResult:
    boto3_raw_data: "type_defs.UpdateDistributionBundleResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDistributionBundleResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionBundleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionResult:
    boto3_raw_data: "type_defs.UpdateDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainEntryResult:
    boto3_raw_data: "type_defs.UpdateDomainEntryResultTypeDef" = dataclasses.field()

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainEntryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainEntryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceMetadataOptionsResult:
    boto3_raw_data: "type_defs.UpdateInstanceMetadataOptionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateInstanceMetadataOptionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceMetadataOptionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLoadBalancerAttributeResult:
    boto3_raw_data: "type_defs.UpdateLoadBalancerAttributeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLoadBalancerAttributeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoadBalancerAttributeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRelationalDatabaseParametersResult:
    boto3_raw_data: "type_defs.UpdateRelationalDatabaseParametersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRelationalDatabaseParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRelationalDatabaseParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRelationalDatabaseResult:
    boto3_raw_data: "type_defs.UpdateRelationalDatabaseResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRelationalDatabaseResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetupHistory:
    boto3_raw_data: "type_defs.SetupHistoryTypeDef" = dataclasses.field()

    operationId = field("operationId")

    @cached_property
    def request(self):  # pragma: no cover
        return SetupRequest.make_one(self.boto3_raw_data["request"])

    @cached_property
    def resource(self):  # pragma: no cover
        return SetupHistoryResource.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def executionDetails(self):  # pragma: no cover
        return SetupExecutionDetails.make_many(self.boto3_raw_data["executionDetails"])

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetupHistoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SetupHistoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticIpResult:
    boto3_raw_data: "type_defs.GetStaticIpResultTypeDef" = dataclasses.field()

    @cached_property
    def staticIp(self):  # pragma: no cover
        return StaticIp.make_one(self.boto3_raw_data["staticIp"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStaticIpResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticIpResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticIpsResult:
    boto3_raw_data: "type_defs.GetStaticIpsResultTypeDef" = dataclasses.field()

    @cached_property
    def staticIps(self):  # pragma: no cover
        return StaticIp.make_many(self.boto3_raw_data["staticIps"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStaticIpsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticIpsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoSnapshotsResult:
    boto3_raw_data: "type_defs.GetAutoSnapshotsResultTypeDef" = dataclasses.field()

    resourceName = field("resourceName")
    resourceType = field("resourceType")

    @cached_property
    def autoSnapshots(self):  # pragma: no cover
        return AutoSnapshotDetails.make_many(self.boto3_raw_data["autoSnapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAutoSnapshotsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegionsResult:
    boto3_raw_data: "type_defs.GetRegionsResultTypeDef" = dataclasses.field()

    @cached_property
    def regions(self):  # pragma: no cover
        return Region.make_many(self.boto3_raw_data["regions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRegionsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketResult:
    boto3_raw_data: "type_defs.CreateBucketResultTypeDef" = dataclasses.field()

    @cached_property
    def bucket(self):  # pragma: no cover
        return Bucket.make_one(self.boto3_raw_data["bucket"])

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketsResult:
    boto3_raw_data: "type_defs.GetBucketsResultTypeDef" = dataclasses.field()

    @cached_property
    def buckets(self):  # pragma: no cover
        return Bucket.make_many(self.boto3_raw_data["buckets"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def accountLevelBpaSync(self):  # pragma: no cover
        return AccountLevelBpaSync.make_one(self.boto3_raw_data["accountLevelBpaSync"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBucketsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBucketResult:
    boto3_raw_data: "type_defs.UpdateBucketResultTypeDef" = dataclasses.field()

    @cached_property
    def bucket(self):  # pragma: no cover
        return Bucket.make_one(self.boto3_raw_data["bucket"])

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBucketResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBucketResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskSnapshotResult:
    boto3_raw_data: "type_defs.GetDiskSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def diskSnapshot(self):  # pragma: no cover
        return DiskSnapshot.make_one(self.boto3_raw_data["diskSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDiskSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiskSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskSnapshotsResult:
    boto3_raw_data: "type_defs.GetDiskSnapshotsResultTypeDef" = dataclasses.field()

    @cached_property
    def diskSnapshots(self):  # pragma: no cover
        return DiskSnapshot.make_many(self.boto3_raw_data["diskSnapshots"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDiskSnapshotsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiskSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiskResult:
    boto3_raw_data: "type_defs.GetDiskResultTypeDef" = dataclasses.field()

    @cached_property
    def disk(self):  # pragma: no cover
        return Disk.make_one(self.boto3_raw_data["disk"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDiskResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDiskResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDisksResult:
    boto3_raw_data: "type_defs.GetDisksResultTypeDef" = dataclasses.field()

    @cached_property
    def disks(self):  # pragma: no cover
        return Disk.make_many(self.boto3_raw_data["disks"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDisksResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDisksResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceHardware:
    boto3_raw_data: "type_defs.InstanceHardwareTypeDef" = dataclasses.field()

    cpuCount = field("cpuCount")

    @cached_property
    def disks(self):  # pragma: no cover
        return Disk.make_many(self.boto3_raw_data["disks"])

    ramSizeInGb = field("ramSizeInGb")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceHardwareTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceHardwareTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceSnapshot:
    boto3_raw_data: "type_defs.InstanceSnapshotTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    state = field("state")
    progress = field("progress")

    @cached_property
    def fromAttachedDisks(self):  # pragma: no cover
        return Disk.make_many(self.boto3_raw_data["fromAttachedDisks"])

    fromInstanceName = field("fromInstanceName")
    fromInstanceArn = field("fromInstanceArn")
    fromBlueprintId = field("fromBlueprintId")
    fromBundleId = field("fromBundleId")
    isFromAutoSnapshot = field("isFromAutoSnapshot")
    sizeInGb = field("sizeInGb")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceSnapshotTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyPairResult:
    boto3_raw_data: "type_defs.CreateKeyPairResultTypeDef" = dataclasses.field()

    @cached_property
    def keyPair(self):  # pragma: no cover
        return KeyPair.make_one(self.boto3_raw_data["keyPair"])

    publicKeyBase64 = field("publicKeyBase64")
    privateKeyBase64 = field("privateKeyBase64")

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyPairResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyPairResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPairResult:
    boto3_raw_data: "type_defs.GetKeyPairResultTypeDef" = dataclasses.field()

    @cached_property
    def keyPair(self):  # pragma: no cover
        return KeyPair.make_one(self.boto3_raw_data["keyPair"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKeyPairResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPairResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPairsResult:
    boto3_raw_data: "type_defs.GetKeyPairsResultTypeDef" = dataclasses.field()

    @cached_property
    def keyPairs(self):  # pragma: no cover
        return KeyPair.make_many(self.boto3_raw_data["keyPairs"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKeyPairsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPairsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseSnapshotResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relationalDatabaseSnapshot(self):  # pragma: no cover
        return RelationalDatabaseSnapshot.make_one(
            self.boto3_raw_data["relationalDatabaseSnapshot"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseSnapshotsResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseSnapshotsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relationalDatabaseSnapshots(self):  # pragma: no cover
        return RelationalDatabaseSnapshot.make_many(
            self.boto3_raw_data["relationalDatabaseSnapshots"]
        )

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRelationalDatabaseSnapshotsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LightsailDistribution:
    boto3_raw_data: "type_defs.LightsailDistributionTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")
    alternativeDomainNames = field("alternativeDomainNames")
    status = field("status")
    isEnabled = field("isEnabled")
    domainName = field("domainName")
    bundleId = field("bundleId")
    certificateName = field("certificateName")

    @cached_property
    def origin(self):  # pragma: no cover
        return Origin.make_one(self.boto3_raw_data["origin"])

    originPublicDNS = field("originPublicDNS")

    @cached_property
    def defaultCacheBehavior(self):  # pragma: no cover
        return CacheBehavior.make_one(self.boto3_raw_data["defaultCacheBehavior"])

    @cached_property
    def cacheBehaviorSettings(self):  # pragma: no cover
        return CacheSettingsOutput.make_one(
            self.boto3_raw_data["cacheBehaviorSettings"]
        )

    @cached_property
    def cacheBehaviors(self):  # pragma: no cover
        return CacheBehaviorPerPath.make_many(self.boto3_raw_data["cacheBehaviors"])

    ableToUpdateBundle = field("ableToUpdateBundle")
    ipAddressType = field("ipAddressType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    viewerMinimumTlsProtocolVersion = field("viewerMinimumTlsProtocolVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LightsailDistributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LightsailDistributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFormationStackRecordsResult:
    boto3_raw_data: "type_defs.GetCloudFormationStackRecordsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudFormationStackRecords(self):  # pragma: no cover
        return CloudFormationStackRecord.make_many(
            self.boto3_raw_data["cloudFormationStackRecords"]
        )

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFormationStackRecordsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudFormationStackRecordsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerServiceRequest:
    boto3_raw_data: "type_defs.UpdateContainerServiceRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    power = field("power")
    scale = field("scale")
    isDisabled = field("isDisabled")
    publicDomainNames = field("publicDomainNames")

    @cached_property
    def privateRegistryAccess(self):  # pragma: no cover
        return PrivateRegistryAccessRequest.make_one(
            self.boto3_raw_data["privateRegistryAccess"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContainerServiceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceDeployment:
    boto3_raw_data: "type_defs.ContainerServiceDeploymentTypeDef" = dataclasses.field()

    version = field("version")
    state = field("state")
    containers = field("containers")

    @cached_property
    def publicEndpoint(self):  # pragma: no cover
        return ContainerServiceEndpoint.make_one(self.boto3_raw_data["publicEndpoint"])

    createdAt = field("createdAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerServiceDeploymentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServiceDeploymentRequest:
    boto3_raw_data: "type_defs.ContainerServiceDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    containers = field("containers")

    @cached_property
    def publicEndpoint(self):  # pragma: no cover
        return EndpointRequest.make_one(self.boto3_raw_data["publicEndpoint"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerServiceDeploymentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerServiceDeploymentRequest:
    boto3_raw_data: "type_defs.CreateContainerServiceDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    containers = field("containers")

    @cached_property
    def publicEndpoint(self):  # pragma: no cover
        return EndpointRequest.make_one(self.boto3_raw_data["publicEndpoint"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContainerServiceDeploymentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerServiceDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSnapshotRecordSourceInfo:
    boto3_raw_data: "type_defs.ExportSnapshotRecordSourceInfoTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    createdAt = field("createdAt")
    name = field("name")
    arn = field("arn")
    fromResourceName = field("fromResourceName")
    fromResourceArn = field("fromResourceArn")

    @cached_property
    def instanceSnapshotInfo(self):  # pragma: no cover
        return InstanceSnapshotInfo.make_one(
            self.boto3_raw_data["instanceSnapshotInfo"]
        )

    @cached_property
    def diskSnapshotInfo(self):  # pragma: no cover
        return DiskSnapshotInfo.make_one(self.boto3_raw_data["diskSnapshotInfo"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportSnapshotRecordSourceInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSnapshotRecordSourceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainEntryRequest:
    boto3_raw_data: "type_defs.CreateDomainEntryRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainEntry = field("domainEntry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainEntryRequest:
    boto3_raw_data: "type_defs.DeleteDomainEntryRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainEntry = field("domainEntry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainEntryRequest:
    boto3_raw_data: "type_defs.UpdateDomainEntryRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainEntry = field("domainEntry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewalSummary:
    boto3_raw_data: "type_defs.RenewalSummaryTypeDef" = dataclasses.field()

    @cached_property
    def domainValidationRecords(self):  # pragma: no cover
        return DomainValidationRecord.make_many(
            self.boto3_raw_data["domainValidationRecords"]
        )

    renewalStatus = field("renewalStatus")
    renewalStatusReason = field("renewalStatusReason")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenewalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenewalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostEstimate:
    boto3_raw_data: "type_defs.CostEstimateTypeDef" = dataclasses.field()

    usageType = field("usageType")

    @cached_property
    def resultsByTime(self):  # pragma: no cover
        return EstimateByTime.make_many(self.boto3_raw_data["resultsByTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostEstimateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostEstimateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceAccessDetailsResult:
    boto3_raw_data: "type_defs.GetInstanceAccessDetailsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accessDetails(self):  # pragma: no cover
        return InstanceAccessDetails.make_one(self.boto3_raw_data["accessDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetInstanceAccessDetailsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceAccessDetailsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTlsCertificate:
    boto3_raw_data: "type_defs.LoadBalancerTlsCertificateTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    loadBalancerName = field("loadBalancerName")
    isAttached = field("isAttached")
    status = field("status")
    domainName = field("domainName")

    @cached_property
    def domainValidationRecords(self):  # pragma: no cover
        return LoadBalancerTlsCertificateDomainValidationRecord.make_many(
            self.boto3_raw_data["domainValidationRecords"]
        )

    failureReason = field("failureReason")
    issuedAt = field("issuedAt")
    issuer = field("issuer")
    keyAlgorithm = field("keyAlgorithm")
    notAfter = field("notAfter")
    notBefore = field("notBefore")

    @cached_property
    def renewalSummary(self):  # pragma: no cover
        return LoadBalancerTlsCertificateRenewalSummary.make_one(
            self.boto3_raw_data["renewalSummary"]
        )

    revocationReason = field("revocationReason")
    revokedAt = field("revokedAt")
    serial = field("serial")
    signatureAlgorithm = field("signatureAlgorithm")
    subject = field("subject")
    subjectAlternativeNames = field("subjectAlternativeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTlsCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerTlsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerResult:
    boto3_raw_data: "type_defs.GetLoadBalancerResultTypeDef" = dataclasses.field()

    @cached_property
    def loadBalancer(self):  # pragma: no cover
        return LoadBalancer.make_one(self.boto3_raw_data["loadBalancer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoadBalancerResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancersResult:
    boto3_raw_data: "type_defs.GetLoadBalancersResultTypeDef" = dataclasses.field()

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoadBalancersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Domain:
    boto3_raw_data: "type_defs.DomainTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def domainEntries(self):  # pragma: no cover
        return DomainEntryOutput.make_many(self.boto3_raw_data["domainEntries"])

    @cached_property
    def registeredDomainDelegationInfo(self):  # pragma: no cover
        return RegisteredDomainDelegationInfo.make_one(
            self.boto3_raw_data["registeredDomainDelegationInfo"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabaseResult:
    boto3_raw_data: "type_defs.GetRelationalDatabaseResultTypeDef" = dataclasses.field()

    @cached_property
    def relationalDatabase(self):  # pragma: no cover
        return RelationalDatabase.make_one(self.boto3_raw_data["relationalDatabase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRelationalDatabaseResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRelationalDatabasesResult:
    boto3_raw_data: "type_defs.GetRelationalDatabasesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relationalDatabases(self):  # pragma: no cover
        return RelationalDatabase.make_many(self.boto3_raw_data["relationalDatabases"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRelationalDatabasesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRelationalDatabasesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSetupHistoryResult:
    boto3_raw_data: "type_defs.GetSetupHistoryResultTypeDef" = dataclasses.field()

    @cached_property
    def setupHistory(self):  # pragma: no cover
        return SetupHistory.make_many(self.boto3_raw_data["setupHistory"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSetupHistoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSetupHistoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    supportCode = field("supportCode")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    blueprintId = field("blueprintId")
    blueprintName = field("blueprintName")
    bundleId = field("bundleId")

    @cached_property
    def addOns(self):  # pragma: no cover
        return AddOn.make_many(self.boto3_raw_data["addOns"])

    isStaticIp = field("isStaticIp")
    privateIpAddress = field("privateIpAddress")
    publicIpAddress = field("publicIpAddress")
    ipv6Addresses = field("ipv6Addresses")
    ipAddressType = field("ipAddressType")

    @cached_property
    def hardware(self):  # pragma: no cover
        return InstanceHardware.make_one(self.boto3_raw_data["hardware"])

    @cached_property
    def networking(self):  # pragma: no cover
        return InstanceNetworking.make_one(self.boto3_raw_data["networking"])

    @cached_property
    def state(self):  # pragma: no cover
        return InstanceState.make_one(self.boto3_raw_data["state"])

    username = field("username")
    sshKeyName = field("sshKeyName")

    @cached_property
    def metadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptions.make_one(self.boto3_raw_data["metadataOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceSnapshotResult:
    boto3_raw_data: "type_defs.GetInstanceSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def instanceSnapshot(self):  # pragma: no cover
        return InstanceSnapshot.make_one(self.boto3_raw_data["instanceSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceSnapshotsResult:
    boto3_raw_data: "type_defs.GetInstanceSnapshotsResultTypeDef" = dataclasses.field()

    @cached_property
    def instanceSnapshots(self):  # pragma: no cover
        return InstanceSnapshot.make_many(self.boto3_raw_data["instanceSnapshots"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceSnapshotsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionResult:
    boto3_raw_data: "type_defs.CreateDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def distribution(self):  # pragma: no cover
        return LightsailDistribution.make_one(self.boto3_raw_data["distribution"])

    @cached_property
    def operation(self):  # pragma: no cover
        return Operation.make_one(self.boto3_raw_data["operation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionsResult:
    boto3_raw_data: "type_defs.GetDistributionsResultTypeDef" = dataclasses.field()

    @cached_property
    def distributions(self):  # pragma: no cover
        return LightsailDistribution.make_many(self.boto3_raw_data["distributions"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionRequest:
    boto3_raw_data: "type_defs.CreateDistributionRequestTypeDef" = dataclasses.field()

    distributionName = field("distributionName")

    @cached_property
    def origin(self):  # pragma: no cover
        return InputOrigin.make_one(self.boto3_raw_data["origin"])

    @cached_property
    def defaultCacheBehavior(self):  # pragma: no cover
        return CacheBehavior.make_one(self.boto3_raw_data["defaultCacheBehavior"])

    bundleId = field("bundleId")
    cacheBehaviorSettings = field("cacheBehaviorSettings")

    @cached_property
    def cacheBehaviors(self):  # pragma: no cover
        return CacheBehaviorPerPath.make_many(self.boto3_raw_data["cacheBehaviors"])

    ipAddressType = field("ipAddressType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    certificateName = field("certificateName")
    viewerMinimumTlsProtocolVersion = field("viewerMinimumTlsProtocolVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionRequest:
    boto3_raw_data: "type_defs.UpdateDistributionRequestTypeDef" = dataclasses.field()

    distributionName = field("distributionName")

    @cached_property
    def origin(self):  # pragma: no cover
        return InputOrigin.make_one(self.boto3_raw_data["origin"])

    @cached_property
    def defaultCacheBehavior(self):  # pragma: no cover
        return CacheBehavior.make_one(self.boto3_raw_data["defaultCacheBehavior"])

    cacheBehaviorSettings = field("cacheBehaviorSettings")

    @cached_property
    def cacheBehaviors(self):  # pragma: no cover
        return CacheBehaviorPerPath.make_many(self.boto3_raw_data["cacheBehaviors"])

    isEnabled = field("isEnabled")
    viewerMinimumTlsProtocolVersion = field("viewerMinimumTlsProtocolVersion")
    certificateName = field("certificateName")
    useDefaultCertificate = field("useDefaultCertificate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerService:
    boto3_raw_data: "type_defs.ContainerServiceTypeDef" = dataclasses.field()

    containerServiceName = field("containerServiceName")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    power = field("power")
    powerId = field("powerId")
    state = field("state")

    @cached_property
    def stateDetail(self):  # pragma: no cover
        return ContainerServiceStateDetail.make_one(self.boto3_raw_data["stateDetail"])

    scale = field("scale")

    @cached_property
    def currentDeployment(self):  # pragma: no cover
        return ContainerServiceDeployment.make_one(
            self.boto3_raw_data["currentDeployment"]
        )

    @cached_property
    def nextDeployment(self):  # pragma: no cover
        return ContainerServiceDeployment.make_one(
            self.boto3_raw_data["nextDeployment"]
        )

    isDisabled = field("isDisabled")
    principalArn = field("principalArn")
    privateDomainName = field("privateDomainName")
    publicDomainNames = field("publicDomainNames")
    url = field("url")

    @cached_property
    def privateRegistryAccess(self):  # pragma: no cover
        return PrivateRegistryAccess.make_one(
            self.boto3_raw_data["privateRegistryAccess"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerServiceDeploymentsResult:
    boto3_raw_data: "type_defs.GetContainerServiceDeploymentsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deployments(self):  # pragma: no cover
        return ContainerServiceDeployment.make_many(self.boto3_raw_data["deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContainerServiceDeploymentsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerServiceDeploymentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerServiceRequest:
    boto3_raw_data: "type_defs.CreateContainerServiceRequestTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    power = field("power")
    scale = field("scale")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    publicDomainNames = field("publicDomainNames")

    @cached_property
    def deployment(self):  # pragma: no cover
        return ContainerServiceDeploymentRequest.make_one(
            self.boto3_raw_data["deployment"]
        )

    @cached_property
    def privateRegistryAccess(self):  # pragma: no cover
        return PrivateRegistryAccessRequest.make_one(
            self.boto3_raw_data["privateRegistryAccess"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContainerServiceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSnapshotRecord:
    boto3_raw_data: "type_defs.ExportSnapshotRecordTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def location(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["location"])

    resourceType = field("resourceType")
    state = field("state")

    @cached_property
    def sourceInfo(self):  # pragma: no cover
        return ExportSnapshotRecordSourceInfo.make_one(
            self.boto3_raw_data["sourceInfo"]
        )

    @cached_property
    def destinationInfo(self):  # pragma: no cover
        return DestinationInfo.make_one(self.boto3_raw_data["destinationInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportSnapshotRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSnapshotRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    domainName = field("domainName")
    status = field("status")
    serialNumber = field("serialNumber")
    subjectAlternativeNames = field("subjectAlternativeNames")

    @cached_property
    def domainValidationRecords(self):  # pragma: no cover
        return DomainValidationRecord.make_many(
            self.boto3_raw_data["domainValidationRecords"]
        )

    requestFailureReason = field("requestFailureReason")
    inUseResourceCount = field("inUseResourceCount")
    keyAlgorithm = field("keyAlgorithm")
    createdAt = field("createdAt")
    issuedAt = field("issuedAt")
    issuerCA = field("issuerCA")
    notBefore = field("notBefore")
    notAfter = field("notAfter")
    eligibleToRenew = field("eligibleToRenew")

    @cached_property
    def renewalSummary(self):  # pragma: no cover
        return RenewalSummary.make_one(self.boto3_raw_data["renewalSummary"])

    revokedAt = field("revokedAt")
    revocationReason = field("revocationReason")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    supportCode = field("supportCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceBudgetEstimate:
    boto3_raw_data: "type_defs.ResourceBudgetEstimateTypeDef" = dataclasses.field()

    resourceName = field("resourceName")
    resourceType = field("resourceType")

    @cached_property
    def costEstimates(self):  # pragma: no cover
        return CostEstimate.make_many(self.boto3_raw_data["costEstimates"])

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceBudgetEstimateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceBudgetEstimateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoadBalancerTlsCertificatesResult:
    boto3_raw_data: "type_defs.GetLoadBalancerTlsCertificatesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tlsCertificates(self):  # pragma: no cover
        return LoadBalancerTlsCertificate.make_many(
            self.boto3_raw_data["tlsCertificates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLoadBalancerTlsCertificatesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoadBalancerTlsCertificatesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainResult:
    boto3_raw_data: "type_defs.GetDomainResultTypeDef" = dataclasses.field()

    @cached_property
    def domain(self):  # pragma: no cover
        return Domain.make_one(self.boto3_raw_data["domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDomainResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainsResult:
    boto3_raw_data: "type_defs.GetDomainsResultTypeDef" = dataclasses.field()

    @cached_property
    def domains(self):  # pragma: no cover
        return Domain.make_many(self.boto3_raw_data["domains"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceResult:
    boto3_raw_data: "type_defs.GetInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return Instance.make_one(self.boto3_raw_data["instance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetInstanceResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstancesResult:
    boto3_raw_data: "type_defs.GetInstancesResultTypeDef" = dataclasses.field()

    @cached_property
    def instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["instances"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstancesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstancesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerServicesListResult:
    boto3_raw_data: "type_defs.ContainerServicesListResultTypeDef" = dataclasses.field()

    @cached_property
    def containerServices(self):  # pragma: no cover
        return ContainerService.make_many(self.boto3_raw_data["containerServices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerServicesListResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerServicesListResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerServiceDeploymentResult:
    boto3_raw_data: "type_defs.CreateContainerServiceDeploymentResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerService(self):  # pragma: no cover
        return ContainerService.make_one(self.boto3_raw_data["containerService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContainerServiceDeploymentResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerServiceDeploymentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerServiceResult:
    boto3_raw_data: "type_defs.CreateContainerServiceResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerService(self):  # pragma: no cover
        return ContainerService.make_one(self.boto3_raw_data["containerService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContainerServiceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerServiceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerServiceResult:
    boto3_raw_data: "type_defs.UpdateContainerServiceResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerService(self):  # pragma: no cover
        return ContainerService.make_one(self.boto3_raw_data["containerService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContainerServiceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerServiceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportSnapshotRecordsResult:
    boto3_raw_data: "type_defs.GetExportSnapshotRecordsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def exportSnapshotRecords(self):  # pragma: no cover
        return ExportSnapshotRecord.make_many(
            self.boto3_raw_data["exportSnapshotRecords"]
        )

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExportSnapshotRecordsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportSnapshotRecordsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateSummary:
    boto3_raw_data: "type_defs.CertificateSummaryTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateName = field("certificateName")
    domainName = field("domainName")

    @cached_property
    def certificateDetail(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["certificateDetail"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostEstimateResult:
    boto3_raw_data: "type_defs.GetCostEstimateResultTypeDef" = dataclasses.field()

    @cached_property
    def resourcesBudgetEstimate(self):  # pragma: no cover
        return ResourceBudgetEstimate.make_many(
            self.boto3_raw_data["resourcesBudgetEstimate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostEstimateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostEstimateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateResult:
    boto3_raw_data: "type_defs.CreateCertificateResultTypeDef" = dataclasses.field()

    @cached_property
    def certificate(self):  # pragma: no cover
        return CertificateSummary.make_one(self.boto3_raw_data["certificate"])

    @cached_property
    def operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["operations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCertificateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificatesResult:
    boto3_raw_data: "type_defs.GetCertificatesResultTypeDef" = dataclasses.field()

    @cached_property
    def certificates(self):  # pragma: no cover
        return CertificateSummary.make_many(self.boto3_raw_data["certificates"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCertificatesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificatesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
