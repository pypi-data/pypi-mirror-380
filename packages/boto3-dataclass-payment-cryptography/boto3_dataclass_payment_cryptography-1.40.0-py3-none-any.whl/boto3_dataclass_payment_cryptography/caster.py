# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_payment_cryptography import type_defs as bs_td


class PAYMENT_CRYPTOGRAPHYCaster:

    def add_key_replication_regions(
        self,
        res: "bs_td.AddKeyReplicationRegionsOutputTypeDef",
    ) -> "dc_td.AddKeyReplicationRegionsOutput":
        return dc_td.AddKeyReplicationRegionsOutput.make_one(res)

    def create_alias(
        self,
        res: "bs_td.CreateAliasOutputTypeDef",
    ) -> "dc_td.CreateAliasOutput":
        return dc_td.CreateAliasOutput.make_one(res)

    def create_key(
        self,
        res: "bs_td.CreateKeyOutputTypeDef",
    ) -> "dc_td.CreateKeyOutput":
        return dc_td.CreateKeyOutput.make_one(res)

    def delete_key(
        self,
        res: "bs_td.DeleteKeyOutputTypeDef",
    ) -> "dc_td.DeleteKeyOutput":
        return dc_td.DeleteKeyOutput.make_one(res)

    def disable_default_key_replication_regions(
        self,
        res: "bs_td.DisableDefaultKeyReplicationRegionsOutputTypeDef",
    ) -> "dc_td.DisableDefaultKeyReplicationRegionsOutput":
        return dc_td.DisableDefaultKeyReplicationRegionsOutput.make_one(res)

    def enable_default_key_replication_regions(
        self,
        res: "bs_td.EnableDefaultKeyReplicationRegionsOutputTypeDef",
    ) -> "dc_td.EnableDefaultKeyReplicationRegionsOutput":
        return dc_td.EnableDefaultKeyReplicationRegionsOutput.make_one(res)

    def export_key(
        self,
        res: "bs_td.ExportKeyOutputTypeDef",
    ) -> "dc_td.ExportKeyOutput":
        return dc_td.ExportKeyOutput.make_one(res)

    def get_alias(
        self,
        res: "bs_td.GetAliasOutputTypeDef",
    ) -> "dc_td.GetAliasOutput":
        return dc_td.GetAliasOutput.make_one(res)

    def get_certificate_signing_request(
        self,
        res: "bs_td.GetCertificateSigningRequestOutputTypeDef",
    ) -> "dc_td.GetCertificateSigningRequestOutput":
        return dc_td.GetCertificateSigningRequestOutput.make_one(res)

    def get_default_key_replication_regions(
        self,
        res: "bs_td.GetDefaultKeyReplicationRegionsOutputTypeDef",
    ) -> "dc_td.GetDefaultKeyReplicationRegionsOutput":
        return dc_td.GetDefaultKeyReplicationRegionsOutput.make_one(res)

    def get_key(
        self,
        res: "bs_td.GetKeyOutputTypeDef",
    ) -> "dc_td.GetKeyOutput":
        return dc_td.GetKeyOutput.make_one(res)

    def get_parameters_for_export(
        self,
        res: "bs_td.GetParametersForExportOutputTypeDef",
    ) -> "dc_td.GetParametersForExportOutput":
        return dc_td.GetParametersForExportOutput.make_one(res)

    def get_parameters_for_import(
        self,
        res: "bs_td.GetParametersForImportOutputTypeDef",
    ) -> "dc_td.GetParametersForImportOutput":
        return dc_td.GetParametersForImportOutput.make_one(res)

    def get_public_key_certificate(
        self,
        res: "bs_td.GetPublicKeyCertificateOutputTypeDef",
    ) -> "dc_td.GetPublicKeyCertificateOutput":
        return dc_td.GetPublicKeyCertificateOutput.make_one(res)

    def import_key(
        self,
        res: "bs_td.ImportKeyOutputTypeDef",
    ) -> "dc_td.ImportKeyOutput":
        return dc_td.ImportKeyOutput.make_one(res)

    def list_aliases(
        self,
        res: "bs_td.ListAliasesOutputTypeDef",
    ) -> "dc_td.ListAliasesOutput":
        return dc_td.ListAliasesOutput.make_one(res)

    def list_keys(
        self,
        res: "bs_td.ListKeysOutputTypeDef",
    ) -> "dc_td.ListKeysOutput":
        return dc_td.ListKeysOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def remove_key_replication_regions(
        self,
        res: "bs_td.RemoveKeyReplicationRegionsOutputTypeDef",
    ) -> "dc_td.RemoveKeyReplicationRegionsOutput":
        return dc_td.RemoveKeyReplicationRegionsOutput.make_one(res)

    def restore_key(
        self,
        res: "bs_td.RestoreKeyOutputTypeDef",
    ) -> "dc_td.RestoreKeyOutput":
        return dc_td.RestoreKeyOutput.make_one(res)

    def start_key_usage(
        self,
        res: "bs_td.StartKeyUsageOutputTypeDef",
    ) -> "dc_td.StartKeyUsageOutput":
        return dc_td.StartKeyUsageOutput.make_one(res)

    def stop_key_usage(
        self,
        res: "bs_td.StopKeyUsageOutputTypeDef",
    ) -> "dc_td.StopKeyUsageOutput":
        return dc_td.StopKeyUsageOutput.make_one(res)

    def update_alias(
        self,
        res: "bs_td.UpdateAliasOutputTypeDef",
    ) -> "dc_td.UpdateAliasOutput":
        return dc_td.UpdateAliasOutput.make_one(res)


payment_cryptography_caster = PAYMENT_CRYPTOGRAPHYCaster()
