# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_keyspacesstreams import type_defs as bs_td


class KEYSPACESSTREAMSCaster:

    def get_records(
        self,
        res: "bs_td.GetRecordsOutputTypeDef",
    ) -> "dc_td.GetRecordsOutput":
        return dc_td.GetRecordsOutput.make_one(res)

    def get_shard_iterator(
        self,
        res: "bs_td.GetShardIteratorOutputTypeDef",
    ) -> "dc_td.GetShardIteratorOutput":
        return dc_td.GetShardIteratorOutput.make_one(res)

    def get_stream(
        self,
        res: "bs_td.GetStreamOutputTypeDef",
    ) -> "dc_td.GetStreamOutput":
        return dc_td.GetStreamOutput.make_one(res)

    def list_streams(
        self,
        res: "bs_td.ListStreamsOutputTypeDef",
    ) -> "dc_td.ListStreamsOutput":
        return dc_td.ListStreamsOutput.make_one(res)


keyspacesstreams_caster = KEYSPACESSTREAMSCaster()
