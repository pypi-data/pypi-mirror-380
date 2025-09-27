# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesisanalytics import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOption:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionTypeDef" = dataclasses.field()

    LogStreamARN = field("LogStreamARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLoggingOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOptionDescription:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionDescriptionTypeDef" = (
        dataclasses.field()
    )

    LogStreamARN = field("LogStreamARN")
    RoleARN = field("RoleARN")
    CloudWatchLoggingOptionId = field("CloudWatchLoggingOptionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchLoggingOptionDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSummary:
    boto3_raw_data: "type_defs.ApplicationSummaryTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    ApplicationARN = field("ApplicationARN")
    ApplicationStatus = field("ApplicationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOptionUpdate:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionUpdateTypeDef" = (
        dataclasses.field()
    )

    CloudWatchLoggingOptionId = field("CloudWatchLoggingOptionId")
    LogStreamARNUpdate = field("LogStreamARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLoggingOptionUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSVMappingParameters:
    boto3_raw_data: "type_defs.CSVMappingParametersTypeDef" = dataclasses.field()

    RecordRowDelimiter = field("RecordRowDelimiter")
    RecordColumnDelimiter = field("RecordColumnDelimiter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CSVMappingParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CSVMappingParametersTypeDef"]
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
class DeleteApplicationCloudWatchLoggingOptionRequest:
    boto3_raw_data: (
        "type_defs.DeleteApplicationCloudWatchLoggingOptionRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    CloudWatchLoggingOptionId = field("CloudWatchLoggingOptionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationCloudWatchLoggingOptionRequestTypeDef"
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
                "type_defs.DeleteApplicationCloudWatchLoggingOptionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationInputProcessingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteApplicationInputProcessingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    InputId = field("InputId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationInputProcessingConfigurationRequestTypeDef"
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
                "type_defs.DeleteApplicationInputProcessingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationOutputRequest:
    boto3_raw_data: "type_defs.DeleteApplicationOutputRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    OutputId = field("OutputId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApplicationOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationReferenceDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteApplicationReferenceDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    ReferenceId = field("ReferenceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationReferenceDataSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationReferenceDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationRequest:
    boto3_raw_data: "type_defs.DescribeApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationSchema:
    boto3_raw_data: "type_defs.DestinationSchemaTypeDef" = dataclasses.field()

    RecordFormatType = field("RecordFormatType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputStartingPositionConfiguration:
    boto3_raw_data: "type_defs.InputStartingPositionConfigurationTypeDef" = (
        dataclasses.field()
    )

    InputStartingPosition = field("InputStartingPosition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputStartingPositionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputStartingPositionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Configuration:
    boto3_raw_data: "type_defs.S3ConfigurationTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")
    FileKey = field("FileKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputParallelism:
    boto3_raw_data: "type_defs.InputParallelismTypeDef" = dataclasses.field()

    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputParallelismTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputParallelismTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseInputDescription:
    boto3_raw_data: "type_defs.KinesisFirehoseInputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisFirehoseInputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseInputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsInputDescription:
    boto3_raw_data: "type_defs.KinesisStreamsInputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamsInputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsInputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLambdaProcessorDescription:
    boto3_raw_data: "type_defs.InputLambdaProcessorDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InputLambdaProcessorDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLambdaProcessorDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLambdaProcessor:
    boto3_raw_data: "type_defs.InputLambdaProcessorTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputLambdaProcessorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLambdaProcessorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLambdaProcessorUpdate:
    boto3_raw_data: "type_defs.InputLambdaProcessorUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputLambdaProcessorUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLambdaProcessorUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputParallelismUpdate:
    boto3_raw_data: "type_defs.InputParallelismUpdateTypeDef" = dataclasses.field()

    CountUpdate = field("CountUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputParallelismUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputParallelismUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordColumn:
    boto3_raw_data: "type_defs.RecordColumnTypeDef" = dataclasses.field()

    Name = field("Name")
    SqlType = field("SqlType")
    Mapping = field("Mapping")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordColumnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseInput:
    boto3_raw_data: "type_defs.KinesisFirehoseInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsInput:
    boto3_raw_data: "type_defs.KinesisStreamsInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseInputUpdate:
    boto3_raw_data: "type_defs.KinesisFirehoseInputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseInputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseInputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsInputUpdate:
    boto3_raw_data: "type_defs.KinesisStreamsInputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsInputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsInputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JSONMappingParameters:
    boto3_raw_data: "type_defs.JSONMappingParametersTypeDef" = dataclasses.field()

    RecordRowPath = field("RecordRowPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JSONMappingParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JSONMappingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseOutputDescription:
    boto3_raw_data: "type_defs.KinesisFirehoseOutputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisFirehoseOutputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseOutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseOutput:
    boto3_raw_data: "type_defs.KinesisFirehoseOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseOutputUpdate:
    boto3_raw_data: "type_defs.KinesisFirehoseOutputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseOutputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseOutputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsOutputDescription:
    boto3_raw_data: "type_defs.KinesisStreamsOutputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamsOutputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsOutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsOutput:
    boto3_raw_data: "type_defs.KinesisStreamsOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsOutputUpdate:
    boto3_raw_data: "type_defs.KinesisStreamsOutputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsOutputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsOutputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaOutputDescription:
    boto3_raw_data: "type_defs.LambdaOutputDescriptionTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaOutputDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaOutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaOutput:
    boto3_raw_data: "type_defs.LambdaOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaOutputUpdate:
    boto3_raw_data: "type_defs.LambdaOutputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")
    RoleARNUpdate = field("RoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaOutputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaOutputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    Limit = field("Limit")
    ExclusiveStartApplicationName = field("ExclusiveStartApplicationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class S3ReferenceDataSourceDescription:
    boto3_raw_data: "type_defs.S3ReferenceDataSourceDescriptionTypeDef" = (
        dataclasses.field()
    )

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")
    ReferenceRoleARN = field("ReferenceRoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ReferenceDataSourceDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReferenceDataSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReferenceDataSource:
    boto3_raw_data: "type_defs.S3ReferenceDataSourceTypeDef" = dataclasses.field()

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")
    ReferenceRoleARN = field("ReferenceRoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ReferenceDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReferenceDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReferenceDataSourceUpdate:
    boto3_raw_data: "type_defs.S3ReferenceDataSourceUpdateTypeDef" = dataclasses.field()

    BucketARNUpdate = field("BucketARNUpdate")
    FileKeyUpdate = field("FileKeyUpdate")
    ReferenceRoleARNUpdate = field("ReferenceRoleARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ReferenceDataSourceUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReferenceDataSourceUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopApplicationRequest:
    boto3_raw_data: "type_defs.StopApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopApplicationRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class AddApplicationCloudWatchLoggingOptionRequest:
    boto3_raw_data: "type_defs.AddApplicationCloudWatchLoggingOptionRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def CloudWatchLoggingOption(self):  # pragma: no cover
        return CloudWatchLoggingOption.make_one(
            self.boto3_raw_data["CloudWatchLoggingOption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationCloudWatchLoggingOptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationCloudWatchLoggingOptionRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationSummary(self):  # pragma: no cover
        return ApplicationSummary.make_one(self.boto3_raw_data["ApplicationSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationSummaries(self):  # pragma: no cover
        return ApplicationSummary.make_many(self.boto3_raw_data["ApplicationSummaries"])

    HasMoreApplications = field("HasMoreApplications")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
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
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CreateTimestamp = field("CreateTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConfiguration:
    boto3_raw_data: "type_defs.InputConfigurationTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def InputStartingPositionConfiguration(self):  # pragma: no cover
        return InputStartingPositionConfiguration.make_one(
            self.boto3_raw_data["InputStartingPositionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputProcessingConfigurationDescription:
    boto3_raw_data: "type_defs.InputProcessingConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputLambdaProcessorDescription(self):  # pragma: no cover
        return InputLambdaProcessorDescription.make_one(
            self.boto3_raw_data["InputLambdaProcessorDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputProcessingConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputProcessingConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputProcessingConfiguration:
    boto3_raw_data: "type_defs.InputProcessingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputLambdaProcessor(self):  # pragma: no cover
        return InputLambdaProcessor.make_one(
            self.boto3_raw_data["InputLambdaProcessor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputProcessingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputProcessingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputProcessingConfigurationUpdate:
    boto3_raw_data: "type_defs.InputProcessingConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputLambdaProcessorUpdate(self):  # pragma: no cover
        return InputLambdaProcessorUpdate.make_one(
            self.boto3_raw_data["InputLambdaProcessorUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputProcessingConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputProcessingConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MappingParameters:
    boto3_raw_data: "type_defs.MappingParametersTypeDef" = dataclasses.field()

    @cached_property
    def JSONMappingParameters(self):  # pragma: no cover
        return JSONMappingParameters.make_one(
            self.boto3_raw_data["JSONMappingParameters"]
        )

    @cached_property
    def CSVMappingParameters(self):  # pragma: no cover
        return CSVMappingParameters.make_one(
            self.boto3_raw_data["CSVMappingParameters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MappingParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MappingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDescription:
    boto3_raw_data: "type_defs.OutputDescriptionTypeDef" = dataclasses.field()

    OutputId = field("OutputId")
    Name = field("Name")

    @cached_property
    def KinesisStreamsOutputDescription(self):  # pragma: no cover
        return KinesisStreamsOutputDescription.make_one(
            self.boto3_raw_data["KinesisStreamsOutputDescription"]
        )

    @cached_property
    def KinesisFirehoseOutputDescription(self):  # pragma: no cover
        return KinesisFirehoseOutputDescription.make_one(
            self.boto3_raw_data["KinesisFirehoseOutputDescription"]
        )

    @cached_property
    def LambdaOutputDescription(self):  # pragma: no cover
        return LambdaOutputDescription.make_one(
            self.boto3_raw_data["LambdaOutputDescription"]
        )

    @cached_property
    def DestinationSchema(self):  # pragma: no cover
        return DestinationSchema.make_one(self.boto3_raw_data["DestinationSchema"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def DestinationSchema(self):  # pragma: no cover
        return DestinationSchema.make_one(self.boto3_raw_data["DestinationSchema"])

    @cached_property
    def KinesisStreamsOutput(self):  # pragma: no cover
        return KinesisStreamsOutput.make_one(
            self.boto3_raw_data["KinesisStreamsOutput"]
        )

    @cached_property
    def KinesisFirehoseOutput(self):  # pragma: no cover
        return KinesisFirehoseOutput.make_one(
            self.boto3_raw_data["KinesisFirehoseOutput"]
        )

    @cached_property
    def LambdaOutput(self):  # pragma: no cover
        return LambdaOutput.make_one(self.boto3_raw_data["LambdaOutput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputUpdate:
    boto3_raw_data: "type_defs.OutputUpdateTypeDef" = dataclasses.field()

    OutputId = field("OutputId")
    NameUpdate = field("NameUpdate")

    @cached_property
    def KinesisStreamsOutputUpdate(self):  # pragma: no cover
        return KinesisStreamsOutputUpdate.make_one(
            self.boto3_raw_data["KinesisStreamsOutputUpdate"]
        )

    @cached_property
    def KinesisFirehoseOutputUpdate(self):  # pragma: no cover
        return KinesisFirehoseOutputUpdate.make_one(
            self.boto3_raw_data["KinesisFirehoseOutputUpdate"]
        )

    @cached_property
    def LambdaOutputUpdate(self):  # pragma: no cover
        return LambdaOutputUpdate.make_one(self.boto3_raw_data["LambdaOutputUpdate"])

    @cached_property
    def DestinationSchemaUpdate(self):  # pragma: no cover
        return DestinationSchema.make_one(
            self.boto3_raw_data["DestinationSchemaUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartApplicationRequest:
    boto3_raw_data: "type_defs.StartApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")

    @cached_property
    def InputConfigurations(self):  # pragma: no cover
        return InputConfiguration.make_many(self.boto3_raw_data["InputConfigurations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationInputProcessingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.AddApplicationInputProcessingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    InputId = field("InputId")

    @cached_property
    def InputProcessingConfiguration(self):  # pragma: no cover
        return InputProcessingConfiguration.make_one(
            self.boto3_raw_data["InputProcessingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationInputProcessingConfigurationRequestTypeDef"
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
                "type_defs.AddApplicationInputProcessingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverInputSchemaRequest:
    boto3_raw_data: "type_defs.DiscoverInputSchemaRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @cached_property
    def InputStartingPositionConfiguration(self):  # pragma: no cover
        return InputStartingPositionConfiguration.make_one(
            self.boto3_raw_data["InputStartingPositionConfiguration"]
        )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["S3Configuration"])

    @cached_property
    def InputProcessingConfiguration(self):  # pragma: no cover
        return InputProcessingConfiguration.make_one(
            self.boto3_raw_data["InputProcessingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoverInputSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverInputSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordFormat:
    boto3_raw_data: "type_defs.RecordFormatTypeDef" = dataclasses.field()

    RecordFormatType = field("RecordFormatType")

    @cached_property
    def MappingParameters(self):  # pragma: no cover
        return MappingParameters.make_one(self.boto3_raw_data["MappingParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordFormatTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationOutputRequest:
    boto3_raw_data: "type_defs.AddApplicationOutputRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def Output(self):  # pragma: no cover
        return Output.make_one(self.boto3_raw_data["Output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddApplicationOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSchemaUpdate:
    boto3_raw_data: "type_defs.InputSchemaUpdateTypeDef" = dataclasses.field()

    @cached_property
    def RecordFormatUpdate(self):  # pragma: no cover
        return RecordFormat.make_one(self.boto3_raw_data["RecordFormatUpdate"])

    RecordEncodingUpdate = field("RecordEncodingUpdate")

    @cached_property
    def RecordColumnUpdates(self):  # pragma: no cover
        return RecordColumn.make_many(self.boto3_raw_data["RecordColumnUpdates"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSchemaUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSchemaUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSchemaOutput:
    boto3_raw_data: "type_defs.SourceSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def RecordFormat(self):  # pragma: no cover
        return RecordFormat.make_one(self.boto3_raw_data["RecordFormat"])

    @cached_property
    def RecordColumns(self):  # pragma: no cover
        return RecordColumn.make_many(self.boto3_raw_data["RecordColumns"])

    RecordEncoding = field("RecordEncoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSchema:
    boto3_raw_data: "type_defs.SourceSchemaTypeDef" = dataclasses.field()

    @cached_property
    def RecordFormat(self):  # pragma: no cover
        return RecordFormat.make_one(self.boto3_raw_data["RecordFormat"])

    @cached_property
    def RecordColumns(self):  # pragma: no cover
        return RecordColumn.make_many(self.boto3_raw_data["RecordColumns"])

    RecordEncoding = field("RecordEncoding")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputUpdate:
    boto3_raw_data: "type_defs.InputUpdateTypeDef" = dataclasses.field()

    InputId = field("InputId")
    NamePrefixUpdate = field("NamePrefixUpdate")

    @cached_property
    def InputProcessingConfigurationUpdate(self):  # pragma: no cover
        return InputProcessingConfigurationUpdate.make_one(
            self.boto3_raw_data["InputProcessingConfigurationUpdate"]
        )

    @cached_property
    def KinesisStreamsInputUpdate(self):  # pragma: no cover
        return KinesisStreamsInputUpdate.make_one(
            self.boto3_raw_data["KinesisStreamsInputUpdate"]
        )

    @cached_property
    def KinesisFirehoseInputUpdate(self):  # pragma: no cover
        return KinesisFirehoseInputUpdate.make_one(
            self.boto3_raw_data["KinesisFirehoseInputUpdate"]
        )

    @cached_property
    def InputSchemaUpdate(self):  # pragma: no cover
        return InputSchemaUpdate.make_one(self.boto3_raw_data["InputSchemaUpdate"])

    @cached_property
    def InputParallelismUpdate(self):  # pragma: no cover
        return InputParallelismUpdate.make_one(
            self.boto3_raw_data["InputParallelismUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputUpdateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverInputSchemaResponse:
    boto3_raw_data: "type_defs.DiscoverInputSchemaResponseTypeDef" = dataclasses.field()

    @cached_property
    def InputSchema(self):  # pragma: no cover
        return SourceSchemaOutput.make_one(self.boto3_raw_data["InputSchema"])

    ParsedInputRecords = field("ParsedInputRecords")
    ProcessedInputRecords = field("ProcessedInputRecords")
    RawInputRecords = field("RawInputRecords")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoverInputSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverInputSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDescription:
    boto3_raw_data: "type_defs.InputDescriptionTypeDef" = dataclasses.field()

    InputId = field("InputId")
    NamePrefix = field("NamePrefix")
    InAppStreamNames = field("InAppStreamNames")

    @cached_property
    def InputProcessingConfigurationDescription(self):  # pragma: no cover
        return InputProcessingConfigurationDescription.make_one(
            self.boto3_raw_data["InputProcessingConfigurationDescription"]
        )

    @cached_property
    def KinesisStreamsInputDescription(self):  # pragma: no cover
        return KinesisStreamsInputDescription.make_one(
            self.boto3_raw_data["KinesisStreamsInputDescription"]
        )

    @cached_property
    def KinesisFirehoseInputDescription(self):  # pragma: no cover
        return KinesisFirehoseInputDescription.make_one(
            self.boto3_raw_data["KinesisFirehoseInputDescription"]
        )

    @cached_property
    def InputSchema(self):  # pragma: no cover
        return SourceSchemaOutput.make_one(self.boto3_raw_data["InputSchema"])

    @cached_property
    def InputParallelism(self):  # pragma: no cover
        return InputParallelism.make_one(self.boto3_raw_data["InputParallelism"])

    @cached_property
    def InputStartingPositionConfiguration(self):  # pragma: no cover
        return InputStartingPositionConfiguration.make_one(
            self.boto3_raw_data["InputStartingPositionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceDataSourceDescription:
    boto3_raw_data: "type_defs.ReferenceDataSourceDescriptionTypeDef" = (
        dataclasses.field()
    )

    ReferenceId = field("ReferenceId")
    TableName = field("TableName")

    @cached_property
    def S3ReferenceDataSourceDescription(self):  # pragma: no cover
        return S3ReferenceDataSourceDescription.make_one(
            self.boto3_raw_data["S3ReferenceDataSourceDescription"]
        )

    @cached_property
    def ReferenceSchema(self):  # pragma: no cover
        return SourceSchemaOutput.make_one(self.boto3_raw_data["ReferenceSchema"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReferenceDataSourceDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDataSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDetail:
    boto3_raw_data: "type_defs.ApplicationDetailTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    ApplicationARN = field("ApplicationARN")
    ApplicationStatus = field("ApplicationStatus")
    ApplicationVersionId = field("ApplicationVersionId")
    ApplicationDescription = field("ApplicationDescription")
    CreateTimestamp = field("CreateTimestamp")
    LastUpdateTimestamp = field("LastUpdateTimestamp")

    @cached_property
    def InputDescriptions(self):  # pragma: no cover
        return InputDescription.make_many(self.boto3_raw_data["InputDescriptions"])

    @cached_property
    def OutputDescriptions(self):  # pragma: no cover
        return OutputDescription.make_many(self.boto3_raw_data["OutputDescriptions"])

    @cached_property
    def ReferenceDataSourceDescriptions(self):  # pragma: no cover
        return ReferenceDataSourceDescription.make_many(
            self.boto3_raw_data["ReferenceDataSourceDescriptions"]
        )

    @cached_property
    def CloudWatchLoggingOptionDescriptions(self):  # pragma: no cover
        return CloudWatchLoggingOptionDescription.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptionDescriptions"]
        )

    ApplicationCode = field("ApplicationCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Input:
    boto3_raw_data: "type_defs.InputTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    InputSchema = field("InputSchema")

    @cached_property
    def InputProcessingConfiguration(self):  # pragma: no cover
        return InputProcessingConfiguration.make_one(
            self.boto3_raw_data["InputProcessingConfiguration"]
        )

    @cached_property
    def KinesisStreamsInput(self):  # pragma: no cover
        return KinesisStreamsInput.make_one(self.boto3_raw_data["KinesisStreamsInput"])

    @cached_property
    def KinesisFirehoseInput(self):  # pragma: no cover
        return KinesisFirehoseInput.make_one(
            self.boto3_raw_data["KinesisFirehoseInput"]
        )

    @cached_property
    def InputParallelism(self):  # pragma: no cover
        return InputParallelism.make_one(self.boto3_raw_data["InputParallelism"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceDataSource:
    boto3_raw_data: "type_defs.ReferenceDataSourceTypeDef" = dataclasses.field()

    TableName = field("TableName")
    ReferenceSchema = field("ReferenceSchema")

    @cached_property
    def S3ReferenceDataSource(self):  # pragma: no cover
        return S3ReferenceDataSource.make_one(
            self.boto3_raw_data["S3ReferenceDataSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceDataSourceUpdate:
    boto3_raw_data: "type_defs.ReferenceDataSourceUpdateTypeDef" = dataclasses.field()

    ReferenceId = field("ReferenceId")
    TableNameUpdate = field("TableNameUpdate")

    @cached_property
    def S3ReferenceDataSourceUpdate(self):  # pragma: no cover
        return S3ReferenceDataSourceUpdate.make_one(
            self.boto3_raw_data["S3ReferenceDataSourceUpdate"]
        )

    ReferenceSchemaUpdate = field("ReferenceSchemaUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceDataSourceUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDataSourceUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationResponse:
    boto3_raw_data: "type_defs.DescribeApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationDetail(self):  # pragma: no cover
        return ApplicationDetail.make_one(self.boto3_raw_data["ApplicationDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationInputRequest:
    boto3_raw_data: "type_defs.AddApplicationInputRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddApplicationInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    ApplicationDescription = field("ApplicationDescription")

    @cached_property
    def Inputs(self):  # pragma: no cover
        return Input.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOption.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ApplicationCode = field("ApplicationCode")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationReferenceDataSourceRequest:
    boto3_raw_data: "type_defs.AddApplicationReferenceDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def ReferenceDataSource(self):  # pragma: no cover
        return ReferenceDataSource.make_one(self.boto3_raw_data["ReferenceDataSource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationReferenceDataSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationReferenceDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationUpdate:
    boto3_raw_data: "type_defs.ApplicationUpdateTypeDef" = dataclasses.field()

    @cached_property
    def InputUpdates(self):  # pragma: no cover
        return InputUpdate.make_many(self.boto3_raw_data["InputUpdates"])

    ApplicationCodeUpdate = field("ApplicationCodeUpdate")

    @cached_property
    def OutputUpdates(self):  # pragma: no cover
        return OutputUpdate.make_many(self.boto3_raw_data["OutputUpdates"])

    @cached_property
    def ReferenceDataSourceUpdates(self):  # pragma: no cover
        return ReferenceDataSourceUpdate.make_many(
            self.boto3_raw_data["ReferenceDataSourceUpdates"]
        )

    @cached_property
    def CloudWatchLoggingOptionUpdates(self):  # pragma: no cover
        return CloudWatchLoggingOptionUpdate.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptionUpdates"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def ApplicationUpdate(self):  # pragma: no cover
        return ApplicationUpdate.make_one(self.boto3_raw_data["ApplicationUpdate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
