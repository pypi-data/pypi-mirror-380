# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_supplychain import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BillOfMaterialsImportJob:
    boto3_raw_data: "type_defs.BillOfMaterialsImportJobTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    jobId = field("jobId")
    status = field("status")
    s3uri = field("s3uri")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillOfMaterialsImportJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillOfMaterialsImportJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillOfMaterialsImportJobRequest:
    boto3_raw_data: "type_defs.CreateBillOfMaterialsImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    s3uri = field("s3uri")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBillOfMaterialsImportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillOfMaterialsImportJobRequestTypeDef"]
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
class CreateDataLakeNamespaceRequest:
    boto3_raw_data: "type_defs.CreateDataLakeNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataLakeNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeNamespace:
    boto3_raw_data: "type_defs.DataLakeNamespaceTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    name = field("name")
    arn = field("arn")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakeNamespaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeNamespaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceRequest:
    boto3_raw_data: "type_defs.CreateInstanceRequestTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    instanceDescription = field("instanceDescription")
    kmsKeyArn = field("kmsKeyArn")
    webAppDnsDomain = field("webAppDnsDomain")
    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    awsAccountId = field("awsAccountId")
    state = field("state")
    errorMessage = field("errorMessage")
    webAppDnsDomain = field("webAppDnsDomain")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    instanceName = field("instanceName")
    instanceDescription = field("instanceDescription")
    kmsKeyArn = field("kmsKeyArn")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationEventDatasetLoadExecutionDetails:
    boto3_raw_data: (
        "type_defs.DataIntegrationEventDatasetLoadExecutionDetailsTypeDef"
    ) = dataclasses.field()

    status = field("status")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationEventDatasetLoadExecutionDetailsTypeDef"
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
                "type_defs.DataIntegrationEventDatasetLoadExecutionDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationEventDatasetTargetConfiguration:
    boto3_raw_data: (
        "type_defs.DataIntegrationEventDatasetTargetConfigurationTypeDef"
    ) = dataclasses.field()

    datasetIdentifier = field("datasetIdentifier")
    operationType = field("operationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationEventDatasetTargetConfigurationTypeDef"
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
                "type_defs.DataIntegrationEventDatasetTargetConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetSource:
    boto3_raw_data: "type_defs.DataIntegrationFlowDatasetSourceTypeDef" = (
        dataclasses.field()
    )

    datasetIdentifier = field("datasetIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowDatasetSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDatasetSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowExecutionOutputMetadata:
    boto3_raw_data: "type_defs.DataIntegrationFlowExecutionOutputMetadataTypeDef" = (
        dataclasses.field()
    )

    diagnosticReportsRootS3URI = field("diagnosticReportsRootS3URI")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowExecutionOutputMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowExecutionOutputMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowS3Source:
    boto3_raw_data: "type_defs.DataIntegrationFlowS3SourceTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    key = field("key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowS3SourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowS3SourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowFieldPriorityDedupeField:
    boto3_raw_data: "type_defs.DataIntegrationFlowFieldPriorityDedupeFieldTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowFieldPriorityDedupeFieldTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowFieldPriorityDedupeFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowS3Options:
    boto3_raw_data: "type_defs.DataIntegrationFlowS3OptionsTypeDef" = (
        dataclasses.field()
    )

    fileType = field("fileType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowS3OptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowS3OptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowSQLTransformationConfiguration:
    boto3_raw_data: (
        "type_defs.DataIntegrationFlowSQLTransformationConfigurationTypeDef"
    ) = dataclasses.field()

    query = field("query")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowSQLTransformationConfigurationTypeDef"
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
                "type_defs.DataIntegrationFlowSQLTransformationConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetPartitionFieldTransform:
    boto3_raw_data: "type_defs.DataLakeDatasetPartitionFieldTransformTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataLakeDatasetPartitionFieldTransformTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetPartitionFieldTransformTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetPrimaryKeyField:
    boto3_raw_data: "type_defs.DataLakeDatasetPrimaryKeyFieldTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataLakeDatasetPrimaryKeyFieldTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetPrimaryKeyFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetSchemaField:
    boto3_raw_data: "type_defs.DataLakeDatasetSchemaFieldTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    isRequired = field("isRequired")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeDatasetSchemaFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetSchemaFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataIntegrationFlowRequest:
    boto3_raw_data: "type_defs.DeleteDataIntegrationFlowRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDataIntegrationFlowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataIntegrationFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataLakeDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDataLakeDatasetRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataLakeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataLakeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataLakeNamespaceRequest:
    boto3_raw_data: "type_defs.DeleteDataLakeNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDataLakeNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataLakeNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceRequest:
    boto3_raw_data: "type_defs.DeleteInstanceRequestTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillOfMaterialsImportJobRequest:
    boto3_raw_data: "type_defs.GetBillOfMaterialsImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBillOfMaterialsImportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillOfMaterialsImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataIntegrationEventRequest:
    boto3_raw_data: "type_defs.GetDataIntegrationEventRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    eventId = field("eventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataIntegrationEventRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataIntegrationEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataIntegrationFlowExecutionRequest:
    boto3_raw_data: "type_defs.GetDataIntegrationFlowExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    flowName = field("flowName")
    executionId = field("executionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataIntegrationFlowExecutionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataIntegrationFlowExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataIntegrationFlowRequest:
    boto3_raw_data: "type_defs.GetDataIntegrationFlowRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataIntegrationFlowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataIntegrationFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeDatasetRequest:
    boto3_raw_data: "type_defs.GetDataLakeDatasetRequestTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    namespace = field("namespace")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeNamespaceRequest:
    boto3_raw_data: "type_defs.GetDataLakeNamespaceRequestTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceRequest:
    boto3_raw_data: "type_defs.GetInstanceRequestTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceRequestTypeDef"]
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
class ListDataIntegrationEventsRequest:
    boto3_raw_data: "type_defs.ListDataIntegrationEventsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    eventType = field("eventType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataIntegrationEventsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationFlowExecutionsRequest:
    boto3_raw_data: "type_defs.ListDataIntegrationFlowExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    flowName = field("flowName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataIntegrationFlowExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationFlowExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationFlowsRequest:
    boto3_raw_data: "type_defs.ListDataIntegrationFlowsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataIntegrationFlowsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationFlowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeDatasetsRequest:
    boto3_raw_data: "type_defs.ListDataLakeDatasetsRequestTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    namespace = field("namespace")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataLakeDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeNamespacesRequest:
    boto3_raw_data: "type_defs.ListDataLakeNamespacesRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataLakeNamespacesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeNamespacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequest:
    boto3_raw_data: "type_defs.ListInstancesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    instanceNameFilter = field("instanceNameFilter")
    instanceStateFilter = field("instanceStateFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestTypeDef"]
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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class UpdateDataLakeDatasetRequest:
    boto3_raw_data: "type_defs.UpdateDataLakeDatasetRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    namespace = field("namespace")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataLakeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataLakeNamespaceRequest:
    boto3_raw_data: "type_defs.UpdateDataLakeNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDataLakeNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceRequest:
    boto3_raw_data: "type_defs.UpdateInstanceRequestTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    instanceName = field("instanceName")
    instanceDescription = field("instanceDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillOfMaterialsImportJobResponse:
    boto3_raw_data: "type_defs.CreateBillOfMaterialsImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBillOfMaterialsImportJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillOfMaterialsImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataIntegrationFlowResponse:
    boto3_raw_data: "type_defs.CreateDataIntegrationFlowResponseTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataIntegrationFlowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataIntegrationFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataIntegrationFlowResponse:
    boto3_raw_data: "type_defs.DeleteDataIntegrationFlowResponseTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataIntegrationFlowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataIntegrationFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataLakeDatasetResponse:
    boto3_raw_data: "type_defs.DeleteDataLakeDatasetResponseTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    namespace = field("namespace")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDataLakeDatasetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataLakeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataLakeNamespaceResponse:
    boto3_raw_data: "type_defs.DeleteDataLakeNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDataLakeNamespaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataLakeNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillOfMaterialsImportJobResponse:
    boto3_raw_data: "type_defs.GetBillOfMaterialsImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def job(self):  # pragma: no cover
        return BillOfMaterialsImportJob.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBillOfMaterialsImportJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillOfMaterialsImportJobResponseTypeDef"]
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

    tags = field("tags")

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
class SendDataIntegrationEventResponse:
    boto3_raw_data: "type_defs.SendDataIntegrationEventResponseTypeDef" = (
        dataclasses.field()
    )

    eventId = field("eventId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataIntegrationEventResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataIntegrationEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeNamespaceResponse:
    boto3_raw_data: "type_defs.CreateDataLakeNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def namespace(self):  # pragma: no cover
        return DataLakeNamespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataLakeNamespaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeNamespaceResponse:
    boto3_raw_data: "type_defs.GetDataLakeNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def namespace(self):  # pragma: no cover
        return DataLakeNamespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeNamespacesResponse:
    boto3_raw_data: "type_defs.ListDataLakeNamespacesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def namespaces(self):  # pragma: no cover
        return DataLakeNamespace.make_many(self.boto3_raw_data["namespaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataLakeNamespacesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeNamespacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataLakeNamespaceResponse:
    boto3_raw_data: "type_defs.UpdateDataLakeNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def namespace(self):  # pragma: no cover
        return DataLakeNamespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDataLakeNamespaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceResponse:
    boto3_raw_data: "type_defs.CreateInstanceResponseTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return Instance.make_one(self.boto3_raw_data["instance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceResponse:
    boto3_raw_data: "type_defs.DeleteInstanceResponseTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return Instance.make_one(self.boto3_raw_data["instance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceResponse:
    boto3_raw_data: "type_defs.GetInstanceResponseTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return Instance.make_one(self.boto3_raw_data["instance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesResponse:
    boto3_raw_data: "type_defs.ListInstancesResponseTypeDef" = dataclasses.field()

    @cached_property
    def instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceResponse:
    boto3_raw_data: "type_defs.UpdateInstanceResponseTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return Instance.make_one(self.boto3_raw_data["instance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationEventDatasetTargetDetails:
    boto3_raw_data: "type_defs.DataIntegrationEventDatasetTargetDetailsTypeDef" = (
        dataclasses.field()
    )

    datasetIdentifier = field("datasetIdentifier")
    operationType = field("operationType")

    @cached_property
    def datasetLoadExecution(self):  # pragma: no cover
        return DataIntegrationEventDatasetLoadExecutionDetails.make_one(
            self.boto3_raw_data["datasetLoadExecution"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationEventDatasetTargetDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationEventDatasetTargetDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowExecutionSourceInfo:
    boto3_raw_data: "type_defs.DataIntegrationFlowExecutionSourceInfoTypeDef" = (
        dataclasses.field()
    )

    sourceType = field("sourceType")

    @cached_property
    def s3Source(self):  # pragma: no cover
        return DataIntegrationFlowS3Source.make_one(self.boto3_raw_data["s3Source"])

    @cached_property
    def datasetSource(self):  # pragma: no cover
        return DataIntegrationFlowDatasetSource.make_one(
            self.boto3_raw_data["datasetSource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowExecutionSourceInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowExecutionSourceInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationOutput:
    boto3_raw_data: "type_defs.DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationOutputTypeDef" = (dataclasses.field())

    @cached_property
    def fields(self):  # pragma: no cover
        return DataIntegrationFlowFieldPriorityDedupeField.make_many(
            self.boto3_raw_data["fields"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationOutputTypeDef"
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
                "type_defs.DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration:
    boto3_raw_data: (
        "type_defs.DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return DataIntegrationFlowFieldPriorityDedupeField.make_many(
            self.boto3_raw_data["fields"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationTypeDef"
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
                "type_defs.DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowS3SourceConfiguration:
    boto3_raw_data: "type_defs.DataIntegrationFlowS3SourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    prefix = field("prefix")

    @cached_property
    def options(self):  # pragma: no cover
        return DataIntegrationFlowS3Options.make_one(self.boto3_raw_data["options"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowS3SourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowS3SourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowS3TargetConfiguration:
    boto3_raw_data: "type_defs.DataIntegrationFlowS3TargetConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    prefix = field("prefix")

    @cached_property
    def options(self):  # pragma: no cover
        return DataIntegrationFlowS3Options.make_one(self.boto3_raw_data["options"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowS3TargetConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowS3TargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowTransformation:
    boto3_raw_data: "type_defs.DataIntegrationFlowTransformationTypeDef" = (
        dataclasses.field()
    )

    transformationType = field("transformationType")

    @cached_property
    def sqlTransformation(self):  # pragma: no cover
        return DataIntegrationFlowSQLTransformationConfiguration.make_one(
            self.boto3_raw_data["sqlTransformation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowTransformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetPartitionField:
    boto3_raw_data: "type_defs.DataLakeDatasetPartitionFieldTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def transform(self):  # pragma: no cover
        return DataLakeDatasetPartitionFieldTransform.make_one(
            self.boto3_raw_data["transform"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataLakeDatasetPartitionFieldTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetPartitionFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetSchemaOutput:
    boto3_raw_data: "type_defs.DataLakeDatasetSchemaOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def fields(self):  # pragma: no cover
        return DataLakeDatasetSchemaField.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def primaryKeys(self):  # pragma: no cover
        return DataLakeDatasetPrimaryKeyField.make_many(
            self.boto3_raw_data["primaryKeys"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeDatasetSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetSchema:
    boto3_raw_data: "type_defs.DataLakeDatasetSchemaTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def fields(self):  # pragma: no cover
        return DataLakeDatasetSchemaField.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def primaryKeys(self):  # pragma: no cover
        return DataLakeDatasetPrimaryKeyField.make_many(
            self.boto3_raw_data["primaryKeys"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeDatasetSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataIntegrationEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    eventType = field("eventType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataIntegrationEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationFlowExecutionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDataIntegrationFlowExecutionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    instanceId = field("instanceId")
    flowName = field("flowName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataIntegrationFlowExecutionsRequestPaginateTypeDef"
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
                "type_defs.ListDataIntegrationFlowExecutionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationFlowsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataIntegrationFlowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataIntegrationFlowsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationFlowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeDatasetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataLakeDatasetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    namespace = field("namespace")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataLakeDatasetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeDatasetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeNamespacesRequestPaginate:
    boto3_raw_data: "type_defs.ListDataLakeNamespacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataLakeNamespacesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeNamespacesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    instanceNameFilter = field("instanceNameFilter")
    instanceStateFilter = field("instanceStateFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataIntegrationEventRequest:
    boto3_raw_data: "type_defs.SendDataIntegrationEventRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    eventType = field("eventType")
    data = field("data")
    eventGroupId = field("eventGroupId")
    eventTimestamp = field("eventTimestamp")
    clientToken = field("clientToken")

    @cached_property
    def datasetTarget(self):  # pragma: no cover
        return DataIntegrationEventDatasetTargetConfiguration.make_one(
            self.boto3_raw_data["datasetTarget"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataIntegrationEventRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataIntegrationEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationEvent:
    boto3_raw_data: "type_defs.DataIntegrationEventTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    eventId = field("eventId")
    eventType = field("eventType")
    eventGroupId = field("eventGroupId")
    eventTimestamp = field("eventTimestamp")

    @cached_property
    def datasetTargetDetails(self):  # pragma: no cover
        return DataIntegrationEventDatasetTargetDetails.make_one(
            self.boto3_raw_data["datasetTargetDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowExecution:
    boto3_raw_data: "type_defs.DataIntegrationFlowExecutionTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    flowName = field("flowName")
    executionId = field("executionId")
    status = field("status")

    @cached_property
    def sourceInfo(self):  # pragma: no cover
        return DataIntegrationFlowExecutionSourceInfo.make_one(
            self.boto3_raw_data["sourceInfo"]
        )

    message = field("message")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def outputMetadata(self):  # pragma: no cover
        return DataIntegrationFlowExecutionOutputMetadata.make_one(
            self.boto3_raw_data["outputMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDedupeStrategyOutput:
    boto3_raw_data: "type_defs.DataIntegrationFlowDedupeStrategyOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def fieldPriority(self):  # pragma: no cover
        return (
            DataIntegrationFlowFieldPriorityDedupeStrategyConfigurationOutput.make_one(
                self.boto3_raw_data["fieldPriority"]
            )
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDedupeStrategyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDedupeStrategyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetPartitionSpecOutput:
    boto3_raw_data: "type_defs.DataLakeDatasetPartitionSpecOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fields(self):  # pragma: no cover
        return DataLakeDatasetPartitionField.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataLakeDatasetPartitionSpecOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetPartitionSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDatasetPartitionSpec:
    boto3_raw_data: "type_defs.DataLakeDatasetPartitionSpecTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fields(self):  # pragma: no cover
        return DataLakeDatasetPartitionField.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataLakeDatasetPartitionSpecTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataLakeDatasetPartitionSpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataIntegrationEventResponse:
    boto3_raw_data: "type_defs.GetDataIntegrationEventResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def event(self):  # pragma: no cover
        return DataIntegrationEvent.make_one(self.boto3_raw_data["event"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataIntegrationEventResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataIntegrationEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationEventsResponse:
    boto3_raw_data: "type_defs.ListDataIntegrationEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def events(self):  # pragma: no cover
        return DataIntegrationEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataIntegrationEventsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataIntegrationFlowExecutionResponse:
    boto3_raw_data: "type_defs.GetDataIntegrationFlowExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flowExecution(self):  # pragma: no cover
        return DataIntegrationFlowExecution.make_one(
            self.boto3_raw_data["flowExecution"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataIntegrationFlowExecutionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataIntegrationFlowExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationFlowExecutionsResponse:
    boto3_raw_data: "type_defs.ListDataIntegrationFlowExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flowExecutions(self):  # pragma: no cover
        return DataIntegrationFlowExecution.make_many(
            self.boto3_raw_data["flowExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataIntegrationFlowExecutionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationFlowExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetOptionsOutput:
    boto3_raw_data: "type_defs.DataIntegrationFlowDatasetOptionsOutputTypeDef" = (
        dataclasses.field()
    )

    loadType = field("loadType")
    dedupeRecords = field("dedupeRecords")

    @cached_property
    def dedupeStrategy(self):  # pragma: no cover
        return DataIntegrationFlowDedupeStrategyOutput.make_one(
            self.boto3_raw_data["dedupeStrategy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDatasetOptionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDatasetOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDedupeStrategy:
    boto3_raw_data: "type_defs.DataIntegrationFlowDedupeStrategyTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    fieldPriority = field("fieldPriority")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDedupeStrategyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDedupeStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataLakeDataset:
    boto3_raw_data: "type_defs.DataLakeDatasetTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    namespace = field("namespace")
    name = field("name")
    arn = field("arn")

    @cached_property
    def schema(self):  # pragma: no cover
        return DataLakeDatasetSchemaOutput.make_one(self.boto3_raw_data["schema"])

    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    description = field("description")

    @cached_property
    def partitionSpec(self):  # pragma: no cover
        return DataLakeDatasetPartitionSpecOutput.make_one(
            self.boto3_raw_data["partitionSpec"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataLakeDatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataLakeDatasetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetSourceConfigurationOutput:
    boto3_raw_data: (
        "type_defs.DataIntegrationFlowDatasetSourceConfigurationOutputTypeDef"
    ) = dataclasses.field()

    datasetIdentifier = field("datasetIdentifier")

    @cached_property
    def options(self):  # pragma: no cover
        return DataIntegrationFlowDatasetOptionsOutput.make_one(
            self.boto3_raw_data["options"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDatasetSourceConfigurationOutputTypeDef"
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
                "type_defs.DataIntegrationFlowDatasetSourceConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetTargetConfigurationOutput:
    boto3_raw_data: (
        "type_defs.DataIntegrationFlowDatasetTargetConfigurationOutputTypeDef"
    ) = dataclasses.field()

    datasetIdentifier = field("datasetIdentifier")

    @cached_property
    def options(self):  # pragma: no cover
        return DataIntegrationFlowDatasetOptionsOutput.make_one(
            self.boto3_raw_data["options"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDatasetTargetConfigurationOutputTypeDef"
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
                "type_defs.DataIntegrationFlowDatasetTargetConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeDatasetResponse:
    boto3_raw_data: "type_defs.CreateDataLakeDatasetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataset(self):  # pragma: no cover
        return DataLakeDataset.make_one(self.boto3_raw_data["dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataLakeDatasetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataLakeDatasetResponse:
    boto3_raw_data: "type_defs.GetDataLakeDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataset(self):  # pragma: no cover
        return DataLakeDataset.make_one(self.boto3_raw_data["dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataLakeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataLakeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataLakeDatasetsResponse:
    boto3_raw_data: "type_defs.ListDataLakeDatasetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasets(self):  # pragma: no cover
        return DataLakeDataset.make_many(self.boto3_raw_data["datasets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataLakeDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataLakeDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataLakeDatasetResponse:
    boto3_raw_data: "type_defs.UpdateDataLakeDatasetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataset(self):  # pragma: no cover
        return DataLakeDataset.make_one(self.boto3_raw_data["dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDataLakeDatasetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataLakeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataLakeDatasetRequest:
    boto3_raw_data: "type_defs.CreateDataLakeDatasetRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    namespace = field("namespace")
    name = field("name")
    schema = field("schema")
    description = field("description")
    partitionSpec = field("partitionSpec")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataLakeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataLakeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowSourceOutput:
    boto3_raw_data: "type_defs.DataIntegrationFlowSourceOutputTypeDef" = (
        dataclasses.field()
    )

    sourceType = field("sourceType")
    sourceName = field("sourceName")

    @cached_property
    def s3Source(self):  # pragma: no cover
        return DataIntegrationFlowS3SourceConfiguration.make_one(
            self.boto3_raw_data["s3Source"]
        )

    @cached_property
    def datasetSource(self):  # pragma: no cover
        return DataIntegrationFlowDatasetSourceConfigurationOutput.make_one(
            self.boto3_raw_data["datasetSource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowSourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowTargetOutput:
    boto3_raw_data: "type_defs.DataIntegrationFlowTargetOutputTypeDef" = (
        dataclasses.field()
    )

    targetType = field("targetType")

    @cached_property
    def s3Target(self):  # pragma: no cover
        return DataIntegrationFlowS3TargetConfiguration.make_one(
            self.boto3_raw_data["s3Target"]
        )

    @cached_property
    def datasetTarget(self):  # pragma: no cover
        return DataIntegrationFlowDatasetTargetConfigurationOutput.make_one(
            self.boto3_raw_data["datasetTarget"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowTargetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetOptions:
    boto3_raw_data: "type_defs.DataIntegrationFlowDatasetOptionsTypeDef" = (
        dataclasses.field()
    )

    loadType = field("loadType")
    dedupeRecords = field("dedupeRecords")
    dedupeStrategy = field("dedupeStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDatasetOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDatasetOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlow:
    boto3_raw_data: "type_defs.DataIntegrationFlowTypeDef" = dataclasses.field()

    instanceId = field("instanceId")
    name = field("name")

    @cached_property
    def sources(self):  # pragma: no cover
        return DataIntegrationFlowSourceOutput.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def transformation(self):  # pragma: no cover
        return DataIntegrationFlowTransformation.make_one(
            self.boto3_raw_data["transformation"]
        )

    @cached_property
    def target(self):  # pragma: no cover
        return DataIntegrationFlowTargetOutput.make_one(self.boto3_raw_data["target"])

    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetTargetConfiguration:
    boto3_raw_data: "type_defs.DataIntegrationFlowDatasetTargetConfigurationTypeDef" = (
        dataclasses.field()
    )

    datasetIdentifier = field("datasetIdentifier")

    @cached_property
    def options(self):  # pragma: no cover
        return DataIntegrationFlowDatasetOptions.make_one(
            self.boto3_raw_data["options"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDatasetTargetConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDatasetTargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataIntegrationFlowResponse:
    boto3_raw_data: "type_defs.GetDataIntegrationFlowResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flow(self):  # pragma: no cover
        return DataIntegrationFlow.make_one(self.boto3_raw_data["flow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataIntegrationFlowResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataIntegrationFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataIntegrationFlowsResponse:
    boto3_raw_data: "type_defs.ListDataIntegrationFlowsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flows(self):  # pragma: no cover
        return DataIntegrationFlow.make_many(self.boto3_raw_data["flows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataIntegrationFlowsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataIntegrationFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataIntegrationFlowResponse:
    boto3_raw_data: "type_defs.UpdateDataIntegrationFlowResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flow(self):  # pragma: no cover
        return DataIntegrationFlow.make_one(self.boto3_raw_data["flow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataIntegrationFlowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataIntegrationFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowDatasetSourceConfiguration:
    boto3_raw_data: "type_defs.DataIntegrationFlowDatasetSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    datasetIdentifier = field("datasetIdentifier")
    options = field("options")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataIntegrationFlowDatasetSourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowDatasetSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowTarget:
    boto3_raw_data: "type_defs.DataIntegrationFlowTargetTypeDef" = dataclasses.field()

    targetType = field("targetType")

    @cached_property
    def s3Target(self):  # pragma: no cover
        return DataIntegrationFlowS3TargetConfiguration.make_one(
            self.boto3_raw_data["s3Target"]
        )

    @cached_property
    def datasetTarget(self):  # pragma: no cover
        return DataIntegrationFlowDatasetTargetConfiguration.make_one(
            self.boto3_raw_data["datasetTarget"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataIntegrationFlowSource:
    boto3_raw_data: "type_defs.DataIntegrationFlowSourceTypeDef" = dataclasses.field()

    sourceType = field("sourceType")
    sourceName = field("sourceName")

    @cached_property
    def s3Source(self):  # pragma: no cover
        return DataIntegrationFlowS3SourceConfiguration.make_one(
            self.boto3_raw_data["s3Source"]
        )

    datasetSource = field("datasetSource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataIntegrationFlowSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataIntegrationFlowSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataIntegrationFlowRequest:
    boto3_raw_data: "type_defs.CreateDataIntegrationFlowRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")
    sources = field("sources")

    @cached_property
    def transformation(self):  # pragma: no cover
        return DataIntegrationFlowTransformation.make_one(
            self.boto3_raw_data["transformation"]
        )

    target = field("target")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataIntegrationFlowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataIntegrationFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataIntegrationFlowRequest:
    boto3_raw_data: "type_defs.UpdateDataIntegrationFlowRequestTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    name = field("name")
    sources = field("sources")

    @cached_property
    def transformation(self):  # pragma: no cover
        return DataIntegrationFlowTransformation.make_one(
            self.boto3_raw_data["transformation"]
        )

    target = field("target")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDataIntegrationFlowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataIntegrationFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
