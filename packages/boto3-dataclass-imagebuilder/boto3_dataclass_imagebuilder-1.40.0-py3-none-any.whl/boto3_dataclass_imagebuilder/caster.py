# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_imagebuilder import type_defs as bs_td


class IMAGEBUILDERCaster:

    def cancel_image_creation(
        self,
        res: "bs_td.CancelImageCreationResponseTypeDef",
    ) -> "dc_td.CancelImageCreationResponse":
        return dc_td.CancelImageCreationResponse.make_one(res)

    def cancel_lifecycle_execution(
        self,
        res: "bs_td.CancelLifecycleExecutionResponseTypeDef",
    ) -> "dc_td.CancelLifecycleExecutionResponse":
        return dc_td.CancelLifecycleExecutionResponse.make_one(res)

    def create_component(
        self,
        res: "bs_td.CreateComponentResponseTypeDef",
    ) -> "dc_td.CreateComponentResponse":
        return dc_td.CreateComponentResponse.make_one(res)

    def create_container_recipe(
        self,
        res: "bs_td.CreateContainerRecipeResponseTypeDef",
    ) -> "dc_td.CreateContainerRecipeResponse":
        return dc_td.CreateContainerRecipeResponse.make_one(res)

    def create_distribution_configuration(
        self,
        res: "bs_td.CreateDistributionConfigurationResponseTypeDef",
    ) -> "dc_td.CreateDistributionConfigurationResponse":
        return dc_td.CreateDistributionConfigurationResponse.make_one(res)

    def create_image(
        self,
        res: "bs_td.CreateImageResponseTypeDef",
    ) -> "dc_td.CreateImageResponse":
        return dc_td.CreateImageResponse.make_one(res)

    def create_image_pipeline(
        self,
        res: "bs_td.CreateImagePipelineResponseTypeDef",
    ) -> "dc_td.CreateImagePipelineResponse":
        return dc_td.CreateImagePipelineResponse.make_one(res)

    def create_image_recipe(
        self,
        res: "bs_td.CreateImageRecipeResponseTypeDef",
    ) -> "dc_td.CreateImageRecipeResponse":
        return dc_td.CreateImageRecipeResponse.make_one(res)

    def create_infrastructure_configuration(
        self,
        res: "bs_td.CreateInfrastructureConfigurationResponseTypeDef",
    ) -> "dc_td.CreateInfrastructureConfigurationResponse":
        return dc_td.CreateInfrastructureConfigurationResponse.make_one(res)

    def create_lifecycle_policy(
        self,
        res: "bs_td.CreateLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.CreateLifecyclePolicyResponse":
        return dc_td.CreateLifecyclePolicyResponse.make_one(res)

    def create_workflow(
        self,
        res: "bs_td.CreateWorkflowResponseTypeDef",
    ) -> "dc_td.CreateWorkflowResponse":
        return dc_td.CreateWorkflowResponse.make_one(res)

    def delete_component(
        self,
        res: "bs_td.DeleteComponentResponseTypeDef",
    ) -> "dc_td.DeleteComponentResponse":
        return dc_td.DeleteComponentResponse.make_one(res)

    def delete_container_recipe(
        self,
        res: "bs_td.DeleteContainerRecipeResponseTypeDef",
    ) -> "dc_td.DeleteContainerRecipeResponse":
        return dc_td.DeleteContainerRecipeResponse.make_one(res)

    def delete_distribution_configuration(
        self,
        res: "bs_td.DeleteDistributionConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteDistributionConfigurationResponse":
        return dc_td.DeleteDistributionConfigurationResponse.make_one(res)

    def delete_image(
        self,
        res: "bs_td.DeleteImageResponseTypeDef",
    ) -> "dc_td.DeleteImageResponse":
        return dc_td.DeleteImageResponse.make_one(res)

    def delete_image_pipeline(
        self,
        res: "bs_td.DeleteImagePipelineResponseTypeDef",
    ) -> "dc_td.DeleteImagePipelineResponse":
        return dc_td.DeleteImagePipelineResponse.make_one(res)

    def delete_image_recipe(
        self,
        res: "bs_td.DeleteImageRecipeResponseTypeDef",
    ) -> "dc_td.DeleteImageRecipeResponse":
        return dc_td.DeleteImageRecipeResponse.make_one(res)

    def delete_infrastructure_configuration(
        self,
        res: "bs_td.DeleteInfrastructureConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteInfrastructureConfigurationResponse":
        return dc_td.DeleteInfrastructureConfigurationResponse.make_one(res)

    def delete_lifecycle_policy(
        self,
        res: "bs_td.DeleteLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.DeleteLifecyclePolicyResponse":
        return dc_td.DeleteLifecyclePolicyResponse.make_one(res)

    def delete_workflow(
        self,
        res: "bs_td.DeleteWorkflowResponseTypeDef",
    ) -> "dc_td.DeleteWorkflowResponse":
        return dc_td.DeleteWorkflowResponse.make_one(res)

    def get_component(
        self,
        res: "bs_td.GetComponentResponseTypeDef",
    ) -> "dc_td.GetComponentResponse":
        return dc_td.GetComponentResponse.make_one(res)

    def get_component_policy(
        self,
        res: "bs_td.GetComponentPolicyResponseTypeDef",
    ) -> "dc_td.GetComponentPolicyResponse":
        return dc_td.GetComponentPolicyResponse.make_one(res)

    def get_container_recipe(
        self,
        res: "bs_td.GetContainerRecipeResponseTypeDef",
    ) -> "dc_td.GetContainerRecipeResponse":
        return dc_td.GetContainerRecipeResponse.make_one(res)

    def get_container_recipe_policy(
        self,
        res: "bs_td.GetContainerRecipePolicyResponseTypeDef",
    ) -> "dc_td.GetContainerRecipePolicyResponse":
        return dc_td.GetContainerRecipePolicyResponse.make_one(res)

    def get_distribution_configuration(
        self,
        res: "bs_td.GetDistributionConfigurationResponseTypeDef",
    ) -> "dc_td.GetDistributionConfigurationResponse":
        return dc_td.GetDistributionConfigurationResponse.make_one(res)

    def get_image(
        self,
        res: "bs_td.GetImageResponseTypeDef",
    ) -> "dc_td.GetImageResponse":
        return dc_td.GetImageResponse.make_one(res)

    def get_image_pipeline(
        self,
        res: "bs_td.GetImagePipelineResponseTypeDef",
    ) -> "dc_td.GetImagePipelineResponse":
        return dc_td.GetImagePipelineResponse.make_one(res)

    def get_image_policy(
        self,
        res: "bs_td.GetImagePolicyResponseTypeDef",
    ) -> "dc_td.GetImagePolicyResponse":
        return dc_td.GetImagePolicyResponse.make_one(res)

    def get_image_recipe(
        self,
        res: "bs_td.GetImageRecipeResponseTypeDef",
    ) -> "dc_td.GetImageRecipeResponse":
        return dc_td.GetImageRecipeResponse.make_one(res)

    def get_image_recipe_policy(
        self,
        res: "bs_td.GetImageRecipePolicyResponseTypeDef",
    ) -> "dc_td.GetImageRecipePolicyResponse":
        return dc_td.GetImageRecipePolicyResponse.make_one(res)

    def get_infrastructure_configuration(
        self,
        res: "bs_td.GetInfrastructureConfigurationResponseTypeDef",
    ) -> "dc_td.GetInfrastructureConfigurationResponse":
        return dc_td.GetInfrastructureConfigurationResponse.make_one(res)

    def get_lifecycle_execution(
        self,
        res: "bs_td.GetLifecycleExecutionResponseTypeDef",
    ) -> "dc_td.GetLifecycleExecutionResponse":
        return dc_td.GetLifecycleExecutionResponse.make_one(res)

    def get_lifecycle_policy(
        self,
        res: "bs_td.GetLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.GetLifecyclePolicyResponse":
        return dc_td.GetLifecyclePolicyResponse.make_one(res)

    def get_marketplace_resource(
        self,
        res: "bs_td.GetMarketplaceResourceResponseTypeDef",
    ) -> "dc_td.GetMarketplaceResourceResponse":
        return dc_td.GetMarketplaceResourceResponse.make_one(res)

    def get_workflow(
        self,
        res: "bs_td.GetWorkflowResponseTypeDef",
    ) -> "dc_td.GetWorkflowResponse":
        return dc_td.GetWorkflowResponse.make_one(res)

    def get_workflow_execution(
        self,
        res: "bs_td.GetWorkflowExecutionResponseTypeDef",
    ) -> "dc_td.GetWorkflowExecutionResponse":
        return dc_td.GetWorkflowExecutionResponse.make_one(res)

    def get_workflow_step_execution(
        self,
        res: "bs_td.GetWorkflowStepExecutionResponseTypeDef",
    ) -> "dc_td.GetWorkflowStepExecutionResponse":
        return dc_td.GetWorkflowStepExecutionResponse.make_one(res)

    def import_component(
        self,
        res: "bs_td.ImportComponentResponseTypeDef",
    ) -> "dc_td.ImportComponentResponse":
        return dc_td.ImportComponentResponse.make_one(res)

    def import_disk_image(
        self,
        res: "bs_td.ImportDiskImageResponseTypeDef",
    ) -> "dc_td.ImportDiskImageResponse":
        return dc_td.ImportDiskImageResponse.make_one(res)

    def import_vm_image(
        self,
        res: "bs_td.ImportVmImageResponseTypeDef",
    ) -> "dc_td.ImportVmImageResponse":
        return dc_td.ImportVmImageResponse.make_one(res)

    def list_component_build_versions(
        self,
        res: "bs_td.ListComponentBuildVersionsResponseTypeDef",
    ) -> "dc_td.ListComponentBuildVersionsResponse":
        return dc_td.ListComponentBuildVersionsResponse.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsResponseTypeDef",
    ) -> "dc_td.ListComponentsResponse":
        return dc_td.ListComponentsResponse.make_one(res)

    def list_container_recipes(
        self,
        res: "bs_td.ListContainerRecipesResponseTypeDef",
    ) -> "dc_td.ListContainerRecipesResponse":
        return dc_td.ListContainerRecipesResponse.make_one(res)

    def list_distribution_configurations(
        self,
        res: "bs_td.ListDistributionConfigurationsResponseTypeDef",
    ) -> "dc_td.ListDistributionConfigurationsResponse":
        return dc_td.ListDistributionConfigurationsResponse.make_one(res)

    def list_image_build_versions(
        self,
        res: "bs_td.ListImageBuildVersionsResponseTypeDef",
    ) -> "dc_td.ListImageBuildVersionsResponse":
        return dc_td.ListImageBuildVersionsResponse.make_one(res)

    def list_image_packages(
        self,
        res: "bs_td.ListImagePackagesResponseTypeDef",
    ) -> "dc_td.ListImagePackagesResponse":
        return dc_td.ListImagePackagesResponse.make_one(res)

    def list_image_pipeline_images(
        self,
        res: "bs_td.ListImagePipelineImagesResponseTypeDef",
    ) -> "dc_td.ListImagePipelineImagesResponse":
        return dc_td.ListImagePipelineImagesResponse.make_one(res)

    def list_image_pipelines(
        self,
        res: "bs_td.ListImagePipelinesResponseTypeDef",
    ) -> "dc_td.ListImagePipelinesResponse":
        return dc_td.ListImagePipelinesResponse.make_one(res)

    def list_image_recipes(
        self,
        res: "bs_td.ListImageRecipesResponseTypeDef",
    ) -> "dc_td.ListImageRecipesResponse":
        return dc_td.ListImageRecipesResponse.make_one(res)

    def list_image_scan_finding_aggregations(
        self,
        res: "bs_td.ListImageScanFindingAggregationsResponseTypeDef",
    ) -> "dc_td.ListImageScanFindingAggregationsResponse":
        return dc_td.ListImageScanFindingAggregationsResponse.make_one(res)

    def list_image_scan_findings(
        self,
        res: "bs_td.ListImageScanFindingsResponseTypeDef",
    ) -> "dc_td.ListImageScanFindingsResponse":
        return dc_td.ListImageScanFindingsResponse.make_one(res)

    def list_images(
        self,
        res: "bs_td.ListImagesResponseTypeDef",
    ) -> "dc_td.ListImagesResponse":
        return dc_td.ListImagesResponse.make_one(res)

    def list_infrastructure_configurations(
        self,
        res: "bs_td.ListInfrastructureConfigurationsResponseTypeDef",
    ) -> "dc_td.ListInfrastructureConfigurationsResponse":
        return dc_td.ListInfrastructureConfigurationsResponse.make_one(res)

    def list_lifecycle_execution_resources(
        self,
        res: "bs_td.ListLifecycleExecutionResourcesResponseTypeDef",
    ) -> "dc_td.ListLifecycleExecutionResourcesResponse":
        return dc_td.ListLifecycleExecutionResourcesResponse.make_one(res)

    def list_lifecycle_executions(
        self,
        res: "bs_td.ListLifecycleExecutionsResponseTypeDef",
    ) -> "dc_td.ListLifecycleExecutionsResponse":
        return dc_td.ListLifecycleExecutionsResponse.make_one(res)

    def list_lifecycle_policies(
        self,
        res: "bs_td.ListLifecyclePoliciesResponseTypeDef",
    ) -> "dc_td.ListLifecyclePoliciesResponse":
        return dc_td.ListLifecyclePoliciesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_waiting_workflow_steps(
        self,
        res: "bs_td.ListWaitingWorkflowStepsResponseTypeDef",
    ) -> "dc_td.ListWaitingWorkflowStepsResponse":
        return dc_td.ListWaitingWorkflowStepsResponse.make_one(res)

    def list_workflow_build_versions(
        self,
        res: "bs_td.ListWorkflowBuildVersionsResponseTypeDef",
    ) -> "dc_td.ListWorkflowBuildVersionsResponse":
        return dc_td.ListWorkflowBuildVersionsResponse.make_one(res)

    def list_workflow_executions(
        self,
        res: "bs_td.ListWorkflowExecutionsResponseTypeDef",
    ) -> "dc_td.ListWorkflowExecutionsResponse":
        return dc_td.ListWorkflowExecutionsResponse.make_one(res)

    def list_workflow_step_executions(
        self,
        res: "bs_td.ListWorkflowStepExecutionsResponseTypeDef",
    ) -> "dc_td.ListWorkflowStepExecutionsResponse":
        return dc_td.ListWorkflowStepExecutionsResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListWorkflowsResponseTypeDef",
    ) -> "dc_td.ListWorkflowsResponse":
        return dc_td.ListWorkflowsResponse.make_one(res)

    def put_component_policy(
        self,
        res: "bs_td.PutComponentPolicyResponseTypeDef",
    ) -> "dc_td.PutComponentPolicyResponse":
        return dc_td.PutComponentPolicyResponse.make_one(res)

    def put_container_recipe_policy(
        self,
        res: "bs_td.PutContainerRecipePolicyResponseTypeDef",
    ) -> "dc_td.PutContainerRecipePolicyResponse":
        return dc_td.PutContainerRecipePolicyResponse.make_one(res)

    def put_image_policy(
        self,
        res: "bs_td.PutImagePolicyResponseTypeDef",
    ) -> "dc_td.PutImagePolicyResponse":
        return dc_td.PutImagePolicyResponse.make_one(res)

    def put_image_recipe_policy(
        self,
        res: "bs_td.PutImageRecipePolicyResponseTypeDef",
    ) -> "dc_td.PutImageRecipePolicyResponse":
        return dc_td.PutImageRecipePolicyResponse.make_one(res)

    def send_workflow_step_action(
        self,
        res: "bs_td.SendWorkflowStepActionResponseTypeDef",
    ) -> "dc_td.SendWorkflowStepActionResponse":
        return dc_td.SendWorkflowStepActionResponse.make_one(res)

    def start_image_pipeline_execution(
        self,
        res: "bs_td.StartImagePipelineExecutionResponseTypeDef",
    ) -> "dc_td.StartImagePipelineExecutionResponse":
        return dc_td.StartImagePipelineExecutionResponse.make_one(res)

    def start_resource_state_update(
        self,
        res: "bs_td.StartResourceStateUpdateResponseTypeDef",
    ) -> "dc_td.StartResourceStateUpdateResponse":
        return dc_td.StartResourceStateUpdateResponse.make_one(res)

    def update_distribution_configuration(
        self,
        res: "bs_td.UpdateDistributionConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateDistributionConfigurationResponse":
        return dc_td.UpdateDistributionConfigurationResponse.make_one(res)

    def update_image_pipeline(
        self,
        res: "bs_td.UpdateImagePipelineResponseTypeDef",
    ) -> "dc_td.UpdateImagePipelineResponse":
        return dc_td.UpdateImagePipelineResponse.make_one(res)

    def update_infrastructure_configuration(
        self,
        res: "bs_td.UpdateInfrastructureConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateInfrastructureConfigurationResponse":
        return dc_td.UpdateInfrastructureConfigurationResponse.make_one(res)

    def update_lifecycle_policy(
        self,
        res: "bs_td.UpdateLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.UpdateLifecyclePolicyResponse":
        return dc_td.UpdateLifecyclePolicyResponse.make_one(res)


imagebuilder_caster = IMAGEBUILDERCaster()
