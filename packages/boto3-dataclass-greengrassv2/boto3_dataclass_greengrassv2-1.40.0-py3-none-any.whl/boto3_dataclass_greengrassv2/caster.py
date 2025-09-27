# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_greengrassv2 import type_defs as bs_td


class GREENGRASSV2Caster:

    def associate_service_role_to_account(
        self,
        res: "bs_td.AssociateServiceRoleToAccountResponseTypeDef",
    ) -> "dc_td.AssociateServiceRoleToAccountResponse":
        return dc_td.AssociateServiceRoleToAccountResponse.make_one(res)

    def batch_associate_client_device_with_core_device(
        self,
        res: "bs_td.BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    ) -> "dc_td.BatchAssociateClientDeviceWithCoreDeviceResponse":
        return dc_td.BatchAssociateClientDeviceWithCoreDeviceResponse.make_one(res)

    def batch_disassociate_client_device_from_core_device(
        self,
        res: "bs_td.BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    ) -> "dc_td.BatchDisassociateClientDeviceFromCoreDeviceResponse":
        return dc_td.BatchDisassociateClientDeviceFromCoreDeviceResponse.make_one(res)

    def cancel_deployment(
        self,
        res: "bs_td.CancelDeploymentResponseTypeDef",
    ) -> "dc_td.CancelDeploymentResponse":
        return dc_td.CancelDeploymentResponse.make_one(res)

    def create_component_version(
        self,
        res: "bs_td.CreateComponentVersionResponseTypeDef",
    ) -> "dc_td.CreateComponentVersionResponse":
        return dc_td.CreateComponentVersionResponse.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentResponseTypeDef",
    ) -> "dc_td.CreateDeploymentResponse":
        return dc_td.CreateDeploymentResponse.make_one(res)

    def delete_component(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_core_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_deployment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_component(
        self,
        res: "bs_td.DescribeComponentResponseTypeDef",
    ) -> "dc_td.DescribeComponentResponse":
        return dc_td.DescribeComponentResponse.make_one(res)

    def disassociate_service_role_from_account(
        self,
        res: "bs_td.DisassociateServiceRoleFromAccountResponseTypeDef",
    ) -> "dc_td.DisassociateServiceRoleFromAccountResponse":
        return dc_td.DisassociateServiceRoleFromAccountResponse.make_one(res)

    def get_component(
        self,
        res: "bs_td.GetComponentResponseTypeDef",
    ) -> "dc_td.GetComponentResponse":
        return dc_td.GetComponentResponse.make_one(res)

    def get_component_version_artifact(
        self,
        res: "bs_td.GetComponentVersionArtifactResponseTypeDef",
    ) -> "dc_td.GetComponentVersionArtifactResponse":
        return dc_td.GetComponentVersionArtifactResponse.make_one(res)

    def get_connectivity_info(
        self,
        res: "bs_td.GetConnectivityInfoResponseTypeDef",
    ) -> "dc_td.GetConnectivityInfoResponse":
        return dc_td.GetConnectivityInfoResponse.make_one(res)

    def get_core_device(
        self,
        res: "bs_td.GetCoreDeviceResponseTypeDef",
    ) -> "dc_td.GetCoreDeviceResponse":
        return dc_td.GetCoreDeviceResponse.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.GetDeploymentResponseTypeDef",
    ) -> "dc_td.GetDeploymentResponse":
        return dc_td.GetDeploymentResponse.make_one(res)

    def get_service_role_for_account(
        self,
        res: "bs_td.GetServiceRoleForAccountResponseTypeDef",
    ) -> "dc_td.GetServiceRoleForAccountResponse":
        return dc_td.GetServiceRoleForAccountResponse.make_one(res)

    def list_client_devices_associated_with_core_device(
        self,
        res: "bs_td.ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    ) -> "dc_td.ListClientDevicesAssociatedWithCoreDeviceResponse":
        return dc_td.ListClientDevicesAssociatedWithCoreDeviceResponse.make_one(res)

    def list_component_versions(
        self,
        res: "bs_td.ListComponentVersionsResponseTypeDef",
    ) -> "dc_td.ListComponentVersionsResponse":
        return dc_td.ListComponentVersionsResponse.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsResponseTypeDef",
    ) -> "dc_td.ListComponentsResponse":
        return dc_td.ListComponentsResponse.make_one(res)

    def list_core_devices(
        self,
        res: "bs_td.ListCoreDevicesResponseTypeDef",
    ) -> "dc_td.ListCoreDevicesResponse":
        return dc_td.ListCoreDevicesResponse.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.ListDeploymentsResponseTypeDef",
    ) -> "dc_td.ListDeploymentsResponse":
        return dc_td.ListDeploymentsResponse.make_one(res)

    def list_effective_deployments(
        self,
        res: "bs_td.ListEffectiveDeploymentsResponseTypeDef",
    ) -> "dc_td.ListEffectiveDeploymentsResponse":
        return dc_td.ListEffectiveDeploymentsResponse.make_one(res)

    def list_installed_components(
        self,
        res: "bs_td.ListInstalledComponentsResponseTypeDef",
    ) -> "dc_td.ListInstalledComponentsResponse":
        return dc_td.ListInstalledComponentsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def resolve_component_candidates(
        self,
        res: "bs_td.ResolveComponentCandidatesResponseTypeDef",
    ) -> "dc_td.ResolveComponentCandidatesResponse":
        return dc_td.ResolveComponentCandidatesResponse.make_one(res)

    def update_connectivity_info(
        self,
        res: "bs_td.UpdateConnectivityInfoResponseTypeDef",
    ) -> "dc_td.UpdateConnectivityInfoResponse":
        return dc_td.UpdateConnectivityInfoResponse.make_one(res)


greengrassv2_caster = GREENGRASSV2Caster()
