# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_servicecatalog import type_defs as bs_td


class SERVICECATALOGCaster:

    def batch_associate_service_action_with_provisioning_artifact(
        self,
        res: "bs_td.BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    ) -> "dc_td.BatchAssociateServiceActionWithProvisioningArtifactOutput":
        return dc_td.BatchAssociateServiceActionWithProvisioningArtifactOutput.make_one(
            res
        )

    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        res: "bs_td.BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    ) -> "dc_td.BatchDisassociateServiceActionFromProvisioningArtifactOutput":
        return (
            dc_td.BatchDisassociateServiceActionFromProvisioningArtifactOutput.make_one(
                res
            )
        )

    def copy_product(
        self,
        res: "bs_td.CopyProductOutputTypeDef",
    ) -> "dc_td.CopyProductOutput":
        return dc_td.CopyProductOutput.make_one(res)

    def create_constraint(
        self,
        res: "bs_td.CreateConstraintOutputTypeDef",
    ) -> "dc_td.CreateConstraintOutput":
        return dc_td.CreateConstraintOutput.make_one(res)

    def create_portfolio(
        self,
        res: "bs_td.CreatePortfolioOutputTypeDef",
    ) -> "dc_td.CreatePortfolioOutput":
        return dc_td.CreatePortfolioOutput.make_one(res)

    def create_portfolio_share(
        self,
        res: "bs_td.CreatePortfolioShareOutputTypeDef",
    ) -> "dc_td.CreatePortfolioShareOutput":
        return dc_td.CreatePortfolioShareOutput.make_one(res)

    def create_product(
        self,
        res: "bs_td.CreateProductOutputTypeDef",
    ) -> "dc_td.CreateProductOutput":
        return dc_td.CreateProductOutput.make_one(res)

    def create_provisioned_product_plan(
        self,
        res: "bs_td.CreateProvisionedProductPlanOutputTypeDef",
    ) -> "dc_td.CreateProvisionedProductPlanOutput":
        return dc_td.CreateProvisionedProductPlanOutput.make_one(res)

    def create_provisioning_artifact(
        self,
        res: "bs_td.CreateProvisioningArtifactOutputTypeDef",
    ) -> "dc_td.CreateProvisioningArtifactOutput":
        return dc_td.CreateProvisioningArtifactOutput.make_one(res)

    def create_service_action(
        self,
        res: "bs_td.CreateServiceActionOutputTypeDef",
    ) -> "dc_td.CreateServiceActionOutput":
        return dc_td.CreateServiceActionOutput.make_one(res)

    def create_tag_option(
        self,
        res: "bs_td.CreateTagOptionOutputTypeDef",
    ) -> "dc_td.CreateTagOptionOutput":
        return dc_td.CreateTagOptionOutput.make_one(res)

    def delete_portfolio_share(
        self,
        res: "bs_td.DeletePortfolioShareOutputTypeDef",
    ) -> "dc_td.DeletePortfolioShareOutput":
        return dc_td.DeletePortfolioShareOutput.make_one(res)

    def describe_constraint(
        self,
        res: "bs_td.DescribeConstraintOutputTypeDef",
    ) -> "dc_td.DescribeConstraintOutput":
        return dc_td.DescribeConstraintOutput.make_one(res)

    def describe_copy_product_status(
        self,
        res: "bs_td.DescribeCopyProductStatusOutputTypeDef",
    ) -> "dc_td.DescribeCopyProductStatusOutput":
        return dc_td.DescribeCopyProductStatusOutput.make_one(res)

    def describe_portfolio(
        self,
        res: "bs_td.DescribePortfolioOutputTypeDef",
    ) -> "dc_td.DescribePortfolioOutput":
        return dc_td.DescribePortfolioOutput.make_one(res)

    def describe_portfolio_share_status(
        self,
        res: "bs_td.DescribePortfolioShareStatusOutputTypeDef",
    ) -> "dc_td.DescribePortfolioShareStatusOutput":
        return dc_td.DescribePortfolioShareStatusOutput.make_one(res)

    def describe_portfolio_shares(
        self,
        res: "bs_td.DescribePortfolioSharesOutputTypeDef",
    ) -> "dc_td.DescribePortfolioSharesOutput":
        return dc_td.DescribePortfolioSharesOutput.make_one(res)

    def describe_product(
        self,
        res: "bs_td.DescribeProductOutputTypeDef",
    ) -> "dc_td.DescribeProductOutput":
        return dc_td.DescribeProductOutput.make_one(res)

    def describe_product_as_admin(
        self,
        res: "bs_td.DescribeProductAsAdminOutputTypeDef",
    ) -> "dc_td.DescribeProductAsAdminOutput":
        return dc_td.DescribeProductAsAdminOutput.make_one(res)

    def describe_product_view(
        self,
        res: "bs_td.DescribeProductViewOutputTypeDef",
    ) -> "dc_td.DescribeProductViewOutput":
        return dc_td.DescribeProductViewOutput.make_one(res)

    def describe_provisioned_product(
        self,
        res: "bs_td.DescribeProvisionedProductOutputTypeDef",
    ) -> "dc_td.DescribeProvisionedProductOutput":
        return dc_td.DescribeProvisionedProductOutput.make_one(res)

    def describe_provisioned_product_plan(
        self,
        res: "bs_td.DescribeProvisionedProductPlanOutputTypeDef",
    ) -> "dc_td.DescribeProvisionedProductPlanOutput":
        return dc_td.DescribeProvisionedProductPlanOutput.make_one(res)

    def describe_provisioning_artifact(
        self,
        res: "bs_td.DescribeProvisioningArtifactOutputTypeDef",
    ) -> "dc_td.DescribeProvisioningArtifactOutput":
        return dc_td.DescribeProvisioningArtifactOutput.make_one(res)

    def describe_provisioning_parameters(
        self,
        res: "bs_td.DescribeProvisioningParametersOutputTypeDef",
    ) -> "dc_td.DescribeProvisioningParametersOutput":
        return dc_td.DescribeProvisioningParametersOutput.make_one(res)

    def describe_record(
        self,
        res: "bs_td.DescribeRecordOutputTypeDef",
    ) -> "dc_td.DescribeRecordOutput":
        return dc_td.DescribeRecordOutput.make_one(res)

    def describe_service_action(
        self,
        res: "bs_td.DescribeServiceActionOutputTypeDef",
    ) -> "dc_td.DescribeServiceActionOutput":
        return dc_td.DescribeServiceActionOutput.make_one(res)

    def describe_service_action_execution_parameters(
        self,
        res: "bs_td.DescribeServiceActionExecutionParametersOutputTypeDef",
    ) -> "dc_td.DescribeServiceActionExecutionParametersOutput":
        return dc_td.DescribeServiceActionExecutionParametersOutput.make_one(res)

    def describe_tag_option(
        self,
        res: "bs_td.DescribeTagOptionOutputTypeDef",
    ) -> "dc_td.DescribeTagOptionOutput":
        return dc_td.DescribeTagOptionOutput.make_one(res)

    def execute_provisioned_product_plan(
        self,
        res: "bs_td.ExecuteProvisionedProductPlanOutputTypeDef",
    ) -> "dc_td.ExecuteProvisionedProductPlanOutput":
        return dc_td.ExecuteProvisionedProductPlanOutput.make_one(res)

    def execute_provisioned_product_service_action(
        self,
        res: "bs_td.ExecuteProvisionedProductServiceActionOutputTypeDef",
    ) -> "dc_td.ExecuteProvisionedProductServiceActionOutput":
        return dc_td.ExecuteProvisionedProductServiceActionOutput.make_one(res)

    def get_aws_organizations_access_status(
        self,
        res: "bs_td.GetAWSOrganizationsAccessStatusOutputTypeDef",
    ) -> "dc_td.GetAWSOrganizationsAccessStatusOutput":
        return dc_td.GetAWSOrganizationsAccessStatusOutput.make_one(res)

    def get_provisioned_product_outputs(
        self,
        res: "bs_td.GetProvisionedProductOutputsOutputTypeDef",
    ) -> "dc_td.GetProvisionedProductOutputsOutput":
        return dc_td.GetProvisionedProductOutputsOutput.make_one(res)

    def import_as_provisioned_product(
        self,
        res: "bs_td.ImportAsProvisionedProductOutputTypeDef",
    ) -> "dc_td.ImportAsProvisionedProductOutput":
        return dc_td.ImportAsProvisionedProductOutput.make_one(res)

    def list_accepted_portfolio_shares(
        self,
        res: "bs_td.ListAcceptedPortfolioSharesOutputTypeDef",
    ) -> "dc_td.ListAcceptedPortfolioSharesOutput":
        return dc_td.ListAcceptedPortfolioSharesOutput.make_one(res)

    def list_budgets_for_resource(
        self,
        res: "bs_td.ListBudgetsForResourceOutputTypeDef",
    ) -> "dc_td.ListBudgetsForResourceOutput":
        return dc_td.ListBudgetsForResourceOutput.make_one(res)

    def list_constraints_for_portfolio(
        self,
        res: "bs_td.ListConstraintsForPortfolioOutputTypeDef",
    ) -> "dc_td.ListConstraintsForPortfolioOutput":
        return dc_td.ListConstraintsForPortfolioOutput.make_one(res)

    def list_launch_paths(
        self,
        res: "bs_td.ListLaunchPathsOutputTypeDef",
    ) -> "dc_td.ListLaunchPathsOutput":
        return dc_td.ListLaunchPathsOutput.make_one(res)

    def list_organization_portfolio_access(
        self,
        res: "bs_td.ListOrganizationPortfolioAccessOutputTypeDef",
    ) -> "dc_td.ListOrganizationPortfolioAccessOutput":
        return dc_td.ListOrganizationPortfolioAccessOutput.make_one(res)

    def list_portfolio_access(
        self,
        res: "bs_td.ListPortfolioAccessOutputTypeDef",
    ) -> "dc_td.ListPortfolioAccessOutput":
        return dc_td.ListPortfolioAccessOutput.make_one(res)

    def list_portfolios(
        self,
        res: "bs_td.ListPortfoliosOutputTypeDef",
    ) -> "dc_td.ListPortfoliosOutput":
        return dc_td.ListPortfoliosOutput.make_one(res)

    def list_portfolios_for_product(
        self,
        res: "bs_td.ListPortfoliosForProductOutputTypeDef",
    ) -> "dc_td.ListPortfoliosForProductOutput":
        return dc_td.ListPortfoliosForProductOutput.make_one(res)

    def list_principals_for_portfolio(
        self,
        res: "bs_td.ListPrincipalsForPortfolioOutputTypeDef",
    ) -> "dc_td.ListPrincipalsForPortfolioOutput":
        return dc_td.ListPrincipalsForPortfolioOutput.make_one(res)

    def list_provisioned_product_plans(
        self,
        res: "bs_td.ListProvisionedProductPlansOutputTypeDef",
    ) -> "dc_td.ListProvisionedProductPlansOutput":
        return dc_td.ListProvisionedProductPlansOutput.make_one(res)

    def list_provisioning_artifacts(
        self,
        res: "bs_td.ListProvisioningArtifactsOutputTypeDef",
    ) -> "dc_td.ListProvisioningArtifactsOutput":
        return dc_td.ListProvisioningArtifactsOutput.make_one(res)

    def list_provisioning_artifacts_for_service_action(
        self,
        res: "bs_td.ListProvisioningArtifactsForServiceActionOutputTypeDef",
    ) -> "dc_td.ListProvisioningArtifactsForServiceActionOutput":
        return dc_td.ListProvisioningArtifactsForServiceActionOutput.make_one(res)

    def list_record_history(
        self,
        res: "bs_td.ListRecordHistoryOutputTypeDef",
    ) -> "dc_td.ListRecordHistoryOutput":
        return dc_td.ListRecordHistoryOutput.make_one(res)

    def list_resources_for_tag_option(
        self,
        res: "bs_td.ListResourcesForTagOptionOutputTypeDef",
    ) -> "dc_td.ListResourcesForTagOptionOutput":
        return dc_td.ListResourcesForTagOptionOutput.make_one(res)

    def list_service_actions(
        self,
        res: "bs_td.ListServiceActionsOutputTypeDef",
    ) -> "dc_td.ListServiceActionsOutput":
        return dc_td.ListServiceActionsOutput.make_one(res)

    def list_service_actions_for_provisioning_artifact(
        self,
        res: "bs_td.ListServiceActionsForProvisioningArtifactOutputTypeDef",
    ) -> "dc_td.ListServiceActionsForProvisioningArtifactOutput":
        return dc_td.ListServiceActionsForProvisioningArtifactOutput.make_one(res)

    def list_stack_instances_for_provisioned_product(
        self,
        res: "bs_td.ListStackInstancesForProvisionedProductOutputTypeDef",
    ) -> "dc_td.ListStackInstancesForProvisionedProductOutput":
        return dc_td.ListStackInstancesForProvisionedProductOutput.make_one(res)

    def list_tag_options(
        self,
        res: "bs_td.ListTagOptionsOutputTypeDef",
    ) -> "dc_td.ListTagOptionsOutput":
        return dc_td.ListTagOptionsOutput.make_one(res)

    def provision_product(
        self,
        res: "bs_td.ProvisionProductOutputTypeDef",
    ) -> "dc_td.ProvisionProductOutput":
        return dc_td.ProvisionProductOutput.make_one(res)

    def scan_provisioned_products(
        self,
        res: "bs_td.ScanProvisionedProductsOutputTypeDef",
    ) -> "dc_td.ScanProvisionedProductsOutput":
        return dc_td.ScanProvisionedProductsOutput.make_one(res)

    def search_products(
        self,
        res: "bs_td.SearchProductsOutputTypeDef",
    ) -> "dc_td.SearchProductsOutput":
        return dc_td.SearchProductsOutput.make_one(res)

    def search_products_as_admin(
        self,
        res: "bs_td.SearchProductsAsAdminOutputTypeDef",
    ) -> "dc_td.SearchProductsAsAdminOutput":
        return dc_td.SearchProductsAsAdminOutput.make_one(res)

    def search_provisioned_products(
        self,
        res: "bs_td.SearchProvisionedProductsOutputTypeDef",
    ) -> "dc_td.SearchProvisionedProductsOutput":
        return dc_td.SearchProvisionedProductsOutput.make_one(res)

    def terminate_provisioned_product(
        self,
        res: "bs_td.TerminateProvisionedProductOutputTypeDef",
    ) -> "dc_td.TerminateProvisionedProductOutput":
        return dc_td.TerminateProvisionedProductOutput.make_one(res)

    def update_constraint(
        self,
        res: "bs_td.UpdateConstraintOutputTypeDef",
    ) -> "dc_td.UpdateConstraintOutput":
        return dc_td.UpdateConstraintOutput.make_one(res)

    def update_portfolio(
        self,
        res: "bs_td.UpdatePortfolioOutputTypeDef",
    ) -> "dc_td.UpdatePortfolioOutput":
        return dc_td.UpdatePortfolioOutput.make_one(res)

    def update_portfolio_share(
        self,
        res: "bs_td.UpdatePortfolioShareOutputTypeDef",
    ) -> "dc_td.UpdatePortfolioShareOutput":
        return dc_td.UpdatePortfolioShareOutput.make_one(res)

    def update_product(
        self,
        res: "bs_td.UpdateProductOutputTypeDef",
    ) -> "dc_td.UpdateProductOutput":
        return dc_td.UpdateProductOutput.make_one(res)

    def update_provisioned_product(
        self,
        res: "bs_td.UpdateProvisionedProductOutputTypeDef",
    ) -> "dc_td.UpdateProvisionedProductOutput":
        return dc_td.UpdateProvisionedProductOutput.make_one(res)

    def update_provisioned_product_properties(
        self,
        res: "bs_td.UpdateProvisionedProductPropertiesOutputTypeDef",
    ) -> "dc_td.UpdateProvisionedProductPropertiesOutput":
        return dc_td.UpdateProvisionedProductPropertiesOutput.make_one(res)

    def update_provisioning_artifact(
        self,
        res: "bs_td.UpdateProvisioningArtifactOutputTypeDef",
    ) -> "dc_td.UpdateProvisioningArtifactOutput":
        return dc_td.UpdateProvisioningArtifactOutput.make_one(res)

    def update_service_action(
        self,
        res: "bs_td.UpdateServiceActionOutputTypeDef",
    ) -> "dc_td.UpdateServiceActionOutput":
        return dc_td.UpdateServiceActionOutput.make_one(res)

    def update_tag_option(
        self,
        res: "bs_td.UpdateTagOptionOutputTypeDef",
    ) -> "dc_td.UpdateTagOptionOutput":
        return dc_td.UpdateTagOptionOutput.make_one(res)


servicecatalog_caster = SERVICECATALOGCaster()
