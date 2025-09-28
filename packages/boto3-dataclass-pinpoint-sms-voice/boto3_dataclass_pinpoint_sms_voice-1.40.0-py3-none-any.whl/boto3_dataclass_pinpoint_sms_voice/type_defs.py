# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint_sms_voice import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CallInstructionsMessageType:
    boto3_raw_data: "type_defs.CallInstructionsMessageTypeTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CallInstructionsMessageTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CallInstructionsMessageTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsDestination:
    boto3_raw_data: "type_defs.CloudWatchLogsDestinationTypeDef" = dataclasses.field()

    IamRoleArn = field("IamRoleArn")
    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationSetRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationSetEventDestinationRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationSetEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationSetEventDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationSetRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseDestination:
    boto3_raw_data: "type_defs.KinesisFirehoseDestinationTypeDef" = dataclasses.field()

    DeliveryStreamArn = field("DeliveryStreamArn")
    IamRoleArn = field("IamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsDestination:
    boto3_raw_data: "type_defs.SnsDestinationTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnsDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationSetEventDestinationsRequest:
    boto3_raw_data: "type_defs.GetConfigurationSetEventDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfigurationSetEventDestinationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationSetEventDestinationsRequestTypeDef"]
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
class ListConfigurationSetsRequest:
    boto3_raw_data: "type_defs.ListConfigurationSetsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigurationSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlainTextMessageType:
    boto3_raw_data: "type_defs.PlainTextMessageTypeTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    Text = field("Text")
    VoiceId = field("VoiceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlainTextMessageTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlainTextMessageTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSMLMessageType:
    boto3_raw_data: "type_defs.SSMLMessageTypeTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    Text = field("Text")
    VoiceId = field("VoiceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSMLMessageTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSMLMessageTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDestinationDefinition:
    boto3_raw_data: "type_defs.EventDestinationDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchLogsDestination(self):  # pragma: no cover
        return CloudWatchLogsDestination.make_one(
            self.boto3_raw_data["CloudWatchLogsDestination"]
        )

    Enabled = field("Enabled")

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    MatchingEventTypes = field("MatchingEventTypes")

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventDestinationDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDestinationDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDestination:
    boto3_raw_data: "type_defs.EventDestinationTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchLogsDestination(self):  # pragma: no cover
        return CloudWatchLogsDestination.make_one(
            self.boto3_raw_data["CloudWatchLogsDestination"]
        )

    Enabled = field("Enabled")

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    MatchingEventTypes = field("MatchingEventTypes")
    Name = field("Name")

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationSetsResponse:
    boto3_raw_data: "type_defs.ListConfigurationSetsResponseTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSets = field("ConfigurationSets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConfigurationSetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendVoiceMessageResponse:
    boto3_raw_data: "type_defs.SendVoiceMessageResponseTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendVoiceMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendVoiceMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceMessageContent:
    boto3_raw_data: "type_defs.VoiceMessageContentTypeDef" = dataclasses.field()

    @cached_property
    def CallInstructionsMessage(self):  # pragma: no cover
        return CallInstructionsMessageType.make_one(
            self.boto3_raw_data["CallInstructionsMessage"]
        )

    @cached_property
    def PlainTextMessage(self):  # pragma: no cover
        return PlainTextMessageType.make_one(self.boto3_raw_data["PlainTextMessage"])

    @cached_property
    def SSMLMessage(self):  # pragma: no cover
        return SSMLMessageType.make_one(self.boto3_raw_data["SSMLMessage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceMessageContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceMessageContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationSetEventDestinationRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestinationDefinition.make_one(
            self.boto3_raw_data["EventDestination"]
        )

    EventDestinationName = field("EventDestinationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfigurationSetEventDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationSetEventDestinationRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationSetEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestinationDefinition.make_one(
            self.boto3_raw_data["EventDestination"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationSetEventDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationSetEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationSetEventDestinationsResponse:
    boto3_raw_data: "type_defs.GetConfigurationSetEventDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventDestinations(self):  # pragma: no cover
        return EventDestination.make_many(self.boto3_raw_data["EventDestinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfigurationSetEventDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationSetEventDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendVoiceMessageRequest:
    boto3_raw_data: "type_defs.SendVoiceMessageRequestTypeDef" = dataclasses.field()

    CallerId = field("CallerId")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def Content(self):  # pragma: no cover
        return VoiceMessageContent.make_one(self.boto3_raw_data["Content"])

    DestinationPhoneNumber = field("DestinationPhoneNumber")
    OriginationPhoneNumber = field("OriginationPhoneNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendVoiceMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendVoiceMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
