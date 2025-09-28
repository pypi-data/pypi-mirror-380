# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_license_manager_user_subscriptions import type_defs as bs_td


class LICENSE_MANAGER_USER_SUBSCRIPTIONSCaster:

    def associate_user(
        self,
        res: "bs_td.AssociateUserResponseTypeDef",
    ) -> "dc_td.AssociateUserResponse":
        return dc_td.AssociateUserResponse.make_one(res)

    def create_license_server_endpoint(
        self,
        res: "bs_td.CreateLicenseServerEndpointResponseTypeDef",
    ) -> "dc_td.CreateLicenseServerEndpointResponse":
        return dc_td.CreateLicenseServerEndpointResponse.make_one(res)

    def delete_license_server_endpoint(
        self,
        res: "bs_td.DeleteLicenseServerEndpointResponseTypeDef",
    ) -> "dc_td.DeleteLicenseServerEndpointResponse":
        return dc_td.DeleteLicenseServerEndpointResponse.make_one(res)

    def deregister_identity_provider(
        self,
        res: "bs_td.DeregisterIdentityProviderResponseTypeDef",
    ) -> "dc_td.DeregisterIdentityProviderResponse":
        return dc_td.DeregisterIdentityProviderResponse.make_one(res)

    def disassociate_user(
        self,
        res: "bs_td.DisassociateUserResponseTypeDef",
    ) -> "dc_td.DisassociateUserResponse":
        return dc_td.DisassociateUserResponse.make_one(res)

    def list_identity_providers(
        self,
        res: "bs_td.ListIdentityProvidersResponseTypeDef",
    ) -> "dc_td.ListIdentityProvidersResponse":
        return dc_td.ListIdentityProvidersResponse.make_one(res)

    def list_instances(
        self,
        res: "bs_td.ListInstancesResponseTypeDef",
    ) -> "dc_td.ListInstancesResponse":
        return dc_td.ListInstancesResponse.make_one(res)

    def list_license_server_endpoints(
        self,
        res: "bs_td.ListLicenseServerEndpointsResponseTypeDef",
    ) -> "dc_td.ListLicenseServerEndpointsResponse":
        return dc_td.ListLicenseServerEndpointsResponse.make_one(res)

    def list_product_subscriptions(
        self,
        res: "bs_td.ListProductSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListProductSubscriptionsResponse":
        return dc_td.ListProductSubscriptionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_user_associations(
        self,
        res: "bs_td.ListUserAssociationsResponseTypeDef",
    ) -> "dc_td.ListUserAssociationsResponse":
        return dc_td.ListUserAssociationsResponse.make_one(res)

    def register_identity_provider(
        self,
        res: "bs_td.RegisterIdentityProviderResponseTypeDef",
    ) -> "dc_td.RegisterIdentityProviderResponse":
        return dc_td.RegisterIdentityProviderResponse.make_one(res)

    def start_product_subscription(
        self,
        res: "bs_td.StartProductSubscriptionResponseTypeDef",
    ) -> "dc_td.StartProductSubscriptionResponse":
        return dc_td.StartProductSubscriptionResponse.make_one(res)

    def stop_product_subscription(
        self,
        res: "bs_td.StopProductSubscriptionResponseTypeDef",
    ) -> "dc_td.StopProductSubscriptionResponse":
        return dc_td.StopProductSubscriptionResponse.make_one(res)

    def update_identity_provider_settings(
        self,
        res: "bs_td.UpdateIdentityProviderSettingsResponseTypeDef",
    ) -> "dc_td.UpdateIdentityProviderSettingsResponse":
        return dc_td.UpdateIdentityProviderSettingsResponse.make_one(res)


license_manager_user_subscriptions_caster = LICENSE_MANAGER_USER_SUBSCRIPTIONSCaster()
