# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_featurestore_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BatchGetRecordError:
    boto3_raw_data: "type_defs.BatchGetRecordErrorTypeDef" = dataclasses.field()

    FeatureGroupName = field("FeatureGroupName")
    RecordIdentifierValueAsString = field("RecordIdentifierValueAsString")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRecordErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRecordErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRecordIdentifierOutput:
    boto3_raw_data: "type_defs.BatchGetRecordIdentifierOutputTypeDef" = (
        dataclasses.field()
    )

    FeatureGroupName = field("FeatureGroupName")
    RecordIdentifiersValueAsString = field("RecordIdentifiersValueAsString")
    FeatureNames = field("FeatureNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetRecordIdentifierOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRecordIdentifierOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRecordIdentifier:
    boto3_raw_data: "type_defs.BatchGetRecordIdentifierTypeDef" = dataclasses.field()

    FeatureGroupName = field("FeatureGroupName")
    RecordIdentifiersValueAsString = field("RecordIdentifiersValueAsString")
    FeatureNames = field("FeatureNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRecordIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRecordIdentifierTypeDef"]
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
class FeatureValueOutput:
    boto3_raw_data: "type_defs.FeatureValueOutputTypeDef" = dataclasses.field()

    FeatureName = field("FeatureName")
    ValueAsString = field("ValueAsString")
    ValueAsStringList = field("ValueAsStringList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeatureValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeatureValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecordRequest:
    boto3_raw_data: "type_defs.DeleteRecordRequestTypeDef" = dataclasses.field()

    FeatureGroupName = field("FeatureGroupName")
    RecordIdentifierValueAsString = field("RecordIdentifierValueAsString")
    EventTime = field("EventTime")
    TargetStores = field("TargetStores")
    DeletionMode = field("DeletionMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRecordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeatureValue:
    boto3_raw_data: "type_defs.FeatureValueTypeDef" = dataclasses.field()

    FeatureName = field("FeatureName")
    ValueAsString = field("ValueAsString")
    ValueAsStringList = field("ValueAsStringList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeatureValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FeatureValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecordRequest:
    boto3_raw_data: "type_defs.GetRecordRequestTypeDef" = dataclasses.field()

    FeatureGroupName = field("FeatureGroupName")
    RecordIdentifierValueAsString = field("RecordIdentifierValueAsString")
    FeatureNames = field("FeatureNames")
    ExpirationTimeResponse = field("ExpirationTimeResponse")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TtlDuration:
    boto3_raw_data: "type_defs.TtlDurationTypeDef" = dataclasses.field()

    Unit = field("Unit")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TtlDurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TtlDurationTypeDef"]]
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
class BatchGetRecordResultDetail:
    boto3_raw_data: "type_defs.BatchGetRecordResultDetailTypeDef" = dataclasses.field()

    FeatureGroupName = field("FeatureGroupName")
    RecordIdentifierValueAsString = field("RecordIdentifierValueAsString")

    @cached_property
    def Record(self):  # pragma: no cover
        return FeatureValueOutput.make_many(self.boto3_raw_data["Record"])

    ExpiresAt = field("ExpiresAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRecordResultDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRecordResultDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecordResponse:
    boto3_raw_data: "type_defs.GetRecordResponseTypeDef" = dataclasses.field()

    @cached_property
    def Record(self):  # pragma: no cover
        return FeatureValueOutput.make_many(self.boto3_raw_data["Record"])

    ExpiresAt = field("ExpiresAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecordResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRecordRequest:
    boto3_raw_data: "type_defs.BatchGetRecordRequestTypeDef" = dataclasses.field()

    Identifiers = field("Identifiers")
    ExpirationTimeResponse = field("ExpirationTimeResponse")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRecordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRecordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRecordResponse:
    boto3_raw_data: "type_defs.BatchGetRecordResponseTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return BatchGetRecordResultDetail.make_many(self.boto3_raw_data["Records"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchGetRecordError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def UnprocessedIdentifiers(self):  # pragma: no cover
        return BatchGetRecordIdentifierOutput.make_many(
            self.boto3_raw_data["UnprocessedIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRecordResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRecordResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordRequest:
    boto3_raw_data: "type_defs.PutRecordRequestTypeDef" = dataclasses.field()

    FeatureGroupName = field("FeatureGroupName")
    Record = field("Record")
    TargetStores = field("TargetStores")

    @cached_property
    def TtlDuration(self):  # pragma: no cover
        return TtlDuration.make_one(self.boto3_raw_data["TtlDuration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
