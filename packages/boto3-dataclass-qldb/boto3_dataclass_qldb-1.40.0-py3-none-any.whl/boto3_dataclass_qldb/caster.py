# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qldb import type_defs as bs_td


class QLDBCaster:

    def cancel_journal_kinesis_stream(
        self,
        res: "bs_td.CancelJournalKinesisStreamResponseTypeDef",
    ) -> "dc_td.CancelJournalKinesisStreamResponse":
        return dc_td.CancelJournalKinesisStreamResponse.make_one(res)

    def create_ledger(
        self,
        res: "bs_td.CreateLedgerResponseTypeDef",
    ) -> "dc_td.CreateLedgerResponse":
        return dc_td.CreateLedgerResponse.make_one(res)

    def delete_ledger(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_journal_kinesis_stream(
        self,
        res: "bs_td.DescribeJournalKinesisStreamResponseTypeDef",
    ) -> "dc_td.DescribeJournalKinesisStreamResponse":
        return dc_td.DescribeJournalKinesisStreamResponse.make_one(res)

    def describe_journal_s3_export(
        self,
        res: "bs_td.DescribeJournalS3ExportResponseTypeDef",
    ) -> "dc_td.DescribeJournalS3ExportResponse":
        return dc_td.DescribeJournalS3ExportResponse.make_one(res)

    def describe_ledger(
        self,
        res: "bs_td.DescribeLedgerResponseTypeDef",
    ) -> "dc_td.DescribeLedgerResponse":
        return dc_td.DescribeLedgerResponse.make_one(res)

    def export_journal_to_s3(
        self,
        res: "bs_td.ExportJournalToS3ResponseTypeDef",
    ) -> "dc_td.ExportJournalToS3Response":
        return dc_td.ExportJournalToS3Response.make_one(res)

    def get_block(
        self,
        res: "bs_td.GetBlockResponseTypeDef",
    ) -> "dc_td.GetBlockResponse":
        return dc_td.GetBlockResponse.make_one(res)

    def get_digest(
        self,
        res: "bs_td.GetDigestResponseTypeDef",
    ) -> "dc_td.GetDigestResponse":
        return dc_td.GetDigestResponse.make_one(res)

    def get_revision(
        self,
        res: "bs_td.GetRevisionResponseTypeDef",
    ) -> "dc_td.GetRevisionResponse":
        return dc_td.GetRevisionResponse.make_one(res)

    def list_journal_kinesis_streams_for_ledger(
        self,
        res: "bs_td.ListJournalKinesisStreamsForLedgerResponseTypeDef",
    ) -> "dc_td.ListJournalKinesisStreamsForLedgerResponse":
        return dc_td.ListJournalKinesisStreamsForLedgerResponse.make_one(res)

    def list_journal_s3_exports(
        self,
        res: "bs_td.ListJournalS3ExportsResponseTypeDef",
    ) -> "dc_td.ListJournalS3ExportsResponse":
        return dc_td.ListJournalS3ExportsResponse.make_one(res)

    def list_journal_s3_exports_for_ledger(
        self,
        res: "bs_td.ListJournalS3ExportsForLedgerResponseTypeDef",
    ) -> "dc_td.ListJournalS3ExportsForLedgerResponse":
        return dc_td.ListJournalS3ExportsForLedgerResponse.make_one(res)

    def list_ledgers(
        self,
        res: "bs_td.ListLedgersResponseTypeDef",
    ) -> "dc_td.ListLedgersResponse":
        return dc_td.ListLedgersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def stream_journal_to_kinesis(
        self,
        res: "bs_td.StreamJournalToKinesisResponseTypeDef",
    ) -> "dc_td.StreamJournalToKinesisResponse":
        return dc_td.StreamJournalToKinesisResponse.make_one(res)

    def update_ledger(
        self,
        res: "bs_td.UpdateLedgerResponseTypeDef",
    ) -> "dc_td.UpdateLedgerResponse":
        return dc_td.UpdateLedgerResponse.make_one(res)

    def update_ledger_permissions_mode(
        self,
        res: "bs_td.UpdateLedgerPermissionsModeResponseTypeDef",
    ) -> "dc_td.UpdateLedgerPermissionsModeResponse":
        return dc_td.UpdateLedgerPermissionsModeResponse.make_one(res)


qldb_caster = QLDBCaster()
