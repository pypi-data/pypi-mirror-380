# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lexv2_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessDeniedException:
    boto3_raw_data: "type_defs.AccessDeniedExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessDeniedExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessDeniedExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveContextTimeToLive:
    boto3_raw_data: "type_defs.ActiveContextTimeToLiveTypeDef" = dataclasses.field()

    timeToLiveInSeconds = field("timeToLiveInSeconds")
    turnsToLive = field("turnsToLive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActiveContextTimeToLiveTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveContextTimeToLiveTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioResponseEvent:
    boto3_raw_data: "type_defs.AudioResponseEventTypeDef" = dataclasses.field()

    audioChunk = field("audioChunk")
    contentType = field("contentType")
    eventId = field("eventId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioResponseEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioResponseEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BadGatewayException:
    boto3_raw_data: "type_defs.BadGatewayExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BadGatewayExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BadGatewayExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Button:
    boto3_raw_data: "type_defs.ButtonTypeDef" = dataclasses.field()

    text = field("text")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ButtonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ButtonTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfidenceScore:
    boto3_raw_data: "type_defs.ConfidenceScoreTypeDef" = dataclasses.field()

    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfidenceScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfidenceScoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictException:
    boto3_raw_data: "type_defs.ConflictExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConflictExceptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DTMFInputEvent:
    boto3_raw_data: "type_defs.DTMFInputEventTypeDef" = dataclasses.field()

    inputCharacter = field("inputCharacter")
    eventId = field("eventId")
    clientTimestampMillis = field("clientTimestampMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DTMFInputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DTMFInputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSessionRequest:
    boto3_raw_data: "type_defs.DeleteSessionRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSessionRequestTypeDef"]
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
class DependencyFailedException:
    boto3_raw_data: "type_defs.DependencyFailedExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DependencyFailedExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DependencyFailedExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElicitSubSlotOutput:
    boto3_raw_data: "type_defs.ElicitSubSlotOutputTypeDef" = dataclasses.field()

    name = field("name")
    subSlotToElicit = field("subSlotToElicit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElicitSubSlotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElicitSubSlotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectionEvent:
    boto3_raw_data: "type_defs.DisconnectionEventTypeDef" = dataclasses.field()

    eventId = field("eventId")
    clientTimestampMillis = field("clientTimestampMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisconnectionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElicitSubSlot:
    boto3_raw_data: "type_defs.ElicitSubSlotTypeDef" = dataclasses.field()

    name = field("name")
    subSlotToElicit = field("subSlotToElicit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ElicitSubSlotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ElicitSubSlotTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeartbeatEvent:
    boto3_raw_data: "type_defs.HeartbeatEventTypeDef" = dataclasses.field()

    eventId = field("eventId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeartbeatEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeartbeatEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizedBotMember:
    boto3_raw_data: "type_defs.RecognizedBotMemberTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizedBotMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizedBotMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalServerException:
    boto3_raw_data: "type_defs.InternalServerExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalServerExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalServerExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlaybackCompletionEvent:
    boto3_raw_data: "type_defs.PlaybackCompletionEventTypeDef" = dataclasses.field()

    eventId = field("eventId")
    clientTimestampMillis = field("clientTimestampMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlaybackCompletionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlaybackCompletionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlaybackInterruptionEvent:
    boto3_raw_data: "type_defs.PlaybackInterruptionEventTypeDef" = dataclasses.field()

    eventReason = field("eventReason")
    causedByEventId = field("causedByEventId")
    eventId = field("eventId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlaybackInterruptionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlaybackInterruptionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceNotFoundException:
    boto3_raw_data: "type_defs.ResourceNotFoundExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceNotFoundExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceNotFoundExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHintValue:
    boto3_raw_data: "type_defs.RuntimeHintValueTypeDef" = dataclasses.field()

    phrase = field("phrase")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeHintValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentScore:
    boto3_raw_data: "type_defs.SentimentScoreTypeDef" = dataclasses.field()

    positive = field("positive")
    negative = field("negative")
    neutral = field("neutral")
    mixed = field("mixed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SentimentScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SentimentScoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueOutput:
    boto3_raw_data: "type_defs.ValueOutputTypeDef" = dataclasses.field()

    interpretedValue = field("interpretedValue")
    originalValue = field("originalValue")
    resolvedValues = field("resolvedValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInputEvent:
    boto3_raw_data: "type_defs.TextInputEventTypeDef" = dataclasses.field()

    text = field("text")
    eventId = field("eventId")
    clientTimestampMillis = field("clientTimestampMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextInputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextInputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThrottlingException:
    boto3_raw_data: "type_defs.ThrottlingExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThrottlingExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThrottlingExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptEvent:
    boto3_raw_data: "type_defs.TranscriptEventTypeDef" = dataclasses.field()

    transcript = field("transcript")
    eventId = field("eventId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TranscriptEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationException:
    boto3_raw_data: "type_defs.ValidationExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Value:
    boto3_raw_data: "type_defs.ValueTypeDef" = dataclasses.field()

    interpretedValue = field("interpretedValue")
    originalValue = field("originalValue")
    resolvedValues = field("resolvedValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveContextOutput:
    boto3_raw_data: "type_defs.ActiveContextOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def timeToLive(self):  # pragma: no cover
        return ActiveContextTimeToLive.make_one(self.boto3_raw_data["timeToLive"])

    contextAttributes = field("contextAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActiveContextOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveContext:
    boto3_raw_data: "type_defs.ActiveContextTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def timeToLive(self):  # pragma: no cover
        return ActiveContextTimeToLive.make_one(self.boto3_raw_data["timeToLive"])

    contextAttributes = field("contextAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActiveContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActiveContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioInputEvent:
    boto3_raw_data: "type_defs.AudioInputEventTypeDef" = dataclasses.field()

    contentType = field("contentType")
    audioChunk = field("audioChunk")
    eventId = field("eventId")
    clientTimestampMillis = field("clientTimestampMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioInputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioInputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizeUtteranceRequest:
    boto3_raw_data: "type_defs.RecognizeUtteranceRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")
    requestContentType = field("requestContentType")
    sessionState = field("sessionState")
    requestAttributes = field("requestAttributes")
    responseContentType = field("responseContentType")
    inputStream = field("inputStream")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizeUtteranceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizeUtteranceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageResponseCardOutput:
    boto3_raw_data: "type_defs.ImageResponseCardOutputTypeDef" = dataclasses.field()

    title = field("title")
    subtitle = field("subtitle")
    imageUrl = field("imageUrl")

    @cached_property
    def buttons(self):  # pragma: no cover
        return Button.make_many(self.boto3_raw_data["buttons"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageResponseCardOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageResponseCardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageResponseCard:
    boto3_raw_data: "type_defs.ImageResponseCardTypeDef" = dataclasses.field()

    title = field("title")
    subtitle = field("subtitle")
    imageUrl = field("imageUrl")

    @cached_property
    def buttons(self):  # pragma: no cover
        return Button.make_many(self.boto3_raw_data["buttons"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageResponseCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageResponseCardTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSessionResponse:
    boto3_raw_data: "type_defs.DeleteSessionResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSessionResponse:
    boto3_raw_data: "type_defs.PutSessionResponseTypeDef" = dataclasses.field()

    contentType = field("contentType")
    messages = field("messages")
    sessionState = field("sessionState")
    requestAttributes = field("requestAttributes")
    sessionId = field("sessionId")
    audioStream = field("audioStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizeUtteranceResponse:
    boto3_raw_data: "type_defs.RecognizeUtteranceResponseTypeDef" = dataclasses.field()

    inputMode = field("inputMode")
    contentType = field("contentType")
    messages = field("messages")
    interpretations = field("interpretations")
    sessionState = field("sessionState")
    requestAttributes = field("requestAttributes")
    sessionId = field("sessionId")
    inputTranscript = field("inputTranscript")
    audioStream = field("audioStream")
    recognizedBotMember = field("recognizedBotMember")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizeUtteranceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizeUtteranceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogActionOutput:
    boto3_raw_data: "type_defs.DialogActionOutputTypeDef" = dataclasses.field()

    type = field("type")
    slotToElicit = field("slotToElicit")
    slotElicitationStyle = field("slotElicitationStyle")

    @cached_property
    def subSlotToElicit(self):  # pragma: no cover
        return ElicitSubSlotOutput.make_one(self.boto3_raw_data["subSlotToElicit"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DialogActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DialogActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHintDetailsOutput:
    boto3_raw_data: "type_defs.RuntimeHintDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def runtimeHintValues(self):  # pragma: no cover
        return RuntimeHintValue.make_many(self.boto3_raw_data["runtimeHintValues"])

    subSlotHints = field("subSlotHints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeHintDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHintDetails:
    boto3_raw_data: "type_defs.RuntimeHintDetailsTypeDef" = dataclasses.field()

    @cached_property
    def runtimeHintValues(self):  # pragma: no cover
        return RuntimeHintValue.make_many(self.boto3_raw_data["runtimeHintValues"])

    subSlotHints = field("subSlotHints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeHintDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentResponse:
    boto3_raw_data: "type_defs.SentimentResponseTypeDef" = dataclasses.field()

    sentiment = field("sentiment")

    @cached_property
    def sentimentScore(self):  # pragma: no cover
        return SentimentScore.make_one(self.boto3_raw_data["sentimentScore"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SentimentResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SentimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotOutput:
    boto3_raw_data: "type_defs.SlotOutputTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return ValueOutput.make_one(self.boto3_raw_data["value"])

    shape = field("shape")
    values = field("values")
    subSlots = field("subSlots")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageOutput:
    boto3_raw_data: "type_defs.MessageOutputTypeDef" = dataclasses.field()

    contentType = field("contentType")
    content = field("content")

    @cached_property
    def imageResponseCard(self):  # pragma: no cover
        return ImageResponseCardOutput.make_one(
            self.boto3_raw_data["imageResponseCard"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogAction:
    boto3_raw_data: "type_defs.DialogActionTypeDef" = dataclasses.field()

    type = field("type")
    slotToElicit = field("slotToElicit")
    slotElicitationStyle = field("slotElicitationStyle")
    subSlotToElicit = field("subSlotToElicit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DialogActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DialogActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHintsOutput:
    boto3_raw_data: "type_defs.RuntimeHintsOutputTypeDef" = dataclasses.field()

    slotHints = field("slotHints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeHintsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentOutput:
    boto3_raw_data: "type_defs.IntentOutputTypeDef" = dataclasses.field()

    name = field("name")
    slots = field("slots")
    state = field("state")
    confirmationState = field("confirmationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Slot:
    boto3_raw_data: "type_defs.SlotTypeDef" = dataclasses.field()

    value = field("value")
    shape = field("shape")
    values = field("values")
    subSlots = field("subSlots")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextResponseEvent:
    boto3_raw_data: "type_defs.TextResponseEventTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return MessageOutput.make_many(self.boto3_raw_data["messages"])

    eventId = field("eventId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextResponseEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextResponseEventTypeDef"]
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

    contentType = field("contentType")
    content = field("content")
    imageResponseCard = field("imageResponseCard")

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
class RuntimeHints:
    boto3_raw_data: "type_defs.RuntimeHintsTypeDef" = dataclasses.field()

    slotHints = field("slotHints")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimeHintsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Interpretation:
    boto3_raw_data: "type_defs.InterpretationTypeDef" = dataclasses.field()

    @cached_property
    def nluConfidence(self):  # pragma: no cover
        return ConfidenceScore.make_one(self.boto3_raw_data["nluConfidence"])

    @cached_property
    def sentimentResponse(self):  # pragma: no cover
        return SentimentResponse.make_one(self.boto3_raw_data["sentimentResponse"])

    @cached_property
    def intent(self):  # pragma: no cover
        return IntentOutput.make_one(self.boto3_raw_data["intent"])

    interpretationSource = field("interpretationSource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterpretationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InterpretationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionStateOutput:
    boto3_raw_data: "type_defs.SessionStateOutputTypeDef" = dataclasses.field()

    @cached_property
    def dialogAction(self):  # pragma: no cover
        return DialogActionOutput.make_one(self.boto3_raw_data["dialogAction"])

    @cached_property
    def intent(self):  # pragma: no cover
        return IntentOutput.make_one(self.boto3_raw_data["intent"])

    @cached_property
    def activeContexts(self):  # pragma: no cover
        return ActiveContextOutput.make_many(self.boto3_raw_data["activeContexts"])

    sessionAttributes = field("sessionAttributes")
    originatingRequestId = field("originatingRequestId")

    @cached_property
    def runtimeHints(self):  # pragma: no cover
        return RuntimeHintsOutput.make_one(self.boto3_raw_data["runtimeHints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionStateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionStateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    sessionId = field("sessionId")

    @cached_property
    def messages(self):  # pragma: no cover
        return MessageOutput.make_many(self.boto3_raw_data["messages"])

    @cached_property
    def interpretations(self):  # pragma: no cover
        return Interpretation.make_many(self.boto3_raw_data["interpretations"])

    @cached_property
    def sessionState(self):  # pragma: no cover
        return SessionStateOutput.make_one(self.boto3_raw_data["sessionState"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentResultEvent:
    boto3_raw_data: "type_defs.IntentResultEventTypeDef" = dataclasses.field()

    inputMode = field("inputMode")

    @cached_property
    def interpretations(self):  # pragma: no cover
        return Interpretation.make_many(self.boto3_raw_data["interpretations"])

    @cached_property
    def sessionState(self):  # pragma: no cover
        return SessionStateOutput.make_one(self.boto3_raw_data["sessionState"])

    requestAttributes = field("requestAttributes")
    sessionId = field("sessionId")
    eventId = field("eventId")

    @cached_property
    def recognizedBotMember(self):  # pragma: no cover
        return RecognizedBotMember.make_one(self.boto3_raw_data["recognizedBotMember"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentResultEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentResultEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizeTextResponse:
    boto3_raw_data: "type_defs.RecognizeTextResponseTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return MessageOutput.make_many(self.boto3_raw_data["messages"])

    @cached_property
    def sessionState(self):  # pragma: no cover
        return SessionStateOutput.make_one(self.boto3_raw_data["sessionState"])

    @cached_property
    def interpretations(self):  # pragma: no cover
        return Interpretation.make_many(self.boto3_raw_data["interpretations"])

    requestAttributes = field("requestAttributes")
    sessionId = field("sessionId")

    @cached_property
    def recognizedBotMember(self):  # pragma: no cover
        return RecognizedBotMember.make_one(self.boto3_raw_data["recognizedBotMember"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizeTextResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizeTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Intent:
    boto3_raw_data: "type_defs.IntentTypeDef" = dataclasses.field()

    name = field("name")
    slots = field("slots")
    state = field("state")
    confirmationState = field("confirmationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConversationResponseEventStream:
    boto3_raw_data: "type_defs.StartConversationResponseEventStreamTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PlaybackInterruptionEvent(self):  # pragma: no cover
        return PlaybackInterruptionEvent.make_one(
            self.boto3_raw_data["PlaybackInterruptionEvent"]
        )

    @cached_property
    def TranscriptEvent(self):  # pragma: no cover
        return TranscriptEvent.make_one(self.boto3_raw_data["TranscriptEvent"])

    @cached_property
    def IntentResultEvent(self):  # pragma: no cover
        return IntentResultEvent.make_one(self.boto3_raw_data["IntentResultEvent"])

    @cached_property
    def TextResponseEvent(self):  # pragma: no cover
        return TextResponseEvent.make_one(self.boto3_raw_data["TextResponseEvent"])

    @cached_property
    def AudioResponseEvent(self):  # pragma: no cover
        return AudioResponseEvent.make_one(self.boto3_raw_data["AudioResponseEvent"])

    @cached_property
    def HeartbeatEvent(self):  # pragma: no cover
        return HeartbeatEvent.make_one(self.boto3_raw_data["HeartbeatEvent"])

    @cached_property
    def AccessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["AccessDeniedException"]
        )

    @cached_property
    def ResourceNotFoundException(self):  # pragma: no cover
        return ResourceNotFoundException.make_one(
            self.boto3_raw_data["ResourceNotFoundException"]
        )

    @cached_property
    def ValidationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["ValidationException"])

    @cached_property
    def ThrottlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["ThrottlingException"])

    @cached_property
    def InternalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["InternalServerException"]
        )

    @cached_property
    def ConflictException(self):  # pragma: no cover
        return ConflictException.make_one(self.boto3_raw_data["ConflictException"])

    @cached_property
    def DependencyFailedException(self):  # pragma: no cover
        return DependencyFailedException.make_one(
            self.boto3_raw_data["DependencyFailedException"]
        )

    @cached_property
    def BadGatewayException(self):  # pragma: no cover
        return BadGatewayException.make_one(self.boto3_raw_data["BadGatewayException"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartConversationResponseEventStreamTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConversationResponseEventStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConversationResponse:
    boto3_raw_data: "type_defs.StartConversationResponseTypeDef" = dataclasses.field()

    responseEventStream = field("responseEventStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartConversationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConversationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionState:
    boto3_raw_data: "type_defs.SessionStateTypeDef" = dataclasses.field()

    dialogAction = field("dialogAction")
    intent = field("intent")
    activeContexts = field("activeContexts")
    sessionAttributes = field("sessionAttributes")
    originatingRequestId = field("originatingRequestId")
    runtimeHints = field("runtimeHints")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationEvent:
    boto3_raw_data: "type_defs.ConfigurationEventTypeDef" = dataclasses.field()

    responseContentType = field("responseContentType")
    requestAttributes = field("requestAttributes")
    sessionState = field("sessionState")
    welcomeMessages = field("welcomeMessages")
    disablePlayback = field("disablePlayback")
    eventId = field("eventId")
    clientTimestampMillis = field("clientTimestampMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSessionRequest:
    boto3_raw_data: "type_defs.PutSessionRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")
    sessionState = field("sessionState")
    messages = field("messages")
    requestAttributes = field("requestAttributes")
    responseContentType = field("responseContentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecognizeTextRequest:
    boto3_raw_data: "type_defs.RecognizeTextRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")
    text = field("text")
    sessionState = field("sessionState")
    requestAttributes = field("requestAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecognizeTextRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecognizeTextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConversationRequestEventStream:
    boto3_raw_data: "type_defs.StartConversationRequestEventStreamTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationEvent(self):  # pragma: no cover
        return ConfigurationEvent.make_one(self.boto3_raw_data["ConfigurationEvent"])

    @cached_property
    def AudioInputEvent(self):  # pragma: no cover
        return AudioInputEvent.make_one(self.boto3_raw_data["AudioInputEvent"])

    @cached_property
    def DTMFInputEvent(self):  # pragma: no cover
        return DTMFInputEvent.make_one(self.boto3_raw_data["DTMFInputEvent"])

    @cached_property
    def TextInputEvent(self):  # pragma: no cover
        return TextInputEvent.make_one(self.boto3_raw_data["TextInputEvent"])

    @cached_property
    def PlaybackCompletionEvent(self):  # pragma: no cover
        return PlaybackCompletionEvent.make_one(
            self.boto3_raw_data["PlaybackCompletionEvent"]
        )

    @cached_property
    def DisconnectionEvent(self):  # pragma: no cover
        return DisconnectionEvent.make_one(self.boto3_raw_data["DisconnectionEvent"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartConversationRequestEventStreamTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConversationRequestEventStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConversationRequest:
    boto3_raw_data: "type_defs.StartConversationRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")
    sessionId = field("sessionId")
    requestEventStream = field("requestEventStream")
    conversationMode = field("conversationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartConversationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConversationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
