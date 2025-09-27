# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_healthlake import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class IdentityProviderConfiguration:
    boto3_raw_data: "type_defs.IdentityProviderConfigurationTypeDef" = (
        dataclasses.field()
    )

    AuthorizationStrategy = field("AuthorizationStrategy")
    FineGrainedAuthorizationEnabled = field("FineGrainedAuthorizationEnabled")
    Metadata = field("Metadata")
    IdpLambdaArn = field("IdpLambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityProviderConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreloadDataConfig:
    boto3_raw_data: "type_defs.PreloadDataConfigTypeDef" = dataclasses.field()

    PreloadDataType = field("PreloadDataType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PreloadDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreloadDataConfigTypeDef"]
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
class ErrorCause:
    boto3_raw_data: "type_defs.ErrorCauseTypeDef" = dataclasses.field()

    ErrorMessage = field("ErrorMessage")
    ErrorCategory = field("ErrorCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorCauseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorCauseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFHIRDatastoreRequest:
    boto3_raw_data: "type_defs.DeleteFHIRDatastoreRequestTypeDef" = dataclasses.field()

    DatastoreId = field("DatastoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFHIRDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFHIRDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRDatastoreRequest:
    boto3_raw_data: "type_defs.DescribeFHIRDatastoreRequestTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFHIRDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRExportJobRequest:
    boto3_raw_data: "type_defs.DescribeFHIRExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFHIRExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRImportJobRequest:
    boto3_raw_data: "type_defs.DescribeFHIRImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFHIRImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDataConfig:
    boto3_raw_data: "type_defs.InputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputDataConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobProgressReport:
    boto3_raw_data: "type_defs.JobProgressReportTypeDef" = dataclasses.field()

    TotalNumberOfScannedFiles = field("TotalNumberOfScannedFiles")
    TotalSizeOfScannedFilesInMB = field("TotalSizeOfScannedFilesInMB")
    TotalNumberOfImportedFiles = field("TotalNumberOfImportedFiles")
    TotalNumberOfResourcesScanned = field("TotalNumberOfResourcesScanned")
    TotalNumberOfResourcesImported = field("TotalNumberOfResourcesImported")
    TotalNumberOfResourcesWithCustomerError = field(
        "TotalNumberOfResourcesWithCustomerError"
    )
    TotalNumberOfFilesReadWithCustomerError = field(
        "TotalNumberOfFilesReadWithCustomerError"
    )
    Throughput = field("Throughput")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobProgressReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobProgressReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsEncryptionConfig:
    boto3_raw_data: "type_defs.KmsEncryptionConfigTypeDef" = dataclasses.field()

    CmkType = field("CmkType")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsEncryptionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsEncryptionConfigTypeDef"]
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
class S3Configuration:
    boto3_raw_data: "type_defs.S3ConfigurationTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")

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
class CreateFHIRDatastoreResponse:
    boto3_raw_data: "type_defs.CreateFHIRDatastoreResponseTypeDef" = dataclasses.field()

    DatastoreId = field("DatastoreId")
    DatastoreArn = field("DatastoreArn")
    DatastoreStatus = field("DatastoreStatus")
    DatastoreEndpoint = field("DatastoreEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFHIRDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFHIRDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFHIRDatastoreResponse:
    boto3_raw_data: "type_defs.DeleteFHIRDatastoreResponseTypeDef" = dataclasses.field()

    DatastoreId = field("DatastoreId")
    DatastoreArn = field("DatastoreArn")
    DatastoreStatus = field("DatastoreStatus")
    DatastoreEndpoint = field("DatastoreEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFHIRDatastoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFHIRDatastoreResponseTypeDef"]
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
class StartFHIRExportJobResponse:
    boto3_raw_data: "type_defs.StartFHIRExportJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobStatus = field("JobStatus")
    DatastoreId = field("DatastoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFHIRExportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFHIRExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFHIRImportJobResponse:
    boto3_raw_data: "type_defs.StartFHIRImportJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobStatus = field("JobStatus")
    DatastoreId = field("DatastoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFHIRImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFHIRImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreFilter:
    boto3_raw_data: "type_defs.DatastoreFilterTypeDef" = dataclasses.field()

    DatastoreName = field("DatastoreName")
    DatastoreStatus = field("DatastoreStatus")
    CreatedBefore = field("CreatedBefore")
    CreatedAfter = field("CreatedAfter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatastoreFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatastoreFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFHIRExportJobsRequest:
    boto3_raw_data: "type_defs.ListFHIRExportJobsRequestTypeDef" = dataclasses.field()

    DatastoreId = field("DatastoreId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmittedBefore = field("SubmittedBefore")
    SubmittedAfter = field("SubmittedAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFHIRExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFHIRExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFHIRImportJobsRequest:
    boto3_raw_data: "type_defs.ListFHIRImportJobsRequestTypeDef" = dataclasses.field()

    DatastoreId = field("DatastoreId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmittedBefore = field("SubmittedBefore")
    SubmittedAfter = field("SubmittedAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFHIRImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFHIRImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRDatastoreRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeFHIRDatastoreRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFHIRDatastoreRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRDatastoreRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRDatastoreRequestWait:
    boto3_raw_data: "type_defs.DescribeFHIRDatastoreRequestWaitTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFHIRDatastoreRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRDatastoreRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRExportJobRequestWait:
    boto3_raw_data: "type_defs.DescribeFHIRExportJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")
    JobId = field("JobId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFHIRExportJobRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRExportJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRImportJobRequestWait:
    boto3_raw_data: "type_defs.DescribeFHIRImportJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    DatastoreId = field("DatastoreId")
    JobId = field("JobId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFHIRImportJobRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRImportJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SseConfiguration:
    boto3_raw_data: "type_defs.SseConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def KmsEncryptionConfig(self):  # pragma: no cover
        return KmsEncryptionConfig.make_one(self.boto3_raw_data["KmsEncryptionConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SseConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDataConfig:
    boto3_raw_data: "type_defs.OutputDataConfigTypeDef" = dataclasses.field()

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["S3Configuration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFHIRDatastoresRequest:
    boto3_raw_data: "type_defs.ListFHIRDatastoresRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return DatastoreFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFHIRDatastoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFHIRDatastoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFHIRDatastoreRequest:
    boto3_raw_data: "type_defs.CreateFHIRDatastoreRequestTypeDef" = dataclasses.field()

    DatastoreTypeVersion = field("DatastoreTypeVersion")
    DatastoreName = field("DatastoreName")

    @cached_property
    def SseConfiguration(self):  # pragma: no cover
        return SseConfiguration.make_one(self.boto3_raw_data["SseConfiguration"])

    @cached_property
    def PreloadDataConfig(self):  # pragma: no cover
        return PreloadDataConfig.make_one(self.boto3_raw_data["PreloadDataConfig"])

    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def IdentityProviderConfiguration(self):  # pragma: no cover
        return IdentityProviderConfiguration.make_one(
            self.boto3_raw_data["IdentityProviderConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFHIRDatastoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFHIRDatastoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatastoreProperties:
    boto3_raw_data: "type_defs.DatastorePropertiesTypeDef" = dataclasses.field()

    DatastoreId = field("DatastoreId")
    DatastoreArn = field("DatastoreArn")
    DatastoreStatus = field("DatastoreStatus")
    DatastoreTypeVersion = field("DatastoreTypeVersion")
    DatastoreEndpoint = field("DatastoreEndpoint")
    DatastoreName = field("DatastoreName")
    CreatedAt = field("CreatedAt")

    @cached_property
    def SseConfiguration(self):  # pragma: no cover
        return SseConfiguration.make_one(self.boto3_raw_data["SseConfiguration"])

    @cached_property
    def PreloadDataConfig(self):  # pragma: no cover
        return PreloadDataConfig.make_one(self.boto3_raw_data["PreloadDataConfig"])

    @cached_property
    def IdentityProviderConfiguration(self):  # pragma: no cover
        return IdentityProviderConfiguration.make_one(
            self.boto3_raw_data["IdentityProviderConfiguration"]
        )

    @cached_property
    def ErrorCause(self):  # pragma: no cover
        return ErrorCause.make_one(self.boto3_raw_data["ErrorCause"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatastorePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatastorePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportJobProperties:
    boto3_raw_data: "type_defs.ExportJobPropertiesTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobStatus = field("JobStatus")
    SubmitTime = field("SubmitTime")
    DatastoreId = field("DatastoreId")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    JobName = field("JobName")
    EndTime = field("EndTime")
    DataAccessRoleArn = field("DataAccessRoleArn")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportJobPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobProperties:
    boto3_raw_data: "type_defs.ImportJobPropertiesTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobStatus = field("JobStatus")
    SubmitTime = field("SubmitTime")
    DatastoreId = field("DatastoreId")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    JobName = field("JobName")
    EndTime = field("EndTime")

    @cached_property
    def JobOutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["JobOutputDataConfig"])

    @cached_property
    def JobProgressReport(self):  # pragma: no cover
        return JobProgressReport.make_one(self.boto3_raw_data["JobProgressReport"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    Message = field("Message")
    ValidationLevel = field("ValidationLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportJobPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFHIRExportJobRequest:
    boto3_raw_data: "type_defs.StartFHIRExportJobRequestTypeDef" = dataclasses.field()

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DatastoreId = field("DatastoreId")
    DataAccessRoleArn = field("DataAccessRoleArn")
    JobName = field("JobName")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFHIRExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFHIRExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFHIRImportJobRequest:
    boto3_raw_data: "type_defs.StartFHIRImportJobRequestTypeDef" = dataclasses.field()

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def JobOutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["JobOutputDataConfig"])

    DatastoreId = field("DatastoreId")
    DataAccessRoleArn = field("DataAccessRoleArn")
    JobName = field("JobName")
    ClientToken = field("ClientToken")
    ValidationLevel = field("ValidationLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFHIRImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFHIRImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRDatastoreResponse:
    boto3_raw_data: "type_defs.DescribeFHIRDatastoreResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DatastoreProperties(self):  # pragma: no cover
        return DatastoreProperties.make_one(self.boto3_raw_data["DatastoreProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFHIRDatastoreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRDatastoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFHIRDatastoresResponse:
    boto3_raw_data: "type_defs.ListFHIRDatastoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def DatastorePropertiesList(self):  # pragma: no cover
        return DatastoreProperties.make_many(
            self.boto3_raw_data["DatastorePropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFHIRDatastoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFHIRDatastoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRExportJobResponse:
    boto3_raw_data: "type_defs.DescribeFHIRExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExportJobProperties(self):  # pragma: no cover
        return ExportJobProperties.make_one(self.boto3_raw_data["ExportJobProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFHIRExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFHIRExportJobsResponse:
    boto3_raw_data: "type_defs.ListFHIRExportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ExportJobPropertiesList(self):  # pragma: no cover
        return ExportJobProperties.make_many(
            self.boto3_raw_data["ExportJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFHIRExportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFHIRExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFHIRImportJobResponse:
    boto3_raw_data: "type_defs.DescribeFHIRImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ImportJobProperties(self):  # pragma: no cover
        return ImportJobProperties.make_one(self.boto3_raw_data["ImportJobProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFHIRImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFHIRImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFHIRImportJobsResponse:
    boto3_raw_data: "type_defs.ListFHIRImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ImportJobPropertiesList(self):  # pragma: no cover
        return ImportJobProperties.make_many(
            self.boto3_raw_data["ImportJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFHIRImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFHIRImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
