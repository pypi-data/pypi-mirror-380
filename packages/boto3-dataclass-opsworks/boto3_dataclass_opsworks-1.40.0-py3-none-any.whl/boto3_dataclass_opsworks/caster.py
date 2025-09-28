# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opsworks import type_defs as bs_td


class OPSWORKSCaster:

    def assign_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def assign_volume(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_elastic_ip(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def attach_elastic_load_balancer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def clone_stack(
        self,
        res: "bs_td.CloneStackResultTypeDef",
    ) -> "dc_td.CloneStackResult":
        return dc_td.CloneStackResult.make_one(res)

    def create_app(
        self,
        res: "bs_td.CreateAppResultTypeDef",
    ) -> "dc_td.CreateAppResult":
        return dc_td.CreateAppResult.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentResultTypeDef",
    ) -> "dc_td.CreateDeploymentResult":
        return dc_td.CreateDeploymentResult.make_one(res)

    def create_instance(
        self,
        res: "bs_td.CreateInstanceResultTypeDef",
    ) -> "dc_td.CreateInstanceResult":
        return dc_td.CreateInstanceResult.make_one(res)

    def create_layer(
        self,
        res: "bs_td.CreateLayerResultTypeDef",
    ) -> "dc_td.CreateLayerResult":
        return dc_td.CreateLayerResult.make_one(res)

    def create_stack(
        self,
        res: "bs_td.CreateStackResultTypeDef",
    ) -> "dc_td.CreateStackResult":
        return dc_td.CreateStackResult.make_one(res)

    def create_user_profile(
        self,
        res: "bs_td.CreateUserProfileResultTypeDef",
    ) -> "dc_td.CreateUserProfileResult":
        return dc_td.CreateUserProfileResult.make_one(res)

    def delete_app(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_layer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_ecs_cluster(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_elastic_ip(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_rds_db_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_volume(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_agent_versions(
        self,
        res: "bs_td.DescribeAgentVersionsResultTypeDef",
    ) -> "dc_td.DescribeAgentVersionsResult":
        return dc_td.DescribeAgentVersionsResult.make_one(res)

    def describe_apps(
        self,
        res: "bs_td.DescribeAppsResultTypeDef",
    ) -> "dc_td.DescribeAppsResult":
        return dc_td.DescribeAppsResult.make_one(res)

    def describe_commands(
        self,
        res: "bs_td.DescribeCommandsResultTypeDef",
    ) -> "dc_td.DescribeCommandsResult":
        return dc_td.DescribeCommandsResult.make_one(res)

    def describe_deployments(
        self,
        res: "bs_td.DescribeDeploymentsResultTypeDef",
    ) -> "dc_td.DescribeDeploymentsResult":
        return dc_td.DescribeDeploymentsResult.make_one(res)

    def describe_ecs_clusters(
        self,
        res: "bs_td.DescribeEcsClustersResultTypeDef",
    ) -> "dc_td.DescribeEcsClustersResult":
        return dc_td.DescribeEcsClustersResult.make_one(res)

    def describe_elastic_ips(
        self,
        res: "bs_td.DescribeElasticIpsResultTypeDef",
    ) -> "dc_td.DescribeElasticIpsResult":
        return dc_td.DescribeElasticIpsResult.make_one(res)

    def describe_elastic_load_balancers(
        self,
        res: "bs_td.DescribeElasticLoadBalancersResultTypeDef",
    ) -> "dc_td.DescribeElasticLoadBalancersResult":
        return dc_td.DescribeElasticLoadBalancersResult.make_one(res)

    def describe_instances(
        self,
        res: "bs_td.DescribeInstancesResultTypeDef",
    ) -> "dc_td.DescribeInstancesResult":
        return dc_td.DescribeInstancesResult.make_one(res)

    def describe_layers(
        self,
        res: "bs_td.DescribeLayersResultTypeDef",
    ) -> "dc_td.DescribeLayersResult":
        return dc_td.DescribeLayersResult.make_one(res)

    def describe_load_based_auto_scaling(
        self,
        res: "bs_td.DescribeLoadBasedAutoScalingResultTypeDef",
    ) -> "dc_td.DescribeLoadBasedAutoScalingResult":
        return dc_td.DescribeLoadBasedAutoScalingResult.make_one(res)

    def describe_my_user_profile(
        self,
        res: "bs_td.DescribeMyUserProfileResultTypeDef",
    ) -> "dc_td.DescribeMyUserProfileResult":
        return dc_td.DescribeMyUserProfileResult.make_one(res)

    def describe_operating_systems(
        self,
        res: "bs_td.DescribeOperatingSystemsResponseTypeDef",
    ) -> "dc_td.DescribeOperatingSystemsResponse":
        return dc_td.DescribeOperatingSystemsResponse.make_one(res)

    def describe_permissions(
        self,
        res: "bs_td.DescribePermissionsResultTypeDef",
    ) -> "dc_td.DescribePermissionsResult":
        return dc_td.DescribePermissionsResult.make_one(res)

    def describe_raid_arrays(
        self,
        res: "bs_td.DescribeRaidArraysResultTypeDef",
    ) -> "dc_td.DescribeRaidArraysResult":
        return dc_td.DescribeRaidArraysResult.make_one(res)

    def describe_rds_db_instances(
        self,
        res: "bs_td.DescribeRdsDbInstancesResultTypeDef",
    ) -> "dc_td.DescribeRdsDbInstancesResult":
        return dc_td.DescribeRdsDbInstancesResult.make_one(res)

    def describe_service_errors(
        self,
        res: "bs_td.DescribeServiceErrorsResultTypeDef",
    ) -> "dc_td.DescribeServiceErrorsResult":
        return dc_td.DescribeServiceErrorsResult.make_one(res)

    def describe_stack_provisioning_parameters(
        self,
        res: "bs_td.DescribeStackProvisioningParametersResultTypeDef",
    ) -> "dc_td.DescribeStackProvisioningParametersResult":
        return dc_td.DescribeStackProvisioningParametersResult.make_one(res)

    def describe_stack_summary(
        self,
        res: "bs_td.DescribeStackSummaryResultTypeDef",
    ) -> "dc_td.DescribeStackSummaryResult":
        return dc_td.DescribeStackSummaryResult.make_one(res)

    def describe_stacks(
        self,
        res: "bs_td.DescribeStacksResultTypeDef",
    ) -> "dc_td.DescribeStacksResult":
        return dc_td.DescribeStacksResult.make_one(res)

    def describe_time_based_auto_scaling(
        self,
        res: "bs_td.DescribeTimeBasedAutoScalingResultTypeDef",
    ) -> "dc_td.DescribeTimeBasedAutoScalingResult":
        return dc_td.DescribeTimeBasedAutoScalingResult.make_one(res)

    def describe_user_profiles(
        self,
        res: "bs_td.DescribeUserProfilesResultTypeDef",
    ) -> "dc_td.DescribeUserProfilesResult":
        return dc_td.DescribeUserProfilesResult.make_one(res)

    def describe_volumes(
        self,
        res: "bs_td.DescribeVolumesResultTypeDef",
    ) -> "dc_td.DescribeVolumesResult":
        return dc_td.DescribeVolumesResult.make_one(res)

    def detach_elastic_load_balancer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_elastic_ip(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_hostname_suggestion(
        self,
        res: "bs_td.GetHostnameSuggestionResultTypeDef",
    ) -> "dc_td.GetHostnameSuggestionResult":
        return dc_td.GetHostnameSuggestionResult.make_one(res)

    def grant_access(
        self,
        res: "bs_td.GrantAccessResultTypeDef",
    ) -> "dc_td.GrantAccessResult":
        return dc_td.GrantAccessResult.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResultTypeDef",
    ) -> "dc_td.ListTagsResult":
        return dc_td.ListTagsResult.make_one(res)

    def reboot_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_ecs_cluster(
        self,
        res: "bs_td.RegisterEcsClusterResultTypeDef",
    ) -> "dc_td.RegisterEcsClusterResult":
        return dc_td.RegisterEcsClusterResult.make_one(res)

    def register_elastic_ip(
        self,
        res: "bs_td.RegisterElasticIpResultTypeDef",
    ) -> "dc_td.RegisterElasticIpResult":
        return dc_td.RegisterElasticIpResult.make_one(res)

    def register_instance(
        self,
        res: "bs_td.RegisterInstanceResultTypeDef",
    ) -> "dc_td.RegisterInstanceResult":
        return dc_td.RegisterInstanceResult.make_one(res)

    def register_rds_db_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_volume(
        self,
        res: "bs_td.RegisterVolumeResultTypeDef",
    ) -> "dc_td.RegisterVolumeResult":
        return dc_td.RegisterVolumeResult.make_one(res)

    def set_load_based_auto_scaling(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_time_based_auto_scaling(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_stack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_stack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def unassign_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def unassign_volume(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_app(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_elastic_ip(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_layer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_my_user_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_rds_db_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_stack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_volume(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


opsworks_caster = OPSWORKSCaster()
