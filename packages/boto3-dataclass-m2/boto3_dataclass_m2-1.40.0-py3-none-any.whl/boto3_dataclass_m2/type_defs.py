# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_m2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AlternateKey:
    boto3_raw_data: "type_defs.AlternateKeyTypeDef" = dataclasses.field()

    length = field("length")
    offset = field("offset")
    allowDuplicates = field("allowDuplicates")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlternateKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlternateKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSummary:
    boto3_raw_data: "type_defs.ApplicationSummaryTypeDef" = dataclasses.field()

    applicationArn = field("applicationArn")
    applicationId = field("applicationId")
    applicationVersion = field("applicationVersion")
    creationTime = field("creationTime")
    engineType = field("engineType")
    name = field("name")
    status = field("status")
    deploymentStatus = field("deploymentStatus")
    description = field("description")
    environmentId = field("environmentId")
    lastStartTime = field("lastStartTime")
    roleArn = field("roleArn")
    versionStatus = field("versionStatus")

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
class ApplicationVersionSummary:
    boto3_raw_data: "type_defs.ApplicationVersionSummaryTypeDef" = dataclasses.field()

    applicationVersion = field("applicationVersion")
    creationTime = field("creationTime")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileBatchJobDefinition:
    boto3_raw_data: "type_defs.FileBatchJobDefinitionTypeDef" = dataclasses.field()

    fileName = field("fileName")
    folderPath = field("folderPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileBatchJobDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileBatchJobDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScriptBatchJobDefinition:
    boto3_raw_data: "type_defs.ScriptBatchJobDefinitionTypeDef" = dataclasses.field()

    scriptName = field("scriptName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScriptBatchJobDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScriptBatchJobDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileBatchJobIdentifier:
    boto3_raw_data: "type_defs.FileBatchJobIdentifierTypeDef" = dataclasses.field()

    fileName = field("fileName")
    folderPath = field("folderPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileBatchJobIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileBatchJobIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScriptBatchJobIdentifier:
    boto3_raw_data: "type_defs.ScriptBatchJobIdentifierTypeDef" = dataclasses.field()

    scriptName = field("scriptName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScriptBatchJobIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScriptBatchJobIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelBatchJobExecutionRequest:
    boto3_raw_data: "type_defs.CancelBatchJobExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    executionId = field("executionId")
    authSecretsManagerArn = field("authSecretsManagerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelBatchJobExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelBatchJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Definition:
    boto3_raw_data: "type_defs.DefinitionTypeDef" = dataclasses.field()

    content = field("content")
    s3Location = field("s3Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DefinitionTypeDef"]]
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
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    applicationVersion = field("applicationVersion")
    environmentId = field("environmentId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HighAvailabilityConfig:
    boto3_raw_data: "type_defs.HighAvailabilityConfigTypeDef" = dataclasses.field()

    desiredCapacity = field("desiredCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HighAvailabilityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HighAvailabilityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalLocation:
    boto3_raw_data: "type_defs.ExternalLocationTypeDef" = dataclasses.field()

    s3Location = field("s3Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExternalLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetExportSummary:
    boto3_raw_data: "type_defs.DataSetExportSummaryTypeDef" = dataclasses.field()

    failed = field("failed")
    inProgress = field("inProgress")
    pending = field("pending")
    succeeded = field("succeeded")
    total = field("total")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSetExportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetExportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetImportSummary:
    boto3_raw_data: "type_defs.DataSetImportSummaryTypeDef" = dataclasses.field()

    failed = field("failed")
    inProgress = field("inProgress")
    pending = field("pending")
    succeeded = field("succeeded")
    total = field("total")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSetImportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetImportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetSummary:
    boto3_raw_data: "type_defs.DataSetSummaryTypeDef" = dataclasses.field()

    dataSetName = field("dataSetName")
    creationTime = field("creationTime")
    dataSetOrg = field("dataSetOrg")
    format = field("format")
    lastReferencedTime = field("lastReferencedTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordLength:
    boto3_raw_data: "type_defs.RecordLengthTypeDef" = dataclasses.field()

    max = field("max")
    min = field("min")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordLengthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordLengthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GdgDetailAttributes:
    boto3_raw_data: "type_defs.GdgDetailAttributesTypeDef" = dataclasses.field()

    limit = field("limit")
    rollDisposition = field("rollDisposition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GdgDetailAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GdgDetailAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoDetailAttributes:
    boto3_raw_data: "type_defs.PoDetailAttributesTypeDef" = dataclasses.field()

    encoding = field("encoding")
    format = field("format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PoDetailAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PoDetailAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PsDetailAttributes:
    boto3_raw_data: "type_defs.PsDetailAttributesTypeDef" = dataclasses.field()

    encoding = field("encoding")
    format = field("format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PsDetailAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PsDetailAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GdgAttributes:
    boto3_raw_data: "type_defs.GdgAttributesTypeDef" = dataclasses.field()

    limit = field("limit")
    rollDisposition = field("rollDisposition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GdgAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GdgAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoAttributes:
    boto3_raw_data: "type_defs.PoAttributesTypeDef" = dataclasses.field()

    format = field("format")
    memberFileExtensions = field("memberFileExtensions")
    encoding = field("encoding")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PsAttributes:
    boto3_raw_data: "type_defs.PsAttributesTypeDef" = dataclasses.field()

    format = field("format")
    encoding = field("encoding")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PsAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PsAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationFromEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteApplicationFromEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationFromEnvironmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationFromEnvironmentRequestTypeDef"]
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

    applicationId = field("applicationId")

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
class DeleteEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployedVersionSummary:
    boto3_raw_data: "type_defs.DeployedVersionSummaryTypeDef" = dataclasses.field()

    applicationVersion = field("applicationVersion")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeployedVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployedVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentSummary:
    boto3_raw_data: "type_defs.DeploymentSummaryTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    applicationVersion = field("applicationVersion")
    creationTime = field("creationTime")
    deploymentId = field("deploymentId")
    environmentId = field("environmentId")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EfsStorageConfiguration:
    boto3_raw_data: "type_defs.EfsStorageConfigurationTypeDef" = dataclasses.field()

    fileSystemId = field("fileSystemId")
    mountPoint = field("mountPoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EfsStorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EfsStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineVersionsSummary:
    boto3_raw_data: "type_defs.EngineVersionsSummaryTypeDef" = dataclasses.field()

    engineType = field("engineType")
    engineVersion = field("engineVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngineVersionsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineVersionsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentSummary:
    boto3_raw_data: "type_defs.EnvironmentSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    engineType = field("engineType")
    engineVersion = field("engineVersion")
    environmentArn = field("environmentArn")
    environmentId = field("environmentId")
    instanceType = field("instanceType")
    name = field("name")
    status = field("status")
    networkType = field("networkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxStorageConfiguration:
    boto3_raw_data: "type_defs.FsxStorageConfigurationTypeDef" = dataclasses.field()

    fileSystemId = field("fileSystemId")
    mountPoint = field("mountPoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FsxStorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FsxStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRequest:
    boto3_raw_data: "type_defs.GetApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogGroupSummary:
    boto3_raw_data: "type_defs.LogGroupSummaryTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logType = field("logType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogGroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogGroupSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationVersionRequest:
    boto3_raw_data: "type_defs.GetApplicationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    applicationVersion = field("applicationVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchJobExecutionRequest:
    boto3_raw_data: "type_defs.GetBatchJobExecutionRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    executionId = field("executionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchJobExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobStepRestartMarker:
    boto3_raw_data: "type_defs.JobStepRestartMarkerTypeDef" = dataclasses.field()

    fromStep = field("fromStep")
    fromProcStep = field("fromProcStep")
    skip = field("skip")
    stepCheckpoint = field("stepCheckpoint")
    toProcStep = field("toProcStep")
    toStep = field("toStep")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobStepRestartMarkerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobStepRestartMarkerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetDetailsRequest:
    boto3_raw_data: "type_defs.GetDataSetDetailsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    dataSetName = field("dataSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetExportTaskRequest:
    boto3_raw_data: "type_defs.GetDataSetExportTaskRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    taskId = field("taskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetExportTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetExportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetImportTaskRequest:
    boto3_raw_data: "type_defs.GetDataSetImportTaskRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    taskId = field("taskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetImportTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentRequest:
    boto3_raw_data: "type_defs.GetDeploymentRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentRequest:
    boto3_raw_data: "type_defs.GetEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobIdentifier:
    boto3_raw_data: "type_defs.JobIdentifierTypeDef" = dataclasses.field()

    fileName = field("fileName")
    scriptName = field("scriptName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobStep:
    boto3_raw_data: "type_defs.JobStepTypeDef" = dataclasses.field()

    procStepName = field("procStepName")
    procStepNumber = field("procStepNumber")
    stepCheckpoint = field("stepCheckpoint")
    stepCheckpointStatus = field("stepCheckpointStatus")
    stepCheckpointTime = field("stepCheckpointTime")
    stepCondCode = field("stepCondCode")
    stepName = field("stepName")
    stepNumber = field("stepNumber")
    stepRestartable = field("stepRestartable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobStepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobStepTypeDef"]]
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
class ListApplicationVersionsRequest:
    boto3_raw_data: "type_defs.ListApplicationVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationVersionsRequestTypeDef"]
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

    environmentId = field("environmentId")
    maxResults = field("maxResults")
    names = field("names")
    nextToken = field("nextToken")

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
class ListBatchJobDefinitionsRequest:
    boto3_raw_data: "type_defs.ListBatchJobDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchJobDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobRestartPointsRequest:
    boto3_raw_data: "type_defs.ListBatchJobRestartPointsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    executionId = field("executionId")
    authSecretsManagerArn = field("authSecretsManagerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchJobRestartPointsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobRestartPointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetExportHistoryRequest:
    boto3_raw_data: "type_defs.ListDataSetExportHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSetExportHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetExportHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetImportHistoryRequest:
    boto3_raw_data: "type_defs.ListDataSetImportHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSetImportHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetImportHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetsRequest:
    boto3_raw_data: "type_defs.ListDataSetsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nameFilter = field("nameFilter")
    nextToken = field("nextToken")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsRequest:
    boto3_raw_data: "type_defs.ListDeploymentsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngineVersionsRequest:
    boto3_raw_data: "type_defs.ListEngineVersionsRequestTypeDef" = dataclasses.field()

    engineType = field("engineType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngineVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngineVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestTypeDef" = dataclasses.field()

    engineType = field("engineType")
    maxResults = field("maxResults")
    names = field("names")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestTypeDef"]
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
class MaintenanceSchedule:
    boto3_raw_data: "type_defs.MaintenanceScheduleTypeDef" = dataclasses.field()

    endTime = field("endTime")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrimaryKey:
    boto3_raw_data: "type_defs.PrimaryKeyTypeDef" = dataclasses.field()

    length = field("length")
    offset = field("offset")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrimaryKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrimaryKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartApplicationRequest:
    boto3_raw_data: "type_defs.StartApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

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
class StopApplicationRequest:
    boto3_raw_data: "type_defs.StopApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    forceStop = field("forceStop")

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
class UpdateEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    applyDuringMaintenanceWindow = field("applyDuringMaintenanceWindow")
    desiredCapacity = field("desiredCapacity")
    engineVersion = field("engineVersion")
    forceUpdate = field("forceUpdate")
    instanceType = field("instanceType")
    preferredMaintenanceWindow = field("preferredMaintenanceWindow")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchJobDefinition:
    boto3_raw_data: "type_defs.BatchJobDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def fileBatchJobDefinition(self):  # pragma: no cover
        return FileBatchJobDefinition.make_one(
            self.boto3_raw_data["fileBatchJobDefinition"]
        )

    @cached_property
    def scriptBatchJobDefinition(self):  # pragma: no cover
        return ScriptBatchJobDefinition.make_one(
            self.boto3_raw_data["scriptBatchJobDefinition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchJobDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchJobDefinitionTypeDef"]
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

    @cached_property
    def definition(self):  # pragma: no cover
        return Definition.make_one(self.boto3_raw_data["definition"])

    engineType = field("engineType")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    kmsKeyId = field("kmsKeyId")
    roleArn = field("roleArn")
    tags = field("tags")

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
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    currentApplicationVersion = field("currentApplicationVersion")

    @cached_property
    def definition(self):  # pragma: no cover
        return Definition.make_one(self.boto3_raw_data["definition"])

    description = field("description")

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


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    applicationArn = field("applicationArn")
    applicationId = field("applicationId")
    applicationVersion = field("applicationVersion")

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
class CreateDataSetExportTaskResponse:
    boto3_raw_data: "type_defs.CreateDataSetExportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataSetExportTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSetExportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSetImportTaskResponse:
    boto3_raw_data: "type_defs.CreateDataSetImportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataSetImportTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSetImportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentResponse:
    boto3_raw_data: "type_defs.CreateDeploymentResponseTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateEnvironmentResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationVersionResponse:
    boto3_raw_data: "type_defs.GetApplicationVersionResponseTypeDef" = (
        dataclasses.field()
    )

    applicationVersion = field("applicationVersion")
    creationTime = field("creationTime")
    definitionContent = field("definitionContent")
    description = field("description")
    name = field("name")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApplicationVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentResponse:
    boto3_raw_data: "type_defs.GetDeploymentResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    applicationVersion = field("applicationVersion")
    creationTime = field("creationTime")
    deploymentId = field("deploymentId")
    environmentId = field("environmentId")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignedBluinsightsUrlResponse:
    boto3_raw_data: "type_defs.GetSignedBluinsightsUrlResponseTypeDef" = (
        dataclasses.field()
    )

    signedBiUrl = field("signedBiUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSignedBluinsightsUrlResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignedBluinsightsUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationVersionsResponse:
    boto3_raw_data: "type_defs.ListApplicationVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationVersions(self):  # pragma: no cover
        return ApplicationVersionSummary.make_many(
            self.boto3_raw_data["applicationVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationVersionsResponseTypeDef"]
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
    def applications(self):  # pragma: no cover
        return ApplicationSummary.make_many(self.boto3_raw_data["applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class StartBatchJobResponse:
    boto3_raw_data: "type_defs.StartBatchJobResponseTypeDef" = dataclasses.field()

    executionId = field("executionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBatchJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBatchJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResponse:
    boto3_raw_data: "type_defs.UpdateApplicationResponseTypeDef" = dataclasses.field()

    applicationVersion = field("applicationVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentResponse:
    boto3_raw_data: "type_defs.UpdateEnvironmentResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetExportItem:
    boto3_raw_data: "type_defs.DataSetExportItemTypeDef" = dataclasses.field()

    datasetName = field("datasetName")

    @cached_property
    def externalLocation(self):  # pragma: no cover
        return ExternalLocation.make_one(self.boto3_raw_data["externalLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetExportItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetExportItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetExportTask:
    boto3_raw_data: "type_defs.DataSetExportTaskTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def summary(self):  # pragma: no cover
        return DataSetExportSummary.make_one(self.boto3_raw_data["summary"])

    taskId = field("taskId")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetExportTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetExportTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetExportTaskResponse:
    boto3_raw_data: "type_defs.GetDataSetExportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    kmsKeyArn = field("kmsKeyArn")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def summary(self):  # pragma: no cover
        return DataSetExportSummary.make_one(self.boto3_raw_data["summary"])

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetExportTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetExportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetImportTask:
    boto3_raw_data: "type_defs.DataSetImportTaskTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def summary(self):  # pragma: no cover
        return DataSetImportSummary.make_one(self.boto3_raw_data["summary"])

    taskId = field("taskId")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetImportTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetImportTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetImportTaskResponse:
    boto3_raw_data: "type_defs.GetDataSetImportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def summary(self):  # pragma: no cover
        return DataSetImportSummary.make_one(self.boto3_raw_data["summary"])

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetImportTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetImportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetsResponse:
    boto3_raw_data: "type_defs.ListDataSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSets(self):  # pragma: no cover
        return DataSetSummary.make_many(self.boto3_raw_data["dataSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsResponse:
    boto3_raw_data: "type_defs.ListDeploymentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def deployments(self):  # pragma: no cover
        return DeploymentSummary.make_many(self.boto3_raw_data["deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngineVersionsResponse:
    boto3_raw_data: "type_defs.ListEngineVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def engineVersions(self):  # pragma: no cover
        return EngineVersionsSummary.make_many(self.boto3_raw_data["engineVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngineVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngineVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsResponse:
    boto3_raw_data: "type_defs.ListEnvironmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def environments(self):  # pragma: no cover
        return EnvironmentSummary.make_many(self.boto3_raw_data["environments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfiguration:
    boto3_raw_data: "type_defs.StorageConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def efs(self):  # pragma: no cover
        return EfsStorageConfiguration.make_one(self.boto3_raw_data["efs"])

    @cached_property
    def fsx(self):  # pragma: no cover
        return FsxStorageConfiguration.make_one(self.boto3_raw_data["fsx"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationResponse:
    boto3_raw_data: "type_defs.GetApplicationResponseTypeDef" = dataclasses.field()

    applicationArn = field("applicationArn")
    applicationId = field("applicationId")
    creationTime = field("creationTime")

    @cached_property
    def deployedVersion(self):  # pragma: no cover
        return DeployedVersionSummary.make_one(self.boto3_raw_data["deployedVersion"])

    description = field("description")
    engineType = field("engineType")
    environmentId = field("environmentId")
    kmsKeyId = field("kmsKeyId")
    lastStartTime = field("lastStartTime")

    @cached_property
    def latestVersion(self):  # pragma: no cover
        return ApplicationVersionSummary.make_one(self.boto3_raw_data["latestVersion"])

    listenerArns = field("listenerArns")
    listenerPorts = field("listenerPorts")
    loadBalancerDnsName = field("loadBalancerDnsName")

    @cached_property
    def logGroups(self):  # pragma: no cover
        return LogGroupSummary.make_many(self.boto3_raw_data["logGroups"])

    name = field("name")
    roleArn = field("roleArn")
    status = field("status")
    statusReason = field("statusReason")
    tags = field("tags")
    targetGroupArns = field("targetGroupArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestartBatchJobIdentifier:
    boto3_raw_data: "type_defs.RestartBatchJobIdentifierTypeDef" = dataclasses.field()

    executionId = field("executionId")

    @cached_property
    def jobStepRestartMarker(self):  # pragma: no cover
        return JobStepRestartMarker.make_one(
            self.boto3_raw_data["jobStepRestartMarker"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestartBatchJobIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestartBatchJobIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BatchJobIdentifier:
    boto3_raw_data: "type_defs.S3BatchJobIdentifierTypeDef" = dataclasses.field()

    bucket = field("bucket")

    @cached_property
    def identifier(self):  # pragma: no cover
        return JobIdentifier.make_one(self.boto3_raw_data["identifier"])

    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BatchJobIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BatchJobIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobRestartPointsResponse:
    boto3_raw_data: "type_defs.ListBatchJobRestartPointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchJobSteps(self):  # pragma: no cover
        return JobStep.make_many(self.boto3_raw_data["batchJobSteps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBatchJobRestartPointsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobRestartPointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    names = field("names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListBatchJobDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBatchJobDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetExportHistoryRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSetExportHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataSetExportHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetExportHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetImportHistoryRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSetImportHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataSetImportHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetImportHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSetsRequestPaginateTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nameFilter = field("nameFilter")
    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeploymentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngineVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListEngineVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    engineType = field("engineType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngineVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngineVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    engineType = field("engineType")
    names = field("names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListBatchJobExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    executionIds = field("executionIds")
    jobName = field("jobName")
    startedAfter = field("startedAfter")
    startedBefore = field("startedBefore")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBatchJobExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobExecutionsRequest:
    boto3_raw_data: "type_defs.ListBatchJobExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    executionIds = field("executionIds")
    jobName = field("jobName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    startedAfter = field("startedAfter")
    startedBefore = field("startedBefore")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchJobExecutionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingMaintenance:
    boto3_raw_data: "type_defs.PendingMaintenanceTypeDef" = dataclasses.field()

    engineVersion = field("engineVersion")

    @cached_property
    def schedule(self):  # pragma: no cover
        return MaintenanceSchedule.make_one(self.boto3_raw_data["schedule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingMaintenanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VsamAttributes:
    boto3_raw_data: "type_defs.VsamAttributesTypeDef" = dataclasses.field()

    format = field("format")

    @cached_property
    def alternateKeys(self):  # pragma: no cover
        return AlternateKey.make_many(self.boto3_raw_data["alternateKeys"])

    compressed = field("compressed")
    encoding = field("encoding")

    @cached_property
    def primaryKey(self):  # pragma: no cover
        return PrimaryKey.make_one(self.boto3_raw_data["primaryKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VsamAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VsamAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VsamDetailAttributes:
    boto3_raw_data: "type_defs.VsamDetailAttributesTypeDef" = dataclasses.field()

    @cached_property
    def alternateKeys(self):  # pragma: no cover
        return AlternateKey.make_many(self.boto3_raw_data["alternateKeys"])

    cacheAtStartup = field("cacheAtStartup")
    compressed = field("compressed")
    encoding = field("encoding")

    @cached_property
    def primaryKey(self):  # pragma: no cover
        return PrimaryKey.make_one(self.boto3_raw_data["primaryKey"])

    recordFormat = field("recordFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VsamDetailAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VsamDetailAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobDefinitionsResponse:
    boto3_raw_data: "type_defs.ListBatchJobDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchJobDefinitions(self):  # pragma: no cover
        return BatchJobDefinition.make_many(self.boto3_raw_data["batchJobDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchJobDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetExportConfig:
    boto3_raw_data: "type_defs.DataSetExportConfigTypeDef" = dataclasses.field()

    @cached_property
    def dataSets(self):  # pragma: no cover
        return DataSetExportItem.make_many(self.boto3_raw_data["dataSets"])

    s3Location = field("s3Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSetExportConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetExportConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetExportHistoryResponse:
    boto3_raw_data: "type_defs.ListDataSetExportHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataSetExportTasks(self):  # pragma: no cover
        return DataSetExportTask.make_many(self.boto3_raw_data["dataSetExportTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSetExportHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetExportHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetImportHistoryResponse:
    boto3_raw_data: "type_defs.ListDataSetImportHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataSetImportTasks(self):  # pragma: no cover
        return DataSetImportTask.make_many(self.boto3_raw_data["dataSetImportTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSetImportHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetImportHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateEnvironmentRequestTypeDef" = dataclasses.field()

    engineType = field("engineType")
    instanceType = field("instanceType")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    engineVersion = field("engineVersion")

    @cached_property
    def highAvailabilityConfig(self):  # pragma: no cover
        return HighAvailabilityConfig.make_one(
            self.boto3_raw_data["highAvailabilityConfig"]
        )

    kmsKeyId = field("kmsKeyId")
    networkType = field("networkType")
    preferredMaintenanceWindow = field("preferredMaintenanceWindow")
    publiclyAccessible = field("publiclyAccessible")
    securityGroupIds = field("securityGroupIds")

    @cached_property
    def storageConfigurations(self):  # pragma: no cover
        return StorageConfiguration.make_many(
            self.boto3_raw_data["storageConfigurations"]
        )

    subnetIds = field("subnetIds")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchJobIdentifier:
    boto3_raw_data: "type_defs.BatchJobIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def fileBatchJobIdentifier(self):  # pragma: no cover
        return FileBatchJobIdentifier.make_one(
            self.boto3_raw_data["fileBatchJobIdentifier"]
        )

    @cached_property
    def restartBatchJobIdentifier(self):  # pragma: no cover
        return RestartBatchJobIdentifier.make_one(
            self.boto3_raw_data["restartBatchJobIdentifier"]
        )

    @cached_property
    def s3BatchJobIdentifier(self):  # pragma: no cover
        return S3BatchJobIdentifier.make_one(
            self.boto3_raw_data["s3BatchJobIdentifier"]
        )

    @cached_property
    def scriptBatchJobIdentifier(self):  # pragma: no cover
        return ScriptBatchJobIdentifier.make_one(
            self.boto3_raw_data["scriptBatchJobIdentifier"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchJobIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchJobIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentResponse:
    boto3_raw_data: "type_defs.GetEnvironmentResponseTypeDef" = dataclasses.field()

    actualCapacity = field("actualCapacity")
    creationTime = field("creationTime")
    description = field("description")
    engineType = field("engineType")
    engineVersion = field("engineVersion")
    environmentArn = field("environmentArn")
    environmentId = field("environmentId")

    @cached_property
    def highAvailabilityConfig(self):  # pragma: no cover
        return HighAvailabilityConfig.make_one(
            self.boto3_raw_data["highAvailabilityConfig"]
        )

    instanceType = field("instanceType")
    kmsKeyId = field("kmsKeyId")
    loadBalancerArn = field("loadBalancerArn")
    name = field("name")
    networkType = field("networkType")

    @cached_property
    def pendingMaintenance(self):  # pragma: no cover
        return PendingMaintenance.make_one(self.boto3_raw_data["pendingMaintenance"])

    preferredMaintenanceWindow = field("preferredMaintenanceWindow")
    publiclyAccessible = field("publiclyAccessible")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def storageConfigurations(self):  # pragma: no cover
        return StorageConfiguration.make_many(
            self.boto3_raw_data["storageConfigurations"]
        )

    subnetIds = field("subnetIds")
    tags = field("tags")
    vpcId = field("vpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetOrgAttributes:
    boto3_raw_data: "type_defs.DatasetOrgAttributesTypeDef" = dataclasses.field()

    @cached_property
    def gdg(self):  # pragma: no cover
        return GdgAttributes.make_one(self.boto3_raw_data["gdg"])

    @cached_property
    def po(self):  # pragma: no cover
        return PoAttributes.make_one(self.boto3_raw_data["po"])

    @cached_property
    def ps(self):  # pragma: no cover
        return PsAttributes.make_one(self.boto3_raw_data["ps"])

    @cached_property
    def vsam(self):  # pragma: no cover
        return VsamAttributes.make_one(self.boto3_raw_data["vsam"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetOrgAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetOrgAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetDetailOrgAttributes:
    boto3_raw_data: "type_defs.DatasetDetailOrgAttributesTypeDef" = dataclasses.field()

    @cached_property
    def gdg(self):  # pragma: no cover
        return GdgDetailAttributes.make_one(self.boto3_raw_data["gdg"])

    @cached_property
    def po(self):  # pragma: no cover
        return PoDetailAttributes.make_one(self.boto3_raw_data["po"])

    @cached_property
    def ps(self):  # pragma: no cover
        return PsDetailAttributes.make_one(self.boto3_raw_data["ps"])

    @cached_property
    def vsam(self):  # pragma: no cover
        return VsamDetailAttributes.make_one(self.boto3_raw_data["vsam"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetDetailOrgAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetDetailOrgAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSetExportTaskRequest:
    boto3_raw_data: "type_defs.CreateDataSetExportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def exportConfig(self):  # pragma: no cover
        return DataSetExportConfig.make_one(self.boto3_raw_data["exportConfig"])

    clientToken = field("clientToken")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataSetExportTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSetExportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchJobExecutionSummary:
    boto3_raw_data: "type_defs.BatchJobExecutionSummaryTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    executionId = field("executionId")
    startTime = field("startTime")
    status = field("status")

    @cached_property
    def batchJobIdentifier(self):  # pragma: no cover
        return BatchJobIdentifier.make_one(self.boto3_raw_data["batchJobIdentifier"])

    endTime = field("endTime")
    jobId = field("jobId")
    jobName = field("jobName")
    jobType = field("jobType")
    returnCode = field("returnCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchJobExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchJobExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchJobExecutionResponse:
    boto3_raw_data: "type_defs.GetBatchJobExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def batchJobIdentifier(self):  # pragma: no cover
        return BatchJobIdentifier.make_one(self.boto3_raw_data["batchJobIdentifier"])

    endTime = field("endTime")
    executionId = field("executionId")
    jobId = field("jobId")
    jobName = field("jobName")

    @cached_property
    def jobStepRestartMarker(self):  # pragma: no cover
        return JobStepRestartMarker.make_one(
            self.boto3_raw_data["jobStepRestartMarker"]
        )

    jobType = field("jobType")
    jobUser = field("jobUser")
    returnCode = field("returnCode")
    startTime = field("startTime")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchJobExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchJobExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBatchJobRequest:
    boto3_raw_data: "type_defs.StartBatchJobRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @cached_property
    def batchJobIdentifier(self):  # pragma: no cover
        return BatchJobIdentifier.make_one(self.boto3_raw_data["batchJobIdentifier"])

    authSecretsManagerArn = field("authSecretsManagerArn")
    jobParams = field("jobParams")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBatchJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBatchJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSet:
    boto3_raw_data: "type_defs.DataSetTypeDef" = dataclasses.field()

    datasetName = field("datasetName")

    @cached_property
    def datasetOrg(self):  # pragma: no cover
        return DatasetOrgAttributes.make_one(self.boto3_raw_data["datasetOrg"])

    @cached_property
    def recordLength(self):  # pragma: no cover
        return RecordLength.make_one(self.boto3_raw_data["recordLength"])

    relativePath = field("relativePath")
    storageType = field("storageType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetDetailsResponse:
    boto3_raw_data: "type_defs.GetDataSetDetailsResponseTypeDef" = dataclasses.field()

    blocksize = field("blocksize")
    creationTime = field("creationTime")
    dataSetName = field("dataSetName")

    @cached_property
    def dataSetOrg(self):  # pragma: no cover
        return DatasetDetailOrgAttributes.make_one(self.boto3_raw_data["dataSetOrg"])

    fileSize = field("fileSize")
    lastReferencedTime = field("lastReferencedTime")
    lastUpdatedTime = field("lastUpdatedTime")
    location = field("location")
    recordLength = field("recordLength")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetDetailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchJobExecutionsResponse:
    boto3_raw_data: "type_defs.ListBatchJobExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchJobExecutions(self):  # pragma: no cover
        return BatchJobExecutionSummary.make_many(
            self.boto3_raw_data["batchJobExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchJobExecutionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchJobExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetImportItem:
    boto3_raw_data: "type_defs.DataSetImportItemTypeDef" = dataclasses.field()

    @cached_property
    def dataSet(self):  # pragma: no cover
        return DataSet.make_one(self.boto3_raw_data["dataSet"])

    @cached_property
    def externalLocation(self):  # pragma: no cover
        return ExternalLocation.make_one(self.boto3_raw_data["externalLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetImportItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetImportItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetImportConfig:
    boto3_raw_data: "type_defs.DataSetImportConfigTypeDef" = dataclasses.field()

    @cached_property
    def dataSets(self):  # pragma: no cover
        return DataSetImportItem.make_many(self.boto3_raw_data["dataSets"])

    s3Location = field("s3Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSetImportConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSetImportConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSetImportTaskRequest:
    boto3_raw_data: "type_defs.CreateDataSetImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def importConfig(self):  # pragma: no cover
        return DataSetImportConfig.make_one(self.boto3_raw_data["importConfig"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataSetImportTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSetImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
