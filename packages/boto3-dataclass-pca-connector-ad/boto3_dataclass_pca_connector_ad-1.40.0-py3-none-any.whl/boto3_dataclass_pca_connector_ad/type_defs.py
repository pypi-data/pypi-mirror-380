# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pca_connector_ad import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessRights:
    boto3_raw_data: "type_defs.AccessRightsTypeDef" = dataclasses.field()

    AutoEnroll = field("AutoEnroll")
    Enroll = field("Enroll")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessRightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessRightsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationPolicy:
    boto3_raw_data: "type_defs.ApplicationPolicyTypeDef" = dataclasses.field()

    PolicyObjectIdentifier = field("PolicyObjectIdentifier")
    PolicyType = field("PolicyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidityPeriod:
    boto3_raw_data: "type_defs.ValidityPeriodTypeDef" = dataclasses.field()

    Period = field("Period")
    PeriodType = field("PeriodType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidityPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidityPeriodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcInformationOutput:
    boto3_raw_data: "type_defs.VpcInformationOutputTypeDef" = dataclasses.field()

    SecurityGroupIds = field("SecurityGroupIds")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcInformationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcInformationOutputTypeDef"]
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
class CreateDirectoryRegistrationRequest:
    boto3_raw_data: "type_defs.CreateDirectoryRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectoryRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServicePrincipalNameRequest:
    boto3_raw_data: "type_defs.CreateServicePrincipalNameRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorArn = field("ConnectorArn")
    DirectoryRegistrationArn = field("DirectoryRegistrationArn")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServicePrincipalNameRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServicePrincipalNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectorRequest:
    boto3_raw_data: "type_defs.DeleteConnectorRequestTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectoryRegistrationRequest:
    boto3_raw_data: "type_defs.DeleteDirectoryRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryRegistrationArn = field("DirectoryRegistrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectoryRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectoryRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServicePrincipalNameRequest:
    boto3_raw_data: "type_defs.DeleteServicePrincipalNameRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorArn = field("ConnectorArn")
    DirectoryRegistrationArn = field("DirectoryRegistrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServicePrincipalNameRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServicePrincipalNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateGroupAccessControlEntryRequest:
    boto3_raw_data: "type_defs.DeleteTemplateGroupAccessControlEntryRequestTypeDef" = (
        dataclasses.field()
    )

    GroupSecurityIdentifier = field("GroupSecurityIdentifier")
    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTemplateGroupAccessControlEntryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateGroupAccessControlEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateRequest:
    boto3_raw_data: "type_defs.DeleteTemplateRequestTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryRegistrationSummary:
    boto3_raw_data: "type_defs.DirectoryRegistrationSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    DirectoryId = field("DirectoryId")
    Status = field("Status")
    StatusReason = field("StatusReason")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectoryRegistrationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryRegistrationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryRegistration:
    boto3_raw_data: "type_defs.DirectoryRegistrationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    DirectoryId = field("DirectoryId")
    Status = field("Status")
    StatusReason = field("StatusReason")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectoryRegistrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryRegistrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentFlagsV2:
    boto3_raw_data: "type_defs.EnrollmentFlagsV2TypeDef" = dataclasses.field()

    EnableKeyReuseOnNtTokenKeysetStorageFull = field(
        "EnableKeyReuseOnNtTokenKeysetStorageFull"
    )
    IncludeSymmetricAlgorithms = field("IncludeSymmetricAlgorithms")
    NoSecurityExtension = field("NoSecurityExtension")
    RemoveInvalidCertificateFromPersonalStore = field(
        "RemoveInvalidCertificateFromPersonalStore"
    )
    UserInteractionRequired = field("UserInteractionRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnrollmentFlagsV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentFlagsV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentFlagsV3:
    boto3_raw_data: "type_defs.EnrollmentFlagsV3TypeDef" = dataclasses.field()

    EnableKeyReuseOnNtTokenKeysetStorageFull = field(
        "EnableKeyReuseOnNtTokenKeysetStorageFull"
    )
    IncludeSymmetricAlgorithms = field("IncludeSymmetricAlgorithms")
    NoSecurityExtension = field("NoSecurityExtension")
    RemoveInvalidCertificateFromPersonalStore = field(
        "RemoveInvalidCertificateFromPersonalStore"
    )
    UserInteractionRequired = field("UserInteractionRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnrollmentFlagsV3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentFlagsV3TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentFlagsV4:
    boto3_raw_data: "type_defs.EnrollmentFlagsV4TypeDef" = dataclasses.field()

    EnableKeyReuseOnNtTokenKeysetStorageFull = field(
        "EnableKeyReuseOnNtTokenKeysetStorageFull"
    )
    IncludeSymmetricAlgorithms = field("IncludeSymmetricAlgorithms")
    NoSecurityExtension = field("NoSecurityExtension")
    RemoveInvalidCertificateFromPersonalStore = field(
        "RemoveInvalidCertificateFromPersonalStore"
    )
    UserInteractionRequired = field("UserInteractionRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnrollmentFlagsV4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentFlagsV4TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneralFlagsV2:
    boto3_raw_data: "type_defs.GeneralFlagsV2TypeDef" = dataclasses.field()

    AutoEnrollment = field("AutoEnrollment")
    MachineType = field("MachineType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneralFlagsV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeneralFlagsV2TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneralFlagsV3:
    boto3_raw_data: "type_defs.GeneralFlagsV3TypeDef" = dataclasses.field()

    AutoEnrollment = field("AutoEnrollment")
    MachineType = field("MachineType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneralFlagsV3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeneralFlagsV3TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneralFlagsV4:
    boto3_raw_data: "type_defs.GeneralFlagsV4TypeDef" = dataclasses.field()

    AutoEnrollment = field("AutoEnrollment")
    MachineType = field("MachineType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneralFlagsV4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeneralFlagsV4TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorRequest:
    boto3_raw_data: "type_defs.GetConnectorRequestTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectoryRegistrationRequest:
    boto3_raw_data: "type_defs.GetDirectoryRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryRegistrationArn = field("DirectoryRegistrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDirectoryRegistrationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectoryRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServicePrincipalNameRequest:
    boto3_raw_data: "type_defs.GetServicePrincipalNameRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorArn = field("ConnectorArn")
    DirectoryRegistrationArn = field("DirectoryRegistrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServicePrincipalNameRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServicePrincipalNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServicePrincipalName:
    boto3_raw_data: "type_defs.ServicePrincipalNameTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")
    CreatedAt = field("CreatedAt")
    DirectoryRegistrationArn = field("DirectoryRegistrationArn")
    Status = field("Status")
    StatusReason = field("StatusReason")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServicePrincipalNameTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServicePrincipalNameTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateGroupAccessControlEntryRequest:
    boto3_raw_data: "type_defs.GetTemplateGroupAccessControlEntryRequestTypeDef" = (
        dataclasses.field()
    )

    GroupSecurityIdentifier = field("GroupSecurityIdentifier")
    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTemplateGroupAccessControlEntryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateGroupAccessControlEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateRequest:
    boto3_raw_data: "type_defs.GetTemplateRequestTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyUsageFlags:
    boto3_raw_data: "type_defs.KeyUsageFlagsTypeDef" = dataclasses.field()

    DataEncipherment = field("DataEncipherment")
    DigitalSignature = field("DigitalSignature")
    KeyAgreement = field("KeyAgreement")
    KeyEncipherment = field("KeyEncipherment")
    NonRepudiation = field("NonRepudiation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyUsageFlagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyUsageFlagsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyUsagePropertyFlags:
    boto3_raw_data: "type_defs.KeyUsagePropertyFlagsTypeDef" = dataclasses.field()

    Decrypt = field("Decrypt")
    KeyAgreement = field("KeyAgreement")
    Sign = field("Sign")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyUsagePropertyFlagsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyUsagePropertyFlagsTypeDef"]
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
class ListConnectorsRequest:
    boto3_raw_data: "type_defs.ListConnectorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoryRegistrationsRequest:
    boto3_raw_data: "type_defs.ListDirectoryRegistrationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDirectoryRegistrationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoryRegistrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePrincipalNamesRequest:
    boto3_raw_data: "type_defs.ListServicePrincipalNamesRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryRegistrationArn = field("DirectoryRegistrationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServicePrincipalNamesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePrincipalNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServicePrincipalNameSummary:
    boto3_raw_data: "type_defs.ServicePrincipalNameSummaryTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")
    CreatedAt = field("CreatedAt")
    DirectoryRegistrationArn = field("DirectoryRegistrationArn")
    Status = field("Status")
    StatusReason = field("StatusReason")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServicePrincipalNameSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServicePrincipalNameSummaryTypeDef"]
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
class ListTemplateGroupAccessControlEntriesRequest:
    boto3_raw_data: "type_defs.ListTemplateGroupAccessControlEntriesRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTemplateGroupAccessControlEntriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateGroupAccessControlEntriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplatesRequest:
    boto3_raw_data: "type_defs.ListTemplatesRequestTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyAttributesV2Output:
    boto3_raw_data: "type_defs.PrivateKeyAttributesV2OutputTypeDef" = (
        dataclasses.field()
    )

    KeySpec = field("KeySpec")
    MinimalKeyLength = field("MinimalKeyLength")
    CryptoProviders = field("CryptoProviders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyAttributesV2OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyAttributesV2OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyAttributesV2:
    boto3_raw_data: "type_defs.PrivateKeyAttributesV2TypeDef" = dataclasses.field()

    KeySpec = field("KeySpec")
    MinimalKeyLength = field("MinimalKeyLength")
    CryptoProviders = field("CryptoProviders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyAttributesV2TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyAttributesV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyFlagsV2:
    boto3_raw_data: "type_defs.PrivateKeyFlagsV2TypeDef" = dataclasses.field()

    ClientVersion = field("ClientVersion")
    ExportableKey = field("ExportableKey")
    StrongKeyProtectionRequired = field("StrongKeyProtectionRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyFlagsV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyFlagsV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyFlagsV3:
    boto3_raw_data: "type_defs.PrivateKeyFlagsV3TypeDef" = dataclasses.field()

    ClientVersion = field("ClientVersion")
    ExportableKey = field("ExportableKey")
    RequireAlternateSignatureAlgorithm = field("RequireAlternateSignatureAlgorithm")
    StrongKeyProtectionRequired = field("StrongKeyProtectionRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyFlagsV3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyFlagsV3TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyFlagsV4:
    boto3_raw_data: "type_defs.PrivateKeyFlagsV4TypeDef" = dataclasses.field()

    ClientVersion = field("ClientVersion")
    ExportableKey = field("ExportableKey")
    RequireAlternateSignatureAlgorithm = field("RequireAlternateSignatureAlgorithm")
    RequireSameKeyRenewal = field("RequireSameKeyRenewal")
    StrongKeyProtectionRequired = field("StrongKeyProtectionRequired")
    UseLegacyProvider = field("UseLegacyProvider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyFlagsV4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyFlagsV4TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectNameFlagsV2:
    boto3_raw_data: "type_defs.SubjectNameFlagsV2TypeDef" = dataclasses.field()

    RequireCommonName = field("RequireCommonName")
    RequireDirectoryPath = field("RequireDirectoryPath")
    RequireDnsAsCn = field("RequireDnsAsCn")
    RequireEmail = field("RequireEmail")
    SanRequireDirectoryGuid = field("SanRequireDirectoryGuid")
    SanRequireDns = field("SanRequireDns")
    SanRequireDomainDns = field("SanRequireDomainDns")
    SanRequireEmail = field("SanRequireEmail")
    SanRequireSpn = field("SanRequireSpn")
    SanRequireUpn = field("SanRequireUpn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubjectNameFlagsV2TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectNameFlagsV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectNameFlagsV3:
    boto3_raw_data: "type_defs.SubjectNameFlagsV3TypeDef" = dataclasses.field()

    RequireCommonName = field("RequireCommonName")
    RequireDirectoryPath = field("RequireDirectoryPath")
    RequireDnsAsCn = field("RequireDnsAsCn")
    RequireEmail = field("RequireEmail")
    SanRequireDirectoryGuid = field("SanRequireDirectoryGuid")
    SanRequireDns = field("SanRequireDns")
    SanRequireDomainDns = field("SanRequireDomainDns")
    SanRequireEmail = field("SanRequireEmail")
    SanRequireSpn = field("SanRequireSpn")
    SanRequireUpn = field("SanRequireUpn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubjectNameFlagsV3TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectNameFlagsV3TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectNameFlagsV4:
    boto3_raw_data: "type_defs.SubjectNameFlagsV4TypeDef" = dataclasses.field()

    RequireCommonName = field("RequireCommonName")
    RequireDirectoryPath = field("RequireDirectoryPath")
    RequireDnsAsCn = field("RequireDnsAsCn")
    RequireEmail = field("RequireEmail")
    SanRequireDirectoryGuid = field("SanRequireDirectoryGuid")
    SanRequireDns = field("SanRequireDns")
    SanRequireDomainDns = field("SanRequireDomainDns")
    SanRequireEmail = field("SanRequireEmail")
    SanRequireSpn = field("SanRequireSpn")
    SanRequireUpn = field("SanRequireUpn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubjectNameFlagsV4TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectNameFlagsV4TypeDef"]
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
class TemplateRevision:
    boto3_raw_data: "type_defs.TemplateRevisionTypeDef" = dataclasses.field()

    MajorRevision = field("MajorRevision")
    MinorRevision = field("MinorRevision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateRevisionTypeDef"]
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
class VpcInformation:
    boto3_raw_data: "type_defs.VpcInformationTypeDef" = dataclasses.field()

    SecurityGroupIds = field("SecurityGroupIds")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcInformationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlEntrySummary:
    boto3_raw_data: "type_defs.AccessControlEntrySummaryTypeDef" = dataclasses.field()

    @cached_property
    def AccessRights(self):  # pragma: no cover
        return AccessRights.make_one(self.boto3_raw_data["AccessRights"])

    CreatedAt = field("CreatedAt")
    GroupDisplayName = field("GroupDisplayName")
    GroupSecurityIdentifier = field("GroupSecurityIdentifier")
    TemplateArn = field("TemplateArn")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlEntrySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlEntrySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlEntry:
    boto3_raw_data: "type_defs.AccessControlEntryTypeDef" = dataclasses.field()

    @cached_property
    def AccessRights(self):  # pragma: no cover
        return AccessRights.make_one(self.boto3_raw_data["AccessRights"])

    CreatedAt = field("CreatedAt")
    GroupDisplayName = field("GroupDisplayName")
    GroupSecurityIdentifier = field("GroupSecurityIdentifier")
    TemplateArn = field("TemplateArn")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateGroupAccessControlEntryRequest:
    boto3_raw_data: "type_defs.CreateTemplateGroupAccessControlEntryRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessRights(self):  # pragma: no cover
        return AccessRights.make_one(self.boto3_raw_data["AccessRights"])

    GroupDisplayName = field("GroupDisplayName")
    GroupSecurityIdentifier = field("GroupSecurityIdentifier")
    TemplateArn = field("TemplateArn")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTemplateGroupAccessControlEntryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateGroupAccessControlEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateGroupAccessControlEntryRequest:
    boto3_raw_data: "type_defs.UpdateTemplateGroupAccessControlEntryRequestTypeDef" = (
        dataclasses.field()
    )

    GroupSecurityIdentifier = field("GroupSecurityIdentifier")
    TemplateArn = field("TemplateArn")

    @cached_property
    def AccessRights(self):  # pragma: no cover
        return AccessRights.make_one(self.boto3_raw_data["AccessRights"])

    GroupDisplayName = field("GroupDisplayName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTemplateGroupAccessControlEntryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateGroupAccessControlEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationPoliciesOutput:
    boto3_raw_data: "type_defs.ApplicationPoliciesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Policies(self):  # pragma: no cover
        return ApplicationPolicy.make_many(self.boto3_raw_data["Policies"])

    Critical = field("Critical")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationPoliciesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationPolicies:
    boto3_raw_data: "type_defs.ApplicationPoliciesTypeDef" = dataclasses.field()

    @cached_property
    def Policies(self):  # pragma: no cover
        return ApplicationPolicy.make_many(self.boto3_raw_data["Policies"])

    Critical = field("Critical")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationPoliciesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationPoliciesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateValidity:
    boto3_raw_data: "type_defs.CertificateValidityTypeDef" = dataclasses.field()

    @cached_property
    def RenewalPeriod(self):  # pragma: no cover
        return ValidityPeriod.make_one(self.boto3_raw_data["RenewalPeriod"])

    @cached_property
    def ValidityPeriod(self):  # pragma: no cover
        return ValidityPeriod.make_one(self.boto3_raw_data["ValidityPeriod"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateValidityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateValidityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorSummary:
    boto3_raw_data: "type_defs.ConnectorSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CertificateAuthorityArn = field("CertificateAuthorityArn")
    CertificateEnrollmentPolicyServerEndpoint = field(
        "CertificateEnrollmentPolicyServerEndpoint"
    )
    CreatedAt = field("CreatedAt")
    DirectoryId = field("DirectoryId")
    Status = field("Status")
    StatusReason = field("StatusReason")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def VpcInformation(self):  # pragma: no cover
        return VpcInformationOutput.make_one(self.boto3_raw_data["VpcInformation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connector:
    boto3_raw_data: "type_defs.ConnectorTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CertificateAuthorityArn = field("CertificateAuthorityArn")
    CertificateEnrollmentPolicyServerEndpoint = field(
        "CertificateEnrollmentPolicyServerEndpoint"
    )
    CreatedAt = field("CreatedAt")
    DirectoryId = field("DirectoryId")
    Status = field("Status")
    StatusReason = field("StatusReason")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def VpcInformation(self):  # pragma: no cover
        return VpcInformationOutput.make_one(self.boto3_raw_data["VpcInformation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorResponse:
    boto3_raw_data: "type_defs.CreateConnectorResponseTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryRegistrationResponse:
    boto3_raw_data: "type_defs.CreateDirectoryRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    DirectoryRegistrationArn = field("DirectoryRegistrationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectoryRegistrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateResponse:
    boto3_raw_data: "type_defs.CreateTemplateResponseTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
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
class ListDirectoryRegistrationsResponse:
    boto3_raw_data: "type_defs.ListDirectoryRegistrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectoryRegistrations(self):  # pragma: no cover
        return DirectoryRegistrationSummary.make_many(
            self.boto3_raw_data["DirectoryRegistrations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDirectoryRegistrationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoryRegistrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectoryRegistrationResponse:
    boto3_raw_data: "type_defs.GetDirectoryRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectoryRegistration(self):  # pragma: no cover
        return DirectoryRegistration.make_one(
            self.boto3_raw_data["DirectoryRegistration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDirectoryRegistrationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectoryRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServicePrincipalNameResponse:
    boto3_raw_data: "type_defs.GetServicePrincipalNameResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServicePrincipalName(self):  # pragma: no cover
        return ServicePrincipalName.make_one(
            self.boto3_raw_data["ServicePrincipalName"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServicePrincipalNameResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServicePrincipalNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyUsage:
    boto3_raw_data: "type_defs.KeyUsageTypeDef" = dataclasses.field()

    @cached_property
    def UsageFlags(self):  # pragma: no cover
        return KeyUsageFlags.make_one(self.boto3_raw_data["UsageFlags"])

    Critical = field("Critical")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyUsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyUsageProperty:
    boto3_raw_data: "type_defs.KeyUsagePropertyTypeDef" = dataclasses.field()

    @cached_property
    def PropertyFlags(self):  # pragma: no cover
        return KeyUsagePropertyFlags.make_one(self.boto3_raw_data["PropertyFlags"])

    PropertyType = field("PropertyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyUsagePropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyUsagePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoryRegistrationsRequestPaginate:
    boto3_raw_data: "type_defs.ListDirectoryRegistrationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDirectoryRegistrationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoryRegistrationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePrincipalNamesRequestPaginate:
    boto3_raw_data: "type_defs.ListServicePrincipalNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryRegistrationArn = field("DirectoryRegistrationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicePrincipalNamesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePrincipalNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateGroupAccessControlEntriesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef"
    ) = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef"
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
                "type_defs.ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConnectorArn = field("ConnectorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePrincipalNamesResponse:
    boto3_raw_data: "type_defs.ListServicePrincipalNamesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServicePrincipalNames(self):  # pragma: no cover
        return ServicePrincipalNameSummary.make_many(
            self.boto3_raw_data["ServicePrincipalNames"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicePrincipalNamesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePrincipalNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateGroupAccessControlEntriesResponse:
    boto3_raw_data: "type_defs.ListTemplateGroupAccessControlEntriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlEntries(self):  # pragma: no cover
        return AccessControlEntrySummary.make_many(
            self.boto3_raw_data["AccessControlEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTemplateGroupAccessControlEntriesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateGroupAccessControlEntriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateGroupAccessControlEntryResponse:
    boto3_raw_data: "type_defs.GetTemplateGroupAccessControlEntryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlEntry(self):  # pragma: no cover
        return AccessControlEntry.make_one(self.boto3_raw_data["AccessControlEntry"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTemplateGroupAccessControlEntryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateGroupAccessControlEntryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsResponse:
    boto3_raw_data: "type_defs.ListConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connectors(self):  # pragma: no cover
        return ConnectorSummary.make_many(self.boto3_raw_data["Connectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorResponse:
    boto3_raw_data: "type_defs.GetConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connector(self):  # pragma: no cover
        return Connector.make_one(self.boto3_raw_data["Connector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionsV2Output:
    boto3_raw_data: "type_defs.ExtensionsV2OutputTypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def ApplicationPolicies(self):  # pragma: no cover
        return ApplicationPoliciesOutput.make_one(
            self.boto3_raw_data["ApplicationPolicies"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtensionsV2OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionsV2OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionsV2:
    boto3_raw_data: "type_defs.ExtensionsV2TypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def ApplicationPolicies(self):  # pragma: no cover
        return ApplicationPolicies.make_one(self.boto3_raw_data["ApplicationPolicies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionsV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionsV2TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionsV3Output:
    boto3_raw_data: "type_defs.ExtensionsV3OutputTypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def ApplicationPolicies(self):  # pragma: no cover
        return ApplicationPoliciesOutput.make_one(
            self.boto3_raw_data["ApplicationPolicies"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtensionsV3OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionsV3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionsV3:
    boto3_raw_data: "type_defs.ExtensionsV3TypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def ApplicationPolicies(self):  # pragma: no cover
        return ApplicationPolicies.make_one(self.boto3_raw_data["ApplicationPolicies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionsV3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionsV3TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionsV4Output:
    boto3_raw_data: "type_defs.ExtensionsV4OutputTypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def ApplicationPolicies(self):  # pragma: no cover
        return ApplicationPoliciesOutput.make_one(
            self.boto3_raw_data["ApplicationPolicies"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtensionsV4OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionsV4OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionsV4:
    boto3_raw_data: "type_defs.ExtensionsV4TypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def ApplicationPolicies(self):  # pragma: no cover
        return ApplicationPolicies.make_one(self.boto3_raw_data["ApplicationPolicies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionsV4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionsV4TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyAttributesV3Output:
    boto3_raw_data: "type_defs.PrivateKeyAttributesV3OutputTypeDef" = (
        dataclasses.field()
    )

    Algorithm = field("Algorithm")
    KeySpec = field("KeySpec")

    @cached_property
    def KeyUsageProperty(self):  # pragma: no cover
        return KeyUsageProperty.make_one(self.boto3_raw_data["KeyUsageProperty"])

    MinimalKeyLength = field("MinimalKeyLength")
    CryptoProviders = field("CryptoProviders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyAttributesV3OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyAttributesV3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyAttributesV3:
    boto3_raw_data: "type_defs.PrivateKeyAttributesV3TypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    KeySpec = field("KeySpec")

    @cached_property
    def KeyUsageProperty(self):  # pragma: no cover
        return KeyUsageProperty.make_one(self.boto3_raw_data["KeyUsageProperty"])

    MinimalKeyLength = field("MinimalKeyLength")
    CryptoProviders = field("CryptoProviders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyAttributesV3TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyAttributesV3TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyAttributesV4Output:
    boto3_raw_data: "type_defs.PrivateKeyAttributesV4OutputTypeDef" = (
        dataclasses.field()
    )

    KeySpec = field("KeySpec")
    MinimalKeyLength = field("MinimalKeyLength")
    Algorithm = field("Algorithm")
    CryptoProviders = field("CryptoProviders")

    @cached_property
    def KeyUsageProperty(self):  # pragma: no cover
        return KeyUsageProperty.make_one(self.boto3_raw_data["KeyUsageProperty"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyAttributesV4OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyAttributesV4OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateKeyAttributesV4:
    boto3_raw_data: "type_defs.PrivateKeyAttributesV4TypeDef" = dataclasses.field()

    KeySpec = field("KeySpec")
    MinimalKeyLength = field("MinimalKeyLength")
    Algorithm = field("Algorithm")
    CryptoProviders = field("CryptoProviders")

    @cached_property
    def KeyUsageProperty(self):  # pragma: no cover
        return KeyUsageProperty.make_one(self.boto3_raw_data["KeyUsageProperty"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateKeyAttributesV4TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateKeyAttributesV4TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorRequest:
    boto3_raw_data: "type_defs.CreateConnectorRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    DirectoryId = field("DirectoryId")
    VpcInformation = field("VpcInformation")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateV2Output:
    boto3_raw_data: "type_defs.TemplateV2OutputTypeDef" = dataclasses.field()

    @cached_property
    def CertificateValidity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["CertificateValidity"])

    @cached_property
    def EnrollmentFlags(self):  # pragma: no cover
        return EnrollmentFlagsV2.make_one(self.boto3_raw_data["EnrollmentFlags"])

    @cached_property
    def Extensions(self):  # pragma: no cover
        return ExtensionsV2Output.make_one(self.boto3_raw_data["Extensions"])

    @cached_property
    def GeneralFlags(self):  # pragma: no cover
        return GeneralFlagsV2.make_one(self.boto3_raw_data["GeneralFlags"])

    @cached_property
    def PrivateKeyAttributes(self):  # pragma: no cover
        return PrivateKeyAttributesV2Output.make_one(
            self.boto3_raw_data["PrivateKeyAttributes"]
        )

    @cached_property
    def PrivateKeyFlags(self):  # pragma: no cover
        return PrivateKeyFlagsV2.make_one(self.boto3_raw_data["PrivateKeyFlags"])

    @cached_property
    def SubjectNameFlags(self):  # pragma: no cover
        return SubjectNameFlagsV2.make_one(self.boto3_raw_data["SubjectNameFlags"])

    SupersededTemplates = field("SupersededTemplates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateV2OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateV2OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateV2:
    boto3_raw_data: "type_defs.TemplateV2TypeDef" = dataclasses.field()

    @cached_property
    def CertificateValidity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["CertificateValidity"])

    @cached_property
    def EnrollmentFlags(self):  # pragma: no cover
        return EnrollmentFlagsV2.make_one(self.boto3_raw_data["EnrollmentFlags"])

    @cached_property
    def Extensions(self):  # pragma: no cover
        return ExtensionsV2.make_one(self.boto3_raw_data["Extensions"])

    @cached_property
    def GeneralFlags(self):  # pragma: no cover
        return GeneralFlagsV2.make_one(self.boto3_raw_data["GeneralFlags"])

    @cached_property
    def PrivateKeyAttributes(self):  # pragma: no cover
        return PrivateKeyAttributesV2.make_one(
            self.boto3_raw_data["PrivateKeyAttributes"]
        )

    @cached_property
    def PrivateKeyFlags(self):  # pragma: no cover
        return PrivateKeyFlagsV2.make_one(self.boto3_raw_data["PrivateKeyFlags"])

    @cached_property
    def SubjectNameFlags(self):  # pragma: no cover
        return SubjectNameFlagsV2.make_one(self.boto3_raw_data["SubjectNameFlags"])

    SupersededTemplates = field("SupersededTemplates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateV2TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateV3Output:
    boto3_raw_data: "type_defs.TemplateV3OutputTypeDef" = dataclasses.field()

    @cached_property
    def CertificateValidity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["CertificateValidity"])

    @cached_property
    def EnrollmentFlags(self):  # pragma: no cover
        return EnrollmentFlagsV3.make_one(self.boto3_raw_data["EnrollmentFlags"])

    @cached_property
    def Extensions(self):  # pragma: no cover
        return ExtensionsV3Output.make_one(self.boto3_raw_data["Extensions"])

    @cached_property
    def GeneralFlags(self):  # pragma: no cover
        return GeneralFlagsV3.make_one(self.boto3_raw_data["GeneralFlags"])

    HashAlgorithm = field("HashAlgorithm")

    @cached_property
    def PrivateKeyAttributes(self):  # pragma: no cover
        return PrivateKeyAttributesV3Output.make_one(
            self.boto3_raw_data["PrivateKeyAttributes"]
        )

    @cached_property
    def PrivateKeyFlags(self):  # pragma: no cover
        return PrivateKeyFlagsV3.make_one(self.boto3_raw_data["PrivateKeyFlags"])

    @cached_property
    def SubjectNameFlags(self):  # pragma: no cover
        return SubjectNameFlagsV3.make_one(self.boto3_raw_data["SubjectNameFlags"])

    SupersededTemplates = field("SupersededTemplates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateV3OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateV3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateV3:
    boto3_raw_data: "type_defs.TemplateV3TypeDef" = dataclasses.field()

    @cached_property
    def CertificateValidity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["CertificateValidity"])

    @cached_property
    def EnrollmentFlags(self):  # pragma: no cover
        return EnrollmentFlagsV3.make_one(self.boto3_raw_data["EnrollmentFlags"])

    @cached_property
    def Extensions(self):  # pragma: no cover
        return ExtensionsV3.make_one(self.boto3_raw_data["Extensions"])

    @cached_property
    def GeneralFlags(self):  # pragma: no cover
        return GeneralFlagsV3.make_one(self.boto3_raw_data["GeneralFlags"])

    HashAlgorithm = field("HashAlgorithm")

    @cached_property
    def PrivateKeyAttributes(self):  # pragma: no cover
        return PrivateKeyAttributesV3.make_one(
            self.boto3_raw_data["PrivateKeyAttributes"]
        )

    @cached_property
    def PrivateKeyFlags(self):  # pragma: no cover
        return PrivateKeyFlagsV3.make_one(self.boto3_raw_data["PrivateKeyFlags"])

    @cached_property
    def SubjectNameFlags(self):  # pragma: no cover
        return SubjectNameFlagsV3.make_one(self.boto3_raw_data["SubjectNameFlags"])

    SupersededTemplates = field("SupersededTemplates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateV3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateV3TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateV4Output:
    boto3_raw_data: "type_defs.TemplateV4OutputTypeDef" = dataclasses.field()

    @cached_property
    def CertificateValidity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["CertificateValidity"])

    @cached_property
    def EnrollmentFlags(self):  # pragma: no cover
        return EnrollmentFlagsV4.make_one(self.boto3_raw_data["EnrollmentFlags"])

    @cached_property
    def Extensions(self):  # pragma: no cover
        return ExtensionsV4Output.make_one(self.boto3_raw_data["Extensions"])

    @cached_property
    def GeneralFlags(self):  # pragma: no cover
        return GeneralFlagsV4.make_one(self.boto3_raw_data["GeneralFlags"])

    @cached_property
    def PrivateKeyAttributes(self):  # pragma: no cover
        return PrivateKeyAttributesV4Output.make_one(
            self.boto3_raw_data["PrivateKeyAttributes"]
        )

    @cached_property
    def PrivateKeyFlags(self):  # pragma: no cover
        return PrivateKeyFlagsV4.make_one(self.boto3_raw_data["PrivateKeyFlags"])

    @cached_property
    def SubjectNameFlags(self):  # pragma: no cover
        return SubjectNameFlagsV4.make_one(self.boto3_raw_data["SubjectNameFlags"])

    HashAlgorithm = field("HashAlgorithm")
    SupersededTemplates = field("SupersededTemplates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateV4OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateV4OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateV4:
    boto3_raw_data: "type_defs.TemplateV4TypeDef" = dataclasses.field()

    @cached_property
    def CertificateValidity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["CertificateValidity"])

    @cached_property
    def EnrollmentFlags(self):  # pragma: no cover
        return EnrollmentFlagsV4.make_one(self.boto3_raw_data["EnrollmentFlags"])

    @cached_property
    def Extensions(self):  # pragma: no cover
        return ExtensionsV4.make_one(self.boto3_raw_data["Extensions"])

    @cached_property
    def GeneralFlags(self):  # pragma: no cover
        return GeneralFlagsV4.make_one(self.boto3_raw_data["GeneralFlags"])

    @cached_property
    def PrivateKeyAttributes(self):  # pragma: no cover
        return PrivateKeyAttributesV4.make_one(
            self.boto3_raw_data["PrivateKeyAttributes"]
        )

    @cached_property
    def PrivateKeyFlags(self):  # pragma: no cover
        return PrivateKeyFlagsV4.make_one(self.boto3_raw_data["PrivateKeyFlags"])

    @cached_property
    def SubjectNameFlags(self):  # pragma: no cover
        return SubjectNameFlagsV4.make_one(self.boto3_raw_data["SubjectNameFlags"])

    HashAlgorithm = field("HashAlgorithm")
    SupersededTemplates = field("SupersededTemplates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateV4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateV4TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateDefinitionOutput:
    boto3_raw_data: "type_defs.TemplateDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def TemplateV2(self):  # pragma: no cover
        return TemplateV2Output.make_one(self.boto3_raw_data["TemplateV2"])

    @cached_property
    def TemplateV3(self):  # pragma: no cover
        return TemplateV3Output.make_one(self.boto3_raw_data["TemplateV3"])

    @cached_property
    def TemplateV4(self):  # pragma: no cover
        return TemplateV4Output.make_one(self.boto3_raw_data["TemplateV4"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateDefinition:
    boto3_raw_data: "type_defs.TemplateDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def TemplateV2(self):  # pragma: no cover
        return TemplateV2.make_one(self.boto3_raw_data["TemplateV2"])

    @cached_property
    def TemplateV3(self):  # pragma: no cover
        return TemplateV3.make_one(self.boto3_raw_data["TemplateV3"])

    @cached_property
    def TemplateV4(self):  # pragma: no cover
        return TemplateV4.make_one(self.boto3_raw_data["TemplateV4"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSummary:
    boto3_raw_data: "type_defs.TemplateSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectorArn = field("ConnectorArn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Definition(self):  # pragma: no cover
        return TemplateDefinitionOutput.make_one(self.boto3_raw_data["Definition"])

    Name = field("Name")
    ObjectIdentifier = field("ObjectIdentifier")
    PolicySchema = field("PolicySchema")

    @cached_property
    def Revision(self):  # pragma: no cover
        return TemplateRevision.make_one(self.boto3_raw_data["Revision"])

    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Template:
    boto3_raw_data: "type_defs.TemplateTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectorArn = field("ConnectorArn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Definition(self):  # pragma: no cover
        return TemplateDefinitionOutput.make_one(self.boto3_raw_data["Definition"])

    Name = field("Name")
    ObjectIdentifier = field("ObjectIdentifier")
    PolicySchema = field("PolicySchema")

    @cached_property
    def Revision(self):  # pragma: no cover
        return TemplateRevision.make_one(self.boto3_raw_data["Revision"])

    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplatesResponse:
    boto3_raw_data: "type_defs.ListTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Templates(self):  # pragma: no cover
        return TemplateSummary.make_many(self.boto3_raw_data["Templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateResponse:
    boto3_raw_data: "type_defs.GetTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def Template(self):  # pragma: no cover
        return Template.make_one(self.boto3_raw_data["Template"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateRequest:
    boto3_raw_data: "type_defs.CreateTemplateRequestTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")
    Definition = field("Definition")
    Name = field("Name")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateRequest:
    boto3_raw_data: "type_defs.UpdateTemplateRequestTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")
    Definition = field("Definition")
    ReenrollAllCertificateHolders = field("ReenrollAllCertificateHolders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
