# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_license_manager import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptGrantRequest:
    boto3_raw_data: "type_defs.AcceptGrantRequestTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptGrantRequestTypeDef"]
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
class AutomatedDiscoveryInformation:
    boto3_raw_data: "type_defs.AutomatedDiscoveryInformationTypeDef" = (
        dataclasses.field()
    )

    LastRunTime = field("LastRunTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedDiscoveryInformationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedDiscoveryInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BorrowConfiguration:
    boto3_raw_data: "type_defs.BorrowConfigurationTypeDef" = dataclasses.field()

    AllowEarlyCheckIn = field("AllowEarlyCheckIn")
    MaxTimeToLiveInMinutes = field("MaxTimeToLiveInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BorrowConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BorrowConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckInLicenseRequest:
    boto3_raw_data: "type_defs.CheckInLicenseRequestTypeDef" = dataclasses.field()

    LicenseConsumptionToken = field("LicenseConsumptionToken")
    Beneficiary = field("Beneficiary")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckInLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckInLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitlementData:
    boto3_raw_data: "type_defs.EntitlementDataTypeDef" = dataclasses.field()

    Name = field("Name")
    Unit = field("Unit")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitlementDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntitlementDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metadata:
    boto3_raw_data: "type_defs.MetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumedLicenseSummary:
    boto3_raw_data: "type_defs.ConsumedLicenseSummaryTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ConsumedLicenses = field("ConsumedLicenses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsumedLicenseSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumedLicenseSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionalConfiguration:
    boto3_raw_data: "type_defs.ProvisionalConfigurationTypeDef" = dataclasses.field()

    MaxTimeToLiveInMinutes = field("MaxTimeToLiveInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionalConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionalConfigurationTypeDef"]
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

    Key = field("Key")
    Value = field("Value")

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
class Options:
    boto3_raw_data: "type_defs.OptionsTypeDef" = dataclasses.field()

    ActivationOverrideBehavior = field("ActivationOverrideBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportFrequency:
    boto3_raw_data: "type_defs.ReportFrequencyTypeDef" = dataclasses.field()

    value = field("value")
    period = field("period")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportFrequencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportFrequencyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatetimeRange:
    boto3_raw_data: "type_defs.DatetimeRangeTypeDef" = dataclasses.field()

    Begin = field("Begin")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatetimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatetimeRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entitlement:
    boto3_raw_data: "type_defs.EntitlementTypeDef" = dataclasses.field()

    Name = field("Name")
    Unit = field("Unit")
    Value = field("Value")
    MaxCount = field("MaxCount")
    Overage = field("Overage")
    AllowCheckIn = field("AllowCheckIn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitlementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntitlementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Issuer:
    boto3_raw_data: "type_defs.IssuerTypeDef" = dataclasses.field()

    Name = field("Name")
    SignKey = field("SignKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IssuerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IssuerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenRequest:
    boto3_raw_data: "type_defs.CreateTokenRequestTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    ClientToken = field("ClientToken")
    RoleArns = field("RoleArns")
    ExpirationInDays = field("ExpirationInDays")
    TokenProperties = field("TokenProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGrantRequest:
    boto3_raw_data: "type_defs.DeleteGrantRequestTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Version = field("Version")
    StatusReason = field("StatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteLicenseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArn = field("LicenseConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLicenseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseManagerReportGeneratorRequest:
    boto3_raw_data: "type_defs.DeleteLicenseManagerReportGeneratorRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseManagerReportGeneratorArn = field("LicenseManagerReportGeneratorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLicenseManagerReportGeneratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseManagerReportGeneratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseRequest:
    boto3_raw_data: "type_defs.DeleteLicenseRequestTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    SourceVersion = field("SourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTokenRequest:
    boto3_raw_data: "type_defs.DeleteTokenRequestTypeDef" = dataclasses.field()

    TokenId = field("TokenId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitlementUsage:
    boto3_raw_data: "type_defs.EntitlementUsageTypeDef" = dataclasses.field()

    Name = field("Name")
    ConsumedValue = field("ConsumedValue")
    Unit = field("Unit")
    MaxCount = field("MaxCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitlementUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntitlementUsageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendLicenseConsumptionRequest:
    boto3_raw_data: "type_defs.ExtendLicenseConsumptionRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConsumptionToken = field("LicenseConsumptionToken")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExtendLicenseConsumptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendLicenseConsumptionRequestTypeDef"]
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

    Name = field("Name")
    Values = field("Values")

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
class GetAccessTokenRequest:
    boto3_raw_data: "type_defs.GetAccessTokenRequestTypeDef" = dataclasses.field()

    Token = field("Token")
    TokenProperties = field("TokenProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGrantRequest:
    boto3_raw_data: "type_defs.GetGrantRequestTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGrantRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGrantRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseConfigurationRequest:
    boto3_raw_data: "type_defs.GetLicenseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArn = field("LicenseConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLicenseConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedResourceSummary:
    boto3_raw_data: "type_defs.ManagedResourceSummaryTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    AssociationCount = field("AssociationCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseConversionTaskRequest:
    boto3_raw_data: "type_defs.GetLicenseConversionTaskRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConversionTaskId = field("LicenseConversionTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLicenseConversionTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseConversionTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseManagerReportGeneratorRequest:
    boto3_raw_data: "type_defs.GetLicenseManagerReportGeneratorRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseManagerReportGeneratorArn = field("LicenseManagerReportGeneratorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLicenseManagerReportGeneratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseManagerReportGeneratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseRequest:
    boto3_raw_data: "type_defs.GetLicenseRequestTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLicenseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseUsageRequest:
    boto3_raw_data: "type_defs.GetLicenseUsageRequestTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLicenseUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationConfiguration:
    boto3_raw_data: "type_defs.OrganizationConfigurationTypeDef" = dataclasses.field()

    EnableIntegration = field("EnableIntegration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssuerDetails:
    boto3_raw_data: "type_defs.IssuerDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    SignKey = field("SignKey")
    KeyFingerprint = field("KeyFingerprint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IssuerDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IssuerDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceivedMetadata:
    boto3_raw_data: "type_defs.ReceivedMetadataTypeDef" = dataclasses.field()

    ReceivedStatus = field("ReceivedStatus")
    ReceivedStatusReason = field("ReceivedStatusReason")
    AllowedOperations = field("AllowedOperations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceivedMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceivedMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryFilter:
    boto3_raw_data: "type_defs.InventoryFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Condition = field("Condition")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InventoryFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConfigurationAssociation:
    boto3_raw_data: "type_defs.LicenseConfigurationAssociationTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    ResourceOwnerId = field("ResourceOwnerId")
    AssociationTime = field("AssociationTime")
    AmiAssociationScope = field("AmiAssociationScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LicenseConfigurationAssociationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConfigurationAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConfigurationUsage:
    boto3_raw_data: "type_defs.LicenseConfigurationUsageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    ResourceStatus = field("ResourceStatus")
    ResourceOwnerId = field("ResourceOwnerId")
    AssociationTime = field("AssociationTime")
    ConsumedLicenses = field("ConsumedLicenses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseConfigurationUsageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConfigurationUsageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductCodeListItem:
    boto3_raw_data: "type_defs.ProductCodeListItemTypeDef" = dataclasses.field()

    ProductCodeId = field("ProductCodeId")
    ProductCodeType = field("ProductCodeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductCodeListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductCodeListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseSpecification:
    boto3_raw_data: "type_defs.LicenseSpecificationTypeDef" = dataclasses.field()

    LicenseConfigurationArn = field("LicenseConfigurationArn")
    AmiAssociationScope = field("AmiAssociationScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseSpecificationTypeDef"]
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
class ListAssociationsForLicenseConfigurationRequest:
    boto3_raw_data: (
        "type_defs.ListAssociationsForLicenseConfigurationRequestTypeDef"
    ) = dataclasses.field()

    LicenseConfigurationArn = field("LicenseConfigurationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociationsForLicenseConfigurationRequestTypeDef"
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
                "type_defs.ListAssociationsForLicenseConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFailuresForLicenseConfigurationOperationsRequest:
    boto3_raw_data: (
        "type_defs.ListFailuresForLicenseConfigurationOperationsRequestTypeDef"
    ) = dataclasses.field()

    LicenseConfigurationArn = field("LicenseConfigurationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFailuresForLicenseConfigurationOperationsRequestTypeDef"
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
                "type_defs.ListFailuresForLicenseConfigurationOperationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseSpecificationsForResourceRequest:
    boto3_raw_data: "type_defs.ListLicenseSpecificationsForResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseSpecificationsForResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseSpecificationsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseVersionsRequest:
    boto3_raw_data: "type_defs.ListLicenseVersionsRequestTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLicenseVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceInventory:
    boto3_raw_data: "type_defs.ResourceInventoryTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    ResourceArn = field("ResourceArn")
    Platform = field("Platform")
    PlatformVersion = field("PlatformVersion")
    ResourceOwningAccountId = field("ResourceOwningAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceInventoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceInventoryTypeDef"]
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
class TokenData:
    boto3_raw_data: "type_defs.TokenDataTypeDef" = dataclasses.field()

    TokenId = field("TokenId")
    TokenType = field("TokenType")
    LicenseArn = field("LicenseArn")
    ExpirationTime = field("ExpirationTime")
    TokenProperties = field("TokenProperties")
    RoleArns = field("RoleArns")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TokenDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TokenDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductInformationFilterOutput:
    boto3_raw_data: "type_defs.ProductInformationFilterOutputTypeDef" = (
        dataclasses.field()
    )

    ProductInformationFilterName = field("ProductInformationFilterName")
    ProductInformationFilterComparator = field("ProductInformationFilterComparator")
    ProductInformationFilterValue = field("ProductInformationFilterValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProductInformationFilterOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductInformationFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductInformationFilter:
    boto3_raw_data: "type_defs.ProductInformationFilterTypeDef" = dataclasses.field()

    ProductInformationFilterName = field("ProductInformationFilterName")
    ProductInformationFilterComparator = field("ProductInformationFilterComparator")
    ProductInformationFilterValue = field("ProductInformationFilterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductInformationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductInformationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectGrantRequest:
    boto3_raw_data: "type_defs.RejectGrantRequestTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportContextOutput:
    boto3_raw_data: "type_defs.ReportContextOutputTypeDef" = dataclasses.field()

    licenseConfigurationArns = field("licenseConfigurationArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportContextOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportContext:
    boto3_raw_data: "type_defs.ReportContextTypeDef" = dataclasses.field()

    licenseConfigurationArns = field("licenseConfigurationArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
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
class AcceptGrantResponse:
    boto3_raw_data: "type_defs.AcceptGrantResponseTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Status = field("Status")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGrantResponse:
    boto3_raw_data: "type_defs.CreateGrantResponseTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Status = field("Status")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGrantVersionResponse:
    boto3_raw_data: "type_defs.CreateGrantVersionResponseTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Status = field("Status")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGrantVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGrantVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseConfigurationResponse:
    boto3_raw_data: "type_defs.CreateLicenseConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArn = field("LicenseConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseConversionTaskForResourceResponse:
    boto3_raw_data: (
        "type_defs.CreateLicenseConversionTaskForResourceResponseTypeDef"
    ) = dataclasses.field()

    LicenseConversionTaskId = field("LicenseConversionTaskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseConversionTaskForResourceResponseTypeDef"
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
                "type_defs.CreateLicenseConversionTaskForResourceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseManagerReportGeneratorResponse:
    boto3_raw_data: "type_defs.CreateLicenseManagerReportGeneratorResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseManagerReportGeneratorArn = field("LicenseManagerReportGeneratorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseManagerReportGeneratorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseManagerReportGeneratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseResponse:
    boto3_raw_data: "type_defs.CreateLicenseResponseTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    Status = field("Status")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLicenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseVersionResponse:
    boto3_raw_data: "type_defs.CreateLicenseVersionResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseArn = field("LicenseArn")
    Version = field("Version")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLicenseVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenResponse:
    boto3_raw_data: "type_defs.CreateTokenResponseTypeDef" = dataclasses.field()

    TokenId = field("TokenId")
    TokenType = field("TokenType")
    Token = field("Token")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGrantResponse:
    boto3_raw_data: "type_defs.DeleteGrantResponseTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Status = field("Status")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseResponse:
    boto3_raw_data: "type_defs.DeleteLicenseResponseTypeDef" = dataclasses.field()

    Status = field("Status")
    DeletionDate = field("DeletionDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLicenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendLicenseConsumptionResponse:
    boto3_raw_data: "type_defs.ExtendLicenseConsumptionResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseConsumptionToken = field("LicenseConsumptionToken")
    Expiration = field("Expiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExtendLicenseConsumptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendLicenseConsumptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessTokenResponse:
    boto3_raw_data: "type_defs.GetAccessTokenResponseTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectGrantResponse:
    boto3_raw_data: "type_defs.RejectGrantResponseTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    Status = field("Status")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckoutLicenseRequest:
    boto3_raw_data: "type_defs.CheckoutLicenseRequestTypeDef" = dataclasses.field()

    ProductSKU = field("ProductSKU")
    CheckoutType = field("CheckoutType")
    KeyFingerprint = field("KeyFingerprint")

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return EntitlementData.make_many(self.boto3_raw_data["Entitlements"])

    ClientToken = field("ClientToken")
    Beneficiary = field("Beneficiary")
    NodeId = field("NodeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckoutLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckoutLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckoutLicenseResponse:
    boto3_raw_data: "type_defs.CheckoutLicenseResponseTypeDef" = dataclasses.field()

    CheckoutType = field("CheckoutType")
    LicenseConsumptionToken = field("LicenseConsumptionToken")

    @cached_property
    def EntitlementsAllowed(self):  # pragma: no cover
        return EntitlementData.make_many(self.boto3_raw_data["EntitlementsAllowed"])

    SignedToken = field("SignedToken")
    NodeId = field("NodeId")
    IssuedAt = field("IssuedAt")
    Expiration = field("Expiration")
    LicenseArn = field("LicenseArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckoutLicenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckoutLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckoutBorrowLicenseRequest:
    boto3_raw_data: "type_defs.CheckoutBorrowLicenseRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseArn = field("LicenseArn")

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return EntitlementData.make_many(self.boto3_raw_data["Entitlements"])

    DigitalSignatureMethod = field("DigitalSignatureMethod")
    ClientToken = field("ClientToken")
    NodeId = field("NodeId")

    @cached_property
    def CheckoutMetadata(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["CheckoutMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckoutBorrowLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckoutBorrowLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckoutBorrowLicenseResponse:
    boto3_raw_data: "type_defs.CheckoutBorrowLicenseResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseArn = field("LicenseArn")
    LicenseConsumptionToken = field("LicenseConsumptionToken")

    @cached_property
    def EntitlementsAllowed(self):  # pragma: no cover
        return EntitlementData.make_many(self.boto3_raw_data["EntitlementsAllowed"])

    NodeId = field("NodeId")
    SignedToken = field("SignedToken")
    IssuedAt = field("IssuedAt")
    Expiration = field("Expiration")

    @cached_property
    def CheckoutMetadata(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["CheckoutMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CheckoutBorrowLicenseResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckoutBorrowLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseOperationFailure:
    boto3_raw_data: "type_defs.LicenseOperationFailureTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    ErrorMessage = field("ErrorMessage")
    FailureTime = field("FailureTime")
    OperationName = field("OperationName")
    ResourceOwnerId = field("ResourceOwnerId")
    OperationRequestedBy = field("OperationRequestedBy")

    @cached_property
    def MetadataList(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["MetadataList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseOperationFailureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseOperationFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumptionConfiguration:
    boto3_raw_data: "type_defs.ConsumptionConfigurationTypeDef" = dataclasses.field()

    RenewType = field("RenewType")

    @cached_property
    def ProvisionalConfiguration(self):  # pragma: no cover
        return ProvisionalConfiguration.make_one(
            self.boto3_raw_data["ProvisionalConfiguration"]
        )

    @cached_property
    def BorrowConfiguration(self):  # pragma: no cover
        return BorrowConfiguration.make_one(self.boto3_raw_data["BorrowConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsumptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGrantRequest:
    boto3_raw_data: "type_defs.CreateGrantRequestTypeDef" = dataclasses.field()

    ClientToken = field("ClientToken")
    GrantName = field("GrantName")
    LicenseArn = field("LicenseArn")
    Principals = field("Principals")
    HomeRegion = field("HomeRegion")
    AllowedOperations = field("AllowedOperations")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGrantRequestTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateGrantVersionRequest:
    boto3_raw_data: "type_defs.CreateGrantVersionRequestTypeDef" = dataclasses.field()

    ClientToken = field("ClientToken")
    GrantArn = field("GrantArn")
    GrantName = field("GrantName")
    AllowedOperations = field("AllowedOperations")
    Status = field("Status")
    StatusReason = field("StatusReason")
    SourceVersion = field("SourceVersion")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGrantVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGrantVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grant:
    boto3_raw_data: "type_defs.GrantTypeDef" = dataclasses.field()

    GrantArn = field("GrantArn")
    GrantName = field("GrantName")
    ParentArn = field("ParentArn")
    LicenseArn = field("LicenseArn")
    GranteePrincipalArn = field("GranteePrincipalArn")
    HomeRegion = field("HomeRegion")
    GrantStatus = field("GrantStatus")
    Version = field("Version")
    GrantedOperations = field("GrantedOperations")
    StatusReason = field("StatusReason")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseUsage:
    boto3_raw_data: "type_defs.LicenseUsageTypeDef" = dataclasses.field()

    @cached_property
    def EntitlementUsages(self):  # pragma: no cover
        return EntitlementUsage.make_many(self.boto3_raw_data["EntitlementUsages"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicenseUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicenseUsageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributedGrantsRequest:
    boto3_raw_data: "type_defs.ListDistributedGrantsRequestTypeDef" = (
        dataclasses.field()
    )

    GrantArns = field("GrantArns")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDistributedGrantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributedGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseConfigurationsRequest:
    boto3_raw_data: "type_defs.ListLicenseConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArns = field("LicenseConfigurationArns")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLicenseConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseConversionTasksRequest:
    boto3_raw_data: "type_defs.ListLicenseConversionTasksRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseConversionTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseConversionTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseManagerReportGeneratorsRequest:
    boto3_raw_data: "type_defs.ListLicenseManagerReportGeneratorsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseManagerReportGeneratorsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseManagerReportGeneratorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicensesRequest:
    boto3_raw_data: "type_defs.ListLicensesRequestTypeDef" = dataclasses.field()

    LicenseArns = field("LicenseArns")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLicensesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicensesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedGrantsForOrganizationRequest:
    boto3_raw_data: "type_defs.ListReceivedGrantsForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseArn = field("LicenseArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReceivedGrantsForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedGrantsForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedGrantsRequest:
    boto3_raw_data: "type_defs.ListReceivedGrantsRequestTypeDef" = dataclasses.field()

    GrantArns = field("GrantArns")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceivedGrantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedLicensesForOrganizationRequest:
    boto3_raw_data: "type_defs.ListReceivedLicensesForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReceivedLicensesForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedLicensesForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedLicensesRequest:
    boto3_raw_data: "type_defs.ListReceivedLicensesRequestTypeDef" = dataclasses.field()

    LicenseArns = field("LicenseArns")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceivedLicensesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedLicensesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTokensRequest:
    boto3_raw_data: "type_defs.ListTokensRequestTypeDef" = dataclasses.field()

    TokenIds = field("TokenIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTokensRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTokensRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageForLicenseConfigurationRequest:
    boto3_raw_data: "type_defs.ListUsageForLicenseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArn = field("LicenseConfigurationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUsageForLicenseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageForLicenseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSettingsResponse:
    boto3_raw_data: "type_defs.GetServiceSettingsResponseTypeDef" = dataclasses.field()

    S3BucketArn = field("S3BucketArn")
    SnsTopicArn = field("SnsTopicArn")

    @cached_property
    def OrganizationConfiguration(self):  # pragma: no cover
        return OrganizationConfiguration.make_one(
            self.boto3_raw_data["OrganizationConfiguration"]
        )

    EnableCrossAccountsDiscovery = field("EnableCrossAccountsDiscovery")
    LicenseManagerResourceShareArn = field("LicenseManagerResourceShareArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSettingsRequest:
    boto3_raw_data: "type_defs.UpdateServiceSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    S3BucketArn = field("S3BucketArn")
    SnsTopicArn = field("SnsTopicArn")

    @cached_property
    def OrganizationConfiguration(self):  # pragma: no cover
        return OrganizationConfiguration.make_one(
            self.boto3_raw_data["OrganizationConfiguration"]
        )

    EnableCrossAccountsDiscovery = field("EnableCrossAccountsDiscovery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceInventoryRequest:
    boto3_raw_data: "type_defs.ListResourceInventoryRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return InventoryFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceInventoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceInventoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationsForLicenseConfigurationResponse:
    boto3_raw_data: (
        "type_defs.ListAssociationsForLicenseConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def LicenseConfigurationAssociations(self):  # pragma: no cover
        return LicenseConfigurationAssociation.make_many(
            self.boto3_raw_data["LicenseConfigurationAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociationsForLicenseConfigurationResponseTypeDef"
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
                "type_defs.ListAssociationsForLicenseConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageForLicenseConfigurationResponse:
    boto3_raw_data: "type_defs.ListUsageForLicenseConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LicenseConfigurationUsageList(self):  # pragma: no cover
        return LicenseConfigurationUsage.make_many(
            self.boto3_raw_data["LicenseConfigurationUsageList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUsageForLicenseConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageForLicenseConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConversionContextOutput:
    boto3_raw_data: "type_defs.LicenseConversionContextOutputTypeDef" = (
        dataclasses.field()
    )

    UsageOperation = field("UsageOperation")

    @cached_property
    def ProductCodes(self):  # pragma: no cover
        return ProductCodeListItem.make_many(self.boto3_raw_data["ProductCodes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LicenseConversionContextOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConversionContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConversionContext:
    boto3_raw_data: "type_defs.LicenseConversionContextTypeDef" = dataclasses.field()

    UsageOperation = field("UsageOperation")

    @cached_property
    def ProductCodes(self):  # pragma: no cover
        return ProductCodeListItem.make_many(self.boto3_raw_data["ProductCodes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseConversionContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConversionContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseSpecificationsForResourceResponse:
    boto3_raw_data: "type_defs.ListLicenseSpecificationsForResourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LicenseSpecifications(self):  # pragma: no cover
        return LicenseSpecification.make_many(
            self.boto3_raw_data["LicenseSpecifications"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseSpecificationsForResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseSpecificationsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLicenseSpecificationsForResourceRequest:
    boto3_raw_data: "type_defs.UpdateLicenseSpecificationsForResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def AddLicenseSpecifications(self):  # pragma: no cover
        return LicenseSpecification.make_many(
            self.boto3_raw_data["AddLicenseSpecifications"]
        )

    @cached_property
    def RemoveLicenseSpecifications(self):  # pragma: no cover
        return LicenseSpecification.make_many(
            self.boto3_raw_data["RemoveLicenseSpecifications"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLicenseSpecificationsForResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLicenseSpecificationsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationsForLicenseConfigurationRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAssociationsForLicenseConfigurationRequestPaginateTypeDef"
    ) = dataclasses.field()

    LicenseConfigurationArn = field("LicenseConfigurationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociationsForLicenseConfigurationRequestPaginateTypeDef"
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
                "type_defs.ListAssociationsForLicenseConfigurationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListLicenseConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArns = field("LicenseConfigurationArns")

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
            "type_defs.ListLicenseConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseSpecificationsForResourceRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListLicenseSpecificationsForResourceRequestPaginateTypeDef"
    ) = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseSpecificationsForResourceRequestPaginateTypeDef"
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
                "type_defs.ListLicenseSpecificationsForResourceRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceInventoryRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceInventoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return InventoryFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceInventoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceInventoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageForLicenseConfigurationRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListUsageForLicenseConfigurationRequestPaginateTypeDef"
    ) = dataclasses.field()

    LicenseConfigurationArn = field("LicenseConfigurationArn")

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
            "type_defs.ListUsageForLicenseConfigurationRequestPaginateTypeDef"
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
                "type_defs.ListUsageForLicenseConfigurationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceInventoryResponse:
    boto3_raw_data: "type_defs.ListResourceInventoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceInventoryList(self):  # pragma: no cover
        return ResourceInventory.make_many(self.boto3_raw_data["ResourceInventoryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceInventoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceInventoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTokensResponse:
    boto3_raw_data: "type_defs.ListTokensResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tokens(self):  # pragma: no cover
        return TokenData.make_many(self.boto3_raw_data["Tokens"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTokensResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTokensResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductInformationOutput:
    boto3_raw_data: "type_defs.ProductInformationOutputTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")

    @cached_property
    def ProductInformationFilterList(self):  # pragma: no cover
        return ProductInformationFilterOutput.make_many(
            self.boto3_raw_data["ProductInformationFilterList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductInformationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductInformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportGenerator:
    boto3_raw_data: "type_defs.ReportGeneratorTypeDef" = dataclasses.field()

    ReportGeneratorName = field("ReportGeneratorName")
    ReportType = field("ReportType")

    @cached_property
    def ReportContext(self):  # pragma: no cover
        return ReportContextOutput.make_one(self.boto3_raw_data["ReportContext"])

    @cached_property
    def ReportFrequency(self):  # pragma: no cover
        return ReportFrequency.make_one(self.boto3_raw_data["ReportFrequency"])

    LicenseManagerReportGeneratorArn = field("LicenseManagerReportGeneratorArn")
    LastRunStatus = field("LastRunStatus")
    LastRunFailureReason = field("LastRunFailureReason")
    LastReportGenerationTime = field("LastReportGenerationTime")
    ReportCreatorAccount = field("ReportCreatorAccount")
    Description = field("Description")

    @cached_property
    def S3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["S3Location"])

    CreateTime = field("CreateTime")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportGeneratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportGeneratorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFailuresForLicenseConfigurationOperationsResponse:
    boto3_raw_data: (
        "type_defs.ListFailuresForLicenseConfigurationOperationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def LicenseOperationFailureList(self):  # pragma: no cover
        return LicenseOperationFailure.make_many(
            self.boto3_raw_data["LicenseOperationFailureList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFailuresForLicenseConfigurationOperationsResponseTypeDef"
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
                "type_defs.ListFailuresForLicenseConfigurationOperationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseRequest:
    boto3_raw_data: "type_defs.CreateLicenseRequestTypeDef" = dataclasses.field()

    LicenseName = field("LicenseName")
    ProductName = field("ProductName")
    ProductSKU = field("ProductSKU")

    @cached_property
    def Issuer(self):  # pragma: no cover
        return Issuer.make_one(self.boto3_raw_data["Issuer"])

    HomeRegion = field("HomeRegion")

    @cached_property
    def Validity(self):  # pragma: no cover
        return DatetimeRange.make_one(self.boto3_raw_data["Validity"])

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    Beneficiary = field("Beneficiary")

    @cached_property
    def ConsumptionConfiguration(self):  # pragma: no cover
        return ConsumptionConfiguration.make_one(
            self.boto3_raw_data["ConsumptionConfiguration"]
        )

    ClientToken = field("ClientToken")

    @cached_property
    def LicenseMetadata(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["LicenseMetadata"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLicenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseVersionRequest:
    boto3_raw_data: "type_defs.CreateLicenseVersionRequestTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    LicenseName = field("LicenseName")
    ProductName = field("ProductName")

    @cached_property
    def Issuer(self):  # pragma: no cover
        return Issuer.make_one(self.boto3_raw_data["Issuer"])

    HomeRegion = field("HomeRegion")

    @cached_property
    def Validity(self):  # pragma: no cover
        return DatetimeRange.make_one(self.boto3_raw_data["Validity"])

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    @cached_property
    def ConsumptionConfiguration(self):  # pragma: no cover
        return ConsumptionConfiguration.make_one(
            self.boto3_raw_data["ConsumptionConfiguration"]
        )

    Status = field("Status")
    ClientToken = field("ClientToken")

    @cached_property
    def LicenseMetadata(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["LicenseMetadata"])

    SourceVersion = field("SourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLicenseVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantedLicense:
    boto3_raw_data: "type_defs.GrantedLicenseTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    LicenseName = field("LicenseName")
    ProductName = field("ProductName")
    ProductSKU = field("ProductSKU")

    @cached_property
    def Issuer(self):  # pragma: no cover
        return IssuerDetails.make_one(self.boto3_raw_data["Issuer"])

    HomeRegion = field("HomeRegion")
    Status = field("Status")

    @cached_property
    def Validity(self):  # pragma: no cover
        return DatetimeRange.make_one(self.boto3_raw_data["Validity"])

    Beneficiary = field("Beneficiary")

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    @cached_property
    def ConsumptionConfiguration(self):  # pragma: no cover
        return ConsumptionConfiguration.make_one(
            self.boto3_raw_data["ConsumptionConfiguration"]
        )

    @cached_property
    def LicenseMetadata(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["LicenseMetadata"])

    CreateTime = field("CreateTime")
    Version = field("Version")

    @cached_property
    def ReceivedMetadata(self):  # pragma: no cover
        return ReceivedMetadata.make_one(self.boto3_raw_data["ReceivedMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantedLicenseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantedLicenseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class License:
    boto3_raw_data: "type_defs.LicenseTypeDef" = dataclasses.field()

    LicenseArn = field("LicenseArn")
    LicenseName = field("LicenseName")
    ProductName = field("ProductName")
    ProductSKU = field("ProductSKU")

    @cached_property
    def Issuer(self):  # pragma: no cover
        return IssuerDetails.make_one(self.boto3_raw_data["Issuer"])

    HomeRegion = field("HomeRegion")
    Status = field("Status")

    @cached_property
    def Validity(self):  # pragma: no cover
        return DatetimeRange.make_one(self.boto3_raw_data["Validity"])

    Beneficiary = field("Beneficiary")

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    @cached_property
    def ConsumptionConfiguration(self):  # pragma: no cover
        return ConsumptionConfiguration.make_one(
            self.boto3_raw_data["ConsumptionConfiguration"]
        )

    @cached_property
    def LicenseMetadata(self):  # pragma: no cover
        return Metadata.make_many(self.boto3_raw_data["LicenseMetadata"])

    CreateTime = field("CreateTime")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicenseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicenseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGrantResponse:
    boto3_raw_data: "type_defs.GetGrantResponseTypeDef" = dataclasses.field()

    @cached_property
    def Grant(self):  # pragma: no cover
        return Grant.make_one(self.boto3_raw_data["Grant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGrantResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributedGrantsResponse:
    boto3_raw_data: "type_defs.ListDistributedGrantsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Grants(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["Grants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDistributedGrantsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributedGrantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedGrantsForOrganizationResponse:
    boto3_raw_data: "type_defs.ListReceivedGrantsForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Grants(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["Grants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReceivedGrantsForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedGrantsForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedGrantsResponse:
    boto3_raw_data: "type_defs.ListReceivedGrantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Grants(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["Grants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceivedGrantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedGrantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseUsageResponse:
    boto3_raw_data: "type_defs.GetLicenseUsageResponseTypeDef" = dataclasses.field()

    @cached_property
    def LicenseUsage(self):  # pragma: no cover
        return LicenseUsage.make_one(self.boto3_raw_data["LicenseUsage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLicenseUsageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseConversionTaskResponse:
    boto3_raw_data: "type_defs.GetLicenseConversionTaskResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseConversionTaskId = field("LicenseConversionTaskId")
    ResourceArn = field("ResourceArn")

    @cached_property
    def SourceLicenseContext(self):  # pragma: no cover
        return LicenseConversionContextOutput.make_one(
            self.boto3_raw_data["SourceLicenseContext"]
        )

    @cached_property
    def DestinationLicenseContext(self):  # pragma: no cover
        return LicenseConversionContextOutput.make_one(
            self.boto3_raw_data["DestinationLicenseContext"]
        )

    StatusMessage = field("StatusMessage")
    Status = field("Status")
    StartTime = field("StartTime")
    LicenseConversionTime = field("LicenseConversionTime")
    EndTime = field("EndTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLicenseConversionTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseConversionTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConversionTask:
    boto3_raw_data: "type_defs.LicenseConversionTaskTypeDef" = dataclasses.field()

    LicenseConversionTaskId = field("LicenseConversionTaskId")
    ResourceArn = field("ResourceArn")

    @cached_property
    def SourceLicenseContext(self):  # pragma: no cover
        return LicenseConversionContextOutput.make_one(
            self.boto3_raw_data["SourceLicenseContext"]
        )

    @cached_property
    def DestinationLicenseContext(self):  # pragma: no cover
        return LicenseConversionContextOutput.make_one(
            self.boto3_raw_data["DestinationLicenseContext"]
        )

    Status = field("Status")
    StatusMessage = field("StatusMessage")
    StartTime = field("StartTime")
    LicenseConversionTime = field("LicenseConversionTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseConversionTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConversionTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseConfigurationResponse:
    boto3_raw_data: "type_defs.GetLicenseConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationId = field("LicenseConfigurationId")
    LicenseConfigurationArn = field("LicenseConfigurationArn")
    Name = field("Name")
    Description = field("Description")
    LicenseCountingType = field("LicenseCountingType")
    LicenseRules = field("LicenseRules")
    LicenseCount = field("LicenseCount")
    LicenseCountHardLimit = field("LicenseCountHardLimit")
    ConsumedLicenses = field("ConsumedLicenses")
    Status = field("Status")
    OwnerAccountId = field("OwnerAccountId")

    @cached_property
    def ConsumedLicenseSummaryList(self):  # pragma: no cover
        return ConsumedLicenseSummary.make_many(
            self.boto3_raw_data["ConsumedLicenseSummaryList"]
        )

    @cached_property
    def ManagedResourceSummaryList(self):  # pragma: no cover
        return ManagedResourceSummary.make_many(
            self.boto3_raw_data["ManagedResourceSummaryList"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ProductInformationList(self):  # pragma: no cover
        return ProductInformationOutput.make_many(
            self.boto3_raw_data["ProductInformationList"]
        )

    @cached_property
    def AutomatedDiscoveryInformation(self):  # pragma: no cover
        return AutomatedDiscoveryInformation.make_one(
            self.boto3_raw_data["AutomatedDiscoveryInformation"]
        )

    DisassociateWhenNotFound = field("DisassociateWhenNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLicenseConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConfiguration:
    boto3_raw_data: "type_defs.LicenseConfigurationTypeDef" = dataclasses.field()

    LicenseConfigurationId = field("LicenseConfigurationId")
    LicenseConfigurationArn = field("LicenseConfigurationArn")
    Name = field("Name")
    Description = field("Description")
    LicenseCountingType = field("LicenseCountingType")
    LicenseRules = field("LicenseRules")
    LicenseCount = field("LicenseCount")
    LicenseCountHardLimit = field("LicenseCountHardLimit")
    DisassociateWhenNotFound = field("DisassociateWhenNotFound")
    ConsumedLicenses = field("ConsumedLicenses")
    Status = field("Status")
    OwnerAccountId = field("OwnerAccountId")

    @cached_property
    def ConsumedLicenseSummaryList(self):  # pragma: no cover
        return ConsumedLicenseSummary.make_many(
            self.boto3_raw_data["ConsumedLicenseSummaryList"]
        )

    @cached_property
    def ManagedResourceSummaryList(self):  # pragma: no cover
        return ManagedResourceSummary.make_many(
            self.boto3_raw_data["ManagedResourceSummaryList"]
        )

    @cached_property
    def ProductInformationList(self):  # pragma: no cover
        return ProductInformationOutput.make_many(
            self.boto3_raw_data["ProductInformationList"]
        )

    @cached_property
    def AutomatedDiscoveryInformation(self):  # pragma: no cover
        return AutomatedDiscoveryInformation.make_one(
            self.boto3_raw_data["AutomatedDiscoveryInformation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductInformation:
    boto3_raw_data: "type_defs.ProductInformationTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ProductInformationFilterList = field("ProductInformationFilterList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseManagerReportGeneratorRequest:
    boto3_raw_data: "type_defs.CreateLicenseManagerReportGeneratorRequestTypeDef" = (
        dataclasses.field()
    )

    ReportGeneratorName = field("ReportGeneratorName")
    Type = field("Type")
    ReportContext = field("ReportContext")

    @cached_property
    def ReportFrequency(self):  # pragma: no cover
        return ReportFrequency.make_one(self.boto3_raw_data["ReportFrequency"])

    ClientToken = field("ClientToken")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseManagerReportGeneratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseManagerReportGeneratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLicenseManagerReportGeneratorRequest:
    boto3_raw_data: "type_defs.UpdateLicenseManagerReportGeneratorRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseManagerReportGeneratorArn = field("LicenseManagerReportGeneratorArn")
    ReportGeneratorName = field("ReportGeneratorName")
    Type = field("Type")
    ReportContext = field("ReportContext")

    @cached_property
    def ReportFrequency(self):  # pragma: no cover
        return ReportFrequency.make_one(self.boto3_raw_data["ReportFrequency"])

    ClientToken = field("ClientToken")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLicenseManagerReportGeneratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLicenseManagerReportGeneratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseManagerReportGeneratorResponse:
    boto3_raw_data: "type_defs.GetLicenseManagerReportGeneratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReportGenerator(self):  # pragma: no cover
        return ReportGenerator.make_one(self.boto3_raw_data["ReportGenerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLicenseManagerReportGeneratorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseManagerReportGeneratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseManagerReportGeneratorsResponse:
    boto3_raw_data: "type_defs.ListLicenseManagerReportGeneratorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReportGenerators(self):  # pragma: no cover
        return ReportGenerator.make_many(self.boto3_raw_data["ReportGenerators"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseManagerReportGeneratorsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseManagerReportGeneratorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedLicensesForOrganizationResponse:
    boto3_raw_data: "type_defs.ListReceivedLicensesForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Licenses(self):  # pragma: no cover
        return GrantedLicense.make_many(self.boto3_raw_data["Licenses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReceivedLicensesForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedLicensesForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedLicensesResponse:
    boto3_raw_data: "type_defs.ListReceivedLicensesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Licenses(self):  # pragma: no cover
        return GrantedLicense.make_many(self.boto3_raw_data["Licenses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReceivedLicensesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedLicensesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseResponse:
    boto3_raw_data: "type_defs.GetLicenseResponseTypeDef" = dataclasses.field()

    @cached_property
    def License(self):  # pragma: no cover
        return License.make_one(self.boto3_raw_data["License"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLicenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseVersionsResponse:
    boto3_raw_data: "type_defs.ListLicenseVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Licenses(self):  # pragma: no cover
        return License.make_many(self.boto3_raw_data["Licenses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLicenseVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicensesResponse:
    boto3_raw_data: "type_defs.ListLicensesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Licenses(self):  # pragma: no cover
        return License.make_many(self.boto3_raw_data["Licenses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLicensesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicensesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseConversionTasksResponse:
    boto3_raw_data: "type_defs.ListLicenseConversionTasksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LicenseConversionTasks(self):  # pragma: no cover
        return LicenseConversionTask.make_many(
            self.boto3_raw_data["LicenseConversionTasks"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseConversionTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseConversionTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseConversionTaskForResourceRequest:
    boto3_raw_data: "type_defs.CreateLicenseConversionTaskForResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    SourceLicenseContext = field("SourceLicenseContext")
    DestinationLicenseContext = field("DestinationLicenseContext")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseConversionTaskForResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseConversionTaskForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseConfigurationsResponse:
    boto3_raw_data: "type_defs.ListLicenseConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LicenseConfigurations(self):  # pragma: no cover
        return LicenseConfiguration.make_many(
            self.boto3_raw_data["LicenseConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseConfigurationRequest:
    boto3_raw_data: "type_defs.CreateLicenseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    LicenseCountingType = field("LicenseCountingType")
    Description = field("Description")
    LicenseCount = field("LicenseCount")
    LicenseCountHardLimit = field("LicenseCountHardLimit")
    LicenseRules = field("LicenseRules")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DisassociateWhenNotFound = field("DisassociateWhenNotFound")
    ProductInformationList = field("ProductInformationList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLicenseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLicenseConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateLicenseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    LicenseConfigurationArn = field("LicenseConfigurationArn")
    LicenseConfigurationStatus = field("LicenseConfigurationStatus")
    LicenseRules = field("LicenseRules")
    LicenseCount = field("LicenseCount")
    LicenseCountHardLimit = field("LicenseCountHardLimit")
    Name = field("Name")
    Description = field("Description")
    ProductInformationList = field("ProductInformationList")
    DisassociateWhenNotFound = field("DisassociateWhenNotFound")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLicenseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLicenseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
