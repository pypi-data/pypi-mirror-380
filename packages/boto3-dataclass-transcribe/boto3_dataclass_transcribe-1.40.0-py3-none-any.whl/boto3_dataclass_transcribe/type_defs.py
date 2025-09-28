# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_transcribe import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbsoluteTimeRange:
    boto3_raw_data: "type_defs.AbsoluteTimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    First = field("First")
    Last = field("Last")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AbsoluteTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbsoluteTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallAnalyticsSkippedFeature:
    boto3_raw_data: "type_defs.CallAnalyticsSkippedFeatureTypeDef" = dataclasses.field()

    Feature = field("Feature")
    ReasonCode = field("ReasonCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CallAnalyticsSkippedFeatureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallAnalyticsSkippedFeatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentRedactionOutput:
    boto3_raw_data: "type_defs.ContentRedactionOutputTypeDef" = dataclasses.field()

    RedactionType = field("RedactionType")
    RedactionOutput = field("RedactionOutput")
    PiiEntityTypes = field("PiiEntityTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentRedactionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentRedactionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LanguageIdSettings:
    boto3_raw_data: "type_defs.LanguageIdSettingsTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    LanguageModelName = field("LanguageModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LanguageIdSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LanguageIdSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Summarization:
    boto3_raw_data: "type_defs.SummarizationTypeDef" = dataclasses.field()

    GenerateAbstractiveSummary = field("GenerateAbstractiveSummary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SummarizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SummarizationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentRedaction:
    boto3_raw_data: "type_defs.ContentRedactionTypeDef" = dataclasses.field()

    RedactionType = field("RedactionType")
    RedactionOutput = field("RedactionOutput")
    PiiEntityTypes = field("PiiEntityTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentRedactionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentRedactionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelDefinition:
    boto3_raw_data: "type_defs.ChannelDefinitionTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    ParticipantRole = field("ParticipantRole")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Media:
    boto3_raw_data: "type_defs.MediaTypeDef" = dataclasses.field()

    MediaFileUri = field("MediaFileUri")
    RedactedMediaFileUri = field("RedactedMediaFileUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaTypeDef"]]
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
class Transcript:
    boto3_raw_data: "type_defs.TranscriptTypeDef" = dataclasses.field()

    TranscriptFileUri = field("TranscriptFileUri")
    RedactedTranscriptFileUri = field("RedactedTranscriptFileUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TranscriptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClinicalNoteGenerationSettings:
    boto3_raw_data: "type_defs.ClinicalNoteGenerationSettingsTypeDef" = (
        dataclasses.field()
    )

    NoteTemplate = field("NoteTemplate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClinicalNoteGenerationSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClinicalNoteGenerationSettingsTypeDef"]
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
class InputDataConfig:
    boto3_raw_data: "type_defs.InputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    DataAccessRoleArn = field("DataAccessRoleArn")
    TuningDataS3Uri = field("TuningDataS3Uri")

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
class DeleteCallAnalyticsCategoryRequest:
    boto3_raw_data: "type_defs.DeleteCallAnalyticsCategoryRequestTypeDef" = (
        dataclasses.field()
    )

    CategoryName = field("CategoryName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCallAnalyticsCategoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCallAnalyticsCategoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCallAnalyticsJobRequest:
    boto3_raw_data: "type_defs.DeleteCallAnalyticsJobRequestTypeDef" = (
        dataclasses.field()
    )

    CallAnalyticsJobName = field("CallAnalyticsJobName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCallAnalyticsJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCallAnalyticsJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLanguageModelRequest:
    boto3_raw_data: "type_defs.DeleteLanguageModelRequestTypeDef" = dataclasses.field()

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLanguageModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLanguageModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMedicalScribeJobRequest:
    boto3_raw_data: "type_defs.DeleteMedicalScribeJobRequestTypeDef" = (
        dataclasses.field()
    )

    MedicalScribeJobName = field("MedicalScribeJobName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMedicalScribeJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMedicalScribeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMedicalTranscriptionJobRequest:
    boto3_raw_data: "type_defs.DeleteMedicalTranscriptionJobRequestTypeDef" = (
        dataclasses.field()
    )

    MedicalTranscriptionJobName = field("MedicalTranscriptionJobName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMedicalTranscriptionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMedicalTranscriptionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMedicalVocabularyRequest:
    boto3_raw_data: "type_defs.DeleteMedicalVocabularyRequestTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMedicalVocabularyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMedicalVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTranscriptionJobRequest:
    boto3_raw_data: "type_defs.DeleteTranscriptionJobRequestTypeDef" = (
        dataclasses.field()
    )

    TranscriptionJobName = field("TranscriptionJobName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTranscriptionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTranscriptionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVocabularyFilterRequest:
    boto3_raw_data: "type_defs.DeleteVocabularyFilterRequestTypeDef" = (
        dataclasses.field()
    )

    VocabularyFilterName = field("VocabularyFilterName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVocabularyFilterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVocabularyFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVocabularyRequest:
    boto3_raw_data: "type_defs.DeleteVocabularyRequestTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLanguageModelRequest:
    boto3_raw_data: "type_defs.DescribeLanguageModelRequestTypeDef" = (
        dataclasses.field()
    )

    ModelName = field("ModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLanguageModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLanguageModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCallAnalyticsCategoryRequest:
    boto3_raw_data: "type_defs.GetCallAnalyticsCategoryRequestTypeDef" = (
        dataclasses.field()
    )

    CategoryName = field("CategoryName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCallAnalyticsCategoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCallAnalyticsCategoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCallAnalyticsJobRequest:
    boto3_raw_data: "type_defs.GetCallAnalyticsJobRequestTypeDef" = dataclasses.field()

    CallAnalyticsJobName = field("CallAnalyticsJobName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCallAnalyticsJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCallAnalyticsJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMedicalScribeJobRequest:
    boto3_raw_data: "type_defs.GetMedicalScribeJobRequestTypeDef" = dataclasses.field()

    MedicalScribeJobName = field("MedicalScribeJobName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMedicalScribeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMedicalScribeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMedicalTranscriptionJobRequest:
    boto3_raw_data: "type_defs.GetMedicalTranscriptionJobRequestTypeDef" = (
        dataclasses.field()
    )

    MedicalTranscriptionJobName = field("MedicalTranscriptionJobName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMedicalTranscriptionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMedicalTranscriptionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMedicalVocabularyRequest:
    boto3_raw_data: "type_defs.GetMedicalVocabularyRequestTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMedicalVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMedicalVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTranscriptionJobRequest:
    boto3_raw_data: "type_defs.GetTranscriptionJobRequestTypeDef" = dataclasses.field()

    TranscriptionJobName = field("TranscriptionJobName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTranscriptionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTranscriptionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVocabularyFilterRequest:
    boto3_raw_data: "type_defs.GetVocabularyFilterRequestTypeDef" = dataclasses.field()

    VocabularyFilterName = field("VocabularyFilterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVocabularyFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVocabularyFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVocabularyRequest:
    boto3_raw_data: "type_defs.GetVocabularyRequestTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelativeTimeRange:
    boto3_raw_data: "type_defs.RelativeTimeRangeTypeDef" = dataclasses.field()

    StartPercentage = field("StartPercentage")
    EndPercentage = field("EndPercentage")
    First = field("First")
    Last = field("Last")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelativeTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelativeTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionSettings:
    boto3_raw_data: "type_defs.JobExecutionSettingsTypeDef" = dataclasses.field()

    AllowDeferredExecution = field("AllowDeferredExecution")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LanguageCodeItem:
    boto3_raw_data: "type_defs.LanguageCodeItemTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LanguageCodeItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LanguageCodeItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallAnalyticsCategoriesRequest:
    boto3_raw_data: "type_defs.ListCallAnalyticsCategoriesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCallAnalyticsCategoriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallAnalyticsCategoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallAnalyticsJobsRequest:
    boto3_raw_data: "type_defs.ListCallAnalyticsJobsRequestTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    JobNameContains = field("JobNameContains")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCallAnalyticsJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallAnalyticsJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLanguageModelsRequest:
    boto3_raw_data: "type_defs.ListLanguageModelsRequestTypeDef" = dataclasses.field()

    StatusEquals = field("StatusEquals")
    NameContains = field("NameContains")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLanguageModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLanguageModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMedicalScribeJobsRequest:
    boto3_raw_data: "type_defs.ListMedicalScribeJobsRequestTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    JobNameContains = field("JobNameContains")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMedicalScribeJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMedicalScribeJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalScribeJobSummary:
    boto3_raw_data: "type_defs.MedicalScribeJobSummaryTypeDef" = dataclasses.field()

    MedicalScribeJobName = field("MedicalScribeJobName")
    CreationTime = field("CreationTime")
    StartTime = field("StartTime")
    CompletionTime = field("CompletionTime")
    LanguageCode = field("LanguageCode")
    MedicalScribeJobStatus = field("MedicalScribeJobStatus")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalScribeJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribeJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMedicalTranscriptionJobsRequest:
    boto3_raw_data: "type_defs.ListMedicalTranscriptionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    JobNameContains = field("JobNameContains")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMedicalTranscriptionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMedicalTranscriptionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalTranscriptionJobSummary:
    boto3_raw_data: "type_defs.MedicalTranscriptionJobSummaryTypeDef" = (
        dataclasses.field()
    )

    MedicalTranscriptionJobName = field("MedicalTranscriptionJobName")
    CreationTime = field("CreationTime")
    StartTime = field("StartTime")
    CompletionTime = field("CompletionTime")
    LanguageCode = field("LanguageCode")
    TranscriptionJobStatus = field("TranscriptionJobStatus")
    FailureReason = field("FailureReason")
    OutputLocationType = field("OutputLocationType")
    Specialty = field("Specialty")
    ContentIdentificationType = field("ContentIdentificationType")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MedicalTranscriptionJobSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalTranscriptionJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMedicalVocabulariesRequest:
    boto3_raw_data: "type_defs.ListMedicalVocabulariesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StateEquals = field("StateEquals")
    NameContains = field("NameContains")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMedicalVocabulariesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMedicalVocabulariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VocabularyInfo:
    boto3_raw_data: "type_defs.VocabularyInfoTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")
    VocabularyState = field("VocabularyState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VocabularyInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VocabularyInfoTypeDef"]],
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
class ListTranscriptionJobsRequest:
    boto3_raw_data: "type_defs.ListTranscriptionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    JobNameContains = field("JobNameContains")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTranscriptionJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTranscriptionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVocabulariesRequest:
    boto3_raw_data: "type_defs.ListVocabulariesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StateEquals = field("StateEquals")
    NameContains = field("NameContains")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVocabulariesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVocabulariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVocabularyFiltersRequest:
    boto3_raw_data: "type_defs.ListVocabularyFiltersRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    NameContains = field("NameContains")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVocabularyFiltersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVocabularyFiltersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VocabularyFilterInfo:
    boto3_raw_data: "type_defs.VocabularyFilterInfoTypeDef" = dataclasses.field()

    VocabularyFilterName = field("VocabularyFilterName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VocabularyFilterInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VocabularyFilterInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalScribeChannelDefinition:
    boto3_raw_data: "type_defs.MedicalScribeChannelDefinitionTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")
    ParticipantRole = field("ParticipantRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MedicalScribeChannelDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribeChannelDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalScribePatientContext:
    boto3_raw_data: "type_defs.MedicalScribePatientContextTypeDef" = dataclasses.field()

    Pronouns = field("Pronouns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalScribePatientContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribePatientContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalScribeOutput:
    boto3_raw_data: "type_defs.MedicalScribeOutputTypeDef" = dataclasses.field()

    TranscriptFileUri = field("TranscriptFileUri")
    ClinicalDocumentUri = field("ClinicalDocumentUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalScribeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalTranscript:
    boto3_raw_data: "type_defs.MedicalTranscriptTypeDef" = dataclasses.field()

    TranscriptFileUri = field("TranscriptFileUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MedicalTranscriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalTranscriptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalTranscriptionSetting:
    boto3_raw_data: "type_defs.MedicalTranscriptionSettingTypeDef" = dataclasses.field()

    ShowSpeakerLabels = field("ShowSpeakerLabels")
    MaxSpeakerLabels = field("MaxSpeakerLabels")
    ChannelIdentification = field("ChannelIdentification")
    ShowAlternatives = field("ShowAlternatives")
    MaxAlternatives = field("MaxAlternatives")
    VocabularyName = field("VocabularyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalTranscriptionSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalTranscriptionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelSettings:
    boto3_raw_data: "type_defs.ModelSettingsTypeDef" = dataclasses.field()

    LanguageModelName = field("LanguageModelName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Settings:
    boto3_raw_data: "type_defs.SettingsTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    ShowSpeakerLabels = field("ShowSpeakerLabels")
    MaxSpeakerLabels = field("MaxSpeakerLabels")
    ChannelIdentification = field("ChannelIdentification")
    ShowAlternatives = field("ShowAlternatives")
    MaxAlternatives = field("MaxAlternatives")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subtitles:
    boto3_raw_data: "type_defs.SubtitlesTypeDef" = dataclasses.field()

    Formats = field("Formats")
    OutputStartIndex = field("OutputStartIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubtitlesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubtitlesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubtitlesOutput:
    boto3_raw_data: "type_defs.SubtitlesOutputTypeDef" = dataclasses.field()

    Formats = field("Formats")
    SubtitleFileUris = field("SubtitleFileUris")
    OutputStartIndex = field("OutputStartIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubtitlesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubtitlesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToxicityDetectionSettingsOutput:
    boto3_raw_data: "type_defs.ToxicityDetectionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    ToxicityCategories = field("ToxicityCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ToxicityDetectionSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToxicityDetectionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToxicityDetectionSettings:
    boto3_raw_data: "type_defs.ToxicityDetectionSettingsTypeDef" = dataclasses.field()

    ToxicityCategories = field("ToxicityCategories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToxicityDetectionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToxicityDetectionSettingsTypeDef"]
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
class UpdateMedicalVocabularyRequest:
    boto3_raw_data: "type_defs.UpdateMedicalVocabularyRequestTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    VocabularyFileUri = field("VocabularyFileUri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMedicalVocabularyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMedicalVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVocabularyFilterRequest:
    boto3_raw_data: "type_defs.UpdateVocabularyFilterRequestTypeDef" = (
        dataclasses.field()
    )

    VocabularyFilterName = field("VocabularyFilterName")
    Words = field("Words")
    VocabularyFilterFileUri = field("VocabularyFilterFileUri")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateVocabularyFilterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVocabularyFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVocabularyRequest:
    boto3_raw_data: "type_defs.UpdateVocabularyRequestTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    Phrases = field("Phrases")
    VocabularyFileUri = field("VocabularyFileUri")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallAnalyticsJobDetails:
    boto3_raw_data: "type_defs.CallAnalyticsJobDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Skipped(self):  # pragma: no cover
        return CallAnalyticsSkippedFeature.make_many(self.boto3_raw_data["Skipped"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CallAnalyticsJobDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallAnalyticsJobDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallAnalyticsJobSettingsOutput:
    boto3_raw_data: "type_defs.CallAnalyticsJobSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")
    LanguageModelName = field("LanguageModelName")

    @cached_property
    def ContentRedaction(self):  # pragma: no cover
        return ContentRedactionOutput.make_one(self.boto3_raw_data["ContentRedaction"])

    LanguageOptions = field("LanguageOptions")
    LanguageIdSettings = field("LanguageIdSettings")

    @cached_property
    def Summarization(self):  # pragma: no cover
        return Summarization.make_one(self.boto3_raw_data["Summarization"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CallAnalyticsJobSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallAnalyticsJobSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallAnalyticsJobSettings:
    boto3_raw_data: "type_defs.CallAnalyticsJobSettingsTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")
    LanguageModelName = field("LanguageModelName")

    @cached_property
    def ContentRedaction(self):  # pragma: no cover
        return ContentRedaction.make_one(self.boto3_raw_data["ContentRedaction"])

    LanguageOptions = field("LanguageOptions")
    LanguageIdSettings = field("LanguageIdSettings")

    @cached_property
    def Summarization(self):  # pragma: no cover
        return Summarization.make_one(self.boto3_raw_data["Summarization"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CallAnalyticsJobSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallAnalyticsJobSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMedicalVocabularyRequest:
    boto3_raw_data: "type_defs.CreateMedicalVocabularyRequestTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    VocabularyFileUri = field("VocabularyFileUri")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMedicalVocabularyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMedicalVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVocabularyFilterRequest:
    boto3_raw_data: "type_defs.CreateVocabularyFilterRequestTypeDef" = (
        dataclasses.field()
    )

    VocabularyFilterName = field("VocabularyFilterName")
    LanguageCode = field("LanguageCode")
    Words = field("Words")
    VocabularyFilterFileUri = field("VocabularyFilterFileUri")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DataAccessRoleArn = field("DataAccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVocabularyFilterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVocabularyFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVocabularyRequest:
    boto3_raw_data: "type_defs.CreateVocabularyRequestTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    Phrases = field("Phrases")
    VocabularyFileUri = field("VocabularyFileUri")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DataAccessRoleArn = field("DataAccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVocabularyRequestTypeDef"]
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
class MedicalScribeSettings:
    boto3_raw_data: "type_defs.MedicalScribeSettingsTypeDef" = dataclasses.field()

    ShowSpeakerLabels = field("ShowSpeakerLabels")
    MaxSpeakerLabels = field("MaxSpeakerLabels")
    ChannelIdentification = field("ChannelIdentification")
    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")

    @cached_property
    def ClinicalNoteGenerationSettings(self):  # pragma: no cover
        return ClinicalNoteGenerationSettings.make_one(
            self.boto3_raw_data["ClinicalNoteGenerationSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalScribeSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMedicalVocabularyResponse:
    boto3_raw_data: "type_defs.CreateMedicalVocabularyResponseTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    VocabularyState = field("VocabularyState")
    LastModifiedTime = field("LastModifiedTime")
    FailureReason = field("FailureReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMedicalVocabularyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMedicalVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVocabularyFilterResponse:
    boto3_raw_data: "type_defs.CreateVocabularyFilterResponseTypeDef" = (
        dataclasses.field()
    )

    VocabularyFilterName = field("VocabularyFilterName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVocabularyFilterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVocabularyFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVocabularyResponse:
    boto3_raw_data: "type_defs.CreateVocabularyResponseTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    VocabularyState = field("VocabularyState")
    LastModifiedTime = field("LastModifiedTime")
    FailureReason = field("FailureReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVocabularyResponseTypeDef"]
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
class GetMedicalVocabularyResponse:
    boto3_raw_data: "type_defs.GetMedicalVocabularyResponseTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    VocabularyState = field("VocabularyState")
    LastModifiedTime = field("LastModifiedTime")
    FailureReason = field("FailureReason")
    DownloadUri = field("DownloadUri")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMedicalVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMedicalVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVocabularyFilterResponse:
    boto3_raw_data: "type_defs.GetVocabularyFilterResponseTypeDef" = dataclasses.field()

    VocabularyFilterName = field("VocabularyFilterName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")
    DownloadUri = field("DownloadUri")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVocabularyFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVocabularyFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVocabularyResponse:
    boto3_raw_data: "type_defs.GetVocabularyResponseTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    VocabularyState = field("VocabularyState")
    LastModifiedTime = field("LastModifiedTime")
    FailureReason = field("FailureReason")
    DownloadUri = field("DownloadUri")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVocabularyResponseTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class UpdateMedicalVocabularyResponse:
    boto3_raw_data: "type_defs.UpdateMedicalVocabularyResponseTypeDef" = (
        dataclasses.field()
    )

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")
    VocabularyState = field("VocabularyState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMedicalVocabularyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMedicalVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVocabularyFilterResponse:
    boto3_raw_data: "type_defs.UpdateVocabularyFilterResponseTypeDef" = (
        dataclasses.field()
    )

    VocabularyFilterName = field("VocabularyFilterName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateVocabularyFilterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVocabularyFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVocabularyResponse:
    boto3_raw_data: "type_defs.UpdateVocabularyResponseTypeDef" = dataclasses.field()

    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    LastModifiedTime = field("LastModifiedTime")
    VocabularyState = field("VocabularyState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLanguageModelRequest:
    boto3_raw_data: "type_defs.CreateLanguageModelRequestTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    BaseModelName = field("BaseModelName")
    ModelName = field("ModelName")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLanguageModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLanguageModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLanguageModelResponse:
    boto3_raw_data: "type_defs.CreateLanguageModelResponseTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    BaseModelName = field("BaseModelName")
    ModelName = field("ModelName")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    ModelStatus = field("ModelStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLanguageModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLanguageModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LanguageModel:
    boto3_raw_data: "type_defs.LanguageModelTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    CreateTime = field("CreateTime")
    LastModifiedTime = field("LastModifiedTime")
    LanguageCode = field("LanguageCode")
    BaseModelName = field("BaseModelName")
    ModelStatus = field("ModelStatus")
    UpgradeAvailability = field("UpgradeAvailability")
    FailureReason = field("FailureReason")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LanguageModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LanguageModelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterruptionFilter:
    boto3_raw_data: "type_defs.InterruptionFilterTypeDef" = dataclasses.field()

    Threshold = field("Threshold")
    ParticipantRole = field("ParticipantRole")

    @cached_property
    def AbsoluteTimeRange(self):  # pragma: no cover
        return AbsoluteTimeRange.make_one(self.boto3_raw_data["AbsoluteTimeRange"])

    @cached_property
    def RelativeTimeRange(self):  # pragma: no cover
        return RelativeTimeRange.make_one(self.boto3_raw_data["RelativeTimeRange"])

    Negate = field("Negate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InterruptionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterruptionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NonTalkTimeFilter:
    boto3_raw_data: "type_defs.NonTalkTimeFilterTypeDef" = dataclasses.field()

    Threshold = field("Threshold")

    @cached_property
    def AbsoluteTimeRange(self):  # pragma: no cover
        return AbsoluteTimeRange.make_one(self.boto3_raw_data["AbsoluteTimeRange"])

    @cached_property
    def RelativeTimeRange(self):  # pragma: no cover
        return RelativeTimeRange.make_one(self.boto3_raw_data["RelativeTimeRange"])

    Negate = field("Negate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NonTalkTimeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NonTalkTimeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentFilterOutput:
    boto3_raw_data: "type_defs.SentimentFilterOutputTypeDef" = dataclasses.field()

    Sentiments = field("Sentiments")

    @cached_property
    def AbsoluteTimeRange(self):  # pragma: no cover
        return AbsoluteTimeRange.make_one(self.boto3_raw_data["AbsoluteTimeRange"])

    @cached_property
    def RelativeTimeRange(self):  # pragma: no cover
        return RelativeTimeRange.make_one(self.boto3_raw_data["RelativeTimeRange"])

    ParticipantRole = field("ParticipantRole")
    Negate = field("Negate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SentimentFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SentimentFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentFilter:
    boto3_raw_data: "type_defs.SentimentFilterTypeDef" = dataclasses.field()

    Sentiments = field("Sentiments")

    @cached_property
    def AbsoluteTimeRange(self):  # pragma: no cover
        return AbsoluteTimeRange.make_one(self.boto3_raw_data["AbsoluteTimeRange"])

    @cached_property
    def RelativeTimeRange(self):  # pragma: no cover
        return RelativeTimeRange.make_one(self.boto3_raw_data["RelativeTimeRange"])

    ParticipantRole = field("ParticipantRole")
    Negate = field("Negate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SentimentFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SentimentFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptFilterOutput:
    boto3_raw_data: "type_defs.TranscriptFilterOutputTypeDef" = dataclasses.field()

    TranscriptFilterType = field("TranscriptFilterType")
    Targets = field("Targets")

    @cached_property
    def AbsoluteTimeRange(self):  # pragma: no cover
        return AbsoluteTimeRange.make_one(self.boto3_raw_data["AbsoluteTimeRange"])

    @cached_property
    def RelativeTimeRange(self):  # pragma: no cover
        return RelativeTimeRange.make_one(self.boto3_raw_data["RelativeTimeRange"])

    ParticipantRole = field("ParticipantRole")
    Negate = field("Negate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranscriptFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptFilter:
    boto3_raw_data: "type_defs.TranscriptFilterTypeDef" = dataclasses.field()

    TranscriptFilterType = field("TranscriptFilterType")
    Targets = field("Targets")

    @cached_property
    def AbsoluteTimeRange(self):  # pragma: no cover
        return AbsoluteTimeRange.make_one(self.boto3_raw_data["AbsoluteTimeRange"])

    @cached_property
    def RelativeTimeRange(self):  # pragma: no cover
        return RelativeTimeRange.make_one(self.boto3_raw_data["RelativeTimeRange"])

    ParticipantRole = field("ParticipantRole")
    Negate = field("Negate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMedicalScribeJobsResponse:
    boto3_raw_data: "type_defs.ListMedicalScribeJobsResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def MedicalScribeJobSummaries(self):  # pragma: no cover
        return MedicalScribeJobSummary.make_many(
            self.boto3_raw_data["MedicalScribeJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMedicalScribeJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMedicalScribeJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMedicalTranscriptionJobsResponse:
    boto3_raw_data: "type_defs.ListMedicalTranscriptionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def MedicalTranscriptionJobSummaries(self):  # pragma: no cover
        return MedicalTranscriptionJobSummary.make_many(
            self.boto3_raw_data["MedicalTranscriptionJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMedicalTranscriptionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMedicalTranscriptionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMedicalVocabulariesResponse:
    boto3_raw_data: "type_defs.ListMedicalVocabulariesResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def Vocabularies(self):  # pragma: no cover
        return VocabularyInfo.make_many(self.boto3_raw_data["Vocabularies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMedicalVocabulariesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMedicalVocabulariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVocabulariesResponse:
    boto3_raw_data: "type_defs.ListVocabulariesResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Vocabularies(self):  # pragma: no cover
        return VocabularyInfo.make_many(self.boto3_raw_data["Vocabularies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVocabulariesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVocabulariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVocabularyFiltersResponse:
    boto3_raw_data: "type_defs.ListVocabularyFiltersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VocabularyFilters(self):  # pragma: no cover
        return VocabularyFilterInfo.make_many(self.boto3_raw_data["VocabularyFilters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVocabularyFiltersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVocabularyFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalScribeContext:
    boto3_raw_data: "type_defs.MedicalScribeContextTypeDef" = dataclasses.field()

    @cached_property
    def PatientContext(self):  # pragma: no cover
        return MedicalScribePatientContext.make_one(
            self.boto3_raw_data["PatientContext"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalScribeContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribeContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalTranscriptionJob:
    boto3_raw_data: "type_defs.MedicalTranscriptionJobTypeDef" = dataclasses.field()

    MedicalTranscriptionJobName = field("MedicalTranscriptionJobName")
    TranscriptionJobStatus = field("TranscriptionJobStatus")
    LanguageCode = field("LanguageCode")
    MediaSampleRateHertz = field("MediaSampleRateHertz")
    MediaFormat = field("MediaFormat")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    @cached_property
    def Transcript(self):  # pragma: no cover
        return MedicalTranscript.make_one(self.boto3_raw_data["Transcript"])

    StartTime = field("StartTime")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    FailureReason = field("FailureReason")

    @cached_property
    def Settings(self):  # pragma: no cover
        return MedicalTranscriptionSetting.make_one(self.boto3_raw_data["Settings"])

    ContentIdentificationType = field("ContentIdentificationType")
    Specialty = field("Specialty")
    Type = field("Type")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MedicalTranscriptionJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalTranscriptionJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMedicalTranscriptionJobRequest:
    boto3_raw_data: "type_defs.StartMedicalTranscriptionJobRequestTypeDef" = (
        dataclasses.field()
    )

    MedicalTranscriptionJobName = field("MedicalTranscriptionJobName")
    LanguageCode = field("LanguageCode")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    OutputBucketName = field("OutputBucketName")
    Specialty = field("Specialty")
    Type = field("Type")
    MediaSampleRateHertz = field("MediaSampleRateHertz")
    MediaFormat = field("MediaFormat")
    OutputKey = field("OutputKey")
    OutputEncryptionKMSKeyId = field("OutputEncryptionKMSKeyId")
    KMSEncryptionContext = field("KMSEncryptionContext")

    @cached_property
    def Settings(self):  # pragma: no cover
        return MedicalTranscriptionSetting.make_one(self.boto3_raw_data["Settings"])

    ContentIdentificationType = field("ContentIdentificationType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMedicalTranscriptionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMedicalTranscriptionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptionJobSummary:
    boto3_raw_data: "type_defs.TranscriptionJobSummaryTypeDef" = dataclasses.field()

    TranscriptionJobName = field("TranscriptionJobName")
    CreationTime = field("CreationTime")
    StartTime = field("StartTime")
    CompletionTime = field("CompletionTime")
    LanguageCode = field("LanguageCode")
    TranscriptionJobStatus = field("TranscriptionJobStatus")
    FailureReason = field("FailureReason")
    OutputLocationType = field("OutputLocationType")

    @cached_property
    def ContentRedaction(self):  # pragma: no cover
        return ContentRedactionOutput.make_one(self.boto3_raw_data["ContentRedaction"])

    @cached_property
    def ModelSettings(self):  # pragma: no cover
        return ModelSettings.make_one(self.boto3_raw_data["ModelSettings"])

    IdentifyLanguage = field("IdentifyLanguage")
    IdentifyMultipleLanguages = field("IdentifyMultipleLanguages")
    IdentifiedLanguageScore = field("IdentifiedLanguageScore")

    @cached_property
    def LanguageCodes(self):  # pragma: no cover
        return LanguageCodeItem.make_many(self.boto3_raw_data["LanguageCodes"])

    @cached_property
    def ToxicityDetection(self):  # pragma: no cover
        return ToxicityDetectionSettingsOutput.make_many(
            self.boto3_raw_data["ToxicityDetection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranscriptionJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptionJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptionJob:
    boto3_raw_data: "type_defs.TranscriptionJobTypeDef" = dataclasses.field()

    TranscriptionJobName = field("TranscriptionJobName")
    TranscriptionJobStatus = field("TranscriptionJobStatus")
    LanguageCode = field("LanguageCode")
    MediaSampleRateHertz = field("MediaSampleRateHertz")
    MediaFormat = field("MediaFormat")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    @cached_property
    def Transcript(self):  # pragma: no cover
        return Transcript.make_one(self.boto3_raw_data["Transcript"])

    StartTime = field("StartTime")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    FailureReason = field("FailureReason")

    @cached_property
    def Settings(self):  # pragma: no cover
        return Settings.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def ModelSettings(self):  # pragma: no cover
        return ModelSettings.make_one(self.boto3_raw_data["ModelSettings"])

    @cached_property
    def JobExecutionSettings(self):  # pragma: no cover
        return JobExecutionSettings.make_one(
            self.boto3_raw_data["JobExecutionSettings"]
        )

    @cached_property
    def ContentRedaction(self):  # pragma: no cover
        return ContentRedactionOutput.make_one(self.boto3_raw_data["ContentRedaction"])

    IdentifyLanguage = field("IdentifyLanguage")
    IdentifyMultipleLanguages = field("IdentifyMultipleLanguages")
    LanguageOptions = field("LanguageOptions")
    IdentifiedLanguageScore = field("IdentifiedLanguageScore")

    @cached_property
    def LanguageCodes(self):  # pragma: no cover
        return LanguageCodeItem.make_many(self.boto3_raw_data["LanguageCodes"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def Subtitles(self):  # pragma: no cover
        return SubtitlesOutput.make_one(self.boto3_raw_data["Subtitles"])

    LanguageIdSettings = field("LanguageIdSettings")

    @cached_property
    def ToxicityDetection(self):  # pragma: no cover
        return ToxicityDetectionSettingsOutput.make_many(
            self.boto3_raw_data["ToxicityDetection"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptionJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptionJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallAnalyticsJobSummary:
    boto3_raw_data: "type_defs.CallAnalyticsJobSummaryTypeDef" = dataclasses.field()

    CallAnalyticsJobName = field("CallAnalyticsJobName")
    CreationTime = field("CreationTime")
    StartTime = field("StartTime")
    CompletionTime = field("CompletionTime")
    LanguageCode = field("LanguageCode")
    CallAnalyticsJobStatus = field("CallAnalyticsJobStatus")

    @cached_property
    def CallAnalyticsJobDetails(self):  # pragma: no cover
        return CallAnalyticsJobDetails.make_one(
            self.boto3_raw_data["CallAnalyticsJobDetails"]
        )

    FailureReason = field("FailureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CallAnalyticsJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallAnalyticsJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallAnalyticsJob:
    boto3_raw_data: "type_defs.CallAnalyticsJobTypeDef" = dataclasses.field()

    CallAnalyticsJobName = field("CallAnalyticsJobName")
    CallAnalyticsJobStatus = field("CallAnalyticsJobStatus")

    @cached_property
    def CallAnalyticsJobDetails(self):  # pragma: no cover
        return CallAnalyticsJobDetails.make_one(
            self.boto3_raw_data["CallAnalyticsJobDetails"]
        )

    LanguageCode = field("LanguageCode")
    MediaSampleRateHertz = field("MediaSampleRateHertz")
    MediaFormat = field("MediaFormat")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    @cached_property
    def Transcript(self):  # pragma: no cover
        return Transcript.make_one(self.boto3_raw_data["Transcript"])

    StartTime = field("StartTime")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    FailureReason = field("FailureReason")
    DataAccessRoleArn = field("DataAccessRoleArn")
    IdentifiedLanguageScore = field("IdentifiedLanguageScore")

    @cached_property
    def Settings(self):  # pragma: no cover
        return CallAnalyticsJobSettingsOutput.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def ChannelDefinitions(self):  # pragma: no cover
        return ChannelDefinition.make_many(self.boto3_raw_data["ChannelDefinitions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CallAnalyticsJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallAnalyticsJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MedicalScribeJob:
    boto3_raw_data: "type_defs.MedicalScribeJobTypeDef" = dataclasses.field()

    MedicalScribeJobName = field("MedicalScribeJobName")
    MedicalScribeJobStatus = field("MedicalScribeJobStatus")
    LanguageCode = field("LanguageCode")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    @cached_property
    def MedicalScribeOutput(self):  # pragma: no cover
        return MedicalScribeOutput.make_one(self.boto3_raw_data["MedicalScribeOutput"])

    StartTime = field("StartTime")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    FailureReason = field("FailureReason")

    @cached_property
    def Settings(self):  # pragma: no cover
        return MedicalScribeSettings.make_one(self.boto3_raw_data["Settings"])

    DataAccessRoleArn = field("DataAccessRoleArn")

    @cached_property
    def ChannelDefinitions(self):  # pragma: no cover
        return MedicalScribeChannelDefinition.make_many(
            self.boto3_raw_data["ChannelDefinitions"]
        )

    MedicalScribeContextProvided = field("MedicalScribeContextProvided")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MedicalScribeJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MedicalScribeJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLanguageModelResponse:
    boto3_raw_data: "type_defs.DescribeLanguageModelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LanguageModel(self):  # pragma: no cover
        return LanguageModel.make_one(self.boto3_raw_data["LanguageModel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLanguageModelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLanguageModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLanguageModelsResponse:
    boto3_raw_data: "type_defs.ListLanguageModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Models(self):  # pragma: no cover
        return LanguageModel.make_many(self.boto3_raw_data["Models"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLanguageModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLanguageModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOutput:
    boto3_raw_data: "type_defs.RuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def NonTalkTimeFilter(self):  # pragma: no cover
        return NonTalkTimeFilter.make_one(self.boto3_raw_data["NonTalkTimeFilter"])

    @cached_property
    def InterruptionFilter(self):  # pragma: no cover
        return InterruptionFilter.make_one(self.boto3_raw_data["InterruptionFilter"])

    @cached_property
    def TranscriptFilter(self):  # pragma: no cover
        return TranscriptFilterOutput.make_one(self.boto3_raw_data["TranscriptFilter"])

    @cached_property
    def SentimentFilter(self):  # pragma: no cover
        return SentimentFilterOutput.make_one(self.boto3_raw_data["SentimentFilter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMedicalScribeJobRequest:
    boto3_raw_data: "type_defs.StartMedicalScribeJobRequestTypeDef" = (
        dataclasses.field()
    )

    MedicalScribeJobName = field("MedicalScribeJobName")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    OutputBucketName = field("OutputBucketName")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @cached_property
    def Settings(self):  # pragma: no cover
        return MedicalScribeSettings.make_one(self.boto3_raw_data["Settings"])

    OutputEncryptionKMSKeyId = field("OutputEncryptionKMSKeyId")
    KMSEncryptionContext = field("KMSEncryptionContext")

    @cached_property
    def ChannelDefinitions(self):  # pragma: no cover
        return MedicalScribeChannelDefinition.make_many(
            self.boto3_raw_data["ChannelDefinitions"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def MedicalScribeContext(self):  # pragma: no cover
        return MedicalScribeContext.make_one(
            self.boto3_raw_data["MedicalScribeContext"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMedicalScribeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMedicalScribeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMedicalTranscriptionJobResponse:
    boto3_raw_data: "type_defs.GetMedicalTranscriptionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MedicalTranscriptionJob(self):  # pragma: no cover
        return MedicalTranscriptionJob.make_one(
            self.boto3_raw_data["MedicalTranscriptionJob"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMedicalTranscriptionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMedicalTranscriptionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMedicalTranscriptionJobResponse:
    boto3_raw_data: "type_defs.StartMedicalTranscriptionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MedicalTranscriptionJob(self):  # pragma: no cover
        return MedicalTranscriptionJob.make_one(
            self.boto3_raw_data["MedicalTranscriptionJob"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMedicalTranscriptionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMedicalTranscriptionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTranscriptionJobsResponse:
    boto3_raw_data: "type_defs.ListTranscriptionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def TranscriptionJobSummaries(self):  # pragma: no cover
        return TranscriptionJobSummary.make_many(
            self.boto3_raw_data["TranscriptionJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTranscriptionJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTranscriptionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTranscriptionJobResponse:
    boto3_raw_data: "type_defs.GetTranscriptionJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def TranscriptionJob(self):  # pragma: no cover
        return TranscriptionJob.make_one(self.boto3_raw_data["TranscriptionJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTranscriptionJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTranscriptionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTranscriptionJobResponse:
    boto3_raw_data: "type_defs.StartTranscriptionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TranscriptionJob(self):  # pragma: no cover
        return TranscriptionJob.make_one(self.boto3_raw_data["TranscriptionJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTranscriptionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTranscriptionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTranscriptionJobRequest:
    boto3_raw_data: "type_defs.StartTranscriptionJobRequestTypeDef" = (
        dataclasses.field()
    )

    TranscriptionJobName = field("TranscriptionJobName")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    LanguageCode = field("LanguageCode")
    MediaSampleRateHertz = field("MediaSampleRateHertz")
    MediaFormat = field("MediaFormat")
    OutputBucketName = field("OutputBucketName")
    OutputKey = field("OutputKey")
    OutputEncryptionKMSKeyId = field("OutputEncryptionKMSKeyId")
    KMSEncryptionContext = field("KMSEncryptionContext")

    @cached_property
    def Settings(self):  # pragma: no cover
        return Settings.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def ModelSettings(self):  # pragma: no cover
        return ModelSettings.make_one(self.boto3_raw_data["ModelSettings"])

    @cached_property
    def JobExecutionSettings(self):  # pragma: no cover
        return JobExecutionSettings.make_one(
            self.boto3_raw_data["JobExecutionSettings"]
        )

    ContentRedaction = field("ContentRedaction")
    IdentifyLanguage = field("IdentifyLanguage")
    IdentifyMultipleLanguages = field("IdentifyMultipleLanguages")
    LanguageOptions = field("LanguageOptions")

    @cached_property
    def Subtitles(self):  # pragma: no cover
        return Subtitles.make_one(self.boto3_raw_data["Subtitles"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    LanguageIdSettings = field("LanguageIdSettings")
    ToxicityDetection = field("ToxicityDetection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTranscriptionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTranscriptionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallAnalyticsJobsResponse:
    boto3_raw_data: "type_defs.ListCallAnalyticsJobsResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def CallAnalyticsJobSummaries(self):  # pragma: no cover
        return CallAnalyticsJobSummary.make_many(
            self.boto3_raw_data["CallAnalyticsJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCallAnalyticsJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallAnalyticsJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCallAnalyticsJobResponse:
    boto3_raw_data: "type_defs.GetCallAnalyticsJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def CallAnalyticsJob(self):  # pragma: no cover
        return CallAnalyticsJob.make_one(self.boto3_raw_data["CallAnalyticsJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCallAnalyticsJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCallAnalyticsJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCallAnalyticsJobResponse:
    boto3_raw_data: "type_defs.StartCallAnalyticsJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CallAnalyticsJob(self):  # pragma: no cover
        return CallAnalyticsJob.make_one(self.boto3_raw_data["CallAnalyticsJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartCallAnalyticsJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCallAnalyticsJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCallAnalyticsJobRequest:
    boto3_raw_data: "type_defs.StartCallAnalyticsJobRequestTypeDef" = (
        dataclasses.field()
    )

    CallAnalyticsJobName = field("CallAnalyticsJobName")

    @cached_property
    def Media(self):  # pragma: no cover
        return Media.make_one(self.boto3_raw_data["Media"])

    OutputLocation = field("OutputLocation")
    OutputEncryptionKMSKeyId = field("OutputEncryptionKMSKeyId")
    DataAccessRoleArn = field("DataAccessRoleArn")
    Settings = field("Settings")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ChannelDefinitions(self):  # pragma: no cover
        return ChannelDefinition.make_many(self.boto3_raw_data["ChannelDefinitions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCallAnalyticsJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCallAnalyticsJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMedicalScribeJobResponse:
    boto3_raw_data: "type_defs.GetMedicalScribeJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def MedicalScribeJob(self):  # pragma: no cover
        return MedicalScribeJob.make_one(self.boto3_raw_data["MedicalScribeJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMedicalScribeJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMedicalScribeJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMedicalScribeJobResponse:
    boto3_raw_data: "type_defs.StartMedicalScribeJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MedicalScribeJob(self):  # pragma: no cover
        return MedicalScribeJob.make_one(self.boto3_raw_data["MedicalScribeJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMedicalScribeJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMedicalScribeJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoryProperties:
    boto3_raw_data: "type_defs.CategoryPropertiesTypeDef" = dataclasses.field()

    CategoryName = field("CategoryName")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["Rules"])

    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    InputType = field("InputType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CategoryPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CategoryPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    @cached_property
    def NonTalkTimeFilter(self):  # pragma: no cover
        return NonTalkTimeFilter.make_one(self.boto3_raw_data["NonTalkTimeFilter"])

    @cached_property
    def InterruptionFilter(self):  # pragma: no cover
        return InterruptionFilter.make_one(self.boto3_raw_data["InterruptionFilter"])

    TranscriptFilter = field("TranscriptFilter")
    SentimentFilter = field("SentimentFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCallAnalyticsCategoryResponse:
    boto3_raw_data: "type_defs.CreateCallAnalyticsCategoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CategoryProperties(self):  # pragma: no cover
        return CategoryProperties.make_one(self.boto3_raw_data["CategoryProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCallAnalyticsCategoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCallAnalyticsCategoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCallAnalyticsCategoryResponse:
    boto3_raw_data: "type_defs.GetCallAnalyticsCategoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CategoryProperties(self):  # pragma: no cover
        return CategoryProperties.make_one(self.boto3_raw_data["CategoryProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCallAnalyticsCategoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCallAnalyticsCategoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallAnalyticsCategoriesResponse:
    boto3_raw_data: "type_defs.ListCallAnalyticsCategoriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Categories(self):  # pragma: no cover
        return CategoryProperties.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCallAnalyticsCategoriesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallAnalyticsCategoriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCallAnalyticsCategoryResponse:
    boto3_raw_data: "type_defs.UpdateCallAnalyticsCategoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CategoryProperties(self):  # pragma: no cover
        return CategoryProperties.make_one(self.boto3_raw_data["CategoryProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCallAnalyticsCategoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCallAnalyticsCategoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCallAnalyticsCategoryRequest:
    boto3_raw_data: "type_defs.CreateCallAnalyticsCategoryRequestTypeDef" = (
        dataclasses.field()
    )

    CategoryName = field("CategoryName")
    Rules = field("Rules")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    InputType = field("InputType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCallAnalyticsCategoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCallAnalyticsCategoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCallAnalyticsCategoryRequest:
    boto3_raw_data: "type_defs.UpdateCallAnalyticsCategoryRequestTypeDef" = (
        dataclasses.field()
    )

    CategoryName = field("CategoryName")
    Rules = field("Rules")
    InputType = field("InputType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCallAnalyticsCategoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCallAnalyticsCategoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
