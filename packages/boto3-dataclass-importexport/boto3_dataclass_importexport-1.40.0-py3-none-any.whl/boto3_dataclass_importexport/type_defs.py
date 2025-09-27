# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_importexport import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Artifact:
    boto3_raw_data: "type_defs.ArtifactTypeDef" = dataclasses.field()

    Description = field("Description")
    URL = field("URL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArtifactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobInput:
    boto3_raw_data: "type_defs.CancelJobInputTypeDef" = dataclasses.field()

    JobId = field("JobId")
    APIVersion = field("APIVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CancelJobInputTypeDef"]],
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
class CreateJobInput:
    boto3_raw_data: "type_defs.CreateJobInputTypeDef" = dataclasses.field()

    JobType = field("JobType")
    Manifest = field("Manifest")
    ValidateOnly = field("ValidateOnly")
    ManifestAddendum = field("ManifestAddendum")
    APIVersion = field("APIVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateJobInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShippingLabelInput:
    boto3_raw_data: "type_defs.GetShippingLabelInputTypeDef" = dataclasses.field()

    jobIds = field("jobIds")
    name = field("name")
    company = field("company")
    phoneNumber = field("phoneNumber")
    country = field("country")
    stateOrProvince = field("stateOrProvince")
    city = field("city")
    postalCode = field("postalCode")
    street1 = field("street1")
    street2 = field("street2")
    street3 = field("street3")
    APIVersion = field("APIVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShippingLabelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShippingLabelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatusInput:
    boto3_raw_data: "type_defs.GetStatusInputTypeDef" = dataclasses.field()

    JobId = field("JobId")
    APIVersion = field("APIVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStatusInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStatusInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    JobId = field("JobId")
    CreationDate = field("CreationDate")
    IsCanceled = field("IsCanceled")
    JobType = field("JobType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
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
class ListJobsInput:
    boto3_raw_data: "type_defs.ListJobsInputTypeDef" = dataclasses.field()

    MaxJobs = field("MaxJobs")
    Marker = field("Marker")
    APIVersion = field("APIVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobInput:
    boto3_raw_data: "type_defs.UpdateJobInputTypeDef" = dataclasses.field()

    JobId = field("JobId")
    Manifest = field("Manifest")
    JobType = field("JobType")
    ValidateOnly = field("ValidateOnly")
    APIVersion = field("APIVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateJobInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobOutput:
    boto3_raw_data: "type_defs.CancelJobOutputTypeDef" = dataclasses.field()

    Success = field("Success")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CancelJobOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobOutput:
    boto3_raw_data: "type_defs.CreateJobOutputTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobType = field("JobType")
    Signature = field("Signature")
    SignatureFileContents = field("SignatureFileContents")
    WarningMessage = field("WarningMessage")

    @cached_property
    def ArtifactList(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["ArtifactList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateJobOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShippingLabelOutput:
    boto3_raw_data: "type_defs.GetShippingLabelOutputTypeDef" = dataclasses.field()

    ShippingLabelURL = field("ShippingLabelURL")
    Warning = field("Warning")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShippingLabelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShippingLabelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatusOutput:
    boto3_raw_data: "type_defs.GetStatusOutputTypeDef" = dataclasses.field()

    JobId = field("JobId")
    JobType = field("JobType")
    LocationCode = field("LocationCode")
    LocationMessage = field("LocationMessage")
    ProgressCode = field("ProgressCode")
    ProgressMessage = field("ProgressMessage")
    Carrier = field("Carrier")
    TrackingNumber = field("TrackingNumber")
    LogBucket = field("LogBucket")
    LogKey = field("LogKey")
    ErrorCount = field("ErrorCount")
    Signature = field("Signature")
    SignatureFileContents = field("SignatureFileContents")
    CurrentManifest = field("CurrentManifest")
    CreationDate = field("CreationDate")

    @cached_property
    def ArtifactList(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["ArtifactList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStatusOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStatusOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobOutput:
    boto3_raw_data: "type_defs.UpdateJobOutputTypeDef" = dataclasses.field()

    Success = field("Success")
    WarningMessage = field("WarningMessage")

    @cached_property
    def ArtifactList(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["ArtifactList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateJobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateJobOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsOutput:
    boto3_raw_data: "type_defs.ListJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    IsTruncated = field("IsTruncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsInputPaginate:
    boto3_raw_data: "type_defs.ListJobsInputPaginateTypeDef" = dataclasses.field()

    APIVersion = field("APIVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
