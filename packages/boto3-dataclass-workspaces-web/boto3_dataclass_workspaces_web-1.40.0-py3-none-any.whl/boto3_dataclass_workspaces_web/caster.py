# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces_web import type_defs as bs_td


class WORKSPACES_WEBCaster:

    def associate_browser_settings(
        self,
        res: "bs_td.AssociateBrowserSettingsResponseTypeDef",
    ) -> "dc_td.AssociateBrowserSettingsResponse":
        return dc_td.AssociateBrowserSettingsResponse.make_one(res)

    def associate_data_protection_settings(
        self,
        res: "bs_td.AssociateDataProtectionSettingsResponseTypeDef",
    ) -> "dc_td.AssociateDataProtectionSettingsResponse":
        return dc_td.AssociateDataProtectionSettingsResponse.make_one(res)

    def associate_ip_access_settings(
        self,
        res: "bs_td.AssociateIpAccessSettingsResponseTypeDef",
    ) -> "dc_td.AssociateIpAccessSettingsResponse":
        return dc_td.AssociateIpAccessSettingsResponse.make_one(res)

    def associate_network_settings(
        self,
        res: "bs_td.AssociateNetworkSettingsResponseTypeDef",
    ) -> "dc_td.AssociateNetworkSettingsResponse":
        return dc_td.AssociateNetworkSettingsResponse.make_one(res)

    def associate_session_logger(
        self,
        res: "bs_td.AssociateSessionLoggerResponseTypeDef",
    ) -> "dc_td.AssociateSessionLoggerResponse":
        return dc_td.AssociateSessionLoggerResponse.make_one(res)

    def associate_trust_store(
        self,
        res: "bs_td.AssociateTrustStoreResponseTypeDef",
    ) -> "dc_td.AssociateTrustStoreResponse":
        return dc_td.AssociateTrustStoreResponse.make_one(res)

    def associate_user_access_logging_settings(
        self,
        res: "bs_td.AssociateUserAccessLoggingSettingsResponseTypeDef",
    ) -> "dc_td.AssociateUserAccessLoggingSettingsResponse":
        return dc_td.AssociateUserAccessLoggingSettingsResponse.make_one(res)

    def associate_user_settings(
        self,
        res: "bs_td.AssociateUserSettingsResponseTypeDef",
    ) -> "dc_td.AssociateUserSettingsResponse":
        return dc_td.AssociateUserSettingsResponse.make_one(res)

    def create_browser_settings(
        self,
        res: "bs_td.CreateBrowserSettingsResponseTypeDef",
    ) -> "dc_td.CreateBrowserSettingsResponse":
        return dc_td.CreateBrowserSettingsResponse.make_one(res)

    def create_data_protection_settings(
        self,
        res: "bs_td.CreateDataProtectionSettingsResponseTypeDef",
    ) -> "dc_td.CreateDataProtectionSettingsResponse":
        return dc_td.CreateDataProtectionSettingsResponse.make_one(res)

    def create_identity_provider(
        self,
        res: "bs_td.CreateIdentityProviderResponseTypeDef",
    ) -> "dc_td.CreateIdentityProviderResponse":
        return dc_td.CreateIdentityProviderResponse.make_one(res)

    def create_ip_access_settings(
        self,
        res: "bs_td.CreateIpAccessSettingsResponseTypeDef",
    ) -> "dc_td.CreateIpAccessSettingsResponse":
        return dc_td.CreateIpAccessSettingsResponse.make_one(res)

    def create_network_settings(
        self,
        res: "bs_td.CreateNetworkSettingsResponseTypeDef",
    ) -> "dc_td.CreateNetworkSettingsResponse":
        return dc_td.CreateNetworkSettingsResponse.make_one(res)

    def create_portal(
        self,
        res: "bs_td.CreatePortalResponseTypeDef",
    ) -> "dc_td.CreatePortalResponse":
        return dc_td.CreatePortalResponse.make_one(res)

    def create_session_logger(
        self,
        res: "bs_td.CreateSessionLoggerResponseTypeDef",
    ) -> "dc_td.CreateSessionLoggerResponse":
        return dc_td.CreateSessionLoggerResponse.make_one(res)

    def create_trust_store(
        self,
        res: "bs_td.CreateTrustStoreResponseTypeDef",
    ) -> "dc_td.CreateTrustStoreResponse":
        return dc_td.CreateTrustStoreResponse.make_one(res)

    def create_user_access_logging_settings(
        self,
        res: "bs_td.CreateUserAccessLoggingSettingsResponseTypeDef",
    ) -> "dc_td.CreateUserAccessLoggingSettingsResponse":
        return dc_td.CreateUserAccessLoggingSettingsResponse.make_one(res)

    def create_user_settings(
        self,
        res: "bs_td.CreateUserSettingsResponseTypeDef",
    ) -> "dc_td.CreateUserSettingsResponse":
        return dc_td.CreateUserSettingsResponse.make_one(res)

    def get_browser_settings(
        self,
        res: "bs_td.GetBrowserSettingsResponseTypeDef",
    ) -> "dc_td.GetBrowserSettingsResponse":
        return dc_td.GetBrowserSettingsResponse.make_one(res)

    def get_data_protection_settings(
        self,
        res: "bs_td.GetDataProtectionSettingsResponseTypeDef",
    ) -> "dc_td.GetDataProtectionSettingsResponse":
        return dc_td.GetDataProtectionSettingsResponse.make_one(res)

    def get_identity_provider(
        self,
        res: "bs_td.GetIdentityProviderResponseTypeDef",
    ) -> "dc_td.GetIdentityProviderResponse":
        return dc_td.GetIdentityProviderResponse.make_one(res)

    def get_ip_access_settings(
        self,
        res: "bs_td.GetIpAccessSettingsResponseTypeDef",
    ) -> "dc_td.GetIpAccessSettingsResponse":
        return dc_td.GetIpAccessSettingsResponse.make_one(res)

    def get_network_settings(
        self,
        res: "bs_td.GetNetworkSettingsResponseTypeDef",
    ) -> "dc_td.GetNetworkSettingsResponse":
        return dc_td.GetNetworkSettingsResponse.make_one(res)

    def get_portal(
        self,
        res: "bs_td.GetPortalResponseTypeDef",
    ) -> "dc_td.GetPortalResponse":
        return dc_td.GetPortalResponse.make_one(res)

    def get_portal_service_provider_metadata(
        self,
        res: "bs_td.GetPortalServiceProviderMetadataResponseTypeDef",
    ) -> "dc_td.GetPortalServiceProviderMetadataResponse":
        return dc_td.GetPortalServiceProviderMetadataResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def get_session_logger(
        self,
        res: "bs_td.GetSessionLoggerResponseTypeDef",
    ) -> "dc_td.GetSessionLoggerResponse":
        return dc_td.GetSessionLoggerResponse.make_one(res)

    def get_trust_store(
        self,
        res: "bs_td.GetTrustStoreResponseTypeDef",
    ) -> "dc_td.GetTrustStoreResponse":
        return dc_td.GetTrustStoreResponse.make_one(res)

    def get_trust_store_certificate(
        self,
        res: "bs_td.GetTrustStoreCertificateResponseTypeDef",
    ) -> "dc_td.GetTrustStoreCertificateResponse":
        return dc_td.GetTrustStoreCertificateResponse.make_one(res)

    def get_user_access_logging_settings(
        self,
        res: "bs_td.GetUserAccessLoggingSettingsResponseTypeDef",
    ) -> "dc_td.GetUserAccessLoggingSettingsResponse":
        return dc_td.GetUserAccessLoggingSettingsResponse.make_one(res)

    def get_user_settings(
        self,
        res: "bs_td.GetUserSettingsResponseTypeDef",
    ) -> "dc_td.GetUserSettingsResponse":
        return dc_td.GetUserSettingsResponse.make_one(res)

    def list_browser_settings(
        self,
        res: "bs_td.ListBrowserSettingsResponseTypeDef",
    ) -> "dc_td.ListBrowserSettingsResponse":
        return dc_td.ListBrowserSettingsResponse.make_one(res)

    def list_data_protection_settings(
        self,
        res: "bs_td.ListDataProtectionSettingsResponseTypeDef",
    ) -> "dc_td.ListDataProtectionSettingsResponse":
        return dc_td.ListDataProtectionSettingsResponse.make_one(res)

    def list_identity_providers(
        self,
        res: "bs_td.ListIdentityProvidersResponseTypeDef",
    ) -> "dc_td.ListIdentityProvidersResponse":
        return dc_td.ListIdentityProvidersResponse.make_one(res)

    def list_ip_access_settings(
        self,
        res: "bs_td.ListIpAccessSettingsResponseTypeDef",
    ) -> "dc_td.ListIpAccessSettingsResponse":
        return dc_td.ListIpAccessSettingsResponse.make_one(res)

    def list_network_settings(
        self,
        res: "bs_td.ListNetworkSettingsResponseTypeDef",
    ) -> "dc_td.ListNetworkSettingsResponse":
        return dc_td.ListNetworkSettingsResponse.make_one(res)

    def list_portals(
        self,
        res: "bs_td.ListPortalsResponseTypeDef",
    ) -> "dc_td.ListPortalsResponse":
        return dc_td.ListPortalsResponse.make_one(res)

    def list_session_loggers(
        self,
        res: "bs_td.ListSessionLoggersResponseTypeDef",
    ) -> "dc_td.ListSessionLoggersResponse":
        return dc_td.ListSessionLoggersResponse.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsResponseTypeDef",
    ) -> "dc_td.ListSessionsResponse":
        return dc_td.ListSessionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_trust_store_certificates(
        self,
        res: "bs_td.ListTrustStoreCertificatesResponseTypeDef",
    ) -> "dc_td.ListTrustStoreCertificatesResponse":
        return dc_td.ListTrustStoreCertificatesResponse.make_one(res)

    def list_trust_stores(
        self,
        res: "bs_td.ListTrustStoresResponseTypeDef",
    ) -> "dc_td.ListTrustStoresResponse":
        return dc_td.ListTrustStoresResponse.make_one(res)

    def list_user_access_logging_settings(
        self,
        res: "bs_td.ListUserAccessLoggingSettingsResponseTypeDef",
    ) -> "dc_td.ListUserAccessLoggingSettingsResponse":
        return dc_td.ListUserAccessLoggingSettingsResponse.make_one(res)

    def list_user_settings(
        self,
        res: "bs_td.ListUserSettingsResponseTypeDef",
    ) -> "dc_td.ListUserSettingsResponse":
        return dc_td.ListUserSettingsResponse.make_one(res)

    def update_browser_settings(
        self,
        res: "bs_td.UpdateBrowserSettingsResponseTypeDef",
    ) -> "dc_td.UpdateBrowserSettingsResponse":
        return dc_td.UpdateBrowserSettingsResponse.make_one(res)

    def update_data_protection_settings(
        self,
        res: "bs_td.UpdateDataProtectionSettingsResponseTypeDef",
    ) -> "dc_td.UpdateDataProtectionSettingsResponse":
        return dc_td.UpdateDataProtectionSettingsResponse.make_one(res)

    def update_identity_provider(
        self,
        res: "bs_td.UpdateIdentityProviderResponseTypeDef",
    ) -> "dc_td.UpdateIdentityProviderResponse":
        return dc_td.UpdateIdentityProviderResponse.make_one(res)

    def update_ip_access_settings(
        self,
        res: "bs_td.UpdateIpAccessSettingsResponseTypeDef",
    ) -> "dc_td.UpdateIpAccessSettingsResponse":
        return dc_td.UpdateIpAccessSettingsResponse.make_one(res)

    def update_network_settings(
        self,
        res: "bs_td.UpdateNetworkSettingsResponseTypeDef",
    ) -> "dc_td.UpdateNetworkSettingsResponse":
        return dc_td.UpdateNetworkSettingsResponse.make_one(res)

    def update_portal(
        self,
        res: "bs_td.UpdatePortalResponseTypeDef",
    ) -> "dc_td.UpdatePortalResponse":
        return dc_td.UpdatePortalResponse.make_one(res)

    def update_session_logger(
        self,
        res: "bs_td.UpdateSessionLoggerResponseTypeDef",
    ) -> "dc_td.UpdateSessionLoggerResponse":
        return dc_td.UpdateSessionLoggerResponse.make_one(res)

    def update_trust_store(
        self,
        res: "bs_td.UpdateTrustStoreResponseTypeDef",
    ) -> "dc_td.UpdateTrustStoreResponse":
        return dc_td.UpdateTrustStoreResponse.make_one(res)

    def update_user_access_logging_settings(
        self,
        res: "bs_td.UpdateUserAccessLoggingSettingsResponseTypeDef",
    ) -> "dc_td.UpdateUserAccessLoggingSettingsResponse":
        return dc_td.UpdateUserAccessLoggingSettingsResponse.make_one(res)

    def update_user_settings(
        self,
        res: "bs_td.UpdateUserSettingsResponseTypeDef",
    ) -> "dc_td.UpdateUserSettingsResponse":
        return dc_td.UpdateUserSettingsResponse.make_one(res)


workspaces_web_caster = WORKSPACES_WEBCaster()
