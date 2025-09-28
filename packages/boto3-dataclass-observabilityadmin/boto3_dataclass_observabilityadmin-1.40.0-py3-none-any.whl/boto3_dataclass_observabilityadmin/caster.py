# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_observabilityadmin import type_defs as bs_td


class OBSERVABILITYADMINCaster:

    def create_centralization_rule_for_organization(
        self,
        res: "bs_td.CreateCentralizationRuleForOrganizationOutputTypeDef",
    ) -> "dc_td.CreateCentralizationRuleForOrganizationOutput":
        return dc_td.CreateCentralizationRuleForOrganizationOutput.make_one(res)

    def create_telemetry_rule(
        self,
        res: "bs_td.CreateTelemetryRuleOutputTypeDef",
    ) -> "dc_td.CreateTelemetryRuleOutput":
        return dc_td.CreateTelemetryRuleOutput.make_one(res)

    def create_telemetry_rule_for_organization(
        self,
        res: "bs_td.CreateTelemetryRuleForOrganizationOutputTypeDef",
    ) -> "dc_td.CreateTelemetryRuleForOrganizationOutput":
        return dc_td.CreateTelemetryRuleForOrganizationOutput.make_one(res)

    def delete_centralization_rule_for_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_telemetry_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_telemetry_rule_for_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_centralization_rule_for_organization(
        self,
        res: "bs_td.GetCentralizationRuleForOrganizationOutputTypeDef",
    ) -> "dc_td.GetCentralizationRuleForOrganizationOutput":
        return dc_td.GetCentralizationRuleForOrganizationOutput.make_one(res)

    def get_telemetry_evaluation_status(
        self,
        res: "bs_td.GetTelemetryEvaluationStatusOutputTypeDef",
    ) -> "dc_td.GetTelemetryEvaluationStatusOutput":
        return dc_td.GetTelemetryEvaluationStatusOutput.make_one(res)

    def get_telemetry_evaluation_status_for_organization(
        self,
        res: "bs_td.GetTelemetryEvaluationStatusForOrganizationOutputTypeDef",
    ) -> "dc_td.GetTelemetryEvaluationStatusForOrganizationOutput":
        return dc_td.GetTelemetryEvaluationStatusForOrganizationOutput.make_one(res)

    def get_telemetry_rule(
        self,
        res: "bs_td.GetTelemetryRuleOutputTypeDef",
    ) -> "dc_td.GetTelemetryRuleOutput":
        return dc_td.GetTelemetryRuleOutput.make_one(res)

    def get_telemetry_rule_for_organization(
        self,
        res: "bs_td.GetTelemetryRuleForOrganizationOutputTypeDef",
    ) -> "dc_td.GetTelemetryRuleForOrganizationOutput":
        return dc_td.GetTelemetryRuleForOrganizationOutput.make_one(res)

    def list_centralization_rules_for_organization(
        self,
        res: "bs_td.ListCentralizationRulesForOrganizationOutputTypeDef",
    ) -> "dc_td.ListCentralizationRulesForOrganizationOutput":
        return dc_td.ListCentralizationRulesForOrganizationOutput.make_one(res)

    def list_resource_telemetry(
        self,
        res: "bs_td.ListResourceTelemetryOutputTypeDef",
    ) -> "dc_td.ListResourceTelemetryOutput":
        return dc_td.ListResourceTelemetryOutput.make_one(res)

    def list_resource_telemetry_for_organization(
        self,
        res: "bs_td.ListResourceTelemetryForOrganizationOutputTypeDef",
    ) -> "dc_td.ListResourceTelemetryForOrganizationOutput":
        return dc_td.ListResourceTelemetryForOrganizationOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_telemetry_rules(
        self,
        res: "bs_td.ListTelemetryRulesOutputTypeDef",
    ) -> "dc_td.ListTelemetryRulesOutput":
        return dc_td.ListTelemetryRulesOutput.make_one(res)

    def list_telemetry_rules_for_organization(
        self,
        res: "bs_td.ListTelemetryRulesForOrganizationOutputTypeDef",
    ) -> "dc_td.ListTelemetryRulesForOrganizationOutput":
        return dc_td.ListTelemetryRulesForOrganizationOutput.make_one(res)

    def start_telemetry_evaluation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_telemetry_evaluation_for_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_telemetry_evaluation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_telemetry_evaluation_for_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_centralization_rule_for_organization(
        self,
        res: "bs_td.UpdateCentralizationRuleForOrganizationOutputTypeDef",
    ) -> "dc_td.UpdateCentralizationRuleForOrganizationOutput":
        return dc_td.UpdateCentralizationRuleForOrganizationOutput.make_one(res)

    def update_telemetry_rule(
        self,
        res: "bs_td.UpdateTelemetryRuleOutputTypeDef",
    ) -> "dc_td.UpdateTelemetryRuleOutput":
        return dc_td.UpdateTelemetryRuleOutput.make_one(res)

    def update_telemetry_rule_for_organization(
        self,
        res: "bs_td.UpdateTelemetryRuleForOrganizationOutputTypeDef",
    ) -> "dc_td.UpdateTelemetryRuleForOrganizationOutput":
        return dc_td.UpdateTelemetryRuleForOrganizationOutput.make_one(res)


observabilityadmin_caster = OBSERVABILITYADMINCaster()
