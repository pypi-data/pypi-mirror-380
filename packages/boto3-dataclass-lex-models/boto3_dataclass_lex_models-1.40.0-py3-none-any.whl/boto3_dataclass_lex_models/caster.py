# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lex_models import type_defs as bs_td


class LEX_MODELSCaster:

    def create_bot_version(
        self,
        res: "bs_td.CreateBotVersionResponseTypeDef",
    ) -> "dc_td.CreateBotVersionResponse":
        return dc_td.CreateBotVersionResponse.make_one(res)

    def create_intent_version(
        self,
        res: "bs_td.CreateIntentVersionResponseTypeDef",
    ) -> "dc_td.CreateIntentVersionResponse":
        return dc_td.CreateIntentVersionResponse.make_one(res)

    def create_slot_type_version(
        self,
        res: "bs_td.CreateSlotTypeVersionResponseTypeDef",
    ) -> "dc_td.CreateSlotTypeVersionResponse":
        return dc_td.CreateSlotTypeVersionResponse.make_one(res)

    def delete_bot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bot_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bot_channel_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bot_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_intent(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_intent_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_slot_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_slot_type_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_utterances(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_bot(
        self,
        res: "bs_td.GetBotResponseTypeDef",
    ) -> "dc_td.GetBotResponse":
        return dc_td.GetBotResponse.make_one(res)

    def get_bot_alias(
        self,
        res: "bs_td.GetBotAliasResponseTypeDef",
    ) -> "dc_td.GetBotAliasResponse":
        return dc_td.GetBotAliasResponse.make_one(res)

    def get_bot_aliases(
        self,
        res: "bs_td.GetBotAliasesResponseTypeDef",
    ) -> "dc_td.GetBotAliasesResponse":
        return dc_td.GetBotAliasesResponse.make_one(res)

    def get_bot_channel_association(
        self,
        res: "bs_td.GetBotChannelAssociationResponseTypeDef",
    ) -> "dc_td.GetBotChannelAssociationResponse":
        return dc_td.GetBotChannelAssociationResponse.make_one(res)

    def get_bot_channel_associations(
        self,
        res: "bs_td.GetBotChannelAssociationsResponseTypeDef",
    ) -> "dc_td.GetBotChannelAssociationsResponse":
        return dc_td.GetBotChannelAssociationsResponse.make_one(res)

    def get_bot_versions(
        self,
        res: "bs_td.GetBotVersionsResponseTypeDef",
    ) -> "dc_td.GetBotVersionsResponse":
        return dc_td.GetBotVersionsResponse.make_one(res)

    def get_bots(
        self,
        res: "bs_td.GetBotsResponseTypeDef",
    ) -> "dc_td.GetBotsResponse":
        return dc_td.GetBotsResponse.make_one(res)

    def get_builtin_intent(
        self,
        res: "bs_td.GetBuiltinIntentResponseTypeDef",
    ) -> "dc_td.GetBuiltinIntentResponse":
        return dc_td.GetBuiltinIntentResponse.make_one(res)

    def get_builtin_intents(
        self,
        res: "bs_td.GetBuiltinIntentsResponseTypeDef",
    ) -> "dc_td.GetBuiltinIntentsResponse":
        return dc_td.GetBuiltinIntentsResponse.make_one(res)

    def get_builtin_slot_types(
        self,
        res: "bs_td.GetBuiltinSlotTypesResponseTypeDef",
    ) -> "dc_td.GetBuiltinSlotTypesResponse":
        return dc_td.GetBuiltinSlotTypesResponse.make_one(res)

    def get_export(
        self,
        res: "bs_td.GetExportResponseTypeDef",
    ) -> "dc_td.GetExportResponse":
        return dc_td.GetExportResponse.make_one(res)

    def get_import(
        self,
        res: "bs_td.GetImportResponseTypeDef",
    ) -> "dc_td.GetImportResponse":
        return dc_td.GetImportResponse.make_one(res)

    def get_intent(
        self,
        res: "bs_td.GetIntentResponseTypeDef",
    ) -> "dc_td.GetIntentResponse":
        return dc_td.GetIntentResponse.make_one(res)

    def get_intent_versions(
        self,
        res: "bs_td.GetIntentVersionsResponseTypeDef",
    ) -> "dc_td.GetIntentVersionsResponse":
        return dc_td.GetIntentVersionsResponse.make_one(res)

    def get_intents(
        self,
        res: "bs_td.GetIntentsResponseTypeDef",
    ) -> "dc_td.GetIntentsResponse":
        return dc_td.GetIntentsResponse.make_one(res)

    def get_migration(
        self,
        res: "bs_td.GetMigrationResponseTypeDef",
    ) -> "dc_td.GetMigrationResponse":
        return dc_td.GetMigrationResponse.make_one(res)

    def get_migrations(
        self,
        res: "bs_td.GetMigrationsResponseTypeDef",
    ) -> "dc_td.GetMigrationsResponse":
        return dc_td.GetMigrationsResponse.make_one(res)

    def get_slot_type(
        self,
        res: "bs_td.GetSlotTypeResponseTypeDef",
    ) -> "dc_td.GetSlotTypeResponse":
        return dc_td.GetSlotTypeResponse.make_one(res)

    def get_slot_type_versions(
        self,
        res: "bs_td.GetSlotTypeVersionsResponseTypeDef",
    ) -> "dc_td.GetSlotTypeVersionsResponse":
        return dc_td.GetSlotTypeVersionsResponse.make_one(res)

    def get_slot_types(
        self,
        res: "bs_td.GetSlotTypesResponseTypeDef",
    ) -> "dc_td.GetSlotTypesResponse":
        return dc_td.GetSlotTypesResponse.make_one(res)

    def get_utterances_view(
        self,
        res: "bs_td.GetUtterancesViewResponseTypeDef",
    ) -> "dc_td.GetUtterancesViewResponse":
        return dc_td.GetUtterancesViewResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_bot(
        self,
        res: "bs_td.PutBotResponseTypeDef",
    ) -> "dc_td.PutBotResponse":
        return dc_td.PutBotResponse.make_one(res)

    def put_bot_alias(
        self,
        res: "bs_td.PutBotAliasResponseTypeDef",
    ) -> "dc_td.PutBotAliasResponse":
        return dc_td.PutBotAliasResponse.make_one(res)

    def put_intent(
        self,
        res: "bs_td.PutIntentResponseTypeDef",
    ) -> "dc_td.PutIntentResponse":
        return dc_td.PutIntentResponse.make_one(res)

    def put_slot_type(
        self,
        res: "bs_td.PutSlotTypeResponseTypeDef",
    ) -> "dc_td.PutSlotTypeResponse":
        return dc_td.PutSlotTypeResponse.make_one(res)

    def start_import(
        self,
        res: "bs_td.StartImportResponseTypeDef",
    ) -> "dc_td.StartImportResponse":
        return dc_td.StartImportResponse.make_one(res)

    def start_migration(
        self,
        res: "bs_td.StartMigrationResponseTypeDef",
    ) -> "dc_td.StartMigrationResponse":
        return dc_td.StartMigrationResponse.make_one(res)


lex_models_caster = LEX_MODELSCaster()
