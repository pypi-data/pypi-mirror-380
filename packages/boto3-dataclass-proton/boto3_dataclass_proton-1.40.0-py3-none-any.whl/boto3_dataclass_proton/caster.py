# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_proton import type_defs as bs_td


class PROTONCaster:

    def accept_environment_account_connection(
        self,
        res: "bs_td.AcceptEnvironmentAccountConnectionOutputTypeDef",
    ) -> "dc_td.AcceptEnvironmentAccountConnectionOutput":
        return dc_td.AcceptEnvironmentAccountConnectionOutput.make_one(res)

    def cancel_component_deployment(
        self,
        res: "bs_td.CancelComponentDeploymentOutputTypeDef",
    ) -> "dc_td.CancelComponentDeploymentOutput":
        return dc_td.CancelComponentDeploymentOutput.make_one(res)

    def cancel_environment_deployment(
        self,
        res: "bs_td.CancelEnvironmentDeploymentOutputTypeDef",
    ) -> "dc_td.CancelEnvironmentDeploymentOutput":
        return dc_td.CancelEnvironmentDeploymentOutput.make_one(res)

    def cancel_service_instance_deployment(
        self,
        res: "bs_td.CancelServiceInstanceDeploymentOutputTypeDef",
    ) -> "dc_td.CancelServiceInstanceDeploymentOutput":
        return dc_td.CancelServiceInstanceDeploymentOutput.make_one(res)

    def cancel_service_pipeline_deployment(
        self,
        res: "bs_td.CancelServicePipelineDeploymentOutputTypeDef",
    ) -> "dc_td.CancelServicePipelineDeploymentOutput":
        return dc_td.CancelServicePipelineDeploymentOutput.make_one(res)

    def create_component(
        self,
        res: "bs_td.CreateComponentOutputTypeDef",
    ) -> "dc_td.CreateComponentOutput":
        return dc_td.CreateComponentOutput.make_one(res)

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentOutput":
        return dc_td.CreateEnvironmentOutput.make_one(res)

    def create_environment_account_connection(
        self,
        res: "bs_td.CreateEnvironmentAccountConnectionOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentAccountConnectionOutput":
        return dc_td.CreateEnvironmentAccountConnectionOutput.make_one(res)

    def create_environment_template(
        self,
        res: "bs_td.CreateEnvironmentTemplateOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentTemplateOutput":
        return dc_td.CreateEnvironmentTemplateOutput.make_one(res)

    def create_environment_template_version(
        self,
        res: "bs_td.CreateEnvironmentTemplateVersionOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentTemplateVersionOutput":
        return dc_td.CreateEnvironmentTemplateVersionOutput.make_one(res)

    def create_repository(
        self,
        res: "bs_td.CreateRepositoryOutputTypeDef",
    ) -> "dc_td.CreateRepositoryOutput":
        return dc_td.CreateRepositoryOutput.make_one(res)

    def create_service(
        self,
        res: "bs_td.CreateServiceOutputTypeDef",
    ) -> "dc_td.CreateServiceOutput":
        return dc_td.CreateServiceOutput.make_one(res)

    def create_service_instance(
        self,
        res: "bs_td.CreateServiceInstanceOutputTypeDef",
    ) -> "dc_td.CreateServiceInstanceOutput":
        return dc_td.CreateServiceInstanceOutput.make_one(res)

    def create_service_sync_config(
        self,
        res: "bs_td.CreateServiceSyncConfigOutputTypeDef",
    ) -> "dc_td.CreateServiceSyncConfigOutput":
        return dc_td.CreateServiceSyncConfigOutput.make_one(res)

    def create_service_template(
        self,
        res: "bs_td.CreateServiceTemplateOutputTypeDef",
    ) -> "dc_td.CreateServiceTemplateOutput":
        return dc_td.CreateServiceTemplateOutput.make_one(res)

    def create_service_template_version(
        self,
        res: "bs_td.CreateServiceTemplateVersionOutputTypeDef",
    ) -> "dc_td.CreateServiceTemplateVersionOutput":
        return dc_td.CreateServiceTemplateVersionOutput.make_one(res)

    def create_template_sync_config(
        self,
        res: "bs_td.CreateTemplateSyncConfigOutputTypeDef",
    ) -> "dc_td.CreateTemplateSyncConfigOutput":
        return dc_td.CreateTemplateSyncConfigOutput.make_one(res)

    def delete_component(
        self,
        res: "bs_td.DeleteComponentOutputTypeDef",
    ) -> "dc_td.DeleteComponentOutput":
        return dc_td.DeleteComponentOutput.make_one(res)

    def delete_deployment(
        self,
        res: "bs_td.DeleteDeploymentOutputTypeDef",
    ) -> "dc_td.DeleteDeploymentOutput":
        return dc_td.DeleteDeploymentOutput.make_one(res)

    def delete_environment(
        self,
        res: "bs_td.DeleteEnvironmentOutputTypeDef",
    ) -> "dc_td.DeleteEnvironmentOutput":
        return dc_td.DeleteEnvironmentOutput.make_one(res)

    def delete_environment_account_connection(
        self,
        res: "bs_td.DeleteEnvironmentAccountConnectionOutputTypeDef",
    ) -> "dc_td.DeleteEnvironmentAccountConnectionOutput":
        return dc_td.DeleteEnvironmentAccountConnectionOutput.make_one(res)

    def delete_environment_template(
        self,
        res: "bs_td.DeleteEnvironmentTemplateOutputTypeDef",
    ) -> "dc_td.DeleteEnvironmentTemplateOutput":
        return dc_td.DeleteEnvironmentTemplateOutput.make_one(res)

    def delete_environment_template_version(
        self,
        res: "bs_td.DeleteEnvironmentTemplateVersionOutputTypeDef",
    ) -> "dc_td.DeleteEnvironmentTemplateVersionOutput":
        return dc_td.DeleteEnvironmentTemplateVersionOutput.make_one(res)

    def delete_repository(
        self,
        res: "bs_td.DeleteRepositoryOutputTypeDef",
    ) -> "dc_td.DeleteRepositoryOutput":
        return dc_td.DeleteRepositoryOutput.make_one(res)

    def delete_service(
        self,
        res: "bs_td.DeleteServiceOutputTypeDef",
    ) -> "dc_td.DeleteServiceOutput":
        return dc_td.DeleteServiceOutput.make_one(res)

    def delete_service_sync_config(
        self,
        res: "bs_td.DeleteServiceSyncConfigOutputTypeDef",
    ) -> "dc_td.DeleteServiceSyncConfigOutput":
        return dc_td.DeleteServiceSyncConfigOutput.make_one(res)

    def delete_service_template(
        self,
        res: "bs_td.DeleteServiceTemplateOutputTypeDef",
    ) -> "dc_td.DeleteServiceTemplateOutput":
        return dc_td.DeleteServiceTemplateOutput.make_one(res)

    def delete_service_template_version(
        self,
        res: "bs_td.DeleteServiceTemplateVersionOutputTypeDef",
    ) -> "dc_td.DeleteServiceTemplateVersionOutput":
        return dc_td.DeleteServiceTemplateVersionOutput.make_one(res)

    def delete_template_sync_config(
        self,
        res: "bs_td.DeleteTemplateSyncConfigOutputTypeDef",
    ) -> "dc_td.DeleteTemplateSyncConfigOutput":
        return dc_td.DeleteTemplateSyncConfigOutput.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsOutputTypeDef",
    ) -> "dc_td.GetAccountSettingsOutput":
        return dc_td.GetAccountSettingsOutput.make_one(res)

    def get_component(
        self,
        res: "bs_td.GetComponentOutputTypeDef",
    ) -> "dc_td.GetComponentOutput":
        return dc_td.GetComponentOutput.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.GetDeploymentOutputTypeDef",
    ) -> "dc_td.GetDeploymentOutput":
        return dc_td.GetDeploymentOutput.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentOutputTypeDef",
    ) -> "dc_td.GetEnvironmentOutput":
        return dc_td.GetEnvironmentOutput.make_one(res)

    def get_environment_account_connection(
        self,
        res: "bs_td.GetEnvironmentAccountConnectionOutputTypeDef",
    ) -> "dc_td.GetEnvironmentAccountConnectionOutput":
        return dc_td.GetEnvironmentAccountConnectionOutput.make_one(res)

    def get_environment_template(
        self,
        res: "bs_td.GetEnvironmentTemplateOutputTypeDef",
    ) -> "dc_td.GetEnvironmentTemplateOutput":
        return dc_td.GetEnvironmentTemplateOutput.make_one(res)

    def get_environment_template_version(
        self,
        res: "bs_td.GetEnvironmentTemplateVersionOutputTypeDef",
    ) -> "dc_td.GetEnvironmentTemplateVersionOutput":
        return dc_td.GetEnvironmentTemplateVersionOutput.make_one(res)

    def get_repository(
        self,
        res: "bs_td.GetRepositoryOutputTypeDef",
    ) -> "dc_td.GetRepositoryOutput":
        return dc_td.GetRepositoryOutput.make_one(res)

    def get_repository_sync_status(
        self,
        res: "bs_td.GetRepositorySyncStatusOutputTypeDef",
    ) -> "dc_td.GetRepositorySyncStatusOutput":
        return dc_td.GetRepositorySyncStatusOutput.make_one(res)

    def get_resources_summary(
        self,
        res: "bs_td.GetResourcesSummaryOutputTypeDef",
    ) -> "dc_td.GetResourcesSummaryOutput":
        return dc_td.GetResourcesSummaryOutput.make_one(res)

    def get_service(
        self,
        res: "bs_td.GetServiceOutputTypeDef",
    ) -> "dc_td.GetServiceOutput":
        return dc_td.GetServiceOutput.make_one(res)

    def get_service_instance(
        self,
        res: "bs_td.GetServiceInstanceOutputTypeDef",
    ) -> "dc_td.GetServiceInstanceOutput":
        return dc_td.GetServiceInstanceOutput.make_one(res)

    def get_service_instance_sync_status(
        self,
        res: "bs_td.GetServiceInstanceSyncStatusOutputTypeDef",
    ) -> "dc_td.GetServiceInstanceSyncStatusOutput":
        return dc_td.GetServiceInstanceSyncStatusOutput.make_one(res)

    def get_service_sync_blocker_summary(
        self,
        res: "bs_td.GetServiceSyncBlockerSummaryOutputTypeDef",
    ) -> "dc_td.GetServiceSyncBlockerSummaryOutput":
        return dc_td.GetServiceSyncBlockerSummaryOutput.make_one(res)

    def get_service_sync_config(
        self,
        res: "bs_td.GetServiceSyncConfigOutputTypeDef",
    ) -> "dc_td.GetServiceSyncConfigOutput":
        return dc_td.GetServiceSyncConfigOutput.make_one(res)

    def get_service_template(
        self,
        res: "bs_td.GetServiceTemplateOutputTypeDef",
    ) -> "dc_td.GetServiceTemplateOutput":
        return dc_td.GetServiceTemplateOutput.make_one(res)

    def get_service_template_version(
        self,
        res: "bs_td.GetServiceTemplateVersionOutputTypeDef",
    ) -> "dc_td.GetServiceTemplateVersionOutput":
        return dc_td.GetServiceTemplateVersionOutput.make_one(res)

    def get_template_sync_config(
        self,
        res: "bs_td.GetTemplateSyncConfigOutputTypeDef",
    ) -> "dc_td.GetTemplateSyncConfigOutput":
        return dc_td.GetTemplateSyncConfigOutput.make_one(res)

    def get_template_sync_status(
        self,
        res: "bs_td.GetTemplateSyncStatusOutputTypeDef",
    ) -> "dc_td.GetTemplateSyncStatusOutput":
        return dc_td.GetTemplateSyncStatusOutput.make_one(res)

    def list_component_outputs(
        self,
        res: "bs_td.ListComponentOutputsOutputTypeDef",
    ) -> "dc_td.ListComponentOutputsOutput":
        return dc_td.ListComponentOutputsOutput.make_one(res)

    def list_component_provisioned_resources(
        self,
        res: "bs_td.ListComponentProvisionedResourcesOutputTypeDef",
    ) -> "dc_td.ListComponentProvisionedResourcesOutput":
        return dc_td.ListComponentProvisionedResourcesOutput.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsOutputTypeDef",
    ) -> "dc_td.ListComponentsOutput":
        return dc_td.ListComponentsOutput.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.ListDeploymentsOutputTypeDef",
    ) -> "dc_td.ListDeploymentsOutput":
        return dc_td.ListDeploymentsOutput.make_one(res)

    def list_environment_account_connections(
        self,
        res: "bs_td.ListEnvironmentAccountConnectionsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentAccountConnectionsOutput":
        return dc_td.ListEnvironmentAccountConnectionsOutput.make_one(res)

    def list_environment_outputs(
        self,
        res: "bs_td.ListEnvironmentOutputsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentOutputsOutput":
        return dc_td.ListEnvironmentOutputsOutput.make_one(res)

    def list_environment_provisioned_resources(
        self,
        res: "bs_td.ListEnvironmentProvisionedResourcesOutputTypeDef",
    ) -> "dc_td.ListEnvironmentProvisionedResourcesOutput":
        return dc_td.ListEnvironmentProvisionedResourcesOutput.make_one(res)

    def list_environment_template_versions(
        self,
        res: "bs_td.ListEnvironmentTemplateVersionsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentTemplateVersionsOutput":
        return dc_td.ListEnvironmentTemplateVersionsOutput.make_one(res)

    def list_environment_templates(
        self,
        res: "bs_td.ListEnvironmentTemplatesOutputTypeDef",
    ) -> "dc_td.ListEnvironmentTemplatesOutput":
        return dc_td.ListEnvironmentTemplatesOutput.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentsOutput":
        return dc_td.ListEnvironmentsOutput.make_one(res)

    def list_repositories(
        self,
        res: "bs_td.ListRepositoriesOutputTypeDef",
    ) -> "dc_td.ListRepositoriesOutput":
        return dc_td.ListRepositoriesOutput.make_one(res)

    def list_repository_sync_definitions(
        self,
        res: "bs_td.ListRepositorySyncDefinitionsOutputTypeDef",
    ) -> "dc_td.ListRepositorySyncDefinitionsOutput":
        return dc_td.ListRepositorySyncDefinitionsOutput.make_one(res)

    def list_service_instance_outputs(
        self,
        res: "bs_td.ListServiceInstanceOutputsOutputTypeDef",
    ) -> "dc_td.ListServiceInstanceOutputsOutput":
        return dc_td.ListServiceInstanceOutputsOutput.make_one(res)

    def list_service_instance_provisioned_resources(
        self,
        res: "bs_td.ListServiceInstanceProvisionedResourcesOutputTypeDef",
    ) -> "dc_td.ListServiceInstanceProvisionedResourcesOutput":
        return dc_td.ListServiceInstanceProvisionedResourcesOutput.make_one(res)

    def list_service_instances(
        self,
        res: "bs_td.ListServiceInstancesOutputTypeDef",
    ) -> "dc_td.ListServiceInstancesOutput":
        return dc_td.ListServiceInstancesOutput.make_one(res)

    def list_service_pipeline_outputs(
        self,
        res: "bs_td.ListServicePipelineOutputsOutputTypeDef",
    ) -> "dc_td.ListServicePipelineOutputsOutput":
        return dc_td.ListServicePipelineOutputsOutput.make_one(res)

    def list_service_pipeline_provisioned_resources(
        self,
        res: "bs_td.ListServicePipelineProvisionedResourcesOutputTypeDef",
    ) -> "dc_td.ListServicePipelineProvisionedResourcesOutput":
        return dc_td.ListServicePipelineProvisionedResourcesOutput.make_one(res)

    def list_service_template_versions(
        self,
        res: "bs_td.ListServiceTemplateVersionsOutputTypeDef",
    ) -> "dc_td.ListServiceTemplateVersionsOutput":
        return dc_td.ListServiceTemplateVersionsOutput.make_one(res)

    def list_service_templates(
        self,
        res: "bs_td.ListServiceTemplatesOutputTypeDef",
    ) -> "dc_td.ListServiceTemplatesOutput":
        return dc_td.ListServiceTemplatesOutput.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesOutputTypeDef",
    ) -> "dc_td.ListServicesOutput":
        return dc_td.ListServicesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def reject_environment_account_connection(
        self,
        res: "bs_td.RejectEnvironmentAccountConnectionOutputTypeDef",
    ) -> "dc_td.RejectEnvironmentAccountConnectionOutput":
        return dc_td.RejectEnvironmentAccountConnectionOutput.make_one(res)

    def update_account_settings(
        self,
        res: "bs_td.UpdateAccountSettingsOutputTypeDef",
    ) -> "dc_td.UpdateAccountSettingsOutput":
        return dc_td.UpdateAccountSettingsOutput.make_one(res)

    def update_component(
        self,
        res: "bs_td.UpdateComponentOutputTypeDef",
    ) -> "dc_td.UpdateComponentOutput":
        return dc_td.UpdateComponentOutput.make_one(res)

    def update_environment(
        self,
        res: "bs_td.UpdateEnvironmentOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentOutput":
        return dc_td.UpdateEnvironmentOutput.make_one(res)

    def update_environment_account_connection(
        self,
        res: "bs_td.UpdateEnvironmentAccountConnectionOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentAccountConnectionOutput":
        return dc_td.UpdateEnvironmentAccountConnectionOutput.make_one(res)

    def update_environment_template(
        self,
        res: "bs_td.UpdateEnvironmentTemplateOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentTemplateOutput":
        return dc_td.UpdateEnvironmentTemplateOutput.make_one(res)

    def update_environment_template_version(
        self,
        res: "bs_td.UpdateEnvironmentTemplateVersionOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentTemplateVersionOutput":
        return dc_td.UpdateEnvironmentTemplateVersionOutput.make_one(res)

    def update_service(
        self,
        res: "bs_td.UpdateServiceOutputTypeDef",
    ) -> "dc_td.UpdateServiceOutput":
        return dc_td.UpdateServiceOutput.make_one(res)

    def update_service_instance(
        self,
        res: "bs_td.UpdateServiceInstanceOutputTypeDef",
    ) -> "dc_td.UpdateServiceInstanceOutput":
        return dc_td.UpdateServiceInstanceOutput.make_one(res)

    def update_service_pipeline(
        self,
        res: "bs_td.UpdateServicePipelineOutputTypeDef",
    ) -> "dc_td.UpdateServicePipelineOutput":
        return dc_td.UpdateServicePipelineOutput.make_one(res)

    def update_service_sync_blocker(
        self,
        res: "bs_td.UpdateServiceSyncBlockerOutputTypeDef",
    ) -> "dc_td.UpdateServiceSyncBlockerOutput":
        return dc_td.UpdateServiceSyncBlockerOutput.make_one(res)

    def update_service_sync_config(
        self,
        res: "bs_td.UpdateServiceSyncConfigOutputTypeDef",
    ) -> "dc_td.UpdateServiceSyncConfigOutput":
        return dc_td.UpdateServiceSyncConfigOutput.make_one(res)

    def update_service_template(
        self,
        res: "bs_td.UpdateServiceTemplateOutputTypeDef",
    ) -> "dc_td.UpdateServiceTemplateOutput":
        return dc_td.UpdateServiceTemplateOutput.make_one(res)

    def update_service_template_version(
        self,
        res: "bs_td.UpdateServiceTemplateVersionOutputTypeDef",
    ) -> "dc_td.UpdateServiceTemplateVersionOutput":
        return dc_td.UpdateServiceTemplateVersionOutput.make_one(res)

    def update_template_sync_config(
        self,
        res: "bs_td.UpdateTemplateSyncConfigOutputTypeDef",
    ) -> "dc_td.UpdateTemplateSyncConfigOutput":
        return dc_td.UpdateTemplateSyncConfigOutput.make_one(res)


proton_caster = PROTONCaster()
