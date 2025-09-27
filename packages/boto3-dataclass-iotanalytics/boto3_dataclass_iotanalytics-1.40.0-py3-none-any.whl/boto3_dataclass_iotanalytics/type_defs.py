# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotanalytics import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddAttributesActivityOutput:
    boto3_raw_data: "type_defs.AddAttributesActivityOutputTypeDef" = dataclasses.field()

    name = field("name")
    attributes = field("attributes")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddAttributesActivityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAttributesActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAttributesActivity:
    boto3_raw_data: "type_defs.AddAttributesActivityTypeDef" = dataclasses.field()

    name = field("name")
    attributes = field("attributes")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddAttributesActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAttributesActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutMessageErrorEntry:
    boto3_raw_data: "type_defs.BatchPutMessageErrorEntryTypeDef" = dataclasses.field()

    messageId = field("messageId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutMessageErrorEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutMessageErrorEntryTypeDef"]
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
class CancelPipelineReprocessingRequest:
    boto3_raw_data: "type_defs.CancelPipelineReprocessingRequestTypeDef" = (
        dataclasses.field()
    )

    pipelineName = field("pipelineName")
    reprocessingId = field("reprocessingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelPipelineReprocessingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelPipelineReprocessingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelActivity:
    boto3_raw_data: "type_defs.ChannelActivityTypeDef" = dataclasses.field()

    name = field("name")
    channelName = field("channelName")
    next = field("next")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelActivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMessages:
    boto3_raw_data: "type_defs.ChannelMessagesTypeDef" = dataclasses.field()

    s3Paths = field("s3Paths")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelMessagesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelMessagesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstimatedResourceSize:
    boto3_raw_data: "type_defs.EstimatedResourceSizeTypeDef" = dataclasses.field()

    estimatedSizeInBytes = field("estimatedSizeInBytes")
    estimatedOn = field("estimatedOn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EstimatedResourceSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstimatedResourceSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedChannelS3Storage:
    boto3_raw_data: "type_defs.CustomerManagedChannelS3StorageTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    roleArn = field("roleArn")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomerManagedChannelS3StorageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedChannelS3StorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedChannelS3StorageSummary:
    boto3_raw_data: "type_defs.CustomerManagedChannelS3StorageSummaryTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedChannelS3StorageSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedChannelS3StorageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionPeriod:
    boto3_raw_data: "type_defs.RetentionPeriodTypeDef" = dataclasses.field()

    unlimited = field("unlimited")
    numberOfDays = field("numberOfDays")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetentionPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetentionPeriodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Column:
    boto3_raw_data: "type_defs.ColumnTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceConfiguration:
    boto3_raw_data: "type_defs.ResourceConfigurationTypeDef" = dataclasses.field()

    computeType = field("computeType")
    volumeSizeInGB = field("volumeSizeInGB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceConfigurationTypeDef"]
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

    key = field("key")
    value = field("value")

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
class CreateDatasetContentRequest:
    boto3_raw_data: "type_defs.CreateDatasetContentRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersioningConfiguration:
    boto3_raw_data: "type_defs.VersioningConfigurationTypeDef" = dataclasses.field()

    unlimited = field("unlimited")
    maxVersions = field("maxVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersioningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersioningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedDatastoreS3StorageSummary:
    boto3_raw_data: "type_defs.CustomerManagedDatastoreS3StorageSummaryTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedDatastoreS3StorageSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedDatastoreS3StorageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedDatastoreS3Storage:
    boto3_raw_data: "type_defs.CustomerManagedDatastoreS3StorageTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    roleArn = field("roleArn")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedDatastoreS3StorageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedDatastoreS3StorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetActionSummary:
    boto3_raw_data: "type_defs.DatasetActionSummaryTypeDef" = dataclasses.field()

    actionName = field("actionName")
    actionType = field("actionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotEventsDestinationConfiguration:
    boto3_raw_data: "type_defs.IotEventsDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    inputName = field("inputName")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotEventsDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotEventsDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetContentStatus:
    boto3_raw_data: "type_defs.DatasetContentStatusTypeDef" = dataclasses.field()

    state = field("state")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetContentStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetContentStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetContentVersionValue:
    boto3_raw_data: "type_defs.DatasetContentVersionValueTypeDef" = dataclasses.field()

    datasetName = field("datasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetContentVersionValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetContentVersionValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetEntry:
    boto3_raw_data: "type_defs.DatasetEntryTypeDef" = dataclasses.field()

    entryName = field("entryName")
    dataURI = field("dataURI")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    expression = field("expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggeringDataset:
    boto3_raw_data: "type_defs.TriggeringDatasetTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TriggeringDatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TriggeringDatasetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreActivity:
    boto3_raw_data: "type_defs.DatastoreActivityTypeDef" = dataclasses.field()

    name = field("name")
    datastoreName = field("datastoreName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatastoreActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseCustomerManagedDatastoreS3StorageSummary:
    boto3_raw_data: (
        "type_defs.IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef"
    ) = dataclasses.field()

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef"
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
                "type_defs.IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseCustomerManagedDatastoreS3Storage:
    boto3_raw_data: "type_defs.IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Partition:
    boto3_raw_data: "type_defs.PartitionTypeDef" = dataclasses.field()

    attributeName = field("attributeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartitionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampPartition:
    boto3_raw_data: "type_defs.TimestampPartitionTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    timestampFormat = field("timestampFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestampPartitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestampPartitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelRequest:
    boto3_raw_data: "type_defs.DeleteChannelRequestTypeDef" = dataclasses.field()

    channelName = field("channelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetContentRequest:
    boto3_raw_data: "type_defs.DeleteDatasetContentRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatastoreRequest:
    boto3_raw_data: "type_defs.DeleteDatastoreRequestTypeDef" = dataclasses.field()

    datastoreName = field("datastoreName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipelineRequest:
    boto3_raw_data: "type_defs.DeletePipelineRequestTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeltaTimeSessionWindowConfiguration:
    boto3_raw_data: "type_defs.DeltaTimeSessionWindowConfigurationTypeDef" = (
        dataclasses.field()
    )

    timeoutInMinutes = field("timeoutInMinutes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeltaTimeSessionWindowConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeltaTimeSessionWindowConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeltaTime:
    boto3_raw_data: "type_defs.DeltaTimeTypeDef" = dataclasses.field()

    offsetSeconds = field("offsetSeconds")
    timeExpression = field("timeExpression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeltaTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeltaTimeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequest:
    boto3_raw_data: "type_defs.DescribeChannelRequestTypeDef" = dataclasses.field()

    channelName = field("channelName")
    includeStatistics = field("includeStatistics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatastoreRequest:
    boto3_raw_data: "type_defs.DescribeDatastoreRequestTypeDef" = dataclasses.field()

    datastoreName = field("datastoreName")
    includeStatistics = field("includeStatistics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOptions:
    boto3_raw_data: "type_defs.LoggingOptionsTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    level = field("level")
    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePipelineRequest:
    boto3_raw_data: "type_defs.DescribePipelineRequestTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceRegistryEnrichActivity:
    boto3_raw_data: "type_defs.DeviceRegistryEnrichActivityTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    attribute = field("attribute")
    thingName = field("thingName")
    roleArn = field("roleArn")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeviceRegistryEnrichActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceRegistryEnrichActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceShadowEnrichActivity:
    boto3_raw_data: "type_defs.DeviceShadowEnrichActivityTypeDef" = dataclasses.field()

    name = field("name")
    attribute = field("attribute")
    thingName = field("thingName")
    roleArn = field("roleArn")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeviceShadowEnrichActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceShadowEnrichActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterActivity:
    boto3_raw_data: "type_defs.FilterActivityTypeDef" = dataclasses.field()

    name = field("name")
    filter = field("filter")
    next = field("next")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterActivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDatasetContentRequest:
    boto3_raw_data: "type_defs.GetDatasetContentRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDatasetContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDatasetContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueConfiguration:
    boto3_raw_data: "type_defs.GlueConfigurationTypeDef" = dataclasses.field()

    tableName = field("tableName")
    databaseName = field("databaseName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlueConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaActivity:
    boto3_raw_data: "type_defs.LambdaActivityTypeDef" = dataclasses.field()

    name = field("name")
    lambdaName = field("lambdaName")
    batchSize = field("batchSize")
    next = field("next")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaActivityTypeDef"]],
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
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatastoresRequest:
    boto3_raw_data: "type_defs.ListDatastoresRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatastoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatastoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesRequest:
    boto3_raw_data: "type_defs.ListPipelinesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class MathActivity:
    boto3_raw_data: "type_defs.MathActivityTypeDef" = dataclasses.field()

    name = field("name")
    attribute = field("attribute")
    math = field("math")
    next = field("next")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MathActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MathActivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputFileUriValue:
    boto3_raw_data: "type_defs.OutputFileUriValueTypeDef" = dataclasses.field()

    fileName = field("fileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputFileUriValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputFileUriValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAttributesActivityOutput:
    boto3_raw_data: "type_defs.RemoveAttributesActivityOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    attributes = field("attributes")
    next = field("next")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveAttributesActivityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAttributesActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectAttributesActivityOutput:
    boto3_raw_data: "type_defs.SelectAttributesActivityOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    attributes = field("attributes")
    next = field("next")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SelectAttributesActivityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectAttributesActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReprocessingSummary:
    boto3_raw_data: "type_defs.ReprocessingSummaryTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")
    creationTime = field("creationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReprocessingSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReprocessingSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAttributesActivity:
    boto3_raw_data: "type_defs.RemoveAttributesActivityTypeDef" = dataclasses.field()

    name = field("name")
    attributes = field("attributes")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAttributesActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAttributesActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectAttributesActivity:
    boto3_raw_data: "type_defs.SelectAttributesActivityTypeDef" = dataclasses.field()

    name = field("name")
    attributes = field("attributes")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectAttributesActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectAttributesActivityTypeDef"]
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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class BatchPutMessageResponse:
    boto3_raw_data: "type_defs.BatchPutMessageResponseTypeDef" = dataclasses.field()

    @cached_property
    def batchPutMessageErrorEntries(self):  # pragma: no cover
        return BatchPutMessageErrorEntry.make_many(
            self.boto3_raw_data["batchPutMessageErrorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetContentResponse:
    boto3_raw_data: "type_defs.CreateDatasetContentResponseTypeDef" = (
        dataclasses.field()
    )

    versionId = field("versionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineResponse:
    boto3_raw_data: "type_defs.CreatePipelineResponseTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineArn = field("pipelineArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineResponseTypeDef"]
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
class RunPipelineActivityResponse:
    boto3_raw_data: "type_defs.RunPipelineActivityResponseTypeDef" = dataclasses.field()

    payloads = field("payloads")
    logResult = field("logResult")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunPipelineActivityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunPipelineActivityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleChannelDataResponse:
    boto3_raw_data: "type_defs.SampleChannelDataResponseTypeDef" = dataclasses.field()

    payloads = field("payloads")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SampleChannelDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampleChannelDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipelineReprocessingResponse:
    boto3_raw_data: "type_defs.StartPipelineReprocessingResponseTypeDef" = (
        dataclasses.field()
    )

    reprocessingId = field("reprocessingId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartPipelineReprocessingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipelineReprocessingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    messageId = field("messageId")
    payload = field("payload")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelStatistics:
    boto3_raw_data: "type_defs.ChannelStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def size(self):  # pragma: no cover
        return EstimatedResourceSize.make_one(self.boto3_raw_data["size"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreStatistics:
    boto3_raw_data: "type_defs.DatastoreStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def size(self):  # pragma: no cover
        return EstimatedResourceSize.make_one(self.boto3_raw_data["size"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastoreStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelStorageOutput:
    boto3_raw_data: "type_defs.ChannelStorageOutputTypeDef" = dataclasses.field()

    serviceManagedS3 = field("serviceManagedS3")

    @cached_property
    def customerManagedS3(self):  # pragma: no cover
        return CustomerManagedChannelS3Storage.make_one(
            self.boto3_raw_data["customerManagedS3"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelStorageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelStorageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelStorage:
    boto3_raw_data: "type_defs.ChannelStorageTypeDef" = dataclasses.field()

    serviceManagedS3 = field("serviceManagedS3")

    @cached_property
    def customerManagedS3(self):  # pragma: no cover
        return CustomerManagedChannelS3Storage.make_one(
            self.boto3_raw_data["customerManagedS3"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelStorageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelStorageSummary:
    boto3_raw_data: "type_defs.ChannelStorageSummaryTypeDef" = dataclasses.field()

    serviceManagedS3 = field("serviceManagedS3")

    @cached_property
    def customerManagedS3(self):  # pragma: no cover
        return CustomerManagedChannelS3StorageSummary.make_one(
            self.boto3_raw_data["customerManagedS3"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelStorageSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelStorageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    channelName = field("channelName")
    channelArn = field("channelArn")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetResponse:
    boto3_raw_data: "type_defs.CreateDatasetResponseTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    datasetArn = field("datasetArn")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatastoreResponse:
    boto3_raw_data: "type_defs.CreateDatastoreResponseTypeDef" = dataclasses.field()

    datastoreName = field("datastoreName")
    datastoreArn = field("datastoreArn")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaDefinitionOutput:
    boto3_raw_data: "type_defs.SchemaDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def columns(self):  # pragma: no cover
        return Column.make_many(self.boto3_raw_data["columns"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaDefinition:
    boto3_raw_data: "type_defs.SchemaDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def columns(self):  # pragma: no cover
        return Column.make_many(self.boto3_raw_data["columns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionTypeDef"]
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
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class DatasetContentSummary:
    boto3_raw_data: "type_defs.DatasetContentSummaryTypeDef" = dataclasses.field()

    version = field("version")

    @cached_property
    def status(self):  # pragma: no cover
        return DatasetContentStatus.make_one(self.boto3_raw_data["status"])

    creationTime = field("creationTime")
    scheduleTime = field("scheduleTime")
    completionTime = field("completionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetContentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetContentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDatasetContentResponse:
    boto3_raw_data: "type_defs.GetDatasetContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return DatasetEntry.make_many(self.boto3_raw_data["entries"])

    timestamp = field("timestamp")

    @cached_property
    def status(self):  # pragma: no cover
        return DatasetContentStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDatasetContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDatasetContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetTrigger:
    boto3_raw_data: "type_defs.DatasetTriggerTypeDef" = dataclasses.field()

    @cached_property
    def schedule(self):  # pragma: no cover
        return Schedule.make_one(self.boto3_raw_data["schedule"])

    @cached_property
    def dataset(self):  # pragma: no cover
        return TriggeringDataset.make_one(self.boto3_raw_data["dataset"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetTriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetTriggerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreIotSiteWiseMultiLayerStorageSummary:
    boto3_raw_data: "type_defs.DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customerManagedS3Storage(self):  # pragma: no cover
        return IotSiteWiseCustomerManagedDatastoreS3StorageSummary.make_one(
            self.boto3_raw_data["customerManagedS3Storage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreIotSiteWiseMultiLayerStorage:
    boto3_raw_data: "type_defs.DatastoreIotSiteWiseMultiLayerStorageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customerManagedS3Storage(self):  # pragma: no cover
        return IotSiteWiseCustomerManagedDatastoreS3Storage.make_one(
            self.boto3_raw_data["customerManagedS3Storage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatastoreIotSiteWiseMultiLayerStorageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreIotSiteWiseMultiLayerStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastorePartition:
    boto3_raw_data: "type_defs.DatastorePartitionTypeDef" = dataclasses.field()

    @cached_property
    def attributePartition(self):  # pragma: no cover
        return Partition.make_one(self.boto3_raw_data["attributePartition"])

    @cached_property
    def timestampPartition(self):  # pragma: no cover
        return TimestampPartition.make_one(self.boto3_raw_data["timestampPartition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastorePartitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastorePartitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LateDataRuleConfiguration:
    boto3_raw_data: "type_defs.LateDataRuleConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def deltaTimeSessionWindowConfiguration(self):  # pragma: no cover
        return DeltaTimeSessionWindowConfiguration.make_one(
            self.boto3_raw_data["deltaTimeSessionWindowConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LateDataRuleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LateDataRuleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryFilter:
    boto3_raw_data: "type_defs.QueryFilterTypeDef" = dataclasses.field()

    @cached_property
    def deltaTime(self):  # pragma: no cover
        return DeltaTime.make_one(self.boto3_raw_data["deltaTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoggingOptionsResponse:
    boto3_raw_data: "type_defs.DescribeLoggingOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def loggingOptions(self):  # pragma: no cover
        return LoggingOptions.make_one(self.boto3_raw_data["loggingOptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLoggingOptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoggingOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLoggingOptionsRequest:
    boto3_raw_data: "type_defs.PutLoggingOptionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def loggingOptions(self):  # pragma: no cover
        return LoggingOptions.make_one(self.boto3_raw_data["loggingOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLoggingOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLoggingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfiguration:
    boto3_raw_data: "type_defs.S3DestinationConfigurationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")
    roleArn = field("roleArn")

    @cached_property
    def glueConfiguration(self):  # pragma: no cover
        return GlueConfiguration.make_one(self.boto3_raw_data["glueConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatastoresRequestPaginate:
    boto3_raw_data: "type_defs.ListDatastoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatastoresRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatastoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesRequestPaginate:
    boto3_raw_data: "type_defs.ListPipelinesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetContentsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetContentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetName = field("datasetName")
    scheduledOnOrAfter = field("scheduledOnOrAfter")
    scheduledBefore = field("scheduledBefore")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDatasetContentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetContentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetContentsRequest:
    boto3_raw_data: "type_defs.ListDatasetContentsRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    scheduledOnOrAfter = field("scheduledOnOrAfter")
    scheduledBefore = field("scheduledBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetContentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetContentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleChannelDataRequest:
    boto3_raw_data: "type_defs.SampleChannelDataRequestTypeDef" = dataclasses.field()

    channelName = field("channelName")
    maxMessages = field("maxMessages")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SampleChannelDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampleChannelDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipelineReprocessingRequest:
    boto3_raw_data: "type_defs.StartPipelineReprocessingRequestTypeDef" = (
        dataclasses.field()
    )

    pipelineName = field("pipelineName")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def channelMessages(self):  # pragma: no cover
        return ChannelMessages.make_one(self.boto3_raw_data["channelMessages"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartPipelineReprocessingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipelineReprocessingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Variable:
    boto3_raw_data: "type_defs.VariableTypeDef" = dataclasses.field()

    name = field("name")
    stringValue = field("stringValue")
    doubleValue = field("doubleValue")

    @cached_property
    def datasetContentVersionValue(self):  # pragma: no cover
        return DatasetContentVersionValue.make_one(
            self.boto3_raw_data["datasetContentVersionValue"]
        )

    @cached_property
    def outputFileUriValue(self):  # pragma: no cover
        return OutputFileUriValue.make_one(self.boto3_raw_data["outputFileUriValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineActivityOutput:
    boto3_raw_data: "type_defs.PipelineActivityOutputTypeDef" = dataclasses.field()

    @cached_property
    def channel(self):  # pragma: no cover
        return ChannelActivity.make_one(self.boto3_raw_data["channel"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaActivity.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def datastore(self):  # pragma: no cover
        return DatastoreActivity.make_one(self.boto3_raw_data["datastore"])

    @cached_property
    def addAttributes(self):  # pragma: no cover
        return AddAttributesActivityOutput.make_one(
            self.boto3_raw_data["addAttributes"]
        )

    @cached_property
    def removeAttributes(self):  # pragma: no cover
        return RemoveAttributesActivityOutput.make_one(
            self.boto3_raw_data["removeAttributes"]
        )

    @cached_property
    def selectAttributes(self):  # pragma: no cover
        return SelectAttributesActivityOutput.make_one(
            self.boto3_raw_data["selectAttributes"]
        )

    @cached_property
    def filter(self):  # pragma: no cover
        return FilterActivity.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def math(self):  # pragma: no cover
        return MathActivity.make_one(self.boto3_raw_data["math"])

    @cached_property
    def deviceRegistryEnrich(self):  # pragma: no cover
        return DeviceRegistryEnrichActivity.make_one(
            self.boto3_raw_data["deviceRegistryEnrich"]
        )

    @cached_property
    def deviceShadowEnrich(self):  # pragma: no cover
        return DeviceShadowEnrichActivity.make_one(
            self.boto3_raw_data["deviceShadowEnrich"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineActivityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineActivityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineSummary:
    boto3_raw_data: "type_defs.PipelineSummaryTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")

    @cached_property
    def reprocessingSummaries(self):  # pragma: no cover
        return ReprocessingSummary.make_many(
            self.boto3_raw_data["reprocessingSummaries"]
        )

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutMessageRequest:
    boto3_raw_data: "type_defs.BatchPutMessageRequestTypeDef" = dataclasses.field()

    channelName = field("channelName")

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def storage(self):  # pragma: no cover
        return ChannelStorageOutput.make_one(self.boto3_raw_data["storage"])

    arn = field("arn")
    status = field("status")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    lastMessageArrivalTime = field("lastMessageArrivalTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelSummary:
    boto3_raw_data: "type_defs.ChannelSummaryTypeDef" = dataclasses.field()

    channelName = field("channelName")

    @cached_property
    def channelStorage(self):  # pragma: no cover
        return ChannelStorageSummary.make_one(self.boto3_raw_data["channelStorage"])

    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    lastMessageArrivalTime = field("lastMessageArrivalTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParquetConfigurationOutput:
    boto3_raw_data: "type_defs.ParquetConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def schemaDefinition(self):  # pragma: no cover
        return SchemaDefinitionOutput.make_one(self.boto3_raw_data["schemaDefinition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParquetConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParquetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParquetConfiguration:
    boto3_raw_data: "type_defs.ParquetConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def schemaDefinition(self):  # pragma: no cover
        return SchemaDefinition.make_one(self.boto3_raw_data["schemaDefinition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParquetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParquetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetContentsResponse:
    boto3_raw_data: "type_defs.ListDatasetContentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def datasetContentSummaries(self):  # pragma: no cover
        return DatasetContentSummary.make_many(
            self.boto3_raw_data["datasetContentSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetContentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetContentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSummary:
    boto3_raw_data: "type_defs.DatasetSummaryTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @cached_property
    def triggers(self):  # pragma: no cover
        return DatasetTrigger.make_many(self.boto3_raw_data["triggers"])

    @cached_property
    def actions(self):  # pragma: no cover
        return DatasetActionSummary.make_many(self.boto3_raw_data["actions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreStorageSummary:
    boto3_raw_data: "type_defs.DatastoreStorageSummaryTypeDef" = dataclasses.field()

    serviceManagedS3 = field("serviceManagedS3")

    @cached_property
    def customerManagedS3(self):  # pragma: no cover
        return CustomerManagedDatastoreS3StorageSummary.make_one(
            self.boto3_raw_data["customerManagedS3"]
        )

    @cached_property
    def iotSiteWiseMultiLayerStorage(self):  # pragma: no cover
        return DatastoreIotSiteWiseMultiLayerStorageSummary.make_one(
            self.boto3_raw_data["iotSiteWiseMultiLayerStorage"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastoreStorageSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreStorageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreStorageOutput:
    boto3_raw_data: "type_defs.DatastoreStorageOutputTypeDef" = dataclasses.field()

    serviceManagedS3 = field("serviceManagedS3")

    @cached_property
    def customerManagedS3(self):  # pragma: no cover
        return CustomerManagedDatastoreS3Storage.make_one(
            self.boto3_raw_data["customerManagedS3"]
        )

    @cached_property
    def iotSiteWiseMultiLayerStorage(self):  # pragma: no cover
        return DatastoreIotSiteWiseMultiLayerStorage.make_one(
            self.boto3_raw_data["iotSiteWiseMultiLayerStorage"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastoreStorageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreStorageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreStorage:
    boto3_raw_data: "type_defs.DatastoreStorageTypeDef" = dataclasses.field()

    serviceManagedS3 = field("serviceManagedS3")

    @cached_property
    def customerManagedS3(self):  # pragma: no cover
        return CustomerManagedDatastoreS3Storage.make_one(
            self.boto3_raw_data["customerManagedS3"]
        )

    @cached_property
    def iotSiteWiseMultiLayerStorage(self):  # pragma: no cover
        return DatastoreIotSiteWiseMultiLayerStorage.make_one(
            self.boto3_raw_data["iotSiteWiseMultiLayerStorage"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatastoreStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastorePartitionsOutput:
    boto3_raw_data: "type_defs.DatastorePartitionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def partitions(self):  # pragma: no cover
        return DatastorePartition.make_many(self.boto3_raw_data["partitions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastorePartitionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastorePartitionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastorePartitions:
    boto3_raw_data: "type_defs.DatastorePartitionsTypeDef" = dataclasses.field()

    @cached_property
    def partitions(self):  # pragma: no cover
        return DatastorePartition.make_many(self.boto3_raw_data["partitions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastorePartitionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastorePartitionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LateDataRule:
    boto3_raw_data: "type_defs.LateDataRuleTypeDef" = dataclasses.field()

    @cached_property
    def ruleConfiguration(self):  # pragma: no cover
        return LateDataRuleConfiguration.make_one(
            self.boto3_raw_data["ruleConfiguration"]
        )

    ruleName = field("ruleName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LateDataRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LateDataRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlQueryDatasetActionOutput:
    boto3_raw_data: "type_defs.SqlQueryDatasetActionOutputTypeDef" = dataclasses.field()

    sqlQuery = field("sqlQuery")

    @cached_property
    def filters(self):  # pragma: no cover
        return QueryFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqlQueryDatasetActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlQueryDatasetActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlQueryDatasetAction:
    boto3_raw_data: "type_defs.SqlQueryDatasetActionTypeDef" = dataclasses.field()

    sqlQuery = field("sqlQuery")

    @cached_property
    def filters(self):  # pragma: no cover
        return QueryFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqlQueryDatasetActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlQueryDatasetActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetContentDeliveryDestination:
    boto3_raw_data: "type_defs.DatasetContentDeliveryDestinationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def iotEventsDestinationConfiguration(self):  # pragma: no cover
        return IotEventsDestinationConfiguration.make_one(
            self.boto3_raw_data["iotEventsDestinationConfiguration"]
        )

    @cached_property
    def s3DestinationConfiguration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["s3DestinationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatasetContentDeliveryDestinationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetContentDeliveryDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDatasetActionOutput:
    boto3_raw_data: "type_defs.ContainerDatasetActionOutputTypeDef" = (
        dataclasses.field()
    )

    image = field("image")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def resourceConfiguration(self):  # pragma: no cover
        return ResourceConfiguration.make_one(
            self.boto3_raw_data["resourceConfiguration"]
        )

    @cached_property
    def variables(self):  # pragma: no cover
        return Variable.make_many(self.boto3_raw_data["variables"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerDatasetActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDatasetActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDatasetAction:
    boto3_raw_data: "type_defs.ContainerDatasetActionTypeDef" = dataclasses.field()

    image = field("image")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def resourceConfiguration(self):  # pragma: no cover
        return ResourceConfiguration.make_one(
            self.boto3_raw_data["resourceConfiguration"]
        )

    @cached_property
    def variables(self):  # pragma: no cover
        return Variable.make_many(self.boto3_raw_data["variables"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerDatasetActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDatasetActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Pipeline:
    boto3_raw_data: "type_defs.PipelineTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def activities(self):  # pragma: no cover
        return PipelineActivityOutput.make_many(self.boto3_raw_data["activities"])

    @cached_property
    def reprocessingSummaries(self):  # pragma: no cover
        return ReprocessingSummary.make_many(
            self.boto3_raw_data["reprocessingSummaries"]
        )

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesResponse:
    boto3_raw_data: "type_defs.ListPipelinesResponseTypeDef" = dataclasses.field()

    @cached_property
    def pipelineSummaries(self):  # pragma: no cover
        return PipelineSummary.make_many(self.boto3_raw_data["pipelineSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineActivity:
    boto3_raw_data: "type_defs.PipelineActivityTypeDef" = dataclasses.field()

    @cached_property
    def channel(self):  # pragma: no cover
        return ChannelActivity.make_one(self.boto3_raw_data["channel"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaActivity.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def datastore(self):  # pragma: no cover
        return DatastoreActivity.make_one(self.boto3_raw_data["datastore"])

    addAttributes = field("addAttributes")
    removeAttributes = field("removeAttributes")
    selectAttributes = field("selectAttributes")

    @cached_property
    def filter(self):  # pragma: no cover
        return FilterActivity.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def math(self):  # pragma: no cover
        return MathActivity.make_one(self.boto3_raw_data["math"])

    @cached_property
    def deviceRegistryEnrich(self):  # pragma: no cover
        return DeviceRegistryEnrichActivity.make_one(
            self.boto3_raw_data["deviceRegistryEnrich"]
        )

    @cached_property
    def deviceShadowEnrich(self):  # pragma: no cover
        return DeviceShadowEnrichActivity.make_one(
            self.boto3_raw_data["deviceShadowEnrich"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelResponse:
    boto3_raw_data: "type_defs.DescribeChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def channel(self):  # pragma: no cover
        return Channel.make_one(self.boto3_raw_data["channel"])

    @cached_property
    def statistics(self):  # pragma: no cover
        return ChannelStatistics.make_one(self.boto3_raw_data["statistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelRequest:
    boto3_raw_data: "type_defs.CreateChannelRequestTypeDef" = dataclasses.field()

    channelName = field("channelName")
    channelStorage = field("channelStorage")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelRequest:
    boto3_raw_data: "type_defs.UpdateChannelRequestTypeDef" = dataclasses.field()

    channelName = field("channelName")
    channelStorage = field("channelStorage")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def channelSummaries(self):  # pragma: no cover
        return ChannelSummary.make_many(self.boto3_raw_data["channelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFormatConfigurationOutput:
    boto3_raw_data: "type_defs.FileFormatConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    jsonConfiguration = field("jsonConfiguration")

    @cached_property
    def parquetConfiguration(self):  # pragma: no cover
        return ParquetConfigurationOutput.make_one(
            self.boto3_raw_data["parquetConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FileFormatConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileFormatConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFormatConfiguration:
    boto3_raw_data: "type_defs.FileFormatConfigurationTypeDef" = dataclasses.field()

    jsonConfiguration = field("jsonConfiguration")

    @cached_property
    def parquetConfiguration(self):  # pragma: no cover
        return ParquetConfiguration.make_one(
            self.boto3_raw_data["parquetConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileFormatConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileFormatConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def datasetSummaries(self):  # pragma: no cover
        return DatasetSummary.make_many(self.boto3_raw_data["datasetSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreSummary:
    boto3_raw_data: "type_defs.DatastoreSummaryTypeDef" = dataclasses.field()

    datastoreName = field("datastoreName")

    @cached_property
    def datastoreStorage(self):  # pragma: no cover
        return DatastoreStorageSummary.make_one(self.boto3_raw_data["datastoreStorage"])

    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    lastMessageArrivalTime = field("lastMessageArrivalTime")
    fileFormatType = field("fileFormatType")

    @cached_property
    def datastorePartitions(self):  # pragma: no cover
        return DatastorePartitionsOutput.make_one(
            self.boto3_raw_data["datastorePartitions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatastoreSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastoreSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetContentDeliveryRule:
    boto3_raw_data: "type_defs.DatasetContentDeliveryRuleTypeDef" = dataclasses.field()

    @cached_property
    def destination(self):  # pragma: no cover
        return DatasetContentDeliveryDestination.make_one(
            self.boto3_raw_data["destination"]
        )

    entryName = field("entryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetContentDeliveryRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetContentDeliveryRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetActionOutput:
    boto3_raw_data: "type_defs.DatasetActionOutputTypeDef" = dataclasses.field()

    actionName = field("actionName")

    @cached_property
    def queryAction(self):  # pragma: no cover
        return SqlQueryDatasetActionOutput.make_one(self.boto3_raw_data["queryAction"])

    @cached_property
    def containerAction(self):  # pragma: no cover
        return ContainerDatasetActionOutput.make_one(
            self.boto3_raw_data["containerAction"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePipelineResponse:
    boto3_raw_data: "type_defs.DescribePipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Datastore:
    boto3_raw_data: "type_defs.DatastoreTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def storage(self):  # pragma: no cover
        return DatastoreStorageOutput.make_one(self.boto3_raw_data["storage"])

    arn = field("arn")
    status = field("status")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    lastMessageArrivalTime = field("lastMessageArrivalTime")

    @cached_property
    def fileFormatConfiguration(self):  # pragma: no cover
        return FileFormatConfigurationOutput.make_one(
            self.boto3_raw_data["fileFormatConfiguration"]
        )

    @cached_property
    def datastorePartitions(self):  # pragma: no cover
        return DatastorePartitionsOutput.make_one(
            self.boto3_raw_data["datastorePartitions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatastoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatastoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatastoresResponse:
    boto3_raw_data: "type_defs.ListDatastoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def datastoreSummaries(self):  # pragma: no cover
        return DatastoreSummary.make_many(self.boto3_raw_data["datastoreSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatastoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatastoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dataset:
    boto3_raw_data: "type_defs.DatasetTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def actions(self):  # pragma: no cover
        return DatasetActionOutput.make_many(self.boto3_raw_data["actions"])

    @cached_property
    def triggers(self):  # pragma: no cover
        return DatasetTrigger.make_many(self.boto3_raw_data["triggers"])

    @cached_property
    def contentDeliveryRules(self):  # pragma: no cover
        return DatasetContentDeliveryRule.make_many(
            self.boto3_raw_data["contentDeliveryRules"]
        )

    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def versioningConfiguration(self):  # pragma: no cover
        return VersioningConfiguration.make_one(
            self.boto3_raw_data["versioningConfiguration"]
        )

    @cached_property
    def lateDataRules(self):  # pragma: no cover
        return LateDataRule.make_many(self.boto3_raw_data["lateDataRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetAction:
    boto3_raw_data: "type_defs.DatasetActionTypeDef" = dataclasses.field()

    actionName = field("actionName")
    queryAction = field("queryAction")
    containerAction = field("containerAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineRequest:
    boto3_raw_data: "type_defs.CreatePipelineRequestTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineActivities = field("pipelineActivities")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunPipelineActivityRequest:
    boto3_raw_data: "type_defs.RunPipelineActivityRequestTypeDef" = dataclasses.field()

    pipelineActivity = field("pipelineActivity")
    payloads = field("payloads")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunPipelineActivityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunPipelineActivityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineRequest:
    boto3_raw_data: "type_defs.UpdatePipelineRequestTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineActivities = field("pipelineActivities")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatastoreResponse:
    boto3_raw_data: "type_defs.DescribeDatastoreResponseTypeDef" = dataclasses.field()

    @cached_property
    def datastore(self):  # pragma: no cover
        return Datastore.make_one(self.boto3_raw_data["datastore"])

    @cached_property
    def statistics(self):  # pragma: no cover
        return DatastoreStatistics.make_one(self.boto3_raw_data["statistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatastoreRequest:
    boto3_raw_data: "type_defs.CreateDatastoreRequestTypeDef" = dataclasses.field()

    datastoreName = field("datastoreName")
    datastoreStorage = field("datastoreStorage")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    fileFormatConfiguration = field("fileFormatConfiguration")
    datastorePartitions = field("datastorePartitions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatastoreRequest:
    boto3_raw_data: "type_defs.UpdateDatastoreRequestTypeDef" = dataclasses.field()

    datastoreName = field("datastoreName")

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    datastoreStorage = field("datastoreStorage")
    fileFormatConfiguration = field("fileFormatConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataset(self):  # pragma: no cover
        return Dataset.make_one(self.boto3_raw_data["dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    actions = field("actions")

    @cached_property
    def triggers(self):  # pragma: no cover
        return DatasetTrigger.make_many(self.boto3_raw_data["triggers"])

    @cached_property
    def contentDeliveryRules(self):  # pragma: no cover
        return DatasetContentDeliveryRule.make_many(
            self.boto3_raw_data["contentDeliveryRules"]
        )

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def versioningConfiguration(self):  # pragma: no cover
        return VersioningConfiguration.make_one(
            self.boto3_raw_data["versioningConfiguration"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def lateDataRules(self):  # pragma: no cover
        return LateDataRule.make_many(self.boto3_raw_data["lateDataRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatasetRequest:
    boto3_raw_data: "type_defs.UpdateDatasetRequestTypeDef" = dataclasses.field()

    datasetName = field("datasetName")
    actions = field("actions")

    @cached_property
    def triggers(self):  # pragma: no cover
        return DatasetTrigger.make_many(self.boto3_raw_data["triggers"])

    @cached_property
    def contentDeliveryRules(self):  # pragma: no cover
        return DatasetContentDeliveryRule.make_many(
            self.boto3_raw_data["contentDeliveryRules"]
        )

    @cached_property
    def retentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["retentionPeriod"])

    @cached_property
    def versioningConfiguration(self):  # pragma: no cover
        return VersioningConfiguration.make_one(
            self.boto3_raw_data["versioningConfiguration"]
        )

    @cached_property
    def lateDataRules(self):  # pragma: no cover
        return LateDataRule.make_many(self.boto3_raw_data["lateDataRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
