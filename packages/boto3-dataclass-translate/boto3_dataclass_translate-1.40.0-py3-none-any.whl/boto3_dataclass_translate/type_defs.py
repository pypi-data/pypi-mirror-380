# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_translate import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Term:
    boto3_raw_data: "type_defs.TermTypeDef" = dataclasses.field()

    SourceText = field("SourceText")
    TargetText = field("TargetText")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionKey:
    boto3_raw_data: "type_defs.EncryptionKeyTypeDef" = dataclasses.field()

    Type = field("Type")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParallelDataConfig:
    boto3_raw_data: "type_defs.ParallelDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    Format = field("Format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParallelDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParallelDataConfigTypeDef"]
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
class DeleteParallelDataRequest:
    boto3_raw_data: "type_defs.DeleteParallelDataRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParallelDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParallelDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTerminologyRequest:
    boto3_raw_data: "type_defs.DeleteTerminologyRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTerminologyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTerminologyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTextTranslationJobRequest:
    boto3_raw_data: "type_defs.DescribeTextTranslationJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTextTranslationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTextTranslationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParallelDataRequest:
    boto3_raw_data: "type_defs.GetParallelDataRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParallelDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParallelDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParallelDataDataLocation:
    boto3_raw_data: "type_defs.ParallelDataDataLocationTypeDef" = dataclasses.field()

    RepositoryType = field("RepositoryType")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParallelDataDataLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParallelDataDataLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTerminologyRequest:
    boto3_raw_data: "type_defs.GetTerminologyRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    TerminologyDataFormat = field("TerminologyDataFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTerminologyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTerminologyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminologyDataLocation:
    boto3_raw_data: "type_defs.TerminologyDataLocationTypeDef" = dataclasses.field()

    RepositoryType = field("RepositoryType")
    Location = field("Location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminologyDataLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminologyDataLocationTypeDef"]
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
    ContentType = field("ContentType")

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
class JobDetails:
    boto3_raw_data: "type_defs.JobDetailsTypeDef" = dataclasses.field()

    TranslatedDocumentsCount = field("TranslatedDocumentsCount")
    DocumentsWithErrorsCount = field("DocumentsWithErrorsCount")
    InputDocumentsCount = field("InputDocumentsCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Language:
    boto3_raw_data: "type_defs.LanguageTypeDef" = dataclasses.field()

    LanguageName = field("LanguageName")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LanguageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LanguageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLanguagesRequest:
    boto3_raw_data: "type_defs.ListLanguagesRequestTypeDef" = dataclasses.field()

    DisplayLanguageCode = field("DisplayLanguageCode")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLanguagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLanguagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParallelDataRequest:
    boto3_raw_data: "type_defs.ListParallelDataRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListParallelDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParallelDataRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class ListTerminologiesRequest:
    boto3_raw_data: "type_defs.ListTerminologiesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTerminologiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTerminologiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslationSettings:
    boto3_raw_data: "type_defs.TranslationSettingsTypeDef" = dataclasses.field()

    Formality = field("Formality")
    Profanity = field("Profanity")
    Brevity = field("Brevity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTextTranslationJobRequest:
    boto3_raw_data: "type_defs.StopTextTranslationJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopTextTranslationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTextTranslationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslatedDocument:
    boto3_raw_data: "type_defs.TranslatedDocumentTypeDef" = dataclasses.field()

    Content = field("Content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslatedDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslatedDocumentTypeDef"]
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

    ResourceArn = field("ResourceArn")
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
class AppliedTerminology:
    boto3_raw_data: "type_defs.AppliedTerminologyTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Terms(self):  # pragma: no cover
        return Term.make_many(self.boto3_raw_data["Terms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppliedTerminologyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppliedTerminologyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Document:
    boto3_raw_data: "type_defs.DocumentTypeDef" = dataclasses.field()

    Content = field("Content")
    ContentType = field("ContentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminologyData:
    boto3_raw_data: "type_defs.TerminologyDataTypeDef" = dataclasses.field()

    File = field("File")
    Format = field("Format")
    Directionality = field("Directionality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TerminologyDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TerminologyDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDataConfig:
    boto3_raw_data: "type_defs.OutputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")

    @cached_property
    def EncryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["EncryptionKey"])

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
class TerminologyProperties:
    boto3_raw_data: "type_defs.TerminologyPropertiesTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Arn = field("Arn")
    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCodes = field("TargetLanguageCodes")

    @cached_property
    def EncryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["EncryptionKey"])

    SizeBytes = field("SizeBytes")
    TermCount = field("TermCount")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Directionality = field("Directionality")
    Message = field("Message")
    SkippedTermCount = field("SkippedTermCount")
    Format = field("Format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminologyPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminologyPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParallelDataProperties:
    boto3_raw_data: "type_defs.ParallelDataPropertiesTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    Status = field("Status")
    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCodes = field("TargetLanguageCodes")

    @cached_property
    def ParallelDataConfig(self):  # pragma: no cover
        return ParallelDataConfig.make_one(self.boto3_raw_data["ParallelDataConfig"])

    Message = field("Message")
    ImportedDataSize = field("ImportedDataSize")
    ImportedRecordCount = field("ImportedRecordCount")
    FailedRecordCount = field("FailedRecordCount")
    SkippedRecordCount = field("SkippedRecordCount")

    @cached_property
    def EncryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["EncryptionKey"])

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    LatestUpdateAttemptStatus = field("LatestUpdateAttemptStatus")
    LatestUpdateAttemptAt = field("LatestUpdateAttemptAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParallelDataPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParallelDataPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParallelDataRequest:
    boto3_raw_data: "type_defs.UpdateParallelDataRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ParallelDataConfig(self):  # pragma: no cover
        return ParallelDataConfig.make_one(self.boto3_raw_data["ParallelDataConfig"])

    ClientToken = field("ClientToken")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateParallelDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParallelDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParallelDataRequest:
    boto3_raw_data: "type_defs.CreateParallelDataRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ParallelDataConfig(self):  # pragma: no cover
        return ParallelDataConfig.make_one(self.boto3_raw_data["ParallelDataConfig"])

    ClientToken = field("ClientToken")
    Description = field("Description")

    @cached_property
    def EncryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["EncryptionKey"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateParallelDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParallelDataRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class CreateParallelDataResponse:
    boto3_raw_data: "type_defs.CreateParallelDataResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateParallelDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParallelDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteParallelDataResponse:
    boto3_raw_data: "type_defs.DeleteParallelDataResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParallelDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParallelDataResponseTypeDef"]
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
class StartTextTranslationJobResponse:
    boto3_raw_data: "type_defs.StartTextTranslationJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTextTranslationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTextTranslationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTextTranslationJobResponse:
    boto3_raw_data: "type_defs.StopTextTranslationJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopTextTranslationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTextTranslationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParallelDataResponse:
    boto3_raw_data: "type_defs.UpdateParallelDataResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    LatestUpdateAttemptStatus = field("LatestUpdateAttemptStatus")
    LatestUpdateAttemptAt = field("LatestUpdateAttemptAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateParallelDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParallelDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLanguagesResponse:
    boto3_raw_data: "type_defs.ListLanguagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Languages(self):  # pragma: no cover
        return Language.make_many(self.boto3_raw_data["Languages"])

    DisplayLanguageCode = field("DisplayLanguageCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLanguagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLanguagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTerminologiesRequestPaginate:
    boto3_raw_data: "type_defs.ListTerminologiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTerminologiesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTerminologiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslateTextRequest:
    boto3_raw_data: "type_defs.TranslateTextRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCode = field("TargetLanguageCode")
    TerminologyNames = field("TerminologyNames")

    @cached_property
    def Settings(self):  # pragma: no cover
        return TranslationSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslateTextRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslateTextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextTranslationJobFilter:
    boto3_raw_data: "type_defs.TextTranslationJobFilterTypeDef" = dataclasses.field()

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmittedBeforeTime = field("SubmittedBeforeTime")
    SubmittedAfterTime = field("SubmittedAfterTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextTranslationJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextTranslationJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslateDocumentResponse:
    boto3_raw_data: "type_defs.TranslateDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def TranslatedDocument(self):  # pragma: no cover
        return TranslatedDocument.make_one(self.boto3_raw_data["TranslatedDocument"])

    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCode = field("TargetLanguageCode")

    @cached_property
    def AppliedTerminologies(self):  # pragma: no cover
        return AppliedTerminology.make_many(self.boto3_raw_data["AppliedTerminologies"])

    @cached_property
    def AppliedSettings(self):  # pragma: no cover
        return TranslationSettings.make_one(self.boto3_raw_data["AppliedSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslateDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslateDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslateTextResponse:
    boto3_raw_data: "type_defs.TranslateTextResponseTypeDef" = dataclasses.field()

    TranslatedText = field("TranslatedText")
    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCode = field("TargetLanguageCode")

    @cached_property
    def AppliedTerminologies(self):  # pragma: no cover
        return AppliedTerminology.make_many(self.boto3_raw_data["AppliedTerminologies"])

    @cached_property
    def AppliedSettings(self):  # pragma: no cover
        return TranslationSettings.make_one(self.boto3_raw_data["AppliedSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslateTextResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslateTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslateDocumentRequest:
    boto3_raw_data: "type_defs.TranslateDocumentRequestTypeDef" = dataclasses.field()

    @cached_property
    def Document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["Document"])

    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCode = field("TargetLanguageCode")
    TerminologyNames = field("TerminologyNames")

    @cached_property
    def Settings(self):  # pragma: no cover
        return TranslationSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslateDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslateDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTerminologyRequest:
    boto3_raw_data: "type_defs.ImportTerminologyRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    MergeStrategy = field("MergeStrategy")

    @cached_property
    def TerminologyData(self):  # pragma: no cover
        return TerminologyData.make_one(self.boto3_raw_data["TerminologyData"])

    Description = field("Description")

    @cached_property
    def EncryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["EncryptionKey"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTerminologyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTerminologyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTextTranslationJobRequest:
    boto3_raw_data: "type_defs.StartTextTranslationJobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCodes = field("TargetLanguageCodes")
    ClientToken = field("ClientToken")
    JobName = field("JobName")
    TerminologyNames = field("TerminologyNames")
    ParallelDataNames = field("ParallelDataNames")

    @cached_property
    def Settings(self):  # pragma: no cover
        return TranslationSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTextTranslationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTextTranslationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextTranslationJobProperties:
    boto3_raw_data: "type_defs.TextTranslationJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobName = field("JobName")
    JobStatus = field("JobStatus")

    @cached_property
    def JobDetails(self):  # pragma: no cover
        return JobDetails.make_one(self.boto3_raw_data["JobDetails"])

    SourceLanguageCode = field("SourceLanguageCode")
    TargetLanguageCodes = field("TargetLanguageCodes")
    TerminologyNames = field("TerminologyNames")
    ParallelDataNames = field("ParallelDataNames")
    Message = field("Message")
    SubmittedTime = field("SubmittedTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")

    @cached_property
    def Settings(self):  # pragma: no cover
        return TranslationSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextTranslationJobPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextTranslationJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTerminologyResponse:
    boto3_raw_data: "type_defs.GetTerminologyResponseTypeDef" = dataclasses.field()

    @cached_property
    def TerminologyProperties(self):  # pragma: no cover
        return TerminologyProperties.make_one(
            self.boto3_raw_data["TerminologyProperties"]
        )

    @cached_property
    def TerminologyDataLocation(self):  # pragma: no cover
        return TerminologyDataLocation.make_one(
            self.boto3_raw_data["TerminologyDataLocation"]
        )

    @cached_property
    def AuxiliaryDataLocation(self):  # pragma: no cover
        return TerminologyDataLocation.make_one(
            self.boto3_raw_data["AuxiliaryDataLocation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTerminologyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTerminologyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTerminologyResponse:
    boto3_raw_data: "type_defs.ImportTerminologyResponseTypeDef" = dataclasses.field()

    @cached_property
    def TerminologyProperties(self):  # pragma: no cover
        return TerminologyProperties.make_one(
            self.boto3_raw_data["TerminologyProperties"]
        )

    @cached_property
    def AuxiliaryDataLocation(self):  # pragma: no cover
        return TerminologyDataLocation.make_one(
            self.boto3_raw_data["AuxiliaryDataLocation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTerminologyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTerminologyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTerminologiesResponse:
    boto3_raw_data: "type_defs.ListTerminologiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TerminologyPropertiesList(self):  # pragma: no cover
        return TerminologyProperties.make_many(
            self.boto3_raw_data["TerminologyPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTerminologiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTerminologiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParallelDataResponse:
    boto3_raw_data: "type_defs.GetParallelDataResponseTypeDef" = dataclasses.field()

    @cached_property
    def ParallelDataProperties(self):  # pragma: no cover
        return ParallelDataProperties.make_one(
            self.boto3_raw_data["ParallelDataProperties"]
        )

    @cached_property
    def DataLocation(self):  # pragma: no cover
        return ParallelDataDataLocation.make_one(self.boto3_raw_data["DataLocation"])

    @cached_property
    def AuxiliaryDataLocation(self):  # pragma: no cover
        return ParallelDataDataLocation.make_one(
            self.boto3_raw_data["AuxiliaryDataLocation"]
        )

    @cached_property
    def LatestUpdateAttemptAuxiliaryDataLocation(self):  # pragma: no cover
        return ParallelDataDataLocation.make_one(
            self.boto3_raw_data["LatestUpdateAttemptAuxiliaryDataLocation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParallelDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParallelDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListParallelDataResponse:
    boto3_raw_data: "type_defs.ListParallelDataResponseTypeDef" = dataclasses.field()

    @cached_property
    def ParallelDataPropertiesList(self):  # pragma: no cover
        return ParallelDataProperties.make_many(
            self.boto3_raw_data["ParallelDataPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListParallelDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListParallelDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTextTranslationJobsRequest:
    boto3_raw_data: "type_defs.ListTextTranslationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return TextTranslationJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTextTranslationJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTextTranslationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTextTranslationJobResponse:
    boto3_raw_data: "type_defs.DescribeTextTranslationJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TextTranslationJobProperties(self):  # pragma: no cover
        return TextTranslationJobProperties.make_one(
            self.boto3_raw_data["TextTranslationJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTextTranslationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTextTranslationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTextTranslationJobsResponse:
    boto3_raw_data: "type_defs.ListTextTranslationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TextTranslationJobPropertiesList(self):  # pragma: no cover
        return TextTranslationJobProperties.make_many(
            self.boto3_raw_data["TextTranslationJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTextTranslationJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTextTranslationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
