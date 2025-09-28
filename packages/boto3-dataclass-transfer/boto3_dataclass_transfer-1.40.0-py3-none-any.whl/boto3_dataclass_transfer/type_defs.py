# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_transfer import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class As2ConnectorConfig:
    boto3_raw_data: "type_defs.As2ConnectorConfigTypeDef" = dataclasses.field()

    LocalProfileId = field("LocalProfileId")
    PartnerProfileId = field("PartnerProfileId")
    MessageSubject = field("MessageSubject")
    Compression = field("Compression")
    EncryptionAlgorithm = field("EncryptionAlgorithm")
    SigningAlgorithm = field("SigningAlgorithm")
    MdnSigningAlgorithm = field("MdnSigningAlgorithm")
    MdnResponse = field("MdnResponse")
    BasicAuthSecretId = field("BasicAuthSecretId")
    PreserveContentType = field("PreserveContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.As2ConnectorConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.As2ConnectorConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorFileTransferResult:
    boto3_raw_data: "type_defs.ConnectorFileTransferResultTypeDef" = dataclasses.field()

    FilePath = field("FilePath")
    StatusCode = field("StatusCode")
    FailureCode = field("FailureCode")
    FailureMessage = field("FailureMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorFileTransferResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorFileTransferResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HomeDirectoryMapEntry:
    boto3_raw_data: "type_defs.HomeDirectoryMapEntryTypeDef" = dataclasses.field()

    Entry = field("Entry")
    Target = field("Target")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HomeDirectoryMapEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HomeDirectoryMapEntryTypeDef"]
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
class CustomDirectoriesType:
    boto3_raw_data: "type_defs.CustomDirectoriesTypeTypeDef" = dataclasses.field()

    FailedFilesDirectory = field("FailedFilesDirectory")
    MdnFilesDirectory = field("MdnFilesDirectory")
    PayloadFilesDirectory = field("PayloadFilesDirectory")
    StatusFilesDirectory = field("StatusFilesDirectory")
    TemporaryFilesDirectory = field("TemporaryFilesDirectory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDirectoriesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDirectoriesTypeTypeDef"]
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
class IdentityProviderDetails:
    boto3_raw_data: "type_defs.IdentityProviderDetailsTypeDef" = dataclasses.field()

    Url = field("Url")
    InvocationRole = field("InvocationRole")
    DirectoryId = field("DirectoryId")
    Function = field("Function")
    SftpAuthenticationMethods = field("SftpAuthenticationMethods")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3StorageOptions:
    boto3_raw_data: "type_defs.S3StorageOptionsTypeDef" = dataclasses.field()

    DirectoryListingOptimization = field("DirectoryListingOptimization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3StorageOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3StorageOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebAppUnits:
    boto3_raw_data: "type_defs.WebAppUnitsTypeDef" = dataclasses.field()

    Provisioned = field("Provisioned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebAppUnitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebAppUnitsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomStepDetails:
    boto3_raw_data: "type_defs.CustomStepDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Target = field("Target")
    TimeoutSeconds = field("TimeoutSeconds")
    SourceFileLocation = field("SourceFileLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomStepDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessRequest:
    boto3_raw_data: "type_defs.DeleteAccessRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    ExternalId = field("ExternalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgreementRequest:
    boto3_raw_data: "type_defs.DeleteAgreementRequestTypeDef" = dataclasses.field()

    AgreementId = field("AgreementId")
    ServerId = field("ServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgreementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgreementRequestTypeDef"]
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

    CertificateId = field("CertificateId")

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
class DeleteConnectorRequest:
    boto3_raw_data: "type_defs.DeleteConnectorRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")

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
class DeleteHostKeyRequest:
    boto3_raw_data: "type_defs.DeleteHostKeyRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    HostKeyId = field("HostKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteHostKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHostKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileRequest:
    boto3_raw_data: "type_defs.DeleteProfileRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServerRequest:
    boto3_raw_data: "type_defs.DeleteServerRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSshPublicKeyRequest:
    boto3_raw_data: "type_defs.DeleteSshPublicKeyRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    SshPublicKeyId = field("SshPublicKeyId")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSshPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSshPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStepDetails:
    boto3_raw_data: "type_defs.DeleteStepDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    SourceFileLocation = field("SourceFileLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteStepDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    UserName = field("UserName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebAppCustomizationRequest:
    boto3_raw_data: "type_defs.DeleteWebAppCustomizationRequestTypeDef" = (
        dataclasses.field()
    )

    WebAppId = field("WebAppId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWebAppCustomizationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebAppCustomizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebAppRequest:
    boto3_raw_data: "type_defs.DeleteWebAppRequestTypeDef" = dataclasses.field()

    WebAppId = field("WebAppId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWebAppRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowRequestTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessRequest:
    boto3_raw_data: "type_defs.DescribeAccessRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    ExternalId = field("ExternalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgreementRequest:
    boto3_raw_data: "type_defs.DescribeAgreementRequestTypeDef" = dataclasses.field()

    AgreementId = field("AgreementId")
    ServerId = field("ServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgreementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgreementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateRequest:
    boto3_raw_data: "type_defs.DescribeCertificateRequestTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorRequest:
    boto3_raw_data: "type_defs.DescribeConnectorRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExecutionRequest:
    boto3_raw_data: "type_defs.DescribeExecutionRequestTypeDef" = dataclasses.field()

    ExecutionId = field("ExecutionId")
    WorkflowId = field("WorkflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHostKeyRequest:
    boto3_raw_data: "type_defs.DescribeHostKeyRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    HostKeyId = field("HostKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeHostKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHostKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProfileRequest:
    boto3_raw_data: "type_defs.DescribeProfileRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityPolicyRequest:
    boto3_raw_data: "type_defs.DescribeSecurityPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityPolicyName = field("SecurityPolicyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSecurityPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedSecurityPolicy:
    boto3_raw_data: "type_defs.DescribedSecurityPolicyTypeDef" = dataclasses.field()

    SecurityPolicyName = field("SecurityPolicyName")
    Fips = field("Fips")
    SshCiphers = field("SshCiphers")
    SshKexs = field("SshKexs")
    SshMacs = field("SshMacs")
    TlsCiphers = field("TlsCiphers")
    SshHostKeyAlgorithms = field("SshHostKeyAlgorithms")
    Type = field("Type")
    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribedSecurityPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedSecurityPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerRequest:
    boto3_raw_data: "type_defs.DescribeServerRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserRequest:
    boto3_raw_data: "type_defs.DescribeUserRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWebAppCustomizationRequest:
    boto3_raw_data: "type_defs.DescribeWebAppCustomizationRequestTypeDef" = (
        dataclasses.field()
    )

    WebAppId = field("WebAppId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWebAppCustomizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWebAppCustomizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedWebAppCustomization:
    boto3_raw_data: "type_defs.DescribedWebAppCustomizationTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    WebAppId = field("WebAppId")
    Title = field("Title")
    LogoFile = field("LogoFile")
    FaviconFile = field("FaviconFile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribedWebAppCustomizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedWebAppCustomizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWebAppRequest:
    boto3_raw_data: "type_defs.DescribeWebAppRequestTypeDef" = dataclasses.field()

    WebAppId = field("WebAppId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWebAppRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWebAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkflowRequest:
    boto3_raw_data: "type_defs.DescribeWorkflowRequestTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PosixProfileOutput:
    boto3_raw_data: "type_defs.PosixProfileOutputTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Gid = field("Gid")
    SecondaryGids = field("SecondaryGids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PosixProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PosixProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SftpConnectorConfigOutput:
    boto3_raw_data: "type_defs.SftpConnectorConfigOutputTypeDef" = dataclasses.field()

    UserSecretId = field("UserSecretId")
    TrustedHostKeys = field("TrustedHostKeys")
    MaxConcurrentConnections = field("MaxConcurrentConnections")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SftpConnectorConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SftpConnectorConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfiguration:
    boto3_raw_data: "type_defs.LoggingConfigurationTypeDef" = dataclasses.field()

    LoggingRole = field("LoggingRole")
    LogGroupName = field("LogGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedIdentityCenterConfig:
    boto3_raw_data: "type_defs.DescribedIdentityCenterConfigTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    InstanceArn = field("InstanceArn")
    Role = field("Role")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribedIdentityCenterConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedIdentityCenterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointDetailsOutput:
    boto3_raw_data: "type_defs.EndpointDetailsOutputTypeDef" = dataclasses.field()

    AddressAllocationIds = field("AddressAllocationIds")
    SubnetIds = field("SubnetIds")
    VpcEndpointId = field("VpcEndpointId")
    VpcId = field("VpcId")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtocolDetailsOutput:
    boto3_raw_data: "type_defs.ProtocolDetailsOutputTypeDef" = dataclasses.field()

    PassiveIp = field("PassiveIp")
    TlsSessionResumptionMode = field("TlsSessionResumptionMode")
    SetStatOption = field("SetStatOption")
    As2Transports = field("As2Transports")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtocolDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtocolDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SshPublicKey:
    boto3_raw_data: "type_defs.SshPublicKeyTypeDef" = dataclasses.field()

    DateImported = field("DateImported")
    SshPublicKeyBody = field("SshPublicKeyBody")
    SshPublicKeyId = field("SshPublicKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SshPublicKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SshPublicKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EfsFileLocation:
    boto3_raw_data: "type_defs.EfsFileLocationTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    Path = field("Path")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EfsFileLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EfsFileLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointDetails:
    boto3_raw_data: "type_defs.EndpointDetailsTypeDef" = dataclasses.field()

    AddressAllocationIds = field("AddressAllocationIds")
    SubnetIds = field("SubnetIds")
    VpcEndpointId = field("VpcEndpointId")
    VpcId = field("VpcId")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionError:
    boto3_raw_data: "type_defs.ExecutionErrorTypeDef" = dataclasses.field()

    Type = field("Type")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3FileLocation:
    boto3_raw_data: "type_defs.S3FileLocationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")
    Etag = field("Etag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3FileLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3FileLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityCenterConfig:
    boto3_raw_data: "type_defs.IdentityCenterConfigTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    Role = field("Role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSshPublicKeyRequest:
    boto3_raw_data: "type_defs.ImportSshPublicKeyRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    SshPublicKeyBody = field("SshPublicKeyBody")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportSshPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportSshPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3InputFileLocation:
    boto3_raw_data: "type_defs.S3InputFileLocationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3InputFileLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3InputFileLocationTypeDef"]
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
class ListAccessesRequest:
    boto3_raw_data: "type_defs.ListAccessesRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedAccess:
    boto3_raw_data: "type_defs.ListedAccessTypeDef" = dataclasses.field()

    HomeDirectory = field("HomeDirectory")
    HomeDirectoryType = field("HomeDirectoryType")
    Role = field("Role")
    ExternalId = field("ExternalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgreementsRequest:
    boto3_raw_data: "type_defs.ListAgreementsRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgreementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgreementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedAgreement:
    boto3_raw_data: "type_defs.ListedAgreementTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AgreementId = field("AgreementId")
    Description = field("Description")
    Status = field("Status")
    ServerId = field("ServerId")
    LocalProfileId = field("LocalProfileId")
    PartnerProfileId = field("PartnerProfileId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedAgreementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedAgreementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequest:
    boto3_raw_data: "type_defs.ListCertificatesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedCertificate:
    boto3_raw_data: "type_defs.ListedCertificateTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CertificateId = field("CertificateId")
    Usage = field("Usage")
    Status = field("Status")
    ActiveDate = field("ActiveDate")
    InactiveDate = field("InactiveDate")
    Type = field("Type")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedCertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListedCertificateTypeDef"]
        ],
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
class ListedConnector:
    boto3_raw_data: "type_defs.ListedConnectorTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectorId = field("ConnectorId")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedConnectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsRequest:
    boto3_raw_data: "type_defs.ListExecutionsRequestTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileTransferResultsRequest:
    boto3_raw_data: "type_defs.ListFileTransferResultsRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorId = field("ConnectorId")
    TransferId = field("TransferId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFileTransferResultsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileTransferResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostKeysRequest:
    boto3_raw_data: "type_defs.ListHostKeysRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedHostKey:
    boto3_raw_data: "type_defs.ListedHostKeyTypeDef" = dataclasses.field()

    Arn = field("Arn")
    HostKeyId = field("HostKeyId")
    Fingerprint = field("Fingerprint")
    Description = field("Description")
    Type = field("Type")
    DateImported = field("DateImported")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedHostKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedHostKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesRequest:
    boto3_raw_data: "type_defs.ListProfilesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ProfileType = field("ProfileType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedProfile:
    boto3_raw_data: "type_defs.ListedProfileTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ProfileId = field("ProfileId")
    As2Id = field("As2Id")
    ProfileType = field("ProfileType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityPoliciesRequest:
    boto3_raw_data: "type_defs.ListSecurityPoliciesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServersRequest:
    boto3_raw_data: "type_defs.ListServersRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedServer:
    boto3_raw_data: "type_defs.ListedServerTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Domain = field("Domain")
    IdentityProviderType = field("IdentityProviderType")
    EndpointType = field("EndpointType")
    LoggingRole = field("LoggingRole")
    ServerId = field("ServerId")
    State = field("State")
    UserCount = field("UserCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedUser:
    boto3_raw_data: "type_defs.ListedUserTypeDef" = dataclasses.field()

    Arn = field("Arn")
    HomeDirectory = field("HomeDirectory")
    HomeDirectoryType = field("HomeDirectoryType")
    Role = field("Role")
    SshPublicKeyCount = field("SshPublicKeyCount")
    UserName = field("UserName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebAppsRequest:
    boto3_raw_data: "type_defs.ListWebAppsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebAppsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebAppsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedWebApp:
    boto3_raw_data: "type_defs.ListedWebAppTypeDef" = dataclasses.field()

    Arn = field("Arn")
    WebAppId = field("WebAppId")
    AccessEndpoint = field("AccessEndpoint")
    WebAppEndpoint = field("WebAppEndpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedWebAppTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedWebAppTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequest:
    boto3_raw_data: "type_defs.ListWorkflowsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedWorkflow:
    boto3_raw_data: "type_defs.ListedWorkflowTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")
    Description = field("Description")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedWorkflowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedWorkflowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PosixProfile:
    boto3_raw_data: "type_defs.PosixProfileTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Gid = field("Gid")
    SecondaryGids = field("SecondaryGids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PosixProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PosixProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtocolDetails:
    boto3_raw_data: "type_defs.ProtocolDetailsTypeDef" = dataclasses.field()

    PassiveIp = field("PassiveIp")
    TlsSessionResumptionMode = field("TlsSessionResumptionMode")
    SetStatOption = field("SetStatOption")
    As2Transports = field("As2Transports")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtocolDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProtocolDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Tag:
    boto3_raw_data: "type_defs.S3TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendWorkflowStepStateRequest:
    boto3_raw_data: "type_defs.SendWorkflowStepStateRequestTypeDef" = (
        dataclasses.field()
    )

    WorkflowId = field("WorkflowId")
    ExecutionId = field("ExecutionId")
    Token = field("Token")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendWorkflowStepStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendWorkflowStepStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserDetails:
    boto3_raw_data: "type_defs.UserDetailsTypeDef" = dataclasses.field()

    UserName = field("UserName")
    ServerId = field("ServerId")
    SessionId = field("SessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SftpConnectorConfig:
    boto3_raw_data: "type_defs.SftpConnectorConfigTypeDef" = dataclasses.field()

    UserSecretId = field("UserSecretId")
    TrustedHostKeys = field("TrustedHostKeys")
    MaxConcurrentConnections = field("MaxConcurrentConnections")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SftpConnectorConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SftpConnectorConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SftpConnectorConnectionDetails:
    boto3_raw_data: "type_defs.SftpConnectorConnectionDetailsTypeDef" = (
        dataclasses.field()
    )

    HostKey = field("HostKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SftpConnectorConnectionDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SftpConnectorConnectionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDirectoryListingRequest:
    boto3_raw_data: "type_defs.StartDirectoryListingRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorId = field("ConnectorId")
    RemoteDirectoryPath = field("RemoteDirectoryPath")
    OutputDirectoryPath = field("OutputDirectoryPath")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDirectoryListingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDirectoryListingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFileTransferRequest:
    boto3_raw_data: "type_defs.StartFileTransferRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")
    SendFilePaths = field("SendFilePaths")
    RetrieveFilePaths = field("RetrieveFilePaths")
    LocalDirectoryPath = field("LocalDirectoryPath")
    RemoteDirectoryPath = field("RemoteDirectoryPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFileTransferRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFileTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRemoteDeleteRequest:
    boto3_raw_data: "type_defs.StartRemoteDeleteRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")
    DeletePath = field("DeletePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRemoteDeleteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRemoteDeleteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRemoteMoveRequest:
    boto3_raw_data: "type_defs.StartRemoteMoveRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")
    SourcePath = field("SourcePath")
    TargetPath = field("TargetPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRemoteMoveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRemoteMoveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartServerRequest:
    boto3_raw_data: "type_defs.StartServerRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopServerRequest:
    boto3_raw_data: "type_defs.StopServerRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopServerRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConnectionRequest:
    boto3_raw_data: "type_defs.TestConnectionRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestIdentityProviderRequest:
    boto3_raw_data: "type_defs.TestIdentityProviderRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    UserName = field("UserName")
    ServerProtocol = field("ServerProtocol")
    SourceIp = field("SourceIp")
    UserPassword = field("UserPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestIdentityProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestIdentityProviderRequestTypeDef"]
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

    Arn = field("Arn")
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
class UpdateHostKeyRequest:
    boto3_raw_data: "type_defs.UpdateHostKeyRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    HostKeyId = field("HostKeyId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHostKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHostKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileRequest:
    boto3_raw_data: "type_defs.UpdateProfileRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    CertificateIds = field("CertificateIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebAppIdentityCenterConfig:
    boto3_raw_data: "type_defs.UpdateWebAppIdentityCenterConfigTypeDef" = (
        dataclasses.field()
    )

    Role = field("Role")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWebAppIdentityCenterConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebAppIdentityCenterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowDetail:
    boto3_raw_data: "type_defs.WorkflowDetailTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")
    ExecutionRole = field("ExecutionRole")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebAppCustomizationRequest:
    boto3_raw_data: "type_defs.UpdateWebAppCustomizationRequestTypeDef" = (
        dataclasses.field()
    )

    WebAppId = field("WebAppId")
    Title = field("Title")
    LogoFile = field("LogoFile")
    FaviconFile = field("FaviconFile")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWebAppCustomizationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebAppCustomizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessResponse:
    boto3_raw_data: "type_defs.CreateAccessResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    ExternalId = field("ExternalId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgreementResponse:
    boto3_raw_data: "type_defs.CreateAgreementResponseTypeDef" = dataclasses.field()

    AgreementId = field("AgreementId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgreementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgreementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorResponse:
    boto3_raw_data: "type_defs.CreateConnectorResponseTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")

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
class CreateProfileResponse:
    boto3_raw_data: "type_defs.CreateProfileResponseTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServerResponse:
    boto3_raw_data: "type_defs.CreateServerResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResponse:
    boto3_raw_data: "type_defs.CreateUserResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    UserName = field("UserName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebAppResponse:
    boto3_raw_data: "type_defs.CreateWebAppResponseTypeDef" = dataclasses.field()

    WebAppId = field("WebAppId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebAppResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowResponse:
    boto3_raw_data: "type_defs.CreateWorkflowResponseTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowResponseTypeDef"]
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
class ImportCertificateResponse:
    boto3_raw_data: "type_defs.ImportCertificateResponseTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportHostKeyResponse:
    boto3_raw_data: "type_defs.ImportHostKeyResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    HostKeyId = field("HostKeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportHostKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportHostKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSshPublicKeyResponse:
    boto3_raw_data: "type_defs.ImportSshPublicKeyResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    SshPublicKeyId = field("SshPublicKeyId")
    UserName = field("UserName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportSshPublicKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportSshPublicKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileTransferResultsResponse:
    boto3_raw_data: "type_defs.ListFileTransferResultsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileTransferResults(self):  # pragma: no cover
        return ConnectorFileTransferResult.make_many(
            self.boto3_raw_data["FileTransferResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFileTransferResultsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileTransferResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityPoliciesResponse:
    boto3_raw_data: "type_defs.ListSecurityPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    SecurityPolicyNames = field("SecurityPolicyNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDirectoryListingResponse:
    boto3_raw_data: "type_defs.StartDirectoryListingResponseTypeDef" = (
        dataclasses.field()
    )

    ListingId = field("ListingId")
    OutputFileName = field("OutputFileName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDirectoryListingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDirectoryListingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFileTransferResponse:
    boto3_raw_data: "type_defs.StartFileTransferResponseTypeDef" = dataclasses.field()

    TransferId = field("TransferId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFileTransferResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFileTransferResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRemoteDeleteResponse:
    boto3_raw_data: "type_defs.StartRemoteDeleteResponseTypeDef" = dataclasses.field()

    DeleteId = field("DeleteId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRemoteDeleteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRemoteDeleteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRemoteMoveResponse:
    boto3_raw_data: "type_defs.StartRemoteMoveResponseTypeDef" = dataclasses.field()

    MoveId = field("MoveId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRemoteMoveResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRemoteMoveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestIdentityProviderResponse:
    boto3_raw_data: "type_defs.TestIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    Response = field("Response")
    StatusCode = field("StatusCode")
    Message = field("Message")
    Url = field("Url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestIdentityProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessResponse:
    boto3_raw_data: "type_defs.UpdateAccessResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    ExternalId = field("ExternalId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgreementResponse:
    boto3_raw_data: "type_defs.UpdateAgreementResponseTypeDef" = dataclasses.field()

    AgreementId = field("AgreementId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgreementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgreementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateResponse:
    boto3_raw_data: "type_defs.UpdateCertificateResponseTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorResponse:
    boto3_raw_data: "type_defs.UpdateConnectorResponseTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHostKeyResponse:
    boto3_raw_data: "type_defs.UpdateHostKeyResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    HostKeyId = field("HostKeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHostKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHostKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileResponse:
    boto3_raw_data: "type_defs.UpdateProfileResponseTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServerResponse:
    boto3_raw_data: "type_defs.UpdateServerResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserResponse:
    boto3_raw_data: "type_defs.UpdateUserResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    UserName = field("UserName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebAppCustomizationResponse:
    boto3_raw_data: "type_defs.UpdateWebAppCustomizationResponseTypeDef" = (
        dataclasses.field()
    )

    WebAppId = field("WebAppId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWebAppCustomizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebAppCustomizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebAppResponse:
    boto3_raw_data: "type_defs.UpdateWebAppResponseTypeDef" = dataclasses.field()

    WebAppId = field("WebAppId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebAppResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgreementRequest:
    boto3_raw_data: "type_defs.UpdateAgreementRequestTypeDef" = dataclasses.field()

    AgreementId = field("AgreementId")
    ServerId = field("ServerId")
    Description = field("Description")
    Status = field("Status")
    LocalProfileId = field("LocalProfileId")
    PartnerProfileId = field("PartnerProfileId")
    BaseDirectory = field("BaseDirectory")
    AccessRole = field("AccessRole")
    PreserveFilename = field("PreserveFilename")
    EnforceMessageSigning = field("EnforceMessageSigning")

    @cached_property
    def CustomDirectories(self):  # pragma: no cover
        return CustomDirectoriesType.make_one(self.boto3_raw_data["CustomDirectories"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgreementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgreementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgreementRequest:
    boto3_raw_data: "type_defs.CreateAgreementRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    LocalProfileId = field("LocalProfileId")
    PartnerProfileId = field("PartnerProfileId")
    AccessRole = field("AccessRole")
    Description = field("Description")
    BaseDirectory = field("BaseDirectory")
    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PreserveFilename = field("PreserveFilename")
    EnforceMessageSigning = field("EnforceMessageSigning")

    @cached_property
    def CustomDirectories(self):  # pragma: no cover
        return CustomDirectoriesType.make_one(self.boto3_raw_data["CustomDirectories"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgreementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgreementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileRequest:
    boto3_raw_data: "type_defs.CreateProfileRequestTypeDef" = dataclasses.field()

    As2Id = field("As2Id")
    ProfileType = field("ProfileType")
    CertificateIds = field("CertificateIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedAgreement:
    boto3_raw_data: "type_defs.DescribedAgreementTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AgreementId = field("AgreementId")
    Description = field("Description")
    Status = field("Status")
    ServerId = field("ServerId")
    LocalProfileId = field("LocalProfileId")
    PartnerProfileId = field("PartnerProfileId")
    BaseDirectory = field("BaseDirectory")
    AccessRole = field("AccessRole")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PreserveFilename = field("PreserveFilename")
    EnforceMessageSigning = field("EnforceMessageSigning")

    @cached_property
    def CustomDirectories(self):  # pragma: no cover
        return CustomDirectoriesType.make_one(self.boto3_raw_data["CustomDirectories"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribedAgreementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedAgreementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedCertificate:
    boto3_raw_data: "type_defs.DescribedCertificateTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CertificateId = field("CertificateId")
    Usage = field("Usage")
    Status = field("Status")
    Certificate = field("Certificate")
    CertificateChain = field("CertificateChain")
    ActiveDate = field("ActiveDate")
    InactiveDate = field("InactiveDate")
    Serial = field("Serial")
    NotBeforeDate = field("NotBeforeDate")
    NotAfterDate = field("NotAfterDate")
    Type = field("Type")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribedCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedHostKey:
    boto3_raw_data: "type_defs.DescribedHostKeyTypeDef" = dataclasses.field()

    Arn = field("Arn")
    HostKeyId = field("HostKeyId")
    HostKeyFingerprint = field("HostKeyFingerprint")
    Description = field("Description")
    Type = field("Type")
    DateImported = field("DateImported")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedHostKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedHostKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedProfile:
    boto3_raw_data: "type_defs.DescribedProfileTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ProfileId = field("ProfileId")
    ProfileType = field("ProfileType")
    As2Id = field("As2Id")
    CertificateIds = field("CertificateIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportHostKeyRequest:
    boto3_raw_data: "type_defs.ImportHostKeyRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    HostKeyBody = field("HostKeyBody")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportHostKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportHostKeyRequestTypeDef"]
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

    Arn = field("Arn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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

    Arn = field("Arn")

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
class DescribeSecurityPolicyResponse:
    boto3_raw_data: "type_defs.DescribeSecurityPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityPolicy(self):  # pragma: no cover
        return DescribedSecurityPolicy.make_one(self.boto3_raw_data["SecurityPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSecurityPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeServerRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ServerId = field("ServerId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServerRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerRequestWait:
    boto3_raw_data: "type_defs.DescribeServerRequestWaitTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServerRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWebAppCustomizationResponse:
    boto3_raw_data: "type_defs.DescribeWebAppCustomizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WebAppCustomization(self):  # pragma: no cover
        return DescribedWebAppCustomization.make_one(
            self.boto3_raw_data["WebAppCustomization"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWebAppCustomizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWebAppCustomizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedAccess:
    boto3_raw_data: "type_defs.DescribedAccessTypeDef" = dataclasses.field()

    HomeDirectory = field("HomeDirectory")

    @cached_property
    def HomeDirectoryMappings(self):  # pragma: no cover
        return HomeDirectoryMapEntry.make_many(
            self.boto3_raw_data["HomeDirectoryMappings"]
        )

    HomeDirectoryType = field("HomeDirectoryType")
    Policy = field("Policy")

    @cached_property
    def PosixProfile(self):  # pragma: no cover
        return PosixProfileOutput.make_one(self.boto3_raw_data["PosixProfile"])

    Role = field("Role")
    ExternalId = field("ExternalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DescribedAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedConnector:
    boto3_raw_data: "type_defs.DescribedConnectorTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectorId = field("ConnectorId")
    Url = field("Url")

    @cached_property
    def As2Config(self):  # pragma: no cover
        return As2ConnectorConfig.make_one(self.boto3_raw_data["As2Config"])

    AccessRole = field("AccessRole")
    LoggingRole = field("LoggingRole")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def SftpConfig(self):  # pragma: no cover
        return SftpConnectorConfigOutput.make_one(self.boto3_raw_data["SftpConfig"])

    ServiceManagedEgressIpAddresses = field("ServiceManagedEgressIpAddresses")
    SecurityPolicyName = field("SecurityPolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribedConnectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedConnectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedWebAppIdentityProviderDetails:
    boto3_raw_data: "type_defs.DescribedWebAppIdentityProviderDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityCenterConfig(self):  # pragma: no cover
        return DescribedIdentityCenterConfig.make_one(
            self.boto3_raw_data["IdentityCenterConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribedWebAppIdentityProviderDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedWebAppIdentityProviderDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedUser:
    boto3_raw_data: "type_defs.DescribedUserTypeDef" = dataclasses.field()

    Arn = field("Arn")
    HomeDirectory = field("HomeDirectory")

    @cached_property
    def HomeDirectoryMappings(self):  # pragma: no cover
        return HomeDirectoryMapEntry.make_many(
            self.boto3_raw_data["HomeDirectoryMappings"]
        )

    HomeDirectoryType = field("HomeDirectoryType")
    Policy = field("Policy")

    @cached_property
    def PosixProfile(self):  # pragma: no cover
        return PosixProfileOutput.make_one(self.boto3_raw_data["PosixProfile"])

    Role = field("Role")

    @cached_property
    def SshPublicKeys(self):  # pragma: no cover
        return SshPublicKey.make_many(self.boto3_raw_data["SshPublicKeys"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    UserName = field("UserName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DescribedUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionStepResult:
    boto3_raw_data: "type_defs.ExecutionStepResultTypeDef" = dataclasses.field()

    StepType = field("StepType")
    Outputs = field("Outputs")

    @cached_property
    def Error(self):  # pragma: no cover
        return ExecutionError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionStepResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionStepResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileLocation:
    boto3_raw_data: "type_defs.FileLocationTypeDef" = dataclasses.field()

    @cached_property
    def S3FileLocation(self):  # pragma: no cover
        return S3FileLocation.make_one(self.boto3_raw_data["S3FileLocation"])

    @cached_property
    def EfsFileLocation(self):  # pragma: no cover
        return EfsFileLocation.make_one(self.boto3_raw_data["EfsFileLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebAppIdentityProviderDetails:
    boto3_raw_data: "type_defs.WebAppIdentityProviderDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityCenterConfig(self):  # pragma: no cover
        return IdentityCenterConfig.make_one(
            self.boto3_raw_data["IdentityCenterConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebAppIdentityProviderDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebAppIdentityProviderDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCertificateRequest:
    boto3_raw_data: "type_defs.ImportCertificateRequestTypeDef" = dataclasses.field()

    Usage = field("Usage")
    Certificate = field("Certificate")
    CertificateChain = field("CertificateChain")
    PrivateKey = field("PrivateKey")
    ActiveDate = field("ActiveDate")
    InactiveDate = field("InactiveDate")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateRequest:
    boto3_raw_data: "type_defs.UpdateCertificateRequestTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")
    ActiveDate = field("ActiveDate")
    InactiveDate = field("InactiveDate")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFileLocation:
    boto3_raw_data: "type_defs.InputFileLocationTypeDef" = dataclasses.field()

    @cached_property
    def S3FileLocation(self):  # pragma: no cover
        return S3InputFileLocation.make_one(self.boto3_raw_data["S3FileLocation"])

    @cached_property
    def EfsFileLocation(self):  # pragma: no cover
        return EfsFileLocation.make_one(self.boto3_raw_data["EfsFileLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputFileLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputFileLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessesRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessesRequestPaginateTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgreementsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgreementsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServerId = field("ServerId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgreementsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgreementsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestPaginateTypeDef"]
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
class ListExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    WorkflowId = field("WorkflowId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExecutionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileTransferResultsRequestPaginate:
    boto3_raw_data: "type_defs.ListFileTransferResultsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConnectorId = field("ConnectorId")
    TransferId = field("TransferId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFileTransferResultsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileTransferResultsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListProfilesRequestPaginateTypeDef" = dataclasses.field()

    ProfileType = field("ProfileType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServersRequestPaginate:
    boto3_raw_data: "type_defs.ListServersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebAppsRequestPaginate:
    boto3_raw_data: "type_defs.ListWebAppsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebAppsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebAppsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessesResponse:
    boto3_raw_data: "type_defs.ListAccessesResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def Accesses(self):  # pragma: no cover
        return ListedAccess.make_many(self.boto3_raw_data["Accesses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgreementsResponse:
    boto3_raw_data: "type_defs.ListAgreementsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Agreements(self):  # pragma: no cover
        return ListedAgreement.make_many(self.boto3_raw_data["Agreements"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgreementsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgreementsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesResponse:
    boto3_raw_data: "type_defs.ListCertificatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Certificates(self):  # pragma: no cover
        return ListedCertificate.make_many(self.boto3_raw_data["Certificates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesResponseTypeDef"]
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
        return ListedConnector.make_many(self.boto3_raw_data["Connectors"])

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
class ListHostKeysResponse:
    boto3_raw_data: "type_defs.ListHostKeysResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def HostKeys(self):  # pragma: no cover
        return ListedHostKey.make_many(self.boto3_raw_data["HostKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesResponse:
    boto3_raw_data: "type_defs.ListProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Profiles(self):  # pragma: no cover
        return ListedProfile.make_many(self.boto3_raw_data["Profiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServersResponse:
    boto3_raw_data: "type_defs.ListServersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Servers(self):  # pragma: no cover
        return ListedServer.make_many(self.boto3_raw_data["Servers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def Users(self):  # pragma: no cover
        return ListedUser.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebAppsResponse:
    boto3_raw_data: "type_defs.ListWebAppsResponseTypeDef" = dataclasses.field()

    @cached_property
    def WebApps(self):  # pragma: no cover
        return ListedWebApp.make_many(self.boto3_raw_data["WebApps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebAppsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebAppsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsResponse:
    boto3_raw_data: "type_defs.ListWorkflowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Workflows(self):  # pragma: no cover
        return ListedWorkflow.make_many(self.boto3_raw_data["Workflows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagStepDetailsOutput:
    boto3_raw_data: "type_defs.TagStepDetailsOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    SourceFileLocation = field("SourceFileLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagStepDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagStepDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagStepDetails:
    boto3_raw_data: "type_defs.TagStepDetailsTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    SourceFileLocation = field("SourceFileLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagStepDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagStepDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceMetadata:
    boto3_raw_data: "type_defs.ServiceMetadataTypeDef" = dataclasses.field()

    @cached_property
    def UserDetails(self):  # pragma: no cover
        return UserDetails.make_one(self.boto3_raw_data["UserDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConnectionResponse:
    boto3_raw_data: "type_defs.TestConnectionResponseTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def SftpConnectionDetails(self):  # pragma: no cover
        return SftpConnectorConnectionDetails.make_one(
            self.boto3_raw_data["SftpConnectionDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebAppIdentityProviderDetails:
    boto3_raw_data: "type_defs.UpdateWebAppIdentityProviderDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityCenterConfig(self):  # pragma: no cover
        return UpdateWebAppIdentityCenterConfig.make_one(
            self.boto3_raw_data["IdentityCenterConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWebAppIdentityProviderDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebAppIdentityProviderDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowDetailsOutput:
    boto3_raw_data: "type_defs.WorkflowDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def OnUpload(self):  # pragma: no cover
        return WorkflowDetail.make_many(self.boto3_raw_data["OnUpload"])

    @cached_property
    def OnPartialUpload(self):  # pragma: no cover
        return WorkflowDetail.make_many(self.boto3_raw_data["OnPartialUpload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowDetails:
    boto3_raw_data: "type_defs.WorkflowDetailsTypeDef" = dataclasses.field()

    @cached_property
    def OnUpload(self):  # pragma: no cover
        return WorkflowDetail.make_many(self.boto3_raw_data["OnUpload"])

    @cached_property
    def OnPartialUpload(self):  # pragma: no cover
        return WorkflowDetail.make_many(self.boto3_raw_data["OnPartialUpload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgreementResponse:
    boto3_raw_data: "type_defs.DescribeAgreementResponseTypeDef" = dataclasses.field()

    @cached_property
    def Agreement(self):  # pragma: no cover
        return DescribedAgreement.make_one(self.boto3_raw_data["Agreement"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgreementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgreementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateResponse:
    boto3_raw_data: "type_defs.DescribeCertificateResponseTypeDef" = dataclasses.field()

    @cached_property
    def Certificate(self):  # pragma: no cover
        return DescribedCertificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHostKeyResponse:
    boto3_raw_data: "type_defs.DescribeHostKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def HostKey(self):  # pragma: no cover
        return DescribedHostKey.make_one(self.boto3_raw_data["HostKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeHostKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHostKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProfileResponse:
    boto3_raw_data: "type_defs.DescribeProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def Profile(self):  # pragma: no cover
        return DescribedProfile.make_one(self.boto3_raw_data["Profile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessResponse:
    boto3_raw_data: "type_defs.DescribeAccessResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def Access(self):  # pragma: no cover
        return DescribedAccess.make_one(self.boto3_raw_data["Access"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorResponse:
    boto3_raw_data: "type_defs.DescribeConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connector(self):  # pragma: no cover
        return DescribedConnector.make_one(self.boto3_raw_data["Connector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedWebApp:
    boto3_raw_data: "type_defs.DescribedWebAppTypeDef" = dataclasses.field()

    Arn = field("Arn")
    WebAppId = field("WebAppId")

    @cached_property
    def DescribedIdentityProviderDetails(self):  # pragma: no cover
        return DescribedWebAppIdentityProviderDetails.make_one(
            self.boto3_raw_data["DescribedIdentityProviderDetails"]
        )

    AccessEndpoint = field("AccessEndpoint")
    WebAppEndpoint = field("WebAppEndpoint")

    @cached_property
    def WebAppUnits(self):  # pragma: no cover
        return WebAppUnits.make_one(self.boto3_raw_data["WebAppUnits"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    WebAppEndpointPolicy = field("WebAppEndpointPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedWebAppTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DescribedWebAppTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserResponse:
    boto3_raw_data: "type_defs.DescribeUserResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")

    @cached_property
    def User(self):  # pragma: no cover
        return DescribedUser.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionResults:
    boto3_raw_data: "type_defs.ExecutionResultsTypeDef" = dataclasses.field()

    @cached_property
    def Steps(self):  # pragma: no cover
        return ExecutionStepResult.make_many(self.boto3_raw_data["Steps"])

    @cached_property
    def OnExceptionSteps(self):  # pragma: no cover
        return ExecutionStepResult.make_many(self.boto3_raw_data["OnExceptionSteps"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionResultsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebAppRequest:
    boto3_raw_data: "type_defs.CreateWebAppRequestTypeDef" = dataclasses.field()

    @cached_property
    def IdentityProviderDetails(self):  # pragma: no cover
        return WebAppIdentityProviderDetails.make_one(
            self.boto3_raw_data["IdentityProviderDetails"]
        )

    AccessEndpoint = field("AccessEndpoint")

    @cached_property
    def WebAppUnits(self):  # pragma: no cover
        return WebAppUnits.make_one(self.boto3_raw_data["WebAppUnits"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    WebAppEndpointPolicy = field("WebAppEndpointPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebAppRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyStepDetails:
    boto3_raw_data: "type_defs.CopyStepDetailsTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def DestinationFileLocation(self):  # pragma: no cover
        return InputFileLocation.make_one(
            self.boto3_raw_data["DestinationFileLocation"]
        )

    OverwriteExisting = field("OverwriteExisting")
    SourceFileLocation = field("SourceFileLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyStepDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyStepDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecryptStepDetails:
    boto3_raw_data: "type_defs.DecryptStepDetailsTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def DestinationFileLocation(self):  # pragma: no cover
        return InputFileLocation.make_one(
            self.boto3_raw_data["DestinationFileLocation"]
        )

    Name = field("Name")
    SourceFileLocation = field("SourceFileLocation")
    OverwriteExisting = field("OverwriteExisting")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DecryptStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecryptStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessRequest:
    boto3_raw_data: "type_defs.CreateAccessRequestTypeDef" = dataclasses.field()

    Role = field("Role")
    ServerId = field("ServerId")
    ExternalId = field("ExternalId")
    HomeDirectory = field("HomeDirectory")
    HomeDirectoryType = field("HomeDirectoryType")

    @cached_property
    def HomeDirectoryMappings(self):  # pragma: no cover
        return HomeDirectoryMapEntry.make_many(
            self.boto3_raw_data["HomeDirectoryMappings"]
        )

    Policy = field("Policy")
    PosixProfile = field("PosixProfile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    Role = field("Role")
    ServerId = field("ServerId")
    UserName = field("UserName")
    HomeDirectory = field("HomeDirectory")
    HomeDirectoryType = field("HomeDirectoryType")

    @cached_property
    def HomeDirectoryMappings(self):  # pragma: no cover
        return HomeDirectoryMapEntry.make_many(
            self.boto3_raw_data["HomeDirectoryMappings"]
        )

    Policy = field("Policy")
    PosixProfile = field("PosixProfile")
    SshPublicKeyBody = field("SshPublicKeyBody")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessRequest:
    boto3_raw_data: "type_defs.UpdateAccessRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    ExternalId = field("ExternalId")
    HomeDirectory = field("HomeDirectory")
    HomeDirectoryType = field("HomeDirectoryType")

    @cached_property
    def HomeDirectoryMappings(self):  # pragma: no cover
        return HomeDirectoryMapEntry.make_many(
            self.boto3_raw_data["HomeDirectoryMappings"]
        )

    Policy = field("Policy")
    PosixProfile = field("PosixProfile")
    Role = field("Role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    UserName = field("UserName")
    HomeDirectory = field("HomeDirectory")
    HomeDirectoryType = field("HomeDirectoryType")

    @cached_property
    def HomeDirectoryMappings(self):  # pragma: no cover
        return HomeDirectoryMapEntry.make_many(
            self.boto3_raw_data["HomeDirectoryMappings"]
        )

    Policy = field("Policy")
    PosixProfile = field("PosixProfile")
    Role = field("Role")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListedExecution:
    boto3_raw_data: "type_defs.ListedExecutionTypeDef" = dataclasses.field()

    ExecutionId = field("ExecutionId")

    @cached_property
    def InitialFileLocation(self):  # pragma: no cover
        return FileLocation.make_one(self.boto3_raw_data["InitialFileLocation"])

    @cached_property
    def ServiceMetadata(self):  # pragma: no cover
        return ServiceMetadata.make_one(self.boto3_raw_data["ServiceMetadata"])

    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListedExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListedExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorRequest:
    boto3_raw_data: "type_defs.CreateConnectorRequestTypeDef" = dataclasses.field()

    Url = field("Url")
    AccessRole = field("AccessRole")

    @cached_property
    def As2Config(self):  # pragma: no cover
        return As2ConnectorConfig.make_one(self.boto3_raw_data["As2Config"])

    LoggingRole = field("LoggingRole")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SftpConfig = field("SftpConfig")
    SecurityPolicyName = field("SecurityPolicyName")

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
class UpdateConnectorRequest:
    boto3_raw_data: "type_defs.UpdateConnectorRequestTypeDef" = dataclasses.field()

    ConnectorId = field("ConnectorId")
    Url = field("Url")

    @cached_property
    def As2Config(self):  # pragma: no cover
        return As2ConnectorConfig.make_one(self.boto3_raw_data["As2Config"])

    AccessRole = field("AccessRole")
    LoggingRole = field("LoggingRole")
    SftpConfig = field("SftpConfig")
    SecurityPolicyName = field("SecurityPolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebAppRequest:
    boto3_raw_data: "type_defs.UpdateWebAppRequestTypeDef" = dataclasses.field()

    WebAppId = field("WebAppId")

    @cached_property
    def IdentityProviderDetails(self):  # pragma: no cover
        return UpdateWebAppIdentityProviderDetails.make_one(
            self.boto3_raw_data["IdentityProviderDetails"]
        )

    AccessEndpoint = field("AccessEndpoint")

    @cached_property
    def WebAppUnits(self):  # pragma: no cover
        return WebAppUnits.make_one(self.boto3_raw_data["WebAppUnits"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebAppRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedServer:
    boto3_raw_data: "type_defs.DescribedServerTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Certificate = field("Certificate")

    @cached_property
    def ProtocolDetails(self):  # pragma: no cover
        return ProtocolDetailsOutput.make_one(self.boto3_raw_data["ProtocolDetails"])

    Domain = field("Domain")

    @cached_property
    def EndpointDetails(self):  # pragma: no cover
        return EndpointDetailsOutput.make_one(self.boto3_raw_data["EndpointDetails"])

    EndpointType = field("EndpointType")
    HostKeyFingerprint = field("HostKeyFingerprint")

    @cached_property
    def IdentityProviderDetails(self):  # pragma: no cover
        return IdentityProviderDetails.make_one(
            self.boto3_raw_data["IdentityProviderDetails"]
        )

    IdentityProviderType = field("IdentityProviderType")
    LoggingRole = field("LoggingRole")
    PostAuthenticationLoginBanner = field("PostAuthenticationLoginBanner")
    PreAuthenticationLoginBanner = field("PreAuthenticationLoginBanner")
    Protocols = field("Protocols")
    SecurityPolicyName = field("SecurityPolicyName")
    ServerId = field("ServerId")
    State = field("State")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    UserCount = field("UserCount")

    @cached_property
    def WorkflowDetails(self):  # pragma: no cover
        return WorkflowDetailsOutput.make_one(self.boto3_raw_data["WorkflowDetails"])

    StructuredLogDestinations = field("StructuredLogDestinations")

    @cached_property
    def S3StorageOptions(self):  # pragma: no cover
        return S3StorageOptions.make_one(self.boto3_raw_data["S3StorageOptions"])

    As2ServiceManagedEgressIpAddresses = field("As2ServiceManagedEgressIpAddresses")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DescribedServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWebAppResponse:
    boto3_raw_data: "type_defs.DescribeWebAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def WebApp(self):  # pragma: no cover
        return DescribedWebApp.make_one(self.boto3_raw_data["WebApp"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWebAppResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWebAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedExecution:
    boto3_raw_data: "type_defs.DescribedExecutionTypeDef" = dataclasses.field()

    ExecutionId = field("ExecutionId")

    @cached_property
    def InitialFileLocation(self):  # pragma: no cover
        return FileLocation.make_one(self.boto3_raw_data["InitialFileLocation"])

    @cached_property
    def ServiceMetadata(self):  # pragma: no cover
        return ServiceMetadata.make_one(self.boto3_raw_data["ServiceMetadata"])

    ExecutionRole = field("ExecutionRole")

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfiguration.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @cached_property
    def PosixProfile(self):  # pragma: no cover
        return PosixProfileOutput.make_one(self.boto3_raw_data["PosixProfile"])

    Status = field("Status")

    @cached_property
    def Results(self):  # pragma: no cover
        return ExecutionResults.make_one(self.boto3_raw_data["Results"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribedExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepOutput:
    boto3_raw_data: "type_defs.WorkflowStepOutputTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def CopyStepDetails(self):  # pragma: no cover
        return CopyStepDetails.make_one(self.boto3_raw_data["CopyStepDetails"])

    @cached_property
    def CustomStepDetails(self):  # pragma: no cover
        return CustomStepDetails.make_one(self.boto3_raw_data["CustomStepDetails"])

    @cached_property
    def DeleteStepDetails(self):  # pragma: no cover
        return DeleteStepDetails.make_one(self.boto3_raw_data["DeleteStepDetails"])

    @cached_property
    def TagStepDetails(self):  # pragma: no cover
        return TagStepDetailsOutput.make_one(self.boto3_raw_data["TagStepDetails"])

    @cached_property
    def DecryptStepDetails(self):  # pragma: no cover
        return DecryptStepDetails.make_one(self.boto3_raw_data["DecryptStepDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStep:
    boto3_raw_data: "type_defs.WorkflowStepTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def CopyStepDetails(self):  # pragma: no cover
        return CopyStepDetails.make_one(self.boto3_raw_data["CopyStepDetails"])

    @cached_property
    def CustomStepDetails(self):  # pragma: no cover
        return CustomStepDetails.make_one(self.boto3_raw_data["CustomStepDetails"])

    @cached_property
    def DeleteStepDetails(self):  # pragma: no cover
        return DeleteStepDetails.make_one(self.boto3_raw_data["DeleteStepDetails"])

    TagStepDetails = field("TagStepDetails")

    @cached_property
    def DecryptStepDetails(self):  # pragma: no cover
        return DecryptStepDetails.make_one(self.boto3_raw_data["DecryptStepDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowStepTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutionsResponse:
    boto3_raw_data: "type_defs.ListExecutionsResponseTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")

    @cached_property
    def Executions(self):  # pragma: no cover
        return ListedExecution.make_many(self.boto3_raw_data["Executions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerResponse:
    boto3_raw_data: "type_defs.DescribeServerResponseTypeDef" = dataclasses.field()

    @cached_property
    def Server(self):  # pragma: no cover
        return DescribedServer.make_one(self.boto3_raw_data["Server"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServerRequest:
    boto3_raw_data: "type_defs.CreateServerRequestTypeDef" = dataclasses.field()

    Certificate = field("Certificate")
    Domain = field("Domain")
    EndpointDetails = field("EndpointDetails")
    EndpointType = field("EndpointType")
    HostKey = field("HostKey")

    @cached_property
    def IdentityProviderDetails(self):  # pragma: no cover
        return IdentityProviderDetails.make_one(
            self.boto3_raw_data["IdentityProviderDetails"]
        )

    IdentityProviderType = field("IdentityProviderType")
    LoggingRole = field("LoggingRole")
    PostAuthenticationLoginBanner = field("PostAuthenticationLoginBanner")
    PreAuthenticationLoginBanner = field("PreAuthenticationLoginBanner")
    Protocols = field("Protocols")
    ProtocolDetails = field("ProtocolDetails")
    SecurityPolicyName = field("SecurityPolicyName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    WorkflowDetails = field("WorkflowDetails")
    StructuredLogDestinations = field("StructuredLogDestinations")

    @cached_property
    def S3StorageOptions(self):  # pragma: no cover
        return S3StorageOptions.make_one(self.boto3_raw_data["S3StorageOptions"])

    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServerRequest:
    boto3_raw_data: "type_defs.UpdateServerRequestTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    Certificate = field("Certificate")
    ProtocolDetails = field("ProtocolDetails")
    EndpointDetails = field("EndpointDetails")
    EndpointType = field("EndpointType")
    HostKey = field("HostKey")

    @cached_property
    def IdentityProviderDetails(self):  # pragma: no cover
        return IdentityProviderDetails.make_one(
            self.boto3_raw_data["IdentityProviderDetails"]
        )

    LoggingRole = field("LoggingRole")
    PostAuthenticationLoginBanner = field("PostAuthenticationLoginBanner")
    PreAuthenticationLoginBanner = field("PreAuthenticationLoginBanner")
    Protocols = field("Protocols")
    SecurityPolicyName = field("SecurityPolicyName")
    WorkflowDetails = field("WorkflowDetails")
    StructuredLogDestinations = field("StructuredLogDestinations")

    @cached_property
    def S3StorageOptions(self):  # pragma: no cover
        return S3StorageOptions.make_one(self.boto3_raw_data["S3StorageOptions"])

    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExecutionResponse:
    boto3_raw_data: "type_defs.DescribeExecutionResponseTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")

    @cached_property
    def Execution(self):  # pragma: no cover
        return DescribedExecution.make_one(self.boto3_raw_data["Execution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribedWorkflow:
    boto3_raw_data: "type_defs.DescribedWorkflowTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Description = field("Description")

    @cached_property
    def Steps(self):  # pragma: no cover
        return WorkflowStepOutput.make_many(self.boto3_raw_data["Steps"])

    @cached_property
    def OnExceptionSteps(self):  # pragma: no cover
        return WorkflowStepOutput.make_many(self.boto3_raw_data["OnExceptionSteps"])

    WorkflowId = field("WorkflowId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribedWorkflowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribedWorkflowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkflowResponse:
    boto3_raw_data: "type_defs.DescribeWorkflowResponseTypeDef" = dataclasses.field()

    @cached_property
    def Workflow(self):  # pragma: no cover
        return DescribedWorkflow.make_one(self.boto3_raw_data["Workflow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowRequest:
    boto3_raw_data: "type_defs.CreateWorkflowRequestTypeDef" = dataclasses.field()

    Steps = field("Steps")
    Description = field("Description")
    OnExceptionSteps = field("OnExceptionSteps")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
