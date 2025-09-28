# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_license_manager_linux_subscriptions import type_defs as bs_td


class LICENSE_MANAGER_LINUX_SUBSCRIPTIONSCaster:

    def get_registered_subscription_provider(
        self,
        res: "bs_td.GetRegisteredSubscriptionProviderResponseTypeDef",
    ) -> "dc_td.GetRegisteredSubscriptionProviderResponse":
        return dc_td.GetRegisteredSubscriptionProviderResponse.make_one(res)

    def get_service_settings(
        self,
        res: "bs_td.GetServiceSettingsResponseTypeDef",
    ) -> "dc_td.GetServiceSettingsResponse":
        return dc_td.GetServiceSettingsResponse.make_one(res)

    def list_linux_subscription_instances(
        self,
        res: "bs_td.ListLinuxSubscriptionInstancesResponseTypeDef",
    ) -> "dc_td.ListLinuxSubscriptionInstancesResponse":
        return dc_td.ListLinuxSubscriptionInstancesResponse.make_one(res)

    def list_linux_subscriptions(
        self,
        res: "bs_td.ListLinuxSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListLinuxSubscriptionsResponse":
        return dc_td.ListLinuxSubscriptionsResponse.make_one(res)

    def list_registered_subscription_providers(
        self,
        res: "bs_td.ListRegisteredSubscriptionProvidersResponseTypeDef",
    ) -> "dc_td.ListRegisteredSubscriptionProvidersResponse":
        return dc_td.ListRegisteredSubscriptionProvidersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_subscription_provider(
        self,
        res: "bs_td.RegisterSubscriptionProviderResponseTypeDef",
    ) -> "dc_td.RegisterSubscriptionProviderResponse":
        return dc_td.RegisterSubscriptionProviderResponse.make_one(res)

    def update_service_settings(
        self,
        res: "bs_td.UpdateServiceSettingsResponseTypeDef",
    ) -> "dc_td.UpdateServiceSettingsResponse":
        return dc_td.UpdateServiceSettingsResponse.make_one(res)


license_manager_linux_subscriptions_caster = LICENSE_MANAGER_LINUX_SUBSCRIPTIONSCaster()
