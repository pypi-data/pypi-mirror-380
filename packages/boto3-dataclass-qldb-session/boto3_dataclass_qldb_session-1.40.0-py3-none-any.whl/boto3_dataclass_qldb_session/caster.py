# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qldb_session import type_defs as bs_td


class QLDB_SESSIONCaster:

    def send_command(
        self,
        res: "bs_td.SendCommandResultTypeDef",
    ) -> "dc_td.SendCommandResult":
        return dc_td.SendCommandResult.make_one(res)


qldb_session_caster = QLDB_SESSIONCaster()
