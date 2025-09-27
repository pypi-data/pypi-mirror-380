# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lex_models import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BotChannelAssociation:
    boto3_raw_data: "type_defs.BotChannelAssociationTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    botAlias = field("botAlias")
    botName = field("botName")
    createdDate = field("createdDate")
    type = field("type")
    botConfiguration = field("botConfiguration")
    status = field("status")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotChannelAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotChannelAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotMetadata:
    boto3_raw_data: "type_defs.BotMetadataTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    status = field("status")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotMetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltinIntentMetadata:
    boto3_raw_data: "type_defs.BuiltinIntentMetadataTypeDef" = dataclasses.field()

    signature = field("signature")
    supportedLocales = field("supportedLocales")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuiltinIntentMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltinIntentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltinIntentSlot:
    boto3_raw_data: "type_defs.BuiltinIntentSlotTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuiltinIntentSlotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltinIntentSlotTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltinSlotTypeMetadata:
    boto3_raw_data: "type_defs.BuiltinSlotTypeMetadataTypeDef" = dataclasses.field()

    signature = field("signature")
    supportedLocales = field("supportedLocales")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuiltinSlotTypeMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltinSlotTypeMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeHook:
    boto3_raw_data: "type_defs.CodeHookTypeDef" = dataclasses.field()

    uri = field("uri")
    messageVersion = field("messageVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeHookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeHookTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSettingsRequest:
    boto3_raw_data: "type_defs.LogSettingsRequestTypeDef" = dataclasses.field()

    logType = field("logType")
    destination = field("destination")
    resourceArn = field("resourceArn")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSettingsResponse:
    boto3_raw_data: "type_defs.LogSettingsResponseTypeDef" = dataclasses.field()

    logType = field("logType")
    destination = field("destination")
    kmsKeyArn = field("kmsKeyArn")
    resourceArn = field("resourceArn")
    resourcePrefix = field("resourcePrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotVersionRequest:
    boto3_raw_data: "type_defs.CreateBotVersionRequestTypeDef" = dataclasses.field()

    name = field("name")
    checksum = field("checksum")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotVersionRequestTypeDef"]
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

    intentName = field("intentName")
    intentVersion = field("intentVersion")

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
class CreateIntentVersionRequest:
    boto3_raw_data: "type_defs.CreateIntentVersionRequestTypeDef" = dataclasses.field()

    name = field("name")
    checksum = field("checksum")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputContext:
    boto3_raw_data: "type_defs.InputContextTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KendraConfiguration:
    boto3_raw_data: "type_defs.KendraConfigurationTypeDef" = dataclasses.field()

    kendraIndex = field("kendraIndex")
    role = field("role")
    queryFilterString = field("queryFilterString")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KendraConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KendraConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputContext:
    boto3_raw_data: "type_defs.OutputContextTypeDef" = dataclasses.field()

    name = field("name")
    timeToLiveInSeconds = field("timeToLiveInSeconds")
    turnsToLive = field("turnsToLive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSlotTypeVersionRequest:
    boto3_raw_data: "type_defs.CreateSlotTypeVersionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    checksum = field("checksum")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSlotTypeVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlotTypeVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnumerationValueOutput:
    boto3_raw_data: "type_defs.EnumerationValueOutputTypeDef" = dataclasses.field()

    value = field("value")
    synonyms = field("synonyms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnumerationValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnumerationValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotAliasRequest:
    boto3_raw_data: "type_defs.DeleteBotAliasRequestTypeDef" = dataclasses.field()

    name = field("name")
    botName = field("botName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotChannelAssociationRequest:
    boto3_raw_data: "type_defs.DeleteBotChannelAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    botName = field("botName")
    botAlias = field("botAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBotChannelAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotChannelAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotRequest:
    boto3_raw_data: "type_defs.DeleteBotRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotVersionRequest:
    boto3_raw_data: "type_defs.DeleteBotVersionRequestTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntentRequest:
    boto3_raw_data: "type_defs.DeleteIntentRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntentVersionRequest:
    boto3_raw_data: "type_defs.DeleteIntentVersionRequestTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSlotTypeRequest:
    boto3_raw_data: "type_defs.DeleteSlotTypeRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSlotTypeVersionRequest:
    boto3_raw_data: "type_defs.DeleteSlotTypeVersionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSlotTypeVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSlotTypeVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUtterancesRequest:
    boto3_raw_data: "type_defs.DeleteUtterancesRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    userId = field("userId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUtterancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUtterancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnumerationValue:
    boto3_raw_data: "type_defs.EnumerationValueTypeDef" = dataclasses.field()

    value = field("value")
    synonyms = field("synonyms")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnumerationValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnumerationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotAliasRequest:
    boto3_raw_data: "type_defs.GetBotAliasRequestTypeDef" = dataclasses.field()

    name = field("name")
    botName = field("botName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotAliasRequestTypeDef"]
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
class GetBotAliasesRequest:
    boto3_raw_data: "type_defs.GetBotAliasesRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    nameContains = field("nameContains")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotChannelAssociationRequest:
    boto3_raw_data: "type_defs.GetBotChannelAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    botName = field("botName")
    botAlias = field("botAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBotChannelAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotChannelAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotChannelAssociationsRequest:
    boto3_raw_data: "type_defs.GetBotChannelAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    botName = field("botName")
    botAlias = field("botAlias")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    nameContains = field("nameContains")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBotChannelAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotChannelAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotRequest:
    boto3_raw_data: "type_defs.GetBotRequestTypeDef" = dataclasses.field()

    name = field("name")
    versionOrAlias = field("versionOrAlias")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBotRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotVersionsRequest:
    boto3_raw_data: "type_defs.GetBotVersionsRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotsRequest:
    boto3_raw_data: "type_defs.GetBotsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    nameContains = field("nameContains")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBotsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBotsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinIntentRequest:
    boto3_raw_data: "type_defs.GetBuiltinIntentRequestTypeDef" = dataclasses.field()

    signature = field("signature")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBuiltinIntentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinIntentsRequest:
    boto3_raw_data: "type_defs.GetBuiltinIntentsRequestTypeDef" = dataclasses.field()

    locale = field("locale")
    signatureContains = field("signatureContains")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBuiltinIntentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinIntentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinSlotTypesRequest:
    boto3_raw_data: "type_defs.GetBuiltinSlotTypesRequestTypeDef" = dataclasses.field()

    locale = field("locale")
    signatureContains = field("signatureContains")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBuiltinSlotTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinSlotTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportRequest:
    boto3_raw_data: "type_defs.GetExportRequestTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    resourceType = field("resourceType")
    exportType = field("exportType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetExportRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportRequest:
    boto3_raw_data: "type_defs.GetImportRequestTypeDef" = dataclasses.field()

    importId = field("importId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImportRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentRequest:
    boto3_raw_data: "type_defs.GetIntentRequestTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIntentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentVersionsRequest:
    boto3_raw_data: "type_defs.GetIntentVersionsRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentMetadata:
    boto3_raw_data: "type_defs.IntentMetadataTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentsRequest:
    boto3_raw_data: "type_defs.GetIntentsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    nameContains = field("nameContains")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIntentsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationRequest:
    boto3_raw_data: "type_defs.GetMigrationRequestTypeDef" = dataclasses.field()

    migrationId = field("migrationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMigrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MigrationAlert:
    boto3_raw_data: "type_defs.MigrationAlertTypeDef" = dataclasses.field()

    type = field("type")
    message = field("message")
    details = field("details")
    referenceURLs = field("referenceURLs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MigrationAlertTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MigrationAlertTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationsRequest:
    boto3_raw_data: "type_defs.GetMigrationsRequestTypeDef" = dataclasses.field()

    sortByAttribute = field("sortByAttribute")
    sortByOrder = field("sortByOrder")
    v1BotNameContains = field("v1BotNameContains")
    migrationStatusEquals = field("migrationStatusEquals")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMigrationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MigrationSummary:
    boto3_raw_data: "type_defs.MigrationSummaryTypeDef" = dataclasses.field()

    migrationId = field("migrationId")
    v1BotName = field("v1BotName")
    v1BotVersion = field("v1BotVersion")
    v1BotLocale = field("v1BotLocale")
    v2BotId = field("v2BotId")
    v2BotRole = field("v2BotRole")
    migrationStatus = field("migrationStatus")
    migrationStrategy = field("migrationStrategy")
    migrationTimestamp = field("migrationTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MigrationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MigrationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypeRequest:
    boto3_raw_data: "type_defs.GetSlotTypeRequestTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypeVersionsRequest:
    boto3_raw_data: "type_defs.GetSlotTypeVersionsRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypeVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypeVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeMetadata:
    boto3_raw_data: "type_defs.SlotTypeMetadataTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotTypeMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotTypeMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypesRequest:
    boto3_raw_data: "type_defs.GetSlotTypesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    nameContains = field("nameContains")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUtterancesViewRequest:
    boto3_raw_data: "type_defs.GetUtterancesViewRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    botVersions = field("botVersions")
    statusType = field("statusType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUtterancesViewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUtterancesViewRequestTypeDef"]
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
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

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
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    contentType = field("contentType")
    content = field("content")
    groupNumber = field("groupNumber")

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
class SlotDefaultValue:
    boto3_raw_data: "type_defs.SlotDefaultValueTypeDef" = dataclasses.field()

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotDefaultValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotDefaultValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeRegexConfiguration:
    boto3_raw_data: "type_defs.SlotTypeRegexConfigurationTypeDef" = dataclasses.field()

    pattern = field("pattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotTypeRegexConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotTypeRegexConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMigrationRequest:
    boto3_raw_data: "type_defs.StartMigrationRequestTypeDef" = dataclasses.field()

    v1BotName = field("v1BotName")
    v1BotVersion = field("v1BotVersion")
    v2BotName = field("v2BotName")
    v2BotRole = field("v2BotRole")
    migrationStrategy = field("migrationStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMigrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMigrationRequestTypeDef"]
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
class UtteranceData:
    boto3_raw_data: "type_defs.UtteranceDataTypeDef" = dataclasses.field()

    utteranceString = field("utteranceString")
    count = field("count")
    distinctUsers = field("distinctUsers")
    firstUtteredDate = field("firstUtteredDate")
    lastUtteredDate = field("lastUtteredDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UtteranceDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UtteranceDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentActivity:
    boto3_raw_data: "type_defs.FulfillmentActivityTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def codeHook(self):  # pragma: no cover
        return CodeHook.make_one(self.boto3_raw_data["codeHook"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FulfillmentActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogsRequest:
    boto3_raw_data: "type_defs.ConversationLogsRequestTypeDef" = dataclasses.field()

    @cached_property
    def logSettings(self):  # pragma: no cover
        return LogSettingsRequest.make_many(self.boto3_raw_data["logSettings"])

    iamRoleArn = field("iamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationLogsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogsResponse:
    boto3_raw_data: "type_defs.ConversationLogsResponseTypeDef" = dataclasses.field()

    @cached_property
    def logSettings(self):  # pragma: no cover
        return LogSettingsResponse.make_many(self.boto3_raw_data["logSettings"])

    iamRoleArn = field("iamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationLogsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogsResponseTypeDef"]
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
class GetBotChannelAssociationResponse:
    boto3_raw_data: "type_defs.GetBotChannelAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    botAlias = field("botAlias")
    botName = field("botName")
    createdDate = field("createdDate")
    type = field("type")
    botConfiguration = field("botConfiguration")
    status = field("status")
    failureReason = field("failureReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBotChannelAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotChannelAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotChannelAssociationsResponse:
    boto3_raw_data: "type_defs.GetBotChannelAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def botChannelAssociations(self):  # pragma: no cover
        return BotChannelAssociation.make_many(
            self.boto3_raw_data["botChannelAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBotChannelAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotChannelAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotVersionsResponse:
    boto3_raw_data: "type_defs.GetBotVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def bots(self):  # pragma: no cover
        return BotMetadata.make_many(self.boto3_raw_data["bots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotsResponse:
    boto3_raw_data: "type_defs.GetBotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def bots(self):  # pragma: no cover
        return BotMetadata.make_many(self.boto3_raw_data["bots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBotsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBotsResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinIntentResponse:
    boto3_raw_data: "type_defs.GetBuiltinIntentResponseTypeDef" = dataclasses.field()

    signature = field("signature")
    supportedLocales = field("supportedLocales")

    @cached_property
    def slots(self):  # pragma: no cover
        return BuiltinIntentSlot.make_many(self.boto3_raw_data["slots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBuiltinIntentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinIntentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinIntentsResponse:
    boto3_raw_data: "type_defs.GetBuiltinIntentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def intents(self):  # pragma: no cover
        return BuiltinIntentMetadata.make_many(self.boto3_raw_data["intents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBuiltinIntentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinIntentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinSlotTypesResponse:
    boto3_raw_data: "type_defs.GetBuiltinSlotTypesResponseTypeDef" = dataclasses.field()

    @cached_property
    def slotTypes(self):  # pragma: no cover
        return BuiltinSlotTypeMetadata.make_many(self.boto3_raw_data["slotTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBuiltinSlotTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinSlotTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportResponse:
    boto3_raw_data: "type_defs.GetExportResponseTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    resourceType = field("resourceType")
    exportType = field("exportType")
    exportStatus = field("exportStatus")
    failureReason = field("failureReason")
    url = field("url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetExportResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportResponse:
    boto3_raw_data: "type_defs.GetImportResponseTypeDef" = dataclasses.field()

    name = field("name")
    resourceType = field("resourceType")
    mergeStrategy = field("mergeStrategy")
    importId = field("importId")
    importStatus = field("importStatus")
    failureReason = field("failureReason")
    createdDate = field("createdDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImportResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMigrationResponse:
    boto3_raw_data: "type_defs.StartMigrationResponseTypeDef" = dataclasses.field()

    v1BotName = field("v1BotName")
    v1BotVersion = field("v1BotVersion")
    v1BotLocale = field("v1BotLocale")
    v2BotId = field("v2BotId")
    v2BotRole = field("v2BotRole")
    migrationId = field("migrationId")
    migrationStrategy = field("migrationStrategy")
    migrationTimestamp = field("migrationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotAliasesRequestPaginate:
    boto3_raw_data: "type_defs.GetBotAliasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    botName = field("botName")
    nameContains = field("nameContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotAliasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotChannelAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.GetBotChannelAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    botName = field("botName")
    botAlias = field("botAlias")
    nameContains = field("nameContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBotChannelAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotChannelAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotVersionsRequestPaginate:
    boto3_raw_data: "type_defs.GetBotVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBotVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotsRequestPaginate:
    boto3_raw_data: "type_defs.GetBotsRequestPaginateTypeDef" = dataclasses.field()

    nameContains = field("nameContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinIntentsRequestPaginate:
    boto3_raw_data: "type_defs.GetBuiltinIntentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    locale = field("locale")
    signatureContains = field("signatureContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBuiltinIntentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinIntentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBuiltinSlotTypesRequestPaginate:
    boto3_raw_data: "type_defs.GetBuiltinSlotTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    locale = field("locale")
    signatureContains = field("signatureContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBuiltinSlotTypesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBuiltinSlotTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentVersionsRequestPaginate:
    boto3_raw_data: "type_defs.GetIntentVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntentVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentsRequestPaginate:
    boto3_raw_data: "type_defs.GetIntentsRequestPaginateTypeDef" = dataclasses.field()

    nameContains = field("nameContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypeVersionsRequestPaginate:
    boto3_raw_data: "type_defs.GetSlotTypeVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSlotTypeVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypeVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypesRequestPaginate:
    boto3_raw_data: "type_defs.GetSlotTypesRequestPaginateTypeDef" = dataclasses.field()

    nameContains = field("nameContains")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentVersionsResponse:
    boto3_raw_data: "type_defs.GetIntentVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def intents(self):  # pragma: no cover
        return IntentMetadata.make_many(self.boto3_raw_data["intents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntentVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentsResponse:
    boto3_raw_data: "type_defs.GetIntentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def intents(self):  # pragma: no cover
        return IntentMetadata.make_many(self.boto3_raw_data["intents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationResponse:
    boto3_raw_data: "type_defs.GetMigrationResponseTypeDef" = dataclasses.field()

    migrationId = field("migrationId")
    v1BotName = field("v1BotName")
    v1BotVersion = field("v1BotVersion")
    v1BotLocale = field("v1BotLocale")
    v2BotId = field("v2BotId")
    v2BotRole = field("v2BotRole")
    migrationStatus = field("migrationStatus")
    migrationStrategy = field("migrationStrategy")
    migrationTimestamp = field("migrationTimestamp")

    @cached_property
    def alerts(self):  # pragma: no cover
        return MigrationAlert.make_many(self.boto3_raw_data["alerts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationsResponse:
    boto3_raw_data: "type_defs.GetMigrationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def migrationSummaries(self):  # pragma: no cover
        return MigrationSummary.make_many(self.boto3_raw_data["migrationSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMigrationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypeVersionsResponse:
    boto3_raw_data: "type_defs.GetSlotTypeVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def slotTypes(self):  # pragma: no cover
        return SlotTypeMetadata.make_many(self.boto3_raw_data["slotTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypeVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypeVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypesResponse:
    boto3_raw_data: "type_defs.GetSlotTypesResponseTypeDef" = dataclasses.field()

    @cached_property
    def slotTypes(self):  # pragma: no cover
        return SlotTypeMetadata.make_many(self.boto3_raw_data["slotTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypesResponseTypeDef"]
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
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class StartImportRequest:
    boto3_raw_data: "type_defs.StartImportRequestTypeDef" = dataclasses.field()

    payload = field("payload")
    resourceType = field("resourceType")
    mergeStrategy = field("mergeStrategy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportResponse:
    boto3_raw_data: "type_defs.StartImportResponseTypeDef" = dataclasses.field()

    name = field("name")
    resourceType = field("resourceType")
    mergeStrategy = field("mergeStrategy")
    importId = field("importId")
    importStatus = field("importStatus")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    createdDate = field("createdDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportResponseTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class PromptOutput:
    boto3_raw_data: "type_defs.PromptOutputTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    maxAttempts = field("maxAttempts")
    responseCard = field("responseCard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Prompt:
    boto3_raw_data: "type_defs.PromptTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    maxAttempts = field("maxAttempts")
    responseCard = field("responseCard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatementOutput:
    boto3_raw_data: "type_defs.StatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    responseCard = field("responseCard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatementOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatementOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statement:
    boto3_raw_data: "type_defs.StatementTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    responseCard = field("responseCard")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotDefaultValueSpecOutput:
    boto3_raw_data: "type_defs.SlotDefaultValueSpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def defaultValueList(self):  # pragma: no cover
        return SlotDefaultValue.make_many(self.boto3_raw_data["defaultValueList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotDefaultValueSpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotDefaultValueSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotDefaultValueSpec:
    boto3_raw_data: "type_defs.SlotDefaultValueSpecTypeDef" = dataclasses.field()

    @cached_property
    def defaultValueList(self):  # pragma: no cover
        return SlotDefaultValue.make_many(self.boto3_raw_data["defaultValueList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotDefaultValueSpecTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotDefaultValueSpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeConfiguration:
    boto3_raw_data: "type_defs.SlotTypeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def regexConfiguration(self):  # pragma: no cover
        return SlotTypeRegexConfiguration.make_one(
            self.boto3_raw_data["regexConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotTypeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotTypeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceList:
    boto3_raw_data: "type_defs.UtteranceListTypeDef" = dataclasses.field()

    botVersion = field("botVersion")

    @cached_property
    def utterances(self):  # pragma: no cover
        return UtteranceData.make_many(self.boto3_raw_data["utterances"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UtteranceListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UtteranceListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBotAliasRequest:
    boto3_raw_data: "type_defs.PutBotAliasRequestTypeDef" = dataclasses.field()

    name = field("name")
    botVersion = field("botVersion")
    botName = field("botName")
    description = field("description")
    checksum = field("checksum")

    @cached_property
    def conversationLogs(self):  # pragma: no cover
        return ConversationLogsRequest.make_one(self.boto3_raw_data["conversationLogs"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBotAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotAliasMetadata:
    boto3_raw_data: "type_defs.BotAliasMetadataTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    botVersion = field("botVersion")
    botName = field("botName")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    checksum = field("checksum")

    @cached_property
    def conversationLogs(self):  # pragma: no cover
        return ConversationLogsResponse.make_one(
            self.boto3_raw_data["conversationLogs"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotAliasMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotAliasMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotAliasResponse:
    boto3_raw_data: "type_defs.GetBotAliasResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    botVersion = field("botVersion")
    botName = field("botName")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    checksum = field("checksum")

    @cached_property
    def conversationLogs(self):  # pragma: no cover
        return ConversationLogsResponse.make_one(
            self.boto3_raw_data["conversationLogs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBotAliasResponse:
    boto3_raw_data: "type_defs.PutBotAliasResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    botVersion = field("botVersion")
    botName = field("botName")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    checksum = field("checksum")

    @cached_property
    def conversationLogs(self):  # pragma: no cover
        return ConversationLogsResponse.make_one(
            self.boto3_raw_data["conversationLogs"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBotAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBotAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotVersionResponse:
    boto3_raw_data: "type_defs.CreateBotVersionResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def intents(self):  # pragma: no cover
        return Intent.make_many(self.boto3_raw_data["intents"])

    @cached_property
    def clarificationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["clarificationPrompt"])

    @cached_property
    def abortStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["abortStatement"])

    status = field("status")
    failureReason = field("failureReason")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    voiceId = field("voiceId")
    checksum = field("checksum")
    version = field("version")
    locale = field("locale")
    childDirected = field("childDirected")
    enableModelImprovements = field("enableModelImprovements")
    detectSentiment = field("detectSentiment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FollowUpPromptOutput:
    boto3_raw_data: "type_defs.FollowUpPromptOutputTypeDef" = dataclasses.field()

    @cached_property
    def prompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["prompt"])

    @cached_property
    def rejectionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["rejectionStatement"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FollowUpPromptOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FollowUpPromptOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotResponse:
    boto3_raw_data: "type_defs.GetBotResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def intents(self):  # pragma: no cover
        return Intent.make_many(self.boto3_raw_data["intents"])

    enableModelImprovements = field("enableModelImprovements")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")

    @cached_property
    def clarificationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["clarificationPrompt"])

    @cached_property
    def abortStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["abortStatement"])

    status = field("status")
    failureReason = field("failureReason")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    voiceId = field("voiceId")
    checksum = field("checksum")
    version = field("version")
    locale = field("locale")
    childDirected = field("childDirected")
    detectSentiment = field("detectSentiment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBotResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBotResponse:
    boto3_raw_data: "type_defs.PutBotResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def intents(self):  # pragma: no cover
        return Intent.make_many(self.boto3_raw_data["intents"])

    enableModelImprovements = field("enableModelImprovements")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")

    @cached_property
    def clarificationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["clarificationPrompt"])

    @cached_property
    def abortStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["abortStatement"])

    status = field("status")
    failureReason = field("failureReason")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    voiceId = field("voiceId")
    checksum = field("checksum")
    version = field("version")
    locale = field("locale")
    childDirected = field("childDirected")
    createVersion = field("createVersion")
    detectSentiment = field("detectSentiment")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutBotResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FollowUpPrompt:
    boto3_raw_data: "type_defs.FollowUpPromptTypeDef" = dataclasses.field()

    @cached_property
    def prompt(self):  # pragma: no cover
        return Prompt.make_one(self.boto3_raw_data["prompt"])

    @cached_property
    def rejectionStatement(self):  # pragma: no cover
        return Statement.make_one(self.boto3_raw_data["rejectionStatement"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FollowUpPromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FollowUpPromptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotOutput:
    boto3_raw_data: "type_defs.SlotOutputTypeDef" = dataclasses.field()

    name = field("name")
    slotConstraint = field("slotConstraint")
    description = field("description")
    slotType = field("slotType")
    slotTypeVersion = field("slotTypeVersion")

    @cached_property
    def valueElicitationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["valueElicitationPrompt"])

    priority = field("priority")
    sampleUtterances = field("sampleUtterances")
    responseCard = field("responseCard")
    obfuscationSetting = field("obfuscationSetting")

    @cached_property
    def defaultValueSpec(self):  # pragma: no cover
        return SlotDefaultValueSpecOutput.make_one(
            self.boto3_raw_data["defaultValueSpec"]
        )

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
class CreateSlotTypeVersionResponse:
    boto3_raw_data: "type_defs.CreateSlotTypeVersionResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")

    @cached_property
    def enumerationValues(self):  # pragma: no cover
        return EnumerationValueOutput.make_many(
            self.boto3_raw_data["enumerationValues"]
        )

    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")
    checksum = field("checksum")
    valueSelectionStrategy = field("valueSelectionStrategy")
    parentSlotTypeSignature = field("parentSlotTypeSignature")

    @cached_property
    def slotTypeConfigurations(self):  # pragma: no cover
        return SlotTypeConfiguration.make_many(
            self.boto3_raw_data["slotTypeConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSlotTypeVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlotTypeVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSlotTypeResponse:
    boto3_raw_data: "type_defs.GetSlotTypeResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def enumerationValues(self):  # pragma: no cover
        return EnumerationValueOutput.make_many(
            self.boto3_raw_data["enumerationValues"]
        )

    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")
    checksum = field("checksum")
    valueSelectionStrategy = field("valueSelectionStrategy")
    parentSlotTypeSignature = field("parentSlotTypeSignature")

    @cached_property
    def slotTypeConfigurations(self):  # pragma: no cover
        return SlotTypeConfiguration.make_many(
            self.boto3_raw_data["slotTypeConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSlotTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSlotTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSlotTypeRequest:
    boto3_raw_data: "type_defs.PutSlotTypeRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    enumerationValues = field("enumerationValues")
    checksum = field("checksum")
    valueSelectionStrategy = field("valueSelectionStrategy")
    createVersion = field("createVersion")
    parentSlotTypeSignature = field("parentSlotTypeSignature")

    @cached_property
    def slotTypeConfigurations(self):  # pragma: no cover
        return SlotTypeConfiguration.make_many(
            self.boto3_raw_data["slotTypeConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSlotTypeResponse:
    boto3_raw_data: "type_defs.PutSlotTypeResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def enumerationValues(self):  # pragma: no cover
        return EnumerationValueOutput.make_many(
            self.boto3_raw_data["enumerationValues"]
        )

    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")
    checksum = field("checksum")
    valueSelectionStrategy = field("valueSelectionStrategy")
    createVersion = field("createVersion")
    parentSlotTypeSignature = field("parentSlotTypeSignature")

    @cached_property
    def slotTypeConfigurations(self):  # pragma: no cover
        return SlotTypeConfiguration.make_many(
            self.boto3_raw_data["slotTypeConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSlotTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSlotTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUtterancesViewResponse:
    boto3_raw_data: "type_defs.GetUtterancesViewResponseTypeDef" = dataclasses.field()

    botName = field("botName")

    @cached_property
    def utterances(self):  # pragma: no cover
        return UtteranceList.make_many(self.boto3_raw_data["utterances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUtterancesViewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUtterancesViewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotAliasesResponse:
    boto3_raw_data: "type_defs.GetBotAliasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def BotAliases(self):  # pragma: no cover
        return BotAliasMetadata.make_many(self.boto3_raw_data["BotAliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBotAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBotAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBotRequest:
    boto3_raw_data: "type_defs.PutBotRequestTypeDef" = dataclasses.field()

    name = field("name")
    locale = field("locale")
    childDirected = field("childDirected")
    description = field("description")

    @cached_property
    def intents(self):  # pragma: no cover
        return Intent.make_many(self.boto3_raw_data["intents"])

    enableModelImprovements = field("enableModelImprovements")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")
    clarificationPrompt = field("clarificationPrompt")
    abortStatement = field("abortStatement")
    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    voiceId = field("voiceId")
    checksum = field("checksum")
    processBehavior = field("processBehavior")
    detectSentiment = field("detectSentiment")
    createVersion = field("createVersion")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutBotRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntentVersionResponse:
    boto3_raw_data: "type_defs.CreateIntentVersionResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def slots(self):  # pragma: no cover
        return SlotOutput.make_many(self.boto3_raw_data["slots"])

    sampleUtterances = field("sampleUtterances")

    @cached_property
    def confirmationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["confirmationPrompt"])

    @cached_property
    def rejectionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["rejectionStatement"])

    @cached_property
    def followUpPrompt(self):  # pragma: no cover
        return FollowUpPromptOutput.make_one(self.boto3_raw_data["followUpPrompt"])

    @cached_property
    def conclusionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["conclusionStatement"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return CodeHook.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentActivity(self):  # pragma: no cover
        return FulfillmentActivity.make_one(self.boto3_raw_data["fulfillmentActivity"])

    parentIntentSignature = field("parentIntentSignature")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")
    checksum = field("checksum")

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntentVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntentResponse:
    boto3_raw_data: "type_defs.GetIntentResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def slots(self):  # pragma: no cover
        return SlotOutput.make_many(self.boto3_raw_data["slots"])

    sampleUtterances = field("sampleUtterances")

    @cached_property
    def confirmationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["confirmationPrompt"])

    @cached_property
    def rejectionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["rejectionStatement"])

    @cached_property
    def followUpPrompt(self):  # pragma: no cover
        return FollowUpPromptOutput.make_one(self.boto3_raw_data["followUpPrompt"])

    @cached_property
    def conclusionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["conclusionStatement"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return CodeHook.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentActivity(self):  # pragma: no cover
        return FulfillmentActivity.make_one(self.boto3_raw_data["fulfillmentActivity"])

    parentIntentSignature = field("parentIntentSignature")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")
    checksum = field("checksum")

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIntentResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntentResponse:
    boto3_raw_data: "type_defs.PutIntentResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def slots(self):  # pragma: no cover
        return SlotOutput.make_many(self.boto3_raw_data["slots"])

    sampleUtterances = field("sampleUtterances")

    @cached_property
    def confirmationPrompt(self):  # pragma: no cover
        return PromptOutput.make_one(self.boto3_raw_data["confirmationPrompt"])

    @cached_property
    def rejectionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["rejectionStatement"])

    @cached_property
    def followUpPrompt(self):  # pragma: no cover
        return FollowUpPromptOutput.make_one(self.boto3_raw_data["followUpPrompt"])

    @cached_property
    def conclusionStatement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["conclusionStatement"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return CodeHook.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentActivity(self):  # pragma: no cover
        return FulfillmentActivity.make_one(self.boto3_raw_data["fulfillmentActivity"])

    parentIntentSignature = field("parentIntentSignature")
    lastUpdatedDate = field("lastUpdatedDate")
    createdDate = field("createdDate")
    version = field("version")
    checksum = field("checksum")
    createVersion = field("createVersion")

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutIntentResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Slot:
    boto3_raw_data: "type_defs.SlotTypeDef" = dataclasses.field()

    name = field("name")
    slotConstraint = field("slotConstraint")
    description = field("description")
    slotType = field("slotType")
    slotTypeVersion = field("slotTypeVersion")
    valueElicitationPrompt = field("valueElicitationPrompt")
    priority = field("priority")
    sampleUtterances = field("sampleUtterances")
    responseCard = field("responseCard")
    obfuscationSetting = field("obfuscationSetting")
    defaultValueSpec = field("defaultValueSpec")

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
class PutIntentRequest:
    boto3_raw_data: "type_defs.PutIntentRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    slots = field("slots")
    sampleUtterances = field("sampleUtterances")
    confirmationPrompt = field("confirmationPrompt")
    rejectionStatement = field("rejectionStatement")
    followUpPrompt = field("followUpPrompt")
    conclusionStatement = field("conclusionStatement")

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return CodeHook.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentActivity(self):  # pragma: no cover
        return FulfillmentActivity.make_one(self.boto3_raw_data["fulfillmentActivity"])

    parentIntentSignature = field("parentIntentSignature")
    checksum = field("checksum")
    createVersion = field("createVersion")

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutIntentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
