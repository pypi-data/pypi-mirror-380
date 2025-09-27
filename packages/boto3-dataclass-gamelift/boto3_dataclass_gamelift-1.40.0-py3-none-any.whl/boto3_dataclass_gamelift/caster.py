# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_gamelift import type_defs as bs_td


class GAMELIFTCaster:

    def claim_game_server(
        self,
        res: "bs_td.ClaimGameServerOutputTypeDef",
    ) -> "dc_td.ClaimGameServerOutput":
        return dc_td.ClaimGameServerOutput.make_one(res)

    def create_alias(
        self,
        res: "bs_td.CreateAliasOutputTypeDef",
    ) -> "dc_td.CreateAliasOutput":
        return dc_td.CreateAliasOutput.make_one(res)

    def create_build(
        self,
        res: "bs_td.CreateBuildOutputTypeDef",
    ) -> "dc_td.CreateBuildOutput":
        return dc_td.CreateBuildOutput.make_one(res)

    def create_container_fleet(
        self,
        res: "bs_td.CreateContainerFleetOutputTypeDef",
    ) -> "dc_td.CreateContainerFleetOutput":
        return dc_td.CreateContainerFleetOutput.make_one(res)

    def create_container_group_definition(
        self,
        res: "bs_td.CreateContainerGroupDefinitionOutputTypeDef",
    ) -> "dc_td.CreateContainerGroupDefinitionOutput":
        return dc_td.CreateContainerGroupDefinitionOutput.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetOutputTypeDef",
    ) -> "dc_td.CreateFleetOutput":
        return dc_td.CreateFleetOutput.make_one(res)

    def create_fleet_locations(
        self,
        res: "bs_td.CreateFleetLocationsOutputTypeDef",
    ) -> "dc_td.CreateFleetLocationsOutput":
        return dc_td.CreateFleetLocationsOutput.make_one(res)

    def create_game_server_group(
        self,
        res: "bs_td.CreateGameServerGroupOutputTypeDef",
    ) -> "dc_td.CreateGameServerGroupOutput":
        return dc_td.CreateGameServerGroupOutput.make_one(res)

    def create_game_session(
        self,
        res: "bs_td.CreateGameSessionOutputTypeDef",
    ) -> "dc_td.CreateGameSessionOutput":
        return dc_td.CreateGameSessionOutput.make_one(res)

    def create_game_session_queue(
        self,
        res: "bs_td.CreateGameSessionQueueOutputTypeDef",
    ) -> "dc_td.CreateGameSessionQueueOutput":
        return dc_td.CreateGameSessionQueueOutput.make_one(res)

    def create_location(
        self,
        res: "bs_td.CreateLocationOutputTypeDef",
    ) -> "dc_td.CreateLocationOutput":
        return dc_td.CreateLocationOutput.make_one(res)

    def create_matchmaking_configuration(
        self,
        res: "bs_td.CreateMatchmakingConfigurationOutputTypeDef",
    ) -> "dc_td.CreateMatchmakingConfigurationOutput":
        return dc_td.CreateMatchmakingConfigurationOutput.make_one(res)

    def create_matchmaking_rule_set(
        self,
        res: "bs_td.CreateMatchmakingRuleSetOutputTypeDef",
    ) -> "dc_td.CreateMatchmakingRuleSetOutput":
        return dc_td.CreateMatchmakingRuleSetOutput.make_one(res)

    def create_player_session(
        self,
        res: "bs_td.CreatePlayerSessionOutputTypeDef",
    ) -> "dc_td.CreatePlayerSessionOutput":
        return dc_td.CreatePlayerSessionOutput.make_one(res)

    def create_player_sessions(
        self,
        res: "bs_td.CreatePlayerSessionsOutputTypeDef",
    ) -> "dc_td.CreatePlayerSessionsOutput":
        return dc_td.CreatePlayerSessionsOutput.make_one(res)

    def create_script(
        self,
        res: "bs_td.CreateScriptOutputTypeDef",
    ) -> "dc_td.CreateScriptOutput":
        return dc_td.CreateScriptOutput.make_one(res)

    def create_vpc_peering_authorization(
        self,
        res: "bs_td.CreateVpcPeeringAuthorizationOutputTypeDef",
    ) -> "dc_td.CreateVpcPeeringAuthorizationOutput":
        return dc_td.CreateVpcPeeringAuthorizationOutput.make_one(res)

    def delete_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_build(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_fleet(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_fleet_locations(
        self,
        res: "bs_td.DeleteFleetLocationsOutputTypeDef",
    ) -> "dc_td.DeleteFleetLocationsOutput":
        return dc_td.DeleteFleetLocationsOutput.make_one(res)

    def delete_game_server_group(
        self,
        res: "bs_td.DeleteGameServerGroupOutputTypeDef",
    ) -> "dc_td.DeleteGameServerGroupOutput":
        return dc_td.DeleteGameServerGroupOutput.make_one(res)

    def delete_scaling_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_script(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_game_server(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_alias(
        self,
        res: "bs_td.DescribeAliasOutputTypeDef",
    ) -> "dc_td.DescribeAliasOutput":
        return dc_td.DescribeAliasOutput.make_one(res)

    def describe_build(
        self,
        res: "bs_td.DescribeBuildOutputTypeDef",
    ) -> "dc_td.DescribeBuildOutput":
        return dc_td.DescribeBuildOutput.make_one(res)

    def describe_compute(
        self,
        res: "bs_td.DescribeComputeOutputTypeDef",
    ) -> "dc_td.DescribeComputeOutput":
        return dc_td.DescribeComputeOutput.make_one(res)

    def describe_container_fleet(
        self,
        res: "bs_td.DescribeContainerFleetOutputTypeDef",
    ) -> "dc_td.DescribeContainerFleetOutput":
        return dc_td.DescribeContainerFleetOutput.make_one(res)

    def describe_container_group_definition(
        self,
        res: "bs_td.DescribeContainerGroupDefinitionOutputTypeDef",
    ) -> "dc_td.DescribeContainerGroupDefinitionOutput":
        return dc_td.DescribeContainerGroupDefinitionOutput.make_one(res)

    def describe_ec2_instance_limits(
        self,
        res: "bs_td.DescribeEC2InstanceLimitsOutputTypeDef",
    ) -> "dc_td.DescribeEC2InstanceLimitsOutput":
        return dc_td.DescribeEC2InstanceLimitsOutput.make_one(res)

    def describe_fleet_attributes(
        self,
        res: "bs_td.DescribeFleetAttributesOutputTypeDef",
    ) -> "dc_td.DescribeFleetAttributesOutput":
        return dc_td.DescribeFleetAttributesOutput.make_one(res)

    def describe_fleet_capacity(
        self,
        res: "bs_td.DescribeFleetCapacityOutputTypeDef",
    ) -> "dc_td.DescribeFleetCapacityOutput":
        return dc_td.DescribeFleetCapacityOutput.make_one(res)

    def describe_fleet_deployment(
        self,
        res: "bs_td.DescribeFleetDeploymentOutputTypeDef",
    ) -> "dc_td.DescribeFleetDeploymentOutput":
        return dc_td.DescribeFleetDeploymentOutput.make_one(res)

    def describe_fleet_events(
        self,
        res: "bs_td.DescribeFleetEventsOutputTypeDef",
    ) -> "dc_td.DescribeFleetEventsOutput":
        return dc_td.DescribeFleetEventsOutput.make_one(res)

    def describe_fleet_location_attributes(
        self,
        res: "bs_td.DescribeFleetLocationAttributesOutputTypeDef",
    ) -> "dc_td.DescribeFleetLocationAttributesOutput":
        return dc_td.DescribeFleetLocationAttributesOutput.make_one(res)

    def describe_fleet_location_capacity(
        self,
        res: "bs_td.DescribeFleetLocationCapacityOutputTypeDef",
    ) -> "dc_td.DescribeFleetLocationCapacityOutput":
        return dc_td.DescribeFleetLocationCapacityOutput.make_one(res)

    def describe_fleet_location_utilization(
        self,
        res: "bs_td.DescribeFleetLocationUtilizationOutputTypeDef",
    ) -> "dc_td.DescribeFleetLocationUtilizationOutput":
        return dc_td.DescribeFleetLocationUtilizationOutput.make_one(res)

    def describe_fleet_port_settings(
        self,
        res: "bs_td.DescribeFleetPortSettingsOutputTypeDef",
    ) -> "dc_td.DescribeFleetPortSettingsOutput":
        return dc_td.DescribeFleetPortSettingsOutput.make_one(res)

    def describe_fleet_utilization(
        self,
        res: "bs_td.DescribeFleetUtilizationOutputTypeDef",
    ) -> "dc_td.DescribeFleetUtilizationOutput":
        return dc_td.DescribeFleetUtilizationOutput.make_one(res)

    def describe_game_server(
        self,
        res: "bs_td.DescribeGameServerOutputTypeDef",
    ) -> "dc_td.DescribeGameServerOutput":
        return dc_td.DescribeGameServerOutput.make_one(res)

    def describe_game_server_group(
        self,
        res: "bs_td.DescribeGameServerGroupOutputTypeDef",
    ) -> "dc_td.DescribeGameServerGroupOutput":
        return dc_td.DescribeGameServerGroupOutput.make_one(res)

    def describe_game_server_instances(
        self,
        res: "bs_td.DescribeGameServerInstancesOutputTypeDef",
    ) -> "dc_td.DescribeGameServerInstancesOutput":
        return dc_td.DescribeGameServerInstancesOutput.make_one(res)

    def describe_game_session_details(
        self,
        res: "bs_td.DescribeGameSessionDetailsOutputTypeDef",
    ) -> "dc_td.DescribeGameSessionDetailsOutput":
        return dc_td.DescribeGameSessionDetailsOutput.make_one(res)

    def describe_game_session_placement(
        self,
        res: "bs_td.DescribeGameSessionPlacementOutputTypeDef",
    ) -> "dc_td.DescribeGameSessionPlacementOutput":
        return dc_td.DescribeGameSessionPlacementOutput.make_one(res)

    def describe_game_session_queues(
        self,
        res: "bs_td.DescribeGameSessionQueuesOutputTypeDef",
    ) -> "dc_td.DescribeGameSessionQueuesOutput":
        return dc_td.DescribeGameSessionQueuesOutput.make_one(res)

    def describe_game_sessions(
        self,
        res: "bs_td.DescribeGameSessionsOutputTypeDef",
    ) -> "dc_td.DescribeGameSessionsOutput":
        return dc_td.DescribeGameSessionsOutput.make_one(res)

    def describe_instances(
        self,
        res: "bs_td.DescribeInstancesOutputTypeDef",
    ) -> "dc_td.DescribeInstancesOutput":
        return dc_td.DescribeInstancesOutput.make_one(res)

    def describe_matchmaking(
        self,
        res: "bs_td.DescribeMatchmakingOutputTypeDef",
    ) -> "dc_td.DescribeMatchmakingOutput":
        return dc_td.DescribeMatchmakingOutput.make_one(res)

    def describe_matchmaking_configurations(
        self,
        res: "bs_td.DescribeMatchmakingConfigurationsOutputTypeDef",
    ) -> "dc_td.DescribeMatchmakingConfigurationsOutput":
        return dc_td.DescribeMatchmakingConfigurationsOutput.make_one(res)

    def describe_matchmaking_rule_sets(
        self,
        res: "bs_td.DescribeMatchmakingRuleSetsOutputTypeDef",
    ) -> "dc_td.DescribeMatchmakingRuleSetsOutput":
        return dc_td.DescribeMatchmakingRuleSetsOutput.make_one(res)

    def describe_player_sessions(
        self,
        res: "bs_td.DescribePlayerSessionsOutputTypeDef",
    ) -> "dc_td.DescribePlayerSessionsOutput":
        return dc_td.DescribePlayerSessionsOutput.make_one(res)

    def describe_runtime_configuration(
        self,
        res: "bs_td.DescribeRuntimeConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeRuntimeConfigurationOutput":
        return dc_td.DescribeRuntimeConfigurationOutput.make_one(res)

    def describe_scaling_policies(
        self,
        res: "bs_td.DescribeScalingPoliciesOutputTypeDef",
    ) -> "dc_td.DescribeScalingPoliciesOutput":
        return dc_td.DescribeScalingPoliciesOutput.make_one(res)

    def describe_script(
        self,
        res: "bs_td.DescribeScriptOutputTypeDef",
    ) -> "dc_td.DescribeScriptOutput":
        return dc_td.DescribeScriptOutput.make_one(res)

    def describe_vpc_peering_authorizations(
        self,
        res: "bs_td.DescribeVpcPeeringAuthorizationsOutputTypeDef",
    ) -> "dc_td.DescribeVpcPeeringAuthorizationsOutput":
        return dc_td.DescribeVpcPeeringAuthorizationsOutput.make_one(res)

    def describe_vpc_peering_connections(
        self,
        res: "bs_td.DescribeVpcPeeringConnectionsOutputTypeDef",
    ) -> "dc_td.DescribeVpcPeeringConnectionsOutput":
        return dc_td.DescribeVpcPeeringConnectionsOutput.make_one(res)

    def get_compute_access(
        self,
        res: "bs_td.GetComputeAccessOutputTypeDef",
    ) -> "dc_td.GetComputeAccessOutput":
        return dc_td.GetComputeAccessOutput.make_one(res)

    def get_compute_auth_token(
        self,
        res: "bs_td.GetComputeAuthTokenOutputTypeDef",
    ) -> "dc_td.GetComputeAuthTokenOutput":
        return dc_td.GetComputeAuthTokenOutput.make_one(res)

    def get_game_session_log_url(
        self,
        res: "bs_td.GetGameSessionLogUrlOutputTypeDef",
    ) -> "dc_td.GetGameSessionLogUrlOutput":
        return dc_td.GetGameSessionLogUrlOutput.make_one(res)

    def get_instance_access(
        self,
        res: "bs_td.GetInstanceAccessOutputTypeDef",
    ) -> "dc_td.GetInstanceAccessOutput":
        return dc_td.GetInstanceAccessOutput.make_one(res)

    def list_aliases(
        self,
        res: "bs_td.ListAliasesOutputTypeDef",
    ) -> "dc_td.ListAliasesOutput":
        return dc_td.ListAliasesOutput.make_one(res)

    def list_builds(
        self,
        res: "bs_td.ListBuildsOutputTypeDef",
    ) -> "dc_td.ListBuildsOutput":
        return dc_td.ListBuildsOutput.make_one(res)

    def list_compute(
        self,
        res: "bs_td.ListComputeOutputTypeDef",
    ) -> "dc_td.ListComputeOutput":
        return dc_td.ListComputeOutput.make_one(res)

    def list_container_fleets(
        self,
        res: "bs_td.ListContainerFleetsOutputTypeDef",
    ) -> "dc_td.ListContainerFleetsOutput":
        return dc_td.ListContainerFleetsOutput.make_one(res)

    def list_container_group_definition_versions(
        self,
        res: "bs_td.ListContainerGroupDefinitionVersionsOutputTypeDef",
    ) -> "dc_td.ListContainerGroupDefinitionVersionsOutput":
        return dc_td.ListContainerGroupDefinitionVersionsOutput.make_one(res)

    def list_container_group_definitions(
        self,
        res: "bs_td.ListContainerGroupDefinitionsOutputTypeDef",
    ) -> "dc_td.ListContainerGroupDefinitionsOutput":
        return dc_td.ListContainerGroupDefinitionsOutput.make_one(res)

    def list_fleet_deployments(
        self,
        res: "bs_td.ListFleetDeploymentsOutputTypeDef",
    ) -> "dc_td.ListFleetDeploymentsOutput":
        return dc_td.ListFleetDeploymentsOutput.make_one(res)

    def list_fleets(
        self,
        res: "bs_td.ListFleetsOutputTypeDef",
    ) -> "dc_td.ListFleetsOutput":
        return dc_td.ListFleetsOutput.make_one(res)

    def list_game_server_groups(
        self,
        res: "bs_td.ListGameServerGroupsOutputTypeDef",
    ) -> "dc_td.ListGameServerGroupsOutput":
        return dc_td.ListGameServerGroupsOutput.make_one(res)

    def list_game_servers(
        self,
        res: "bs_td.ListGameServersOutputTypeDef",
    ) -> "dc_td.ListGameServersOutput":
        return dc_td.ListGameServersOutput.make_one(res)

    def list_locations(
        self,
        res: "bs_td.ListLocationsOutputTypeDef",
    ) -> "dc_td.ListLocationsOutput":
        return dc_td.ListLocationsOutput.make_one(res)

    def list_scripts(
        self,
        res: "bs_td.ListScriptsOutputTypeDef",
    ) -> "dc_td.ListScriptsOutput":
        return dc_td.ListScriptsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_scaling_policy(
        self,
        res: "bs_td.PutScalingPolicyOutputTypeDef",
    ) -> "dc_td.PutScalingPolicyOutput":
        return dc_td.PutScalingPolicyOutput.make_one(res)

    def register_compute(
        self,
        res: "bs_td.RegisterComputeOutputTypeDef",
    ) -> "dc_td.RegisterComputeOutput":
        return dc_td.RegisterComputeOutput.make_one(res)

    def register_game_server(
        self,
        res: "bs_td.RegisterGameServerOutputTypeDef",
    ) -> "dc_td.RegisterGameServerOutput":
        return dc_td.RegisterGameServerOutput.make_one(res)

    def request_upload_credentials(
        self,
        res: "bs_td.RequestUploadCredentialsOutputTypeDef",
    ) -> "dc_td.RequestUploadCredentialsOutput":
        return dc_td.RequestUploadCredentialsOutput.make_one(res)

    def resolve_alias(
        self,
        res: "bs_td.ResolveAliasOutputTypeDef",
    ) -> "dc_td.ResolveAliasOutput":
        return dc_td.ResolveAliasOutput.make_one(res)

    def resume_game_server_group(
        self,
        res: "bs_td.ResumeGameServerGroupOutputTypeDef",
    ) -> "dc_td.ResumeGameServerGroupOutput":
        return dc_td.ResumeGameServerGroupOutput.make_one(res)

    def search_game_sessions(
        self,
        res: "bs_td.SearchGameSessionsOutputTypeDef",
    ) -> "dc_td.SearchGameSessionsOutput":
        return dc_td.SearchGameSessionsOutput.make_one(res)

    def start_fleet_actions(
        self,
        res: "bs_td.StartFleetActionsOutputTypeDef",
    ) -> "dc_td.StartFleetActionsOutput":
        return dc_td.StartFleetActionsOutput.make_one(res)

    def start_game_session_placement(
        self,
        res: "bs_td.StartGameSessionPlacementOutputTypeDef",
    ) -> "dc_td.StartGameSessionPlacementOutput":
        return dc_td.StartGameSessionPlacementOutput.make_one(res)

    def start_match_backfill(
        self,
        res: "bs_td.StartMatchBackfillOutputTypeDef",
    ) -> "dc_td.StartMatchBackfillOutput":
        return dc_td.StartMatchBackfillOutput.make_one(res)

    def start_matchmaking(
        self,
        res: "bs_td.StartMatchmakingOutputTypeDef",
    ) -> "dc_td.StartMatchmakingOutput":
        return dc_td.StartMatchmakingOutput.make_one(res)

    def stop_fleet_actions(
        self,
        res: "bs_td.StopFleetActionsOutputTypeDef",
    ) -> "dc_td.StopFleetActionsOutput":
        return dc_td.StopFleetActionsOutput.make_one(res)

    def stop_game_session_placement(
        self,
        res: "bs_td.StopGameSessionPlacementOutputTypeDef",
    ) -> "dc_td.StopGameSessionPlacementOutput":
        return dc_td.StopGameSessionPlacementOutput.make_one(res)

    def suspend_game_server_group(
        self,
        res: "bs_td.SuspendGameServerGroupOutputTypeDef",
    ) -> "dc_td.SuspendGameServerGroupOutput":
        return dc_td.SuspendGameServerGroupOutput.make_one(res)

    def terminate_game_session(
        self,
        res: "bs_td.TerminateGameSessionOutputTypeDef",
    ) -> "dc_td.TerminateGameSessionOutput":
        return dc_td.TerminateGameSessionOutput.make_one(res)

    def update_alias(
        self,
        res: "bs_td.UpdateAliasOutputTypeDef",
    ) -> "dc_td.UpdateAliasOutput":
        return dc_td.UpdateAliasOutput.make_one(res)

    def update_build(
        self,
        res: "bs_td.UpdateBuildOutputTypeDef",
    ) -> "dc_td.UpdateBuildOutput":
        return dc_td.UpdateBuildOutput.make_one(res)

    def update_container_fleet(
        self,
        res: "bs_td.UpdateContainerFleetOutputTypeDef",
    ) -> "dc_td.UpdateContainerFleetOutput":
        return dc_td.UpdateContainerFleetOutput.make_one(res)

    def update_container_group_definition(
        self,
        res: "bs_td.UpdateContainerGroupDefinitionOutputTypeDef",
    ) -> "dc_td.UpdateContainerGroupDefinitionOutput":
        return dc_td.UpdateContainerGroupDefinitionOutput.make_one(res)

    def update_fleet_attributes(
        self,
        res: "bs_td.UpdateFleetAttributesOutputTypeDef",
    ) -> "dc_td.UpdateFleetAttributesOutput":
        return dc_td.UpdateFleetAttributesOutput.make_one(res)

    def update_fleet_capacity(
        self,
        res: "bs_td.UpdateFleetCapacityOutputTypeDef",
    ) -> "dc_td.UpdateFleetCapacityOutput":
        return dc_td.UpdateFleetCapacityOutput.make_one(res)

    def update_fleet_port_settings(
        self,
        res: "bs_td.UpdateFleetPortSettingsOutputTypeDef",
    ) -> "dc_td.UpdateFleetPortSettingsOutput":
        return dc_td.UpdateFleetPortSettingsOutput.make_one(res)

    def update_game_server(
        self,
        res: "bs_td.UpdateGameServerOutputTypeDef",
    ) -> "dc_td.UpdateGameServerOutput":
        return dc_td.UpdateGameServerOutput.make_one(res)

    def update_game_server_group(
        self,
        res: "bs_td.UpdateGameServerGroupOutputTypeDef",
    ) -> "dc_td.UpdateGameServerGroupOutput":
        return dc_td.UpdateGameServerGroupOutput.make_one(res)

    def update_game_session(
        self,
        res: "bs_td.UpdateGameSessionOutputTypeDef",
    ) -> "dc_td.UpdateGameSessionOutput":
        return dc_td.UpdateGameSessionOutput.make_one(res)

    def update_game_session_queue(
        self,
        res: "bs_td.UpdateGameSessionQueueOutputTypeDef",
    ) -> "dc_td.UpdateGameSessionQueueOutput":
        return dc_td.UpdateGameSessionQueueOutput.make_one(res)

    def update_matchmaking_configuration(
        self,
        res: "bs_td.UpdateMatchmakingConfigurationOutputTypeDef",
    ) -> "dc_td.UpdateMatchmakingConfigurationOutput":
        return dc_td.UpdateMatchmakingConfigurationOutput.make_one(res)

    def update_runtime_configuration(
        self,
        res: "bs_td.UpdateRuntimeConfigurationOutputTypeDef",
    ) -> "dc_td.UpdateRuntimeConfigurationOutput":
        return dc_td.UpdateRuntimeConfigurationOutput.make_one(res)

    def update_script(
        self,
        res: "bs_td.UpdateScriptOutputTypeDef",
    ) -> "dc_td.UpdateScriptOutput":
        return dc_td.UpdateScriptOutput.make_one(res)

    def validate_matchmaking_rule_set(
        self,
        res: "bs_td.ValidateMatchmakingRuleSetOutputTypeDef",
    ) -> "dc_td.ValidateMatchmakingRuleSetOutput":
        return dc_td.ValidateMatchmakingRuleSetOutput.make_one(res)


gamelift_caster = GAMELIFTCaster()
