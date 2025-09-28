# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_tnb import type_defs as bs_td


class TNBCaster:

    def cancel_sol_network_operation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_sol_function_package(
        self,
        res: "bs_td.CreateSolFunctionPackageOutputTypeDef",
    ) -> "dc_td.CreateSolFunctionPackageOutput":
        return dc_td.CreateSolFunctionPackageOutput.make_one(res)

    def create_sol_network_instance(
        self,
        res: "bs_td.CreateSolNetworkInstanceOutputTypeDef",
    ) -> "dc_td.CreateSolNetworkInstanceOutput":
        return dc_td.CreateSolNetworkInstanceOutput.make_one(res)

    def create_sol_network_package(
        self,
        res: "bs_td.CreateSolNetworkPackageOutputTypeDef",
    ) -> "dc_td.CreateSolNetworkPackageOutput":
        return dc_td.CreateSolNetworkPackageOutput.make_one(res)

    def delete_sol_function_package(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_sol_network_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_sol_network_package(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_sol_function_instance(
        self,
        res: "bs_td.GetSolFunctionInstanceOutputTypeDef",
    ) -> "dc_td.GetSolFunctionInstanceOutput":
        return dc_td.GetSolFunctionInstanceOutput.make_one(res)

    def get_sol_function_package(
        self,
        res: "bs_td.GetSolFunctionPackageOutputTypeDef",
    ) -> "dc_td.GetSolFunctionPackageOutput":
        return dc_td.GetSolFunctionPackageOutput.make_one(res)

    def get_sol_function_package_content(
        self,
        res: "bs_td.GetSolFunctionPackageContentOutputTypeDef",
    ) -> "dc_td.GetSolFunctionPackageContentOutput":
        return dc_td.GetSolFunctionPackageContentOutput.make_one(res)

    def get_sol_function_package_descriptor(
        self,
        res: "bs_td.GetSolFunctionPackageDescriptorOutputTypeDef",
    ) -> "dc_td.GetSolFunctionPackageDescriptorOutput":
        return dc_td.GetSolFunctionPackageDescriptorOutput.make_one(res)

    def get_sol_network_instance(
        self,
        res: "bs_td.GetSolNetworkInstanceOutputTypeDef",
    ) -> "dc_td.GetSolNetworkInstanceOutput":
        return dc_td.GetSolNetworkInstanceOutput.make_one(res)

    def get_sol_network_operation(
        self,
        res: "bs_td.GetSolNetworkOperationOutputTypeDef",
    ) -> "dc_td.GetSolNetworkOperationOutput":
        return dc_td.GetSolNetworkOperationOutput.make_one(res)

    def get_sol_network_package(
        self,
        res: "bs_td.GetSolNetworkPackageOutputTypeDef",
    ) -> "dc_td.GetSolNetworkPackageOutput":
        return dc_td.GetSolNetworkPackageOutput.make_one(res)

    def get_sol_network_package_content(
        self,
        res: "bs_td.GetSolNetworkPackageContentOutputTypeDef",
    ) -> "dc_td.GetSolNetworkPackageContentOutput":
        return dc_td.GetSolNetworkPackageContentOutput.make_one(res)

    def get_sol_network_package_descriptor(
        self,
        res: "bs_td.GetSolNetworkPackageDescriptorOutputTypeDef",
    ) -> "dc_td.GetSolNetworkPackageDescriptorOutput":
        return dc_td.GetSolNetworkPackageDescriptorOutput.make_one(res)

    def instantiate_sol_network_instance(
        self,
        res: "bs_td.InstantiateSolNetworkInstanceOutputTypeDef",
    ) -> "dc_td.InstantiateSolNetworkInstanceOutput":
        return dc_td.InstantiateSolNetworkInstanceOutput.make_one(res)

    def list_sol_function_instances(
        self,
        res: "bs_td.ListSolFunctionInstancesOutputTypeDef",
    ) -> "dc_td.ListSolFunctionInstancesOutput":
        return dc_td.ListSolFunctionInstancesOutput.make_one(res)

    def list_sol_function_packages(
        self,
        res: "bs_td.ListSolFunctionPackagesOutputTypeDef",
    ) -> "dc_td.ListSolFunctionPackagesOutput":
        return dc_td.ListSolFunctionPackagesOutput.make_one(res)

    def list_sol_network_instances(
        self,
        res: "bs_td.ListSolNetworkInstancesOutputTypeDef",
    ) -> "dc_td.ListSolNetworkInstancesOutput":
        return dc_td.ListSolNetworkInstancesOutput.make_one(res)

    def list_sol_network_operations(
        self,
        res: "bs_td.ListSolNetworkOperationsOutputTypeDef",
    ) -> "dc_td.ListSolNetworkOperationsOutput":
        return dc_td.ListSolNetworkOperationsOutput.make_one(res)

    def list_sol_network_packages(
        self,
        res: "bs_td.ListSolNetworkPackagesOutputTypeDef",
    ) -> "dc_td.ListSolNetworkPackagesOutput":
        return dc_td.ListSolNetworkPackagesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_sol_function_package_content(
        self,
        res: "bs_td.PutSolFunctionPackageContentOutputTypeDef",
    ) -> "dc_td.PutSolFunctionPackageContentOutput":
        return dc_td.PutSolFunctionPackageContentOutput.make_one(res)

    def put_sol_network_package_content(
        self,
        res: "bs_td.PutSolNetworkPackageContentOutputTypeDef",
    ) -> "dc_td.PutSolNetworkPackageContentOutput":
        return dc_td.PutSolNetworkPackageContentOutput.make_one(res)

    def terminate_sol_network_instance(
        self,
        res: "bs_td.TerminateSolNetworkInstanceOutputTypeDef",
    ) -> "dc_td.TerminateSolNetworkInstanceOutput":
        return dc_td.TerminateSolNetworkInstanceOutput.make_one(res)

    def update_sol_function_package(
        self,
        res: "bs_td.UpdateSolFunctionPackageOutputTypeDef",
    ) -> "dc_td.UpdateSolFunctionPackageOutput":
        return dc_td.UpdateSolFunctionPackageOutput.make_one(res)

    def update_sol_network_instance(
        self,
        res: "bs_td.UpdateSolNetworkInstanceOutputTypeDef",
    ) -> "dc_td.UpdateSolNetworkInstanceOutput":
        return dc_td.UpdateSolNetworkInstanceOutput.make_one(res)

    def update_sol_network_package(
        self,
        res: "bs_td.UpdateSolNetworkPackageOutputTypeDef",
    ) -> "dc_td.UpdateSolNetworkPackageOutput":
        return dc_td.UpdateSolNetworkPackageOutput.make_one(res)

    def validate_sol_function_package_content(
        self,
        res: "bs_td.ValidateSolFunctionPackageContentOutputTypeDef",
    ) -> "dc_td.ValidateSolFunctionPackageContentOutput":
        return dc_td.ValidateSolFunctionPackageContentOutput.make_one(res)

    def validate_sol_network_package_content(
        self,
        res: "bs_td.ValidateSolNetworkPackageContentOutputTypeDef",
    ) -> "dc_td.ValidateSolNetworkPackageContentOutput":
        return dc_td.ValidateSolNetworkPackageContentOutput.make_one(res)


tnb_caster = TNBCaster()
