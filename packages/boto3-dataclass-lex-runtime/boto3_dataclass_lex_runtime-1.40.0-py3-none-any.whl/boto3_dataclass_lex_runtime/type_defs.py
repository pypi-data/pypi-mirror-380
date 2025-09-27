# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lex_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class DeleteSessionRequest:
    boto3_raw_data: "type_defs.DeleteSessionRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    botAlias = field("botAlias")
    userId = field("userId")

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
class DialogActionOutput:
    boto3_raw_data: "type_defs.DialogActionOutputTypeDef" = dataclasses.field()

    type = field("type")
    intentName = field("intentName")
    slots = field("slots")
    slotToElicit = field("slotToElicit")
    fulfillmentState = field("fulfillmentState")
    message = field("message")
    messageFormat = field("messageFormat")

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
class DialogAction:
    boto3_raw_data: "type_defs.DialogActionTypeDef" = dataclasses.field()

    type = field("type")
    intentName = field("intentName")
    slots = field("slots")
    slotToElicit = field("slotToElicit")
    fulfillmentState = field("fulfillmentState")
    message = field("message")
    messageFormat = field("messageFormat")

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
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    botAlias = field("botAlias")
    userId = field("userId")
    checkpointLabelFilter = field("checkpointLabelFilter")

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
class IntentSummaryOutput:
    boto3_raw_data: "type_defs.IntentSummaryOutputTypeDef" = dataclasses.field()

    dialogActionType = field("dialogActionType")
    intentName = field("intentName")
    checkpointLabel = field("checkpointLabel")
    slots = field("slots")
    confirmationStatus = field("confirmationStatus")
    fulfillmentState = field("fulfillmentState")
    slotToElicit = field("slotToElicit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntentSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentConfidence:
    boto3_raw_data: "type_defs.IntentConfidenceTypeDef" = dataclasses.field()

    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentConfidenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentConfidenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentSummary:
    boto3_raw_data: "type_defs.IntentSummaryTypeDef" = dataclasses.field()

    dialogActionType = field("dialogActionType")
    intentName = field("intentName")
    checkpointLabel = field("checkpointLabel")
    slots = field("slots")
    confirmationStatus = field("confirmationStatus")
    fulfillmentState = field("fulfillmentState")
    slotToElicit = field("slotToElicit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentResponse:
    boto3_raw_data: "type_defs.SentimentResponseTypeDef" = dataclasses.field()

    sentimentLabel = field("sentimentLabel")
    sentimentScore = field("sentimentScore")

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
class ActiveContextOutput:
    boto3_raw_data: "type_defs.ActiveContextOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def timeToLive(self):  # pragma: no cover
        return ActiveContextTimeToLive.make_one(self.boto3_raw_data["timeToLive"])

    parameters = field("parameters")

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

    parameters = field("parameters")

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
class PostContentRequest:
    boto3_raw_data: "type_defs.PostContentRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    botAlias = field("botAlias")
    userId = field("userId")
    contentType = field("contentType")
    inputStream = field("inputStream")
    sessionAttributes = field("sessionAttributes")
    requestAttributes = field("requestAttributes")
    accept = field("accept")
    activeContexts = field("activeContexts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenericAttachment:
    boto3_raw_data: "type_defs.GenericAttachmentTypeDef" = dataclasses.field()

    title = field("title")
    subTitle = field("subTitle")
    attachmentLinkUrl = field("attachmentLinkUrl")
    imageUrl = field("imageUrl")

    @cached_property
    def buttons(self):  # pragma: no cover
        return Button.make_many(self.boto3_raw_data["buttons"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenericAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenericAttachmentTypeDef"]
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

    botName = field("botName")
    botAlias = field("botAlias")
    userId = field("userId")
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
class PostContentResponse:
    boto3_raw_data: "type_defs.PostContentResponseTypeDef" = dataclasses.field()

    contentType = field("contentType")
    intentName = field("intentName")
    nluIntentConfidence = field("nluIntentConfidence")
    alternativeIntents = field("alternativeIntents")
    slots = field("slots")
    sessionAttributes = field("sessionAttributes")
    sentimentResponse = field("sentimentResponse")
    message = field("message")
    encodedMessage = field("encodedMessage")
    messageFormat = field("messageFormat")
    dialogState = field("dialogState")
    slotToElicit = field("slotToElicit")
    inputTranscript = field("inputTranscript")
    encodedInputTranscript = field("encodedInputTranscript")
    audioStream = field("audioStream")
    botVersion = field("botVersion")
    sessionId = field("sessionId")
    activeContexts = field("activeContexts")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostContentResponseTypeDef"]
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
    intentName = field("intentName")
    slots = field("slots")
    sessionAttributes = field("sessionAttributes")
    message = field("message")
    encodedMessage = field("encodedMessage")
    messageFormat = field("messageFormat")
    dialogState = field("dialogState")
    slotToElicit = field("slotToElicit")
    audioStream = field("audioStream")
    sessionId = field("sessionId")
    activeContexts = field("activeContexts")

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
class PredictedIntent:
    boto3_raw_data: "type_defs.PredictedIntentTypeDef" = dataclasses.field()

    intentName = field("intentName")

    @cached_property
    def nluIntentConfidence(self):  # pragma: no cover
        return IntentConfidence.make_one(self.boto3_raw_data["nluIntentConfidence"])

    slots = field("slots")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictedIntentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictedIntentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def recentIntentSummaryView(self):  # pragma: no cover
        return IntentSummaryOutput.make_many(
            self.boto3_raw_data["recentIntentSummaryView"]
        )

    sessionAttributes = field("sessionAttributes")
    sessionId = field("sessionId")

    @cached_property
    def dialogAction(self):  # pragma: no cover
        return DialogActionOutput.make_one(self.boto3_raw_data["dialogAction"])

    @cached_property
    def activeContexts(self):  # pragma: no cover
        return ActiveContextOutput.make_many(self.boto3_raw_data["activeContexts"])

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
class ResponseCard:
    boto3_raw_data: "type_defs.ResponseCardTypeDef" = dataclasses.field()

    version = field("version")
    contentType = field("contentType")

    @cached_property
    def genericAttachments(self):  # pragma: no cover
        return GenericAttachment.make_many(self.boto3_raw_data["genericAttachments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResponseCardTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostTextRequest:
    boto3_raw_data: "type_defs.PostTextRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    botAlias = field("botAlias")
    userId = field("userId")
    inputText = field("inputText")
    sessionAttributes = field("sessionAttributes")
    requestAttributes = field("requestAttributes")
    activeContexts = field("activeContexts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PostTextRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PostTextRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSessionRequest:
    boto3_raw_data: "type_defs.PutSessionRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    botAlias = field("botAlias")
    userId = field("userId")
    sessionAttributes = field("sessionAttributes")
    dialogAction = field("dialogAction")
    recentIntentSummaryView = field("recentIntentSummaryView")
    accept = field("accept")
    activeContexts = field("activeContexts")

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
class PostTextResponse:
    boto3_raw_data: "type_defs.PostTextResponseTypeDef" = dataclasses.field()

    intentName = field("intentName")

    @cached_property
    def nluIntentConfidence(self):  # pragma: no cover
        return IntentConfidence.make_one(self.boto3_raw_data["nluIntentConfidence"])

    @cached_property
    def alternativeIntents(self):  # pragma: no cover
        return PredictedIntent.make_many(self.boto3_raw_data["alternativeIntents"])

    slots = field("slots")
    sessionAttributes = field("sessionAttributes")
    message = field("message")

    @cached_property
    def sentimentResponse(self):  # pragma: no cover
        return SentimentResponse.make_one(self.boto3_raw_data["sentimentResponse"])

    messageFormat = field("messageFormat")
    dialogState = field("dialogState")
    slotToElicit = field("slotToElicit")

    @cached_property
    def responseCard(self):  # pragma: no cover
        return ResponseCard.make_one(self.boto3_raw_data["responseCard"])

    sessionId = field("sessionId")
    botVersion = field("botVersion")

    @cached_property
    def activeContexts(self):  # pragma: no cover
        return ActiveContextOutput.make_many(self.boto3_raw_data["activeContexts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PostTextResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
