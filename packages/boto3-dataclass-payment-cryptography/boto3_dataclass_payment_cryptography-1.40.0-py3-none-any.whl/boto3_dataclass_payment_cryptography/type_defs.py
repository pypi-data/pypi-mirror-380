# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_payment_cryptography import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddKeyReplicationRegionsInput:
    boto3_raw_data: "type_defs.AddKeyReplicationRegionsInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")
    ReplicationRegions = field("ReplicationRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddKeyReplicationRegionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddKeyReplicationRegionsInputTypeDef"]
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
class Alias:
    boto3_raw_data: "type_defs.AliasTypeDef" = dataclasses.field()

    AliasName = field("AliasName")
    KeyArn = field("KeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateSubjectType:
    boto3_raw_data: "type_defs.CertificateSubjectTypeTypeDef" = dataclasses.field()

    CommonName = field("CommonName")
    OrganizationUnit = field("OrganizationUnit")
    Organization = field("Organization")
    City = field("City")
    Country = field("Country")
    StateOrProvince = field("StateOrProvince")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateSubjectTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateSubjectTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasInput:
    boto3_raw_data: "type_defs.CreateAliasInputTypeDef" = dataclasses.field()

    AliasName = field("AliasName")
    KeyArn = field("KeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasInputTypeDef"]
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
class DeleteAliasInput:
    boto3_raw_data: "type_defs.DeleteAliasInputTypeDef" = dataclasses.field()

    AliasName = field("AliasName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyInput:
    boto3_raw_data: "type_defs.DeleteKeyInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")
    DeleteKeyInDays = field("DeleteKeyInDays")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteKeyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiffieHellmanDerivationData:
    boto3_raw_data: "type_defs.DiffieHellmanDerivationDataTypeDef" = dataclasses.field()

    SharedInformation = field("SharedInformation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiffieHellmanDerivationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiffieHellmanDerivationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDefaultKeyReplicationRegionsInput:
    boto3_raw_data: "type_defs.DisableDefaultKeyReplicationRegionsInputTypeDef" = (
        dataclasses.field()
    )

    ReplicationRegions = field("ReplicationRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableDefaultKeyReplicationRegionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDefaultKeyReplicationRegionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDefaultKeyReplicationRegionsInput:
    boto3_raw_data: "type_defs.EnableDefaultKeyReplicationRegionsInputTypeDef" = (
        dataclasses.field()
    )

    ReplicationRegions = field("ReplicationRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableDefaultKeyReplicationRegionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDefaultKeyReplicationRegionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDukptInitialKey:
    boto3_raw_data: "type_defs.ExportDukptInitialKeyTypeDef" = dataclasses.field()

    KeySerialNumber = field("KeySerialNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportDukptInitialKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDukptInitialKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportKeyCryptogram:
    boto3_raw_data: "type_defs.ExportKeyCryptogramTypeDef" = dataclasses.field()

    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )
    WrappingKeyCertificate = field("WrappingKeyCertificate")
    WrappingSpec = field("WrappingSpec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportKeyCryptogramTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportKeyCryptogramTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WrappedKey:
    boto3_raw_data: "type_defs.WrappedKeyTypeDef" = dataclasses.field()

    WrappingKeyArn = field("WrappingKeyArn")
    WrappedKeyMaterialFormat = field("WrappedKeyMaterialFormat")
    KeyMaterial = field("KeyMaterial")
    KeyCheckValue = field("KeyCheckValue")
    KeyCheckValueAlgorithm = field("KeyCheckValueAlgorithm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WrappedKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WrappedKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAliasInput:
    boto3_raw_data: "type_defs.GetAliasInputTypeDef" = dataclasses.field()

    AliasName = field("AliasName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAliasInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyInput:
    boto3_raw_data: "type_defs.GetKeyInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKeyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetKeyInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersForExportInput:
    boto3_raw_data: "type_defs.GetParametersForExportInputTypeDef" = dataclasses.field()

    KeyMaterialType = field("KeyMaterialType")
    SigningKeyAlgorithm = field("SigningKeyAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersForExportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersForExportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersForImportInput:
    boto3_raw_data: "type_defs.GetParametersForImportInputTypeDef" = dataclasses.field()

    KeyMaterialType = field("KeyMaterialType")
    WrappingKeyAlgorithm = field("WrappingKeyAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersForImportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersForImportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyCertificateInput:
    boto3_raw_data: "type_defs.GetPublicKeyCertificateInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyCertificateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyCertificateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTr31KeyBlock:
    boto3_raw_data: "type_defs.ImportTr31KeyBlockTypeDef" = dataclasses.field()

    WrappingKeyIdentifier = field("WrappingKeyIdentifier")
    WrappedKeyBlock = field("WrappedKeyBlock")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTr31KeyBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTr31KeyBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTr34KeyBlock:
    boto3_raw_data: "type_defs.ImportTr34KeyBlockTypeDef" = dataclasses.field()

    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )
    SigningKeyCertificate = field("SigningKeyCertificate")
    WrappedKeyBlock = field("WrappedKeyBlock")
    KeyBlockFormat = field("KeyBlockFormat")
    ImportToken = field("ImportToken")
    WrappingKeyIdentifier = field("WrappingKeyIdentifier")
    WrappingKeyCertificate = field("WrappingKeyCertificate")
    RandomNonce = field("RandomNonce")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTr34KeyBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTr34KeyBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyModesOfUse:
    boto3_raw_data: "type_defs.KeyModesOfUseTypeDef" = dataclasses.field()

    Encrypt = field("Encrypt")
    Decrypt = field("Decrypt")
    Wrap = field("Wrap")
    Unwrap = field("Unwrap")
    Generate = field("Generate")
    Sign = field("Sign")
    Verify = field("Verify")
    DeriveKey = field("DeriveKey")
    NoRestrictions = field("NoRestrictions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyModesOfUseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyModesOfUseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationStatusType:
    boto3_raw_data: "type_defs.ReplicationStatusTypeTypeDef" = dataclasses.field()

    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationStatusTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationStatusTypeTypeDef"]
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
class ListAliasesInput:
    boto3_raw_data: "type_defs.ListAliasesInputTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAliasesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysInput:
    boto3_raw_data: "type_defs.ListKeysInputTypeDef" = dataclasses.field()

    KeyState = field("KeyState")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListKeysInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListKeysInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveKeyReplicationRegionsInput:
    boto3_raw_data: "type_defs.RemoveKeyReplicationRegionsInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")
    ReplicationRegions = field("ReplicationRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveKeyReplicationRegionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveKeyReplicationRegionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreKeyInput:
    boto3_raw_data: "type_defs.RestoreKeyInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreKeyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestoreKeyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartKeyUsageInput:
    boto3_raw_data: "type_defs.StartKeyUsageInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartKeyUsageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartKeyUsageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopKeyUsageInput:
    boto3_raw_data: "type_defs.StopKeyUsageInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopKeyUsageInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopKeyUsageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAliasInput:
    boto3_raw_data: "type_defs.UpdateAliasInputTypeDef" = dataclasses.field()

    AliasName = field("AliasName")
    KeyArn = field("KeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAliasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAliasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDefaultKeyReplicationRegionsOutput:
    boto3_raw_data: "type_defs.DisableDefaultKeyReplicationRegionsOutputTypeDef" = (
        dataclasses.field()
    )

    EnabledReplicationRegions = field("EnabledReplicationRegions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableDefaultKeyReplicationRegionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDefaultKeyReplicationRegionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDefaultKeyReplicationRegionsOutput:
    boto3_raw_data: "type_defs.EnableDefaultKeyReplicationRegionsOutputTypeDef" = (
        dataclasses.field()
    )

    EnabledReplicationRegions = field("EnabledReplicationRegions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableDefaultKeyReplicationRegionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDefaultKeyReplicationRegionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateSigningRequestOutput:
    boto3_raw_data: "type_defs.GetCertificateSigningRequestOutputTypeDef" = (
        dataclasses.field()
    )

    CertificateSigningRequest = field("CertificateSigningRequest")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateSigningRequestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateSigningRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDefaultKeyReplicationRegionsOutput:
    boto3_raw_data: "type_defs.GetDefaultKeyReplicationRegionsOutputTypeDef" = (
        dataclasses.field()
    )

    EnabledReplicationRegions = field("EnabledReplicationRegions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDefaultKeyReplicationRegionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDefaultKeyReplicationRegionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersForExportOutput:
    boto3_raw_data: "type_defs.GetParametersForExportOutputTypeDef" = (
        dataclasses.field()
    )

    SigningKeyCertificate = field("SigningKeyCertificate")
    SigningKeyCertificateChain = field("SigningKeyCertificateChain")
    SigningKeyAlgorithm = field("SigningKeyAlgorithm")
    ExportToken = field("ExportToken")
    ParametersValidUntilTimestamp = field("ParametersValidUntilTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersForExportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersForExportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersForImportOutput:
    boto3_raw_data: "type_defs.GetParametersForImportOutputTypeDef" = (
        dataclasses.field()
    )

    WrappingKeyCertificate = field("WrappingKeyCertificate")
    WrappingKeyCertificateChain = field("WrappingKeyCertificateChain")
    WrappingKeyAlgorithm = field("WrappingKeyAlgorithm")
    ImportToken = field("ImportToken")
    ParametersValidUntilTimestamp = field("ParametersValidUntilTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersForImportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersForImportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyCertificateOutput:
    boto3_raw_data: "type_defs.GetPublicKeyCertificateOutputTypeDef" = (
        dataclasses.field()
    )

    KeyCertificate = field("KeyCertificate")
    KeyCertificateChain = field("KeyCertificateChain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPublicKeyCertificateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyCertificateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasOutput:
    boto3_raw_data: "type_defs.CreateAliasOutputTypeDef" = dataclasses.field()

    @cached_property
    def Alias(self):  # pragma: no cover
        return Alias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAliasOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAliasOutput:
    boto3_raw_data: "type_defs.GetAliasOutputTypeDef" = dataclasses.field()

    @cached_property
    def Alias(self):  # pragma: no cover
        return Alias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAliasOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAliasOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesOutput:
    boto3_raw_data: "type_defs.ListAliasesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAliasesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAliasOutput:
    boto3_raw_data: "type_defs.UpdateAliasOutputTypeDef" = dataclasses.field()

    @cached_property
    def Alias(self):  # pragma: no cover
        return Alias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAliasOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAliasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateSigningRequestInput:
    boto3_raw_data: "type_defs.GetCertificateSigningRequestInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")
    SigningAlgorithm = field("SigningAlgorithm")

    @cached_property
    def CertificateSubject(self):  # pragma: no cover
        return CertificateSubjectType.make_one(
            self.boto3_raw_data["CertificateSubject"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateSigningRequestInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateSigningRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDiffieHellmanTr31KeyBlock:
    boto3_raw_data: "type_defs.ImportDiffieHellmanTr31KeyBlockTypeDef" = (
        dataclasses.field()
    )

    PrivateKeyIdentifier = field("PrivateKeyIdentifier")
    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )
    PublicKeyCertificate = field("PublicKeyCertificate")
    DeriveKeyAlgorithm = field("DeriveKeyAlgorithm")
    KeyDerivationFunction = field("KeyDerivationFunction")
    KeyDerivationHashAlgorithm = field("KeyDerivationHashAlgorithm")

    @cached_property
    def DerivationData(self):  # pragma: no cover
        return DiffieHellmanDerivationData.make_one(
            self.boto3_raw_data["DerivationData"]
        )

    WrappedKeyBlock = field("WrappedKeyBlock")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportDiffieHellmanTr31KeyBlockTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDiffieHellmanTr31KeyBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAttributes:
    boto3_raw_data: "type_defs.ExportAttributesTypeDef" = dataclasses.field()

    @cached_property
    def ExportDukptInitialKey(self):  # pragma: no cover
        return ExportDukptInitialKey.make_one(
            self.boto3_raw_data["ExportDukptInitialKey"]
        )

    KeyCheckValueAlgorithm = field("KeyCheckValueAlgorithm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportKeyOutput:
    boto3_raw_data: "type_defs.ExportKeyOutputTypeDef" = dataclasses.field()

    @cached_property
    def WrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["WrappedKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportKeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportKeyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyAttributes:
    boto3_raw_data: "type_defs.KeyAttributesTypeDef" = dataclasses.field()

    KeyUsage = field("KeyUsage")
    KeyClass = field("KeyClass")
    KeyAlgorithm = field("KeyAlgorithm")

    @cached_property
    def KeyModesOfUse(self):  # pragma: no cover
        return KeyModesOfUse.make_one(self.boto3_raw_data["KeyModesOfUse"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyBlockHeaders:
    boto3_raw_data: "type_defs.KeyBlockHeadersTypeDef" = dataclasses.field()

    @cached_property
    def KeyModesOfUse(self):  # pragma: no cover
        return KeyModesOfUse.make_one(self.boto3_raw_data["KeyModesOfUse"])

    KeyExportability = field("KeyExportability")
    KeyVersion = field("KeyVersion")
    OptionalBlocks = field("OptionalBlocks")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyBlockHeadersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyBlockHeadersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesInputPaginate:
    boto3_raw_data: "type_defs.ListAliasesInputPaginateTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysInputPaginate:
    boto3_raw_data: "type_defs.ListKeysInputPaginateTypeDef" = dataclasses.field()

    KeyState = field("KeyState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeysInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeysInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyInput:
    boto3_raw_data: "type_defs.CreateKeyInputTypeDef" = dataclasses.field()

    @cached_property
    def KeyAttributes(self):  # pragma: no cover
        return KeyAttributes.make_one(self.boto3_raw_data["KeyAttributes"])

    Exportable = field("Exportable")
    KeyCheckValueAlgorithm = field("KeyCheckValueAlgorithm")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DeriveKeyUsage = field("DeriveKeyUsage")
    ReplicationRegions = field("ReplicationRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateKeyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateKeyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyCryptogram:
    boto3_raw_data: "type_defs.ImportKeyCryptogramTypeDef" = dataclasses.field()

    @cached_property
    def KeyAttributes(self):  # pragma: no cover
        return KeyAttributes.make_one(self.boto3_raw_data["KeyAttributes"])

    Exportable = field("Exportable")
    WrappedKeyCryptogram = field("WrappedKeyCryptogram")
    ImportToken = field("ImportToken")
    WrappingSpec = field("WrappingSpec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportKeyCryptogramTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportKeyCryptogramTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeySummary:
    boto3_raw_data: "type_defs.KeySummaryTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyState = field("KeyState")

    @cached_property
    def KeyAttributes(self):  # pragma: no cover
        return KeyAttributes.make_one(self.boto3_raw_data["KeyAttributes"])

    KeyCheckValue = field("KeyCheckValue")
    Exportable = field("Exportable")
    Enabled = field("Enabled")
    MultiRegionKeyType = field("MultiRegionKeyType")
    PrimaryRegion = field("PrimaryRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeySummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Key:
    boto3_raw_data: "type_defs.KeyTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")

    @cached_property
    def KeyAttributes(self):  # pragma: no cover
        return KeyAttributes.make_one(self.boto3_raw_data["KeyAttributes"])

    KeyCheckValue = field("KeyCheckValue")
    KeyCheckValueAlgorithm = field("KeyCheckValueAlgorithm")
    Enabled = field("Enabled")
    Exportable = field("Exportable")
    KeyState = field("KeyState")
    KeyOrigin = field("KeyOrigin")
    CreateTimestamp = field("CreateTimestamp")
    UsageStartTimestamp = field("UsageStartTimestamp")
    UsageStopTimestamp = field("UsageStopTimestamp")
    DeletePendingTimestamp = field("DeletePendingTimestamp")
    DeleteTimestamp = field("DeleteTimestamp")
    DeriveKeyUsage = field("DeriveKeyUsage")
    MultiRegionKeyType = field("MultiRegionKeyType")
    PrimaryRegion = field("PrimaryRegion")
    ReplicationStatus = field("ReplicationStatus")
    UsingDefaultReplicationRegions = field("UsingDefaultReplicationRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RootCertificatePublicKey:
    boto3_raw_data: "type_defs.RootCertificatePublicKeyTypeDef" = dataclasses.field()

    @cached_property
    def KeyAttributes(self):  # pragma: no cover
        return KeyAttributes.make_one(self.boto3_raw_data["KeyAttributes"])

    PublicKeyCertificate = field("PublicKeyCertificate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RootCertificatePublicKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RootCertificatePublicKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedCertificatePublicKey:
    boto3_raw_data: "type_defs.TrustedCertificatePublicKeyTypeDef" = dataclasses.field()

    @cached_property
    def KeyAttributes(self):  # pragma: no cover
        return KeyAttributes.make_one(self.boto3_raw_data["KeyAttributes"])

    PublicKeyCertificate = field("PublicKeyCertificate")
    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedCertificatePublicKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedCertificatePublicKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDiffieHellmanTr31KeyBlock:
    boto3_raw_data: "type_defs.ExportDiffieHellmanTr31KeyBlockTypeDef" = (
        dataclasses.field()
    )

    PrivateKeyIdentifier = field("PrivateKeyIdentifier")
    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )
    PublicKeyCertificate = field("PublicKeyCertificate")
    DeriveKeyAlgorithm = field("DeriveKeyAlgorithm")
    KeyDerivationFunction = field("KeyDerivationFunction")
    KeyDerivationHashAlgorithm = field("KeyDerivationHashAlgorithm")

    @cached_property
    def DerivationData(self):  # pragma: no cover
        return DiffieHellmanDerivationData.make_one(
            self.boto3_raw_data["DerivationData"]
        )

    @cached_property
    def KeyBlockHeaders(self):  # pragma: no cover
        return KeyBlockHeaders.make_one(self.boto3_raw_data["KeyBlockHeaders"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportDiffieHellmanTr31KeyBlockTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDiffieHellmanTr31KeyBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTr31KeyBlock:
    boto3_raw_data: "type_defs.ExportTr31KeyBlockTypeDef" = dataclasses.field()

    WrappingKeyIdentifier = field("WrappingKeyIdentifier")

    @cached_property
    def KeyBlockHeaders(self):  # pragma: no cover
        return KeyBlockHeaders.make_one(self.boto3_raw_data["KeyBlockHeaders"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportTr31KeyBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTr31KeyBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTr34KeyBlock:
    boto3_raw_data: "type_defs.ExportTr34KeyBlockTypeDef" = dataclasses.field()

    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )
    WrappingKeyCertificate = field("WrappingKeyCertificate")
    KeyBlockFormat = field("KeyBlockFormat")
    ExportToken = field("ExportToken")
    SigningKeyIdentifier = field("SigningKeyIdentifier")
    SigningKeyCertificate = field("SigningKeyCertificate")
    RandomNonce = field("RandomNonce")

    @cached_property
    def KeyBlockHeaders(self):  # pragma: no cover
        return KeyBlockHeaders.make_one(self.boto3_raw_data["KeyBlockHeaders"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportTr34KeyBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTr34KeyBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysOutput:
    boto3_raw_data: "type_defs.ListKeysOutputTypeDef" = dataclasses.field()

    @cached_property
    def Keys(self):  # pragma: no cover
        return KeySummary.make_many(self.boto3_raw_data["Keys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListKeysOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListKeysOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddKeyReplicationRegionsOutput:
    boto3_raw_data: "type_defs.AddKeyReplicationRegionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddKeyReplicationRegionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddKeyReplicationRegionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyOutput:
    boto3_raw_data: "type_defs.CreateKeyOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateKeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateKeyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyOutput:
    boto3_raw_data: "type_defs.DeleteKeyOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteKeyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyOutput:
    boto3_raw_data: "type_defs.GetKeyOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetKeyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyOutput:
    boto3_raw_data: "type_defs.ImportKeyOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportKeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportKeyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveKeyReplicationRegionsOutput:
    boto3_raw_data: "type_defs.RemoveKeyReplicationRegionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveKeyReplicationRegionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveKeyReplicationRegionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreKeyOutput:
    boto3_raw_data: "type_defs.RestoreKeyOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreKeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreKeyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartKeyUsageOutput:
    boto3_raw_data: "type_defs.StartKeyUsageOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartKeyUsageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartKeyUsageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopKeyUsageOutput:
    boto3_raw_data: "type_defs.StopKeyUsageOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return Key.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopKeyUsageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopKeyUsageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyMaterial:
    boto3_raw_data: "type_defs.ImportKeyMaterialTypeDef" = dataclasses.field()

    @cached_property
    def RootCertificatePublicKey(self):  # pragma: no cover
        return RootCertificatePublicKey.make_one(
            self.boto3_raw_data["RootCertificatePublicKey"]
        )

    @cached_property
    def TrustedCertificatePublicKey(self):  # pragma: no cover
        return TrustedCertificatePublicKey.make_one(
            self.boto3_raw_data["TrustedCertificatePublicKey"]
        )

    @cached_property
    def Tr31KeyBlock(self):  # pragma: no cover
        return ImportTr31KeyBlock.make_one(self.boto3_raw_data["Tr31KeyBlock"])

    @cached_property
    def Tr34KeyBlock(self):  # pragma: no cover
        return ImportTr34KeyBlock.make_one(self.boto3_raw_data["Tr34KeyBlock"])

    @cached_property
    def KeyCryptogram(self):  # pragma: no cover
        return ImportKeyCryptogram.make_one(self.boto3_raw_data["KeyCryptogram"])

    @cached_property
    def DiffieHellmanTr31KeyBlock(self):  # pragma: no cover
        return ImportDiffieHellmanTr31KeyBlock.make_one(
            self.boto3_raw_data["DiffieHellmanTr31KeyBlock"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportKeyMaterialTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportKeyMaterialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportKeyMaterial:
    boto3_raw_data: "type_defs.ExportKeyMaterialTypeDef" = dataclasses.field()

    @cached_property
    def Tr31KeyBlock(self):  # pragma: no cover
        return ExportTr31KeyBlock.make_one(self.boto3_raw_data["Tr31KeyBlock"])

    @cached_property
    def Tr34KeyBlock(self):  # pragma: no cover
        return ExportTr34KeyBlock.make_one(self.boto3_raw_data["Tr34KeyBlock"])

    @cached_property
    def KeyCryptogram(self):  # pragma: no cover
        return ExportKeyCryptogram.make_one(self.boto3_raw_data["KeyCryptogram"])

    @cached_property
    def DiffieHellmanTr31KeyBlock(self):  # pragma: no cover
        return ExportDiffieHellmanTr31KeyBlock.make_one(
            self.boto3_raw_data["DiffieHellmanTr31KeyBlock"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportKeyMaterialTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportKeyMaterialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyInput:
    boto3_raw_data: "type_defs.ImportKeyInputTypeDef" = dataclasses.field()

    @cached_property
    def KeyMaterial(self):  # pragma: no cover
        return ImportKeyMaterial.make_one(self.boto3_raw_data["KeyMaterial"])

    KeyCheckValueAlgorithm = field("KeyCheckValueAlgorithm")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ReplicationRegions = field("ReplicationRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportKeyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportKeyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportKeyInput:
    boto3_raw_data: "type_defs.ExportKeyInputTypeDef" = dataclasses.field()

    @cached_property
    def KeyMaterial(self):  # pragma: no cover
        return ExportKeyMaterial.make_one(self.boto3_raw_data["KeyMaterial"])

    ExportKeyIdentifier = field("ExportKeyIdentifier")

    @cached_property
    def ExportAttributes(self):  # pragma: no cover
        return ExportAttributes.make_one(self.boto3_raw_data["ExportAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportKeyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportKeyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
