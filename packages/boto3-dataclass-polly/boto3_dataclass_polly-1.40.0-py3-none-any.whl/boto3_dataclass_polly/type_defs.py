# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_polly import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class DeleteLexiconInput:
    boto3_raw_data: "type_defs.DeleteLexiconInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLexiconInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLexiconInputTypeDef"]
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
class DescribeVoicesInput:
    boto3_raw_data: "type_defs.DescribeVoicesInputTypeDef" = dataclasses.field()

    Engine = field("Engine")
    LanguageCode = field("LanguageCode")
    IncludeAdditionalLanguageCodes = field("IncludeAdditionalLanguageCodes")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVoicesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVoicesInputTypeDef"]
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
class Voice:
    boto3_raw_data: "type_defs.VoiceTypeDef" = dataclasses.field()

    Gender = field("Gender")
    Id = field("Id")
    LanguageCode = field("LanguageCode")
    LanguageName = field("LanguageName")
    Name = field("Name")
    AdditionalLanguageCodes = field("AdditionalLanguageCodes")
    SupportedEngines = field("SupportedEngines")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLexiconInput:
    boto3_raw_data: "type_defs.GetLexiconInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLexiconInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLexiconInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexiconAttributes:
    boto3_raw_data: "type_defs.LexiconAttributesTypeDef" = dataclasses.field()

    Alphabet = field("Alphabet")
    LanguageCode = field("LanguageCode")
    LastModified = field("LastModified")
    LexiconArn = field("LexiconArn")
    LexemesCount = field("LexemesCount")
    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LexiconAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LexiconAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Lexicon:
    boto3_raw_data: "type_defs.LexiconTypeDef" = dataclasses.field()

    Content = field("Content")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LexiconTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LexiconTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpeechSynthesisTaskInput:
    boto3_raw_data: "type_defs.GetSpeechSynthesisTaskInputTypeDef" = dataclasses.field()

    TaskId = field("TaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpeechSynthesisTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpeechSynthesisTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SynthesisTask:
    boto3_raw_data: "type_defs.SynthesisTaskTypeDef" = dataclasses.field()

    Engine = field("Engine")
    TaskId = field("TaskId")
    TaskStatus = field("TaskStatus")
    TaskStatusReason = field("TaskStatusReason")
    OutputUri = field("OutputUri")
    CreationTime = field("CreationTime")
    RequestCharacters = field("RequestCharacters")
    SnsTopicArn = field("SnsTopicArn")
    LexiconNames = field("LexiconNames")
    OutputFormat = field("OutputFormat")
    SampleRate = field("SampleRate")
    SpeechMarkTypes = field("SpeechMarkTypes")
    TextType = field("TextType")
    VoiceId = field("VoiceId")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SynthesisTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SynthesisTaskTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLexiconsInput:
    boto3_raw_data: "type_defs.ListLexiconsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLexiconsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLexiconsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeechSynthesisTasksInput:
    boto3_raw_data: "type_defs.ListSpeechSynthesisTasksInputTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSpeechSynthesisTasksInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeechSynthesisTasksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLexiconInput:
    boto3_raw_data: "type_defs.PutLexiconInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Content = field("Content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutLexiconInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutLexiconInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeechSynthesisTaskInput:
    boto3_raw_data: "type_defs.StartSpeechSynthesisTaskInputTypeDef" = (
        dataclasses.field()
    )

    OutputFormat = field("OutputFormat")
    OutputS3BucketName = field("OutputS3BucketName")
    Text = field("Text")
    VoiceId = field("VoiceId")
    Engine = field("Engine")
    LanguageCode = field("LanguageCode")
    LexiconNames = field("LexiconNames")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")
    SampleRate = field("SampleRate")
    SnsTopicArn = field("SnsTopicArn")
    SpeechMarkTypes = field("SpeechMarkTypes")
    TextType = field("TextType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeechSynthesisTaskInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeechSynthesisTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SynthesizeSpeechInput:
    boto3_raw_data: "type_defs.SynthesizeSpeechInputTypeDef" = dataclasses.field()

    OutputFormat = field("OutputFormat")
    Text = field("Text")
    VoiceId = field("VoiceId")
    Engine = field("Engine")
    LanguageCode = field("LanguageCode")
    LexiconNames = field("LexiconNames")
    SampleRate = field("SampleRate")
    SpeechMarkTypes = field("SpeechMarkTypes")
    TextType = field("TextType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SynthesizeSpeechInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SynthesizeSpeechInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVoicesInputPaginate:
    boto3_raw_data: "type_defs.DescribeVoicesInputPaginateTypeDef" = dataclasses.field()

    Engine = field("Engine")
    LanguageCode = field("LanguageCode")
    IncludeAdditionalLanguageCodes = field("IncludeAdditionalLanguageCodes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVoicesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVoicesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLexiconsInputPaginate:
    boto3_raw_data: "type_defs.ListLexiconsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLexiconsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLexiconsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeechSynthesisTasksInputPaginate:
    boto3_raw_data: "type_defs.ListSpeechSynthesisTasksInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSpeechSynthesisTasksInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeechSynthesisTasksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SynthesizeSpeechOutput:
    boto3_raw_data: "type_defs.SynthesizeSpeechOutputTypeDef" = dataclasses.field()

    AudioStream = field("AudioStream")
    ContentType = field("ContentType")
    RequestCharacters = field("RequestCharacters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SynthesizeSpeechOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SynthesizeSpeechOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVoicesOutput:
    boto3_raw_data: "type_defs.DescribeVoicesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Voices(self):  # pragma: no cover
        return Voice.make_many(self.boto3_raw_data["Voices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVoicesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVoicesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexiconDescription:
    boto3_raw_data: "type_defs.LexiconDescriptionTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return LexiconAttributes.make_one(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LexiconDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LexiconDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLexiconOutput:
    boto3_raw_data: "type_defs.GetLexiconOutputTypeDef" = dataclasses.field()

    @cached_property
    def Lexicon(self):  # pragma: no cover
        return Lexicon.make_one(self.boto3_raw_data["Lexicon"])

    @cached_property
    def LexiconAttributes(self):  # pragma: no cover
        return LexiconAttributes.make_one(self.boto3_raw_data["LexiconAttributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLexiconOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLexiconOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpeechSynthesisTaskOutput:
    boto3_raw_data: "type_defs.GetSpeechSynthesisTaskOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SynthesisTask(self):  # pragma: no cover
        return SynthesisTask.make_one(self.boto3_raw_data["SynthesisTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpeechSynthesisTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpeechSynthesisTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeechSynthesisTasksOutput:
    boto3_raw_data: "type_defs.ListSpeechSynthesisTasksOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SynthesisTasks(self):  # pragma: no cover
        return SynthesisTask.make_many(self.boto3_raw_data["SynthesisTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSpeechSynthesisTasksOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeechSynthesisTasksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeechSynthesisTaskOutput:
    boto3_raw_data: "type_defs.StartSpeechSynthesisTaskOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SynthesisTask(self):  # pragma: no cover
        return SynthesisTask.make_one(self.boto3_raw_data["SynthesisTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeechSynthesisTaskOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeechSynthesisTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLexiconsOutput:
    boto3_raw_data: "type_defs.ListLexiconsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Lexicons(self):  # pragma: no cover
        return LexiconDescription.make_many(self.boto3_raw_data["Lexicons"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLexiconsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLexiconsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
