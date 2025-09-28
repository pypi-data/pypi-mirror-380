# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qldb_session import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class TimingInformation:
    boto3_raw_data: "type_defs.TimingInformationTypeDef" = dataclasses.field()

    ProcessingTimeMilliseconds = field("ProcessingTimeMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimingInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimingInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IOUsage:
    boto3_raw_data: "type_defs.IOUsageTypeDef" = dataclasses.field()

    ReadIOs = field("ReadIOs")
    WriteIOs = field("WriteIOs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IOUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IOUsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FetchPageRequest:
    boto3_raw_data: "type_defs.FetchPageRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FetchPageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FetchPageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueHolderOutput:
    boto3_raw_data: "type_defs.ValueHolderOutputTypeDef" = dataclasses.field()

    IonBinary = field("IonBinary")
    IonText = field("IonText")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueHolderOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValueHolderOutputTypeDef"]
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
class StartSessionRequest:
    boto3_raw_data: "type_defs.StartSessionRequestTypeDef" = dataclasses.field()

    LedgerName = field("LedgerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortTransactionResult:
    boto3_raw_data: "type_defs.AbortTransactionResultTypeDef" = dataclasses.field()

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AbortTransactionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortTransactionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndSessionResult:
    boto3_raw_data: "type_defs.EndSessionResultTypeDef" = dataclasses.field()

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndSessionResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndSessionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSessionResult:
    boto3_raw_data: "type_defs.StartSessionResultTypeDef" = dataclasses.field()

    SessionToken = field("SessionToken")

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSessionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTransactionResult:
    boto3_raw_data: "type_defs.StartTransactionResultTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTransactionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTransactionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitTransactionRequest:
    boto3_raw_data: "type_defs.CommitTransactionRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")
    CommitDigest = field("CommitDigest")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueHolder:
    boto3_raw_data: "type_defs.ValueHolderTypeDef" = dataclasses.field()

    IonBinary = field("IonBinary")
    IonText = field("IonText")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueHolderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueHolderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitTransactionResult:
    boto3_raw_data: "type_defs.CommitTransactionResultTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")
    CommitDigest = field("CommitDigest")

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @cached_property
    def ConsumedIOs(self):  # pragma: no cover
        return IOUsage.make_one(self.boto3_raw_data["ConsumedIOs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitTransactionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitTransactionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Page:
    boto3_raw_data: "type_defs.PageTypeDef" = dataclasses.field()

    @cached_property
    def Values(self):  # pragma: no cover
        return ValueHolderOutput.make_many(self.boto3_raw_data["Values"])

    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementResult:
    boto3_raw_data: "type_defs.ExecuteStatementResultTypeDef" = dataclasses.field()

    @cached_property
    def FirstPage(self):  # pragma: no cover
        return Page.make_one(self.boto3_raw_data["FirstPage"])

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @cached_property
    def ConsumedIOs(self):  # pragma: no cover
        return IOUsage.make_one(self.boto3_raw_data["ConsumedIOs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FetchPageResult:
    boto3_raw_data: "type_defs.FetchPageResultTypeDef" = dataclasses.field()

    @cached_property
    def Page(self):  # pragma: no cover
        return Page.make_one(self.boto3_raw_data["Page"])

    @cached_property
    def TimingInformation(self):  # pragma: no cover
        return TimingInformation.make_one(self.boto3_raw_data["TimingInformation"])

    @cached_property
    def ConsumedIOs(self):  # pragma: no cover
        return IOUsage.make_one(self.boto3_raw_data["ConsumedIOs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FetchPageResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FetchPageResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementRequest:
    boto3_raw_data: "type_defs.ExecuteStatementRequestTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")
    Statement = field("Statement")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCommandResult:
    boto3_raw_data: "type_defs.SendCommandResultTypeDef" = dataclasses.field()

    @cached_property
    def StartSession(self):  # pragma: no cover
        return StartSessionResult.make_one(self.boto3_raw_data["StartSession"])

    @cached_property
    def StartTransaction(self):  # pragma: no cover
        return StartTransactionResult.make_one(self.boto3_raw_data["StartTransaction"])

    @cached_property
    def EndSession(self):  # pragma: no cover
        return EndSessionResult.make_one(self.boto3_raw_data["EndSession"])

    @cached_property
    def CommitTransaction(self):  # pragma: no cover
        return CommitTransactionResult.make_one(
            self.boto3_raw_data["CommitTransaction"]
        )

    @cached_property
    def AbortTransaction(self):  # pragma: no cover
        return AbortTransactionResult.make_one(self.boto3_raw_data["AbortTransaction"])

    @cached_property
    def ExecuteStatement(self):  # pragma: no cover
        return ExecuteStatementResult.make_one(self.boto3_raw_data["ExecuteStatement"])

    @cached_property
    def FetchPage(self):  # pragma: no cover
        return FetchPageResult.make_one(self.boto3_raw_data["FetchPage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendCommandResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCommandResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCommandRequest:
    boto3_raw_data: "type_defs.SendCommandRequestTypeDef" = dataclasses.field()

    SessionToken = field("SessionToken")

    @cached_property
    def StartSession(self):  # pragma: no cover
        return StartSessionRequest.make_one(self.boto3_raw_data["StartSession"])

    StartTransaction = field("StartTransaction")
    EndSession = field("EndSession")

    @cached_property
    def CommitTransaction(self):  # pragma: no cover
        return CommitTransactionRequest.make_one(
            self.boto3_raw_data["CommitTransaction"]
        )

    AbortTransaction = field("AbortTransaction")

    @cached_property
    def ExecuteStatement(self):  # pragma: no cover
        return ExecuteStatementRequest.make_one(self.boto3_raw_data["ExecuteStatement"])

    @cached_property
    def FetchPage(self):  # pragma: no cover
        return FetchPageRequest.make_one(self.boto3_raw_data["FetchPage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
