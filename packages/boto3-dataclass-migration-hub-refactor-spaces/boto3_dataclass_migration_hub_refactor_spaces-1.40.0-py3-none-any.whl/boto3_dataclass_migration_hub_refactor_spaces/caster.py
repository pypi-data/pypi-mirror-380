# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migration_hub_refactor_spaces import type_defs as bs_td


class MIGRATION_HUB_REFACTOR_SPACESCaster:

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateEnvironmentResponse":
        return dc_td.CreateEnvironmentResponse.make_one(res)

    def create_route(
        self,
        res: "bs_td.CreateRouteResponseTypeDef",
    ) -> "dc_td.CreateRouteResponse":
        return dc_td.CreateRouteResponse.make_one(res)

    def create_service(
        self,
        res: "bs_td.CreateServiceResponseTypeDef",
    ) -> "dc_td.CreateServiceResponse":
        return dc_td.CreateServiceResponse.make_one(res)

    def delete_application(
        self,
        res: "bs_td.DeleteApplicationResponseTypeDef",
    ) -> "dc_td.DeleteApplicationResponse":
        return dc_td.DeleteApplicationResponse.make_one(res)

    def delete_environment(
        self,
        res: "bs_td.DeleteEnvironmentResponseTypeDef",
    ) -> "dc_td.DeleteEnvironmentResponse":
        return dc_td.DeleteEnvironmentResponse.make_one(res)

    def delete_route(
        self,
        res: "bs_td.DeleteRouteResponseTypeDef",
    ) -> "dc_td.DeleteRouteResponse":
        return dc_td.DeleteRouteResponse.make_one(res)

    def delete_service(
        self,
        res: "bs_td.DeleteServiceResponseTypeDef",
    ) -> "dc_td.DeleteServiceResponse":
        return dc_td.DeleteServiceResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentResponseTypeDef",
    ) -> "dc_td.GetEnvironmentResponse":
        return dc_td.GetEnvironmentResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_route(
        self,
        res: "bs_td.GetRouteResponseTypeDef",
    ) -> "dc_td.GetRouteResponse":
        return dc_td.GetRouteResponse.make_one(res)

    def get_service(
        self,
        res: "bs_td.GetServiceResponseTypeDef",
    ) -> "dc_td.GetServiceResponse":
        return dc_td.GetServiceResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_environment_vpcs(
        self,
        res: "bs_td.ListEnvironmentVpcsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentVpcsResponse":
        return dc_td.ListEnvironmentVpcsResponse.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentsResponse":
        return dc_td.ListEnvironmentsResponse.make_one(res)

    def list_routes(
        self,
        res: "bs_td.ListRoutesResponseTypeDef",
    ) -> "dc_td.ListRoutesResponse":
        return dc_td.ListRoutesResponse.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesResponseTypeDef",
    ) -> "dc_td.ListServicesResponse":
        return dc_td.ListServicesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_route(
        self,
        res: "bs_td.UpdateRouteResponseTypeDef",
    ) -> "dc_td.UpdateRouteResponse":
        return dc_td.UpdateRouteResponse.make_one(res)


migration_hub_refactor_spaces_caster = MIGRATION_HUB_REFACTOR_SPACESCaster()
