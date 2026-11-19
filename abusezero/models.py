from __future__ import annotations
from typing import Any, TypedDict, Required, NotRequired, Literal
from .core import AbuseZeroError

PublicPricingResponsePlansItemPricesMonthVariant0 = TypedDict("PublicPricingResponsePlansItemPricesMonthVariant0", {"amount_cents": Required[int], "credits": Required[int]}, total=False)

PublicPricingResponsePlansItemPricesYearVariant0 = TypedDict("PublicPricingResponsePlansItemPricesYearVariant0", {"amount_cents": Required[int], "credits": Required[int]}, total=False)

PublicPricingResponsePlansItemPrices = TypedDict("PublicPricingResponsePlansItemPrices", {"month": Required[PublicPricingResponsePlansItemPricesMonthVariant0 | None], "year": Required[PublicPricingResponsePlansItemPricesYearVariant0 | None]}, total=False)

PublicPricingResponsePlansItemIncludesTraffic = TypedDict("PublicPricingResponsePlansItemIncludesTraffic", {"rate_per_second": Required[int], "burst": Required[int], "concurrency": Required[int]}, total=False)

PublicPricingResponsePlansItemIncludes = TypedDict("PublicPricingResponsePlansItemIncludes", {"protected_benefits": Required[int], "team_seats": Required[int], "data_retention_days": Required[int], "traffic": Required[PublicPricingResponsePlansItemIncludesTraffic]}, total=False)

PublicPricingResponsePlansItem = TypedDict("PublicPricingResponsePlansItem", {"object": Required[Literal["plan"]], "plan": Required[Literal["payg", "pro", "scale"]], "name": Required[str], "prices": Required[PublicPricingResponsePlansItemPrices], "includes": Required[PublicPricingResponsePlansItemIncludes]}, total=False)

PublicPricingResponseCreditPacks = TypedDict("PublicPricingResponseCreditPacks", {"credits_per_dollar": Required[int], "amounts": Required[list[int]], "custom_amount_step": Required[int], "custom_amount_max": Required[int], "first_purchase_multiplier": Required[int]}, total=False)

PublicPricingResponseYearly = TypedDict("PublicPricingResponseYearly", {"rollover_percent": Required[int], "converted_credit_expiry_months": Required[int]}, total=False)

PublicPricingResponseEveryPlan = TypedDict("PublicPricingResponseEveryPlan", {"custom_policies": Required[int], "webhook_endpoints": Required[int], "webhook_resends_per_endpoint_per_hour": Required[int], "webhook_deliveries_per_day": Required[int]}, total=False)

PublicPricingResponseEnterprise = TypedDict("PublicPricingResponseEnterprise", {"contact": Required[str]}, total=False)

PublicPricingResponse = TypedDict("PublicPricingResponse", {"object": Required[Literal["pricing"]], "currency": Required[Literal["USD"]], "credits_per_evaluation": Required[int], "plans": Required[list[PublicPricingResponsePlansItem]], "credit_packs": Required[PublicPricingResponseCreditPacks], "yearly": Required[PublicPricingResponseYearly], "every_plan": Required[PublicPricingResponseEveryPlan], "enterprise": Required[PublicPricingResponseEnterprise], "url": Required[str]}, total=False)

PublicPricingQuoteInput = TypedDict("PublicPricingQuoteInput", {"plan": Required[Literal["payg", "pro", "scale"]], "interval": NotRequired[Literal["month", "year"]], "amount": NotRequired[int]}, total=False)

PublicPricingQuoteResponse = TypedDict("PublicPricingQuoteResponse", {"object": Required[Literal["price_quote"]], "plan": Required[Literal["payg", "pro", "scale"]], "interval": Required[Literal["month", "year"] | None], "currency": Required[Literal["USD"]], "amount_cents": Required[int], "credits": Required[int], "bonus_credits": Required[int], "total_credits": Required[int]}, total=False)

PublicDocsInput = TypedDict("PublicDocsInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

PublicDocsResponseDataItem = TypedDict("PublicDocsResponseDataItem", {"object": Required[Literal["docs_page"]], "path": Required[str], "title": Required[str], "description": Required[str | None], "url": Required[str], "updated_at": Required[str]}, total=False)

PublicDocsResponse = TypedDict("PublicDocsResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicDocsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicDocsSearchInput = TypedDict("PublicDocsSearchInput", {"query": Required[str], "limit": NotRequired[int]}, total=False)

PublicDocsSearchResponseDataItem = TypedDict("PublicDocsSearchResponseDataItem", {"object": Required[Literal["docs_page_match"]], "path": Required[str], "title": Required[str], "url": Required[str], "snippet": Required[str], "updated_at": Required[str]}, total=False)

PublicDocsSearchResponse = TypedDict("PublicDocsSearchResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicDocsSearchResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicDocsPageResponse = TypedDict("PublicDocsPageResponse", {"object": Required[Literal["docs_page"]], "path": Required[str], "title": Required[str], "description": Required[str | None], "url": Required[str], "updated_at": Required[str], "markdown": Required[str]}, total=False)

PublicHelpInput = TypedDict("PublicHelpInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

PublicHelpResponseDataItem = TypedDict("PublicHelpResponseDataItem", {"object": Required[Literal["help_article"]], "path": Required[str], "title": Required[str], "description": Required[str | None], "url": Required[str], "updated_at": Required[str]}, total=False)

PublicHelpResponse = TypedDict("PublicHelpResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicHelpResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicHelpSearchInput = TypedDict("PublicHelpSearchInput", {"query": Required[str], "limit": NotRequired[int]}, total=False)

PublicHelpSearchResponseDataItem = TypedDict("PublicHelpSearchResponseDataItem", {"object": Required[Literal["help_article_match"]], "path": Required[str], "title": Required[str], "url": Required[str], "snippet": Required[str], "updated_at": Required[str]}, total=False)

PublicHelpSearchResponse = TypedDict("PublicHelpSearchResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicHelpSearchResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicHelpArticleResponse = TypedDict("PublicHelpArticleResponse", {"object": Required[Literal["help_article"]], "path": Required[str], "title": Required[str], "description": Required[str | None], "url": Required[str], "updated_at": Required[str], "markdown": Required[str]}, total=False)

PublicOpenapiResponse = TypedDict("PublicOpenapiResponse", {"object": Required[Literal["openapi"]], "version": Required[str], "document": Required[dict[str, Any]]}, total=False)

PublicActionsResponseDataItem = TypedDict("PublicActionsResponseDataItem", {"object": Required[Literal["action"]], "id": Required[str], "summary": Required[str], "method": Required[str], "path": Required[str], "scope": Required[str], "sign_in": Required[bool], "mcp_tool": Required[str | None], "cli_command": Required[str | None], "mutation": Required[bool], "destructive": Required[bool]}, total=False)

PublicActionsResponse = TypedDict("PublicActionsResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicActionsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicErrorsResponseDataItem = TypedDict("PublicErrorsResponseDataItem", {"object": Required[Literal["error_code"]], "code": Required[str], "status": Required[int], "type": Required[str], "meaning": Required[str], "retryable": Required[bool], "next_step": Required[str], "docs_url": Required[str]}, total=False)

PublicErrorsResponse = TypedDict("PublicErrorsResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicErrorsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicReasonsResponseDataItem = TypedDict("PublicReasonsResponseDataItem", {"object": Required[Literal["reason_code"]], "code": Required[str], "label": Required[str], "message": Required[str], "meaning": Required[str | None], "docs_url": Required[str]}, total=False)

PublicReasonsResponse = TypedDict("PublicReasonsResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicReasonsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicWebhookEventsResponseDataItemExample = TypedDict("PublicWebhookEventsResponseDataItemExample", {"object": Required[Literal["event"]], "id": Required[str], "type": Required[str], "api_version": Required[str], "created_at": Required[str], "workspace": Required[str], "data": Required[dict[str, Any]]}, total=False)

PublicWebhookEventsResponseDataItem = TypedDict("PublicWebhookEventsResponseDataItem", {"object": Required[Literal["webhook_event_type"]], "type": Required[str], "description": Required[str], "example": Required[PublicWebhookEventsResponseDataItemExample]}, total=False)

PublicWebhookEventsResponse = TypedDict("PublicWebhookEventsResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicWebhookEventsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicConditionsResponseDataItem = TypedDict("PublicConditionsResponseDataItem", {"object": Required[Literal["condition"]], "key": Required[str], "label": Required[str], "group": Required[str], "type": Required[Literal["number", "string", "boolean"]], "values": NotRequired[list[str]], "min": NotRequired[float], "max": NotRequired[float], "integer": NotRequired[bool]}, total=False)

PublicConditionsResponse = TypedDict("PublicConditionsResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicConditionsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicGlossaryResponseTermsItem = TypedDict("PublicGlossaryResponseTermsItem", {"term": Required[str], "definition": Required[str]}, total=False)

PublicGlossaryResponseFaqItem = TypedDict("PublicGlossaryResponseFaqItem", {"section": Required[str | None], "question": Required[str], "answer": Required[str]}, total=False)

PublicGlossaryResponse = TypedDict("PublicGlossaryResponse", {"object": Required[Literal["glossary"]], "terms": Required[list[PublicGlossaryResponseTermsItem]], "faq": Required[list[PublicGlossaryResponseFaqItem]], "url": Required[str], "faq_url": Required[str], "updated_at": Required[str]}, total=False)

PublicLegalResponseDataItem = TypedDict("PublicLegalResponseDataItem", {"object": Required[Literal["legal_document"]], "document": Required[str], "title": Required[str], "version": Required[str], "effective_date": Required[str], "url": Required[str], "updated_at": Required[str]}, total=False)

PublicLegalResponse = TypedDict("PublicLegalResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicLegalResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicLegalDocumentResponse = TypedDict("PublicLegalDocumentResponse", {"object": Required[Literal["legal_document"]], "document": Required[str], "title": Required[str], "version": Required[str], "effective_date": Required[str], "url": Required[str], "updated_at": Required[str], "markdown": Required[str]}, total=False)

PublicChangelogResponseEntriesItem = TypedDict("PublicChangelogResponseEntriesItem", {"id": Required[str], "title": Required[str], "date": Required[str], "markdown": Required[str]}, total=False)

PublicChangelogResponse = TypedDict("PublicChangelogResponse", {"object": Required[Literal["changelog"]], "url": Required[str], "entries": Required[list[PublicChangelogResponseEntriesItem]], "updated_at": Required[str]}, total=False)

PublicBlogInput = TypedDict("PublicBlogInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

PublicBlogResponseDataItem = TypedDict("PublicBlogResponseDataItem", {"object": Required[Literal["blog_post"]], "slug": Required[str], "title": Required[str], "description": Required[str | None], "url": Required[str], "published_on": Required[str | None], "revised_on": Required[str | None], "authors": Required[list[str]], "tags": Required[list[str]], "updated_at": Required[str]}, total=False)

PublicBlogResponse = TypedDict("PublicBlogResponse", {"object": Required[Literal["list"]], "data": Required[list[PublicBlogResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PublicBlogPostResponse = TypedDict("PublicBlogPostResponse", {"object": Required[Literal["blog_post"]], "slug": Required[str], "title": Required[str], "description": Required[str | None], "url": Required[str], "published_on": Required[str | None], "revised_on": Required[str | None], "authors": Required[list[str]], "tags": Required[list[str]], "updated_at": Required[str], "markdown": Required[str]}, total=False)

PublicVersionsResponseNpm = TypedDict("PublicVersionsResponseNpm", {"package": Required[str], "version": Required[str]}, total=False)

PublicVersionsResponseBrowserScript = TypedDict("PublicVersionsResponseBrowserScript", {"version": Required[str], "url": Required[str]}, total=False)

PublicVersionsResponseSkillVariant0 = TypedDict("PublicVersionsResponseSkillVariant0", {"version": Required[str], "url": Required[str]}, total=False)

PublicVersionsResponse = TypedDict("PublicVersionsResponse", {"object": Required[Literal["versions"]], "api": Required[Literal["v1"]], "npm": Required[PublicVersionsResponseNpm], "browser_script": Required[PublicVersionsResponseBrowserScript], "skill": Required[PublicVersionsResponseSkillVariant0 | None]}, total=False)

PublicStatusResponse = TypedDict("PublicStatusResponse", {"object": Required[Literal["service_status"]], "status": Required[Literal["operational", "degraded"]], "checked_at": Required[str]}, total=False)

PublicContactsResponseSupport = TypedDict("PublicContactsResponseSupport", {"email": Required[str], "form": Required[str | None], "api": Required[str]}, total=False)

PublicContactsResponseSales = TypedDict("PublicContactsResponseSales", {"form": Required[str], "api": Required[str]}, total=False)

PublicContactsResponseSecurity = TypedDict("PublicContactsResponseSecurity", {"email": Required[str]}, total=False)

PublicContactsResponse = TypedDict("PublicContactsResponse", {"object": Required[Literal["contacts"]], "support": Required[PublicContactsResponseSupport], "sales": Required[PublicContactsResponseSales], "security": Required[PublicContactsResponseSecurity]}, total=False)

PublicContactSalesInput = TypedDict("PublicContactSalesInput", {"name": Required[str], "email": Required[str], "message": Required[str]}, total=False)

PublicContactSalesResponse = TypedDict("PublicContactSalesResponse", {"object": Required[Literal["sales_request"]], "received": Required[Literal[True]]}, total=False)

PublicContactSupportInput = TypedDict("PublicContactSupportInput", {"email": Required[str], "subject": Required[str], "message": Required[str], "topic": Required[Literal["account", "billing", "integration", "dashboard", "other"]], "name": NotRequired[str], "workspace_id": NotRequired[str], "request_id": NotRequired[str]}, total=False)

PublicContactSupportResponse = TypedDict("PublicContactSupportResponse", {"object": Required[Literal["support_request"]], "reference": Required[str], "email": Required[str]}, total=False)

PublicOnboardingStartInput = TypedDict("PublicOnboardingStartInput", {"workspace_name": Required[str], "plan": Required[Literal["payg", "pro", "scale"]], "interval": NotRequired[Literal["month", "year"]], "credit_pack_dollars": NotRequired[int]}, total=False)

PublicOnboardingStartResponse = TypedDict("PublicOnboardingStartResponse", {"object": Required[Literal["onboarding_session"]], "id": Required[str], "approval_url": Required[str], "secret": Required[str], "expires_at": Required[str], "workspace_name": Required[str], "plan": Required[Literal["payg", "pro", "scale"]], "interval": Required[Literal["month", "year"] | None], "credit_pack_dollars": Required[int | None], "amount_cents": Required[int]}, total=False)

PublicOnboardingStatusInput = TypedDict("PublicOnboardingStatusInput", {"secret": Required[str], "wait": NotRequired[int]}, total=False)

PublicOnboardingStatusResponseSignInVariant0 = TypedDict("PublicOnboardingStatusResponseSignInVariant0", {"token_endpoint": Required[str], "grant_type": Required[str], "client_id": Required[str]}, total=False)

PublicOnboardingStatusResponse = TypedDict("PublicOnboardingStatusResponse", {"object": Required[Literal["onboarding_session"]], "id": Required[str], "status": Required[Literal["waiting", "declined", "expired", "ready", "collected"]], "expires_at": Required[str], "workspace": Required[str | None], "sign_in": Required[PublicOnboardingStatusResponseSignInVariant0 | None]}, total=False)

WorkspacesListResponseDataItem = TypedDict("WorkspacesListResponseDataItem", {"object": Required[str]}, total=False)

WorkspacesListResponse = TypedDict("WorkspacesListResponse", {"object": Required[Literal["list"]], "data": Required[list[WorkspacesListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

MeGetResponsePersonVariant0 = TypedDict("MeGetResponsePersonVariant0", {"name": Required[str | None], "email": Required[str | None]}, total=False)

MeGetResponseAppVariant0 = TypedDict("MeGetResponseAppVariant0", {"id": Required[str], "name": Required[str | None]}, total=False)

MeGetResponseApiKeyVariant0 = TypedDict("MeGetResponseApiKeyVariant0", {"id": Required[str], "name": Required[str | None], "type": Required[Literal["secret", "restricted"]]}, total=False)

MeGetResponseMachineClientVariant0 = TypedDict("MeGetResponseMachineClientVariant0", {"id": Required[str], "name": Required[str | None]}, total=False)

MeGetResponseWorkspaceVariant0 = TypedDict("MeGetResponseWorkspaceVariant0", {"id": Required[str], "name": Required[str | None]}, total=False)

MeGetResponse = TypedDict("MeGetResponse", {"object": Required[Literal["connection"]], "credential": Required[Literal["oauth", "machine_client", "api_key"]], "person": Required[MeGetResponsePersonVariant0 | None], "app": Required[MeGetResponseAppVariant0 | None], "api_key": Required[MeGetResponseApiKeyVariant0 | None], "machine_client": Required[MeGetResponseMachineClientVariant0 | None], "workspace": Required[MeGetResponseWorkspaceVariant0 | None], "role": Required[Literal["owner", "admin", "developer", "viewer"] | None], "permissions": Required[list[Literal["manage", "publish", "keys", "reveal", "export", "members", "delete"]]], "scopes": Required[list[Literal["operations:general", "operations:configuration", "operations:management"]]]}, total=False)

ApiKeysListInput = TypedDict("ApiKeysListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

ApiKeysListResponseDataItem = TypedDict("ApiKeysListResponseDataItem", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted", "publishable"]], "scopes": Required[list[str]], "prefix": Required[str | None], "last_four": Required[str | None], "value": Required[str | None], "status": Required[Literal["active", "expired", "revoked"]], "replacement_available": Required[bool], "expires_at": Required[str | None], "last_used_at": Required[str | None], "created_at": Required[str | None]}, total=False)

ApiKeysListResponse = TypedDict("ApiKeysListResponse", {"object": Required[Literal["list"]], "data": Required[list[ApiKeysListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

ApiKeysCreateInput = TypedDict("ApiKeysCreateInput", {"name": Required[str], "type": Required[Literal["secret", "restricted"]], "scopes": NotRequired[list[Literal["operations:general", "operations:configuration", "operations:management", "observations:create"]]], "expires_in_days": NotRequired[int | None]}, total=False)

ApiKeysCreateResponse = TypedDict("ApiKeysCreateResponse", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted", "publishable"]], "scopes": Required[list[str]], "prefix": Required[str | None], "last_four": Required[str | None], "value": Required[str | None], "status": Required[Literal["active", "expired", "revoked"]], "replacement_available": Required[bool], "expires_at": Required[str | None], "last_used_at": Required[str | None], "created_at": Required[str | None], "secret": Required[str]}, total=False)

ApiKeysUpdateInput = TypedDict("ApiKeysUpdateInput", {"name": NotRequired[str], "scopes": NotRequired[list[Literal["operations:general", "operations:configuration", "operations:management", "observations:create"]]], "expires_in_days": NotRequired[int | None]}, total=False)

ApiKeysUpdateResponse = TypedDict("ApiKeysUpdateResponse", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted", "publishable"]], "scopes": Required[list[str]], "prefix": Required[str | None], "last_four": Required[str | None], "value": Required[str | None], "status": Required[Literal["active", "expired", "revoked"]], "replacement_available": Required[bool], "expires_at": Required[str | None], "last_used_at": Required[str | None], "created_at": Required[str | None]}, total=False)

ApiKeysRollInput = TypedDict("ApiKeysRollInput", {"overlap_hours": Required[Literal[1] | Literal[24] | Literal[168]]}, total=False)

ApiKeysRollResponsePrevious = TypedDict("ApiKeysRollResponsePrevious", {"id": Required[str | None], "expires_at": Required[str | None]}, total=False)

ApiKeysRollResponse = TypedDict("ApiKeysRollResponse", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted", "publishable"]], "scopes": Required[list[str]], "prefix": Required[str | None], "last_four": Required[str | None], "value": Required[str | None], "status": Required[Literal["active", "expired", "revoked"]], "replacement_available": Required[bool], "expires_at": Required[str | None], "last_used_at": Required[str | None], "created_at": Required[str | None], "secret": Required[str], "previous": Required[ApiKeysRollResponsePrevious]}, total=False)

ApiKeysReplacementResponse = TypedDict("ApiKeysReplacementResponse", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted", "publishable"]], "scopes": Required[list[str]], "prefix": Required[str | None], "last_four": Required[str | None], "value": Required[str | None], "status": Required[Literal["active", "expired", "revoked"]], "replacement_available": Required[bool], "expires_at": Required[str | None], "last_used_at": Required[str | None], "created_at": Required[str | None], "secret": Required[str]}, total=False)

ApiKeysRevokeResponse = TypedDict("ApiKeysRevokeResponse", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted", "publishable"]], "scopes": Required[list[str]], "prefix": Required[str | None], "last_four": Required[str | None], "value": Required[str | None], "status": Required[Literal["active", "expired", "revoked"]], "replacement_available": Required[bool], "expires_at": Required[str | None], "last_used_at": Required[str | None], "created_at": Required[str | None]}, total=False)

MachineClientsListInput = TypedDict("MachineClientsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "view": NotRequired[Literal["mine", "everyone"]]}, total=False)

MachineClientsListResponseDataItemMemberVariant0 = TypedDict("MachineClientsListResponseDataItemMemberVariant0", {"name": Required[str | None], "email": Required[str | None], "role": Required[Literal["owner", "admin", "developer", "viewer"] | None], "you": Required[bool], "former": Required[bool]}, total=False)

MachineClientsListResponseDataItem = TypedDict("MachineClientsListResponseDataItem", {"object": Required[Literal["machine_client"]], "id": Required[str | None], "name": Required[str], "scopes": Required[list[str]], "member": Required[MachineClientsListResponseDataItemMemberVariant0 | None], "created_at": Required[str | None], "last_used_at": Required[str | None]}, total=False)

MachineClientsListResponse = TypedDict("MachineClientsListResponse", {"object": Required[Literal["list"]], "data": Required[list[MachineClientsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

MachineClientsCreateInput = TypedDict("MachineClientsCreateInput", {"name": Required[str], "scopes": Required[list[Literal["operations:general", "operations:configuration", "operations:management"]]]}, total=False)

MachineClientsCreateResponseMemberVariant0 = TypedDict("MachineClientsCreateResponseMemberVariant0", {"name": Required[str | None], "email": Required[str | None], "role": Required[Literal["owner", "admin", "developer", "viewer"] | None], "you": Required[bool], "former": Required[bool]}, total=False)

MachineClientsCreateResponse = TypedDict("MachineClientsCreateResponse", {"object": Required[Literal["machine_client"]], "id": Required[str | None], "name": Required[str], "scopes": Required[list[str]], "member": Required[MachineClientsCreateResponseMemberVariant0 | None], "created_at": Required[str | None], "last_used_at": Required[str | None], "secret": Required[str], "token_endpoint": Required[str], "audience": Required[str]}, total=False)

MachineClientsRotateSecretResponse = TypedDict("MachineClientsRotateSecretResponse", {"object": Required[Literal["machine_client_secret"]], "id": Required[str | None], "secret": Required[str]}, total=False)

MachineClientsRevokeResponse = TypedDict("MachineClientsRevokeResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

AuthorizedAppsListInput = TypedDict("AuthorizedAppsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "view": NotRequired[Literal["mine", "everyone"]]}, total=False)

AuthorizedAppsListResponseDataItemMemberVariant0 = TypedDict("AuthorizedAppsListResponseDataItemMemberVariant0", {"name": Required[str | None], "email": Required[str | None], "role": Required[Literal["owner", "admin", "developer", "viewer"] | None], "you": Required[bool], "former": Required[bool]}, total=False)

AuthorizedAppsListResponseDataItem = TypedDict("AuthorizedAppsListResponseDataItem", {"object": Required[Literal["authorized_app"]], "id": Required[str | None], "name": Required[str], "trust": Required[Literal["first_party", "verified", "unverified"]], "destination": Required[str | None], "scopes": Required[list[str]], "member": Required[AuthorizedAppsListResponseDataItemMemberVariant0 | None], "approved_at": Required[str | None]}, total=False)

AuthorizedAppsListResponse = TypedDict("AuthorizedAppsListResponse", {"object": Required[Literal["list"]], "data": Required[list[AuthorizedAppsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

AuthorizedAppsDisconnectResponse = TypedDict("AuthorizedAppsDisconnectResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

MembersListInput = TypedDict("MembersListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

MembersListResponseDataItem = TypedDict("MembersListResponseDataItem", {"object": Required[Literal["member"]], "id": Required[str | None], "name": Required[str | None], "email": Required[str], "role": Required[Literal["owner", "admin", "developer", "viewer"]], "permissions": Required[list[str]], "invited_at": Required[str | None], "joined_at": Required[str | None], "last_sign_in_at": Required[str | None], "you": Required[bool]}, total=False)

MembersListResponse = TypedDict("MembersListResponse", {"object": Required[Literal["list"]], "data": Required[list[MembersListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

MembersUpdateInput = TypedDict("MembersUpdateInput", {"role": NotRequired[Literal["admin", "developer", "viewer"]], "permissions": NotRequired[list[Literal["manage", "publish", "keys", "reveal", "export", "delete"]]]}, total=False)

MembersUpdateResponse = TypedDict("MembersUpdateResponse", {"object": Required[Literal["member"]], "id": Required[str | None], "name": Required[str | None], "email": Required[str], "role": Required[Literal["owner", "admin", "developer", "viewer"]], "permissions": Required[list[str]], "invited_at": Required[str | None], "joined_at": Required[str | None], "last_sign_in_at": Required[str | None], "you": Required[bool]}, total=False)

MembersRemoveResponse = TypedDict("MembersRemoveResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

InvitationsListInput = TypedDict("InvitationsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

InvitationsListResponseDataItem = TypedDict("InvitationsListResponseDataItem", {"object": Required[Literal["invitation"]], "id": Required[str | None], "email": Required[str], "role": Required[Literal["admin", "developer", "viewer"]], "invited_by": Required[str | None], "status": Required[Literal["pending", "canceled"]], "created_at": Required[str | None], "expires_at": Required[str | None]}, total=False)

InvitationsListResponse = TypedDict("InvitationsListResponse", {"object": Required[Literal["list"]], "data": Required[list[InvitationsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

InvitationsCreateInput = TypedDict("InvitationsCreateInput", {"email": Required[str], "role": Required[Literal["admin", "developer", "viewer"]]}, total=False)

InvitationsCreateResponse = TypedDict("InvitationsCreateResponse", {"object": Required[Literal["invitation"]], "id": Required[str | None], "email": Required[str], "role": Required[Literal["admin", "developer", "viewer"]], "invited_by": Required[str | None], "status": Required[Literal["pending", "canceled"]], "created_at": Required[str | None], "expires_at": Required[str | None]}, total=False)

InvitationsResendResponse = TypedDict("InvitationsResendResponse", {"object": Required[Literal["invitation"]], "id": Required[str | None], "email": Required[str], "role": Required[Literal["admin", "developer", "viewer"]], "invited_by": Required[str | None], "status": Required[Literal["pending", "canceled"]], "created_at": Required[str | None], "expires_at": Required[str | None]}, total=False)

InvitationsCancelResponse = TypedDict("InvitationsCancelResponse", {"object": Required[Literal["invitation"]], "id": Required[str | None], "email": Required[str], "role": Required[Literal["admin", "developer", "viewer"]], "invited_by": Required[str | None], "status": Required[Literal["pending", "canceled"]], "created_at": Required[str | None], "expires_at": Required[str | None]}, total=False)

WorkspaceGetResponseIconVariant0 = TypedDict("WorkspaceGetResponseIconVariant0", {"updated_at": Required[str | None]}, total=False)

WorkspaceGetResponseProductTypeVariant0 = TypedDict("WorkspaceGetResponseProductTypeVariant0", {"type": Required[Literal["ai_app", "media_generation", "developer_tool", "b2b_saas", "consumer_app", "marketplace", "game", "other"]], "other": NotRequired[str]}, total=False)

WorkspaceGetResponseDataRetention = TypedDict("WorkspaceGetResponseDataRetention", {"evidence_days": Required[int], "max_days": Required[int], "options": Required[list[int]]}, total=False)

WorkspaceGetResponse = TypedDict("WorkspaceGetResponse", {"object": Required[Literal["workspace_settings"]], "id": Required[str], "name": Required[str], "icon": Required[WorkspaceGetResponseIconVariant0 | None], "time_zone": Required[str | None], "website": Required[str | None], "product_type": Required[WorkspaceGetResponseProductTypeVariant0 | None], "data_retention": Required[WorkspaceGetResponseDataRetention]}, total=False)

WorkspaceUpdateInputProductTypeVariant0 = TypedDict("WorkspaceUpdateInputProductTypeVariant0", {"type": Required[Literal["ai_app", "media_generation", "developer_tool", "b2b_saas", "consumer_app", "marketplace", "game", "other"]], "other": NotRequired[str]}, total=False)

WorkspaceUpdateInput = TypedDict("WorkspaceUpdateInput", {"name": NotRequired[str], "website": NotRequired[str | None], "product_type": NotRequired[WorkspaceUpdateInputProductTypeVariant0 | None], "time_zone": NotRequired[str]}, total=False)

WorkspaceUpdateResponseIconVariant0 = TypedDict("WorkspaceUpdateResponseIconVariant0", {"updated_at": Required[str | None]}, total=False)

WorkspaceUpdateResponseProductTypeVariant0 = TypedDict("WorkspaceUpdateResponseProductTypeVariant0", {"type": Required[Literal["ai_app", "media_generation", "developer_tool", "b2b_saas", "consumer_app", "marketplace", "game", "other"]], "other": NotRequired[str]}, total=False)

WorkspaceUpdateResponseDataRetention = TypedDict("WorkspaceUpdateResponseDataRetention", {"evidence_days": Required[int], "max_days": Required[int], "options": Required[list[int]]}, total=False)

WorkspaceUpdateResponse = TypedDict("WorkspaceUpdateResponse", {"object": Required[Literal["workspace_settings"]], "id": Required[str], "name": Required[str], "icon": Required[WorkspaceUpdateResponseIconVariant0 | None], "time_zone": Required[str | None], "website": Required[str | None], "product_type": Required[WorkspaceUpdateResponseProductTypeVariant0 | None], "data_retention": Required[WorkspaceUpdateResponseDataRetention]}, total=False)

WorkspaceIconUploadInput = TypedDict("WorkspaceIconUploadInput", {"image": Required[str]}, total=False)

WorkspaceIconUploadResponse = TypedDict("WorkspaceIconUploadResponse", {"object": Required[Literal["workspace_icon_upload"]], "id": Required[str], "state": Required[Literal["pending", "ready", "failed"]]}, total=False)

WorkspaceIconRemoveResponseIconVariant0 = TypedDict("WorkspaceIconRemoveResponseIconVariant0", {"updated_at": Required[str | None]}, total=False)

WorkspaceIconRemoveResponseProductTypeVariant0 = TypedDict("WorkspaceIconRemoveResponseProductTypeVariant0", {"type": Required[Literal["ai_app", "media_generation", "developer_tool", "b2b_saas", "consumer_app", "marketplace", "game", "other"]], "other": NotRequired[str]}, total=False)

WorkspaceIconRemoveResponseDataRetention = TypedDict("WorkspaceIconRemoveResponseDataRetention", {"evidence_days": Required[int], "max_days": Required[int], "options": Required[list[int]]}, total=False)

WorkspaceIconRemoveResponse = TypedDict("WorkspaceIconRemoveResponse", {"object": Required[Literal["workspace_settings"]], "id": Required[str], "name": Required[str], "icon": Required[WorkspaceIconRemoveResponseIconVariant0 | None], "time_zone": Required[str | None], "website": Required[str | None], "product_type": Required[WorkspaceIconRemoveResponseProductTypeVariant0 | None], "data_retention": Required[WorkspaceIconRemoveResponseDataRetention]}, total=False)

WorkspaceIconUploadGetResponse = TypedDict("WorkspaceIconUploadGetResponse", {"object": Required[Literal["workspace_icon_upload"]], "id": Required[str], "state": Required[Literal["pending", "ready", "failed"]]}, total=False)

WorkspaceRetentionInput = TypedDict("WorkspaceRetentionInput", {"evidence_days": Required[int]}, total=False)

WorkspaceRetentionResponseIconVariant0 = TypedDict("WorkspaceRetentionResponseIconVariant0", {"updated_at": Required[str | None]}, total=False)

WorkspaceRetentionResponseProductTypeVariant0 = TypedDict("WorkspaceRetentionResponseProductTypeVariant0", {"type": Required[Literal["ai_app", "media_generation", "developer_tool", "b2b_saas", "consumer_app", "marketplace", "game", "other"]], "other": NotRequired[str]}, total=False)

WorkspaceRetentionResponseDataRetention = TypedDict("WorkspaceRetentionResponseDataRetention", {"evidence_days": Required[int], "max_days": Required[int], "options": Required[list[int]]}, total=False)

WorkspaceRetentionResponse = TypedDict("WorkspaceRetentionResponse", {"object": Required[Literal["workspace_settings"]], "id": Required[str], "name": Required[str], "icon": Required[WorkspaceRetentionResponseIconVariant0 | None], "time_zone": Required[str | None], "website": Required[str | None], "product_type": Required[WorkspaceRetentionResponseProductTypeVariant0 | None], "data_retention": Required[WorkspaceRetentionResponseDataRetention]}, total=False)

WorkspaceSetupResponseStepsItem = TypedDict("WorkspaceSetupResponseStepsItem", {"step": Required[Literal["benefit", "server_key", "first_evaluation", "browser_script"]], "done": Required[bool]}, total=False)

WorkspaceSetupResponse = TypedDict("WorkspaceSetupResponse", {"object": Required[Literal["setup_progress"]], "steps": Required[list[WorkspaceSetupResponseStepsItem]], "complete": Required[bool], "finished": Required[bool], "dismissed": Required[bool | None]}, total=False)

WorkspaceSetupFinishInputProductTypeVariant0 = TypedDict("WorkspaceSetupFinishInputProductTypeVariant0", {"type": Required[Literal["ai_app", "media_generation", "developer_tool", "b2b_saas", "consumer_app", "marketplace", "game", "other"]], "other": NotRequired[str]}, total=False)

WorkspaceSetupFinishInput = TypedDict("WorkspaceSetupFinishInput", {"website": NotRequired[str | None], "product_type": NotRequired[WorkspaceSetupFinishInputProductTypeVariant0 | None], "time_zone": NotRequired[str | None]}, total=False)

WorkspaceSetupFinishResponseStepsItem = TypedDict("WorkspaceSetupFinishResponseStepsItem", {"step": Required[Literal["benefit", "server_key", "first_evaluation", "browser_script"]], "done": Required[bool]}, total=False)

WorkspaceSetupFinishResponse = TypedDict("WorkspaceSetupFinishResponse", {"object": Required[Literal["setup_progress"]], "steps": Required[list[WorkspaceSetupFinishResponseStepsItem]], "complete": Required[bool], "finished": Required[bool], "dismissed": Required[bool | None]}, total=False)

WorkspaceSetupDismissResponseStepsItem = TypedDict("WorkspaceSetupDismissResponseStepsItem", {"step": Required[Literal["benefit", "server_key", "first_evaluation", "browser_script"]], "done": Required[bool]}, total=False)

WorkspaceSetupDismissResponse = TypedDict("WorkspaceSetupDismissResponse", {"object": Required[Literal["setup_progress"]], "steps": Required[list[WorkspaceSetupDismissResponseStepsItem]], "complete": Required[bool], "finished": Required[bool], "dismissed": Required[bool | None]}, total=False)

WorkspaceLeaveResponse = TypedDict("WorkspaceLeaveResponse", {"object": Required[Literal["workspace_left"]], "workspace": Required[str]}, total=False)

EvaluationsListInput = TypedDict("EvaluationsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "result": NotRequired[Literal["allow", "deny"]], "benefit": NotRequired[str], "query": NotRequired[str], "days": NotRequired[int]}, total=False)

EvaluationsListResponseDataItem = TypedDict("EvaluationsListResponseDataItem", {"object": Required[str]}, total=False)

EvaluationsListResponse = TypedDict("EvaluationsListResponse", {"object": Required[Literal["list"]], "data": Required[list[EvaluationsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

EvaluationsCreateInputSubject = TypedDict("EvaluationsCreateInputSubject", {"external_id": NotRequired[str], "email": Required[str], "email_verified": NotRequired[bool]}, total=False)

EvaluationsCreateInputContextVariant0 = TypedDict("EvaluationsCreateInputContextVariant0", {"ip": NotRequired[str | None], "user_agent": NotRequired[str], "session_id": NotRequired[str]}, total=False)

EvaluationsCreateInputIdentifiersPayment = TypedDict("EvaluationsCreateInputIdentifiersPayment", {"provider": Required[str], "scope": Required[str], "fingerprint": Required[str]}, total=False)

EvaluationsCreateInputIdentifiersPhoneHash = TypedDict("EvaluationsCreateInputIdentifiersPhoneHash", {"algorithm": Required[Literal["hmac-sha256"]], "key_version": Required[str], "value": Required[str]}, total=False)

EvaluationsCreateInputIdentifiersCustomItemValueHash = TypedDict("EvaluationsCreateInputIdentifiersCustomItemValueHash", {"algorithm": Required[Literal["hmac-sha256"]], "key_version": Required[str], "value": Required[str]}, total=False)

EvaluationsCreateInputIdentifiersCustomItem = TypedDict("EvaluationsCreateInputIdentifiersCustomItem", {"key": Required[str], "value_hash": Required[EvaluationsCreateInputIdentifiersCustomItemValueHash]}, total=False)

EvaluationsCreateInputIdentifiers = TypedDict("EvaluationsCreateInputIdentifiers", {"device_id": NotRequired[str], "device_token": NotRequired[str], "browser_cookie_id": NotRequired[str], "payment": NotRequired[EvaluationsCreateInputIdentifiersPayment], "phone_hash": NotRequired[EvaluationsCreateInputIdentifiersPhoneHash], "phone_verified": NotRequired[bool], "custom": NotRequired[list[EvaluationsCreateInputIdentifiersCustomItem]]}, total=False)

EvaluationsCreateInputRequest = TypedDict("EvaluationsCreateInputRequest", {"method": Required[str], "url": Required[str], "headers": Required[dict[str, Any]]}, total=False)

EvaluationsCreateInput = TypedDict("EvaluationsCreateInput", {"benefit": Required[str], "claim_id": Required[str], "subject": Required[EvaluationsCreateInputSubject], "context": NotRequired[EvaluationsCreateInputContextVariant0 | None], "identifiers": NotRequired[EvaluationsCreateInputIdentifiers], "request": NotRequired[EvaluationsCreateInputRequest]}, total=False)

EvaluationsCreateResponseVariant0Risk = TypedDict("EvaluationsCreateResponseVariant0Risk", {"score": Required[float | None], "band": Required[Literal["low", "elevated", "high", "not_assessed"]]}, total=False)

EvaluationsCreateResponseVariant0ReasonVariant0 = TypedDict("EvaluationsCreateResponseVariant0ReasonVariant0", {"code": Required[str], "message": Required[str], "rule": NotRequired[str]}, total=False)

EvaluationsCreateResponseVariant0OutcomeVariant0 = TypedDict("EvaluationsCreateResponseVariant0OutcomeVariant0", {"state": Required[str], "due_at": Required[str | None]}, total=False)

EvaluationsCreateResponseVariant0 = TypedDict("EvaluationsCreateResponseVariant0", {"object": Required[Literal["evaluation"]], "id": Required[str], "result": Required[Literal["allow", "deny"]], "risk": Required[EvaluationsCreateResponseVariant0Risk], "reason": Required[EvaluationsCreateResponseVariant0ReasonVariant0 | None], "outcome": NotRequired[EvaluationsCreateResponseVariant0OutcomeVariant0 | None]}, total=False)

EvaluationsCreateResponseVariant1 = TypedDict("EvaluationsCreateResponseVariant1", {"object": Required[Literal["evaluation"]], "status": Required[Literal["skipped"]], "reason": Required[Literal["billing_overdue", "service_inactive", "insufficient_credits", "benefit_paused"]]}, total=False)

EvaluationsFiltersInput = TypedDict("EvaluationsFiltersInput", {"days": NotRequired[int]}, total=False)

EvaluationsFiltersResponseReasonsItem = TypedDict("EvaluationsFiltersResponseReasonsItem", {"code": Required[str], "label": Required[str]}, total=False)

EvaluationsFiltersResponse = TypedDict("EvaluationsFiltersResponse", {"object": Required[Literal["evaluation_filters"]], "days": Required[int | None], "benefits": Required[list[str]], "results": Required[list[Literal["allow", "deny"]]], "reasons": Required[list[EvaluationsFiltersResponseReasonsItem]]}, total=False)

EvaluationsGetResponseReasonVariant0 = TypedDict("EvaluationsGetResponseReasonVariant0", {"code": Required[str], "message": Required[str], "rule": NotRequired[str]}, total=False)

EvaluationsGetResponseOutcome = TypedDict("EvaluationsGetResponseOutcome", {"state": Required[str | None], "due_at": NotRequired[str | None]}, total=False)

EvaluationsGetResponseRisk = TypedDict("EvaluationsGetResponseRisk", {"score": Required[float | None], "band": Required[Literal["low", "elevated", "high", "not_assessed"]]}, total=False)

EvaluationsGetResponseInputs = TypedDict("EvaluationsGetResponseInputs", {"email": Required[Literal["received", "missing"]], "ip": Required[Literal["received", "missing"]], "user_id": Required[Literal["received", "missing"]], "phone": Required[Literal["received", "missing"]], "payment": Required[Literal["received", "missing"]], "device": Required[Literal["received", "missing"]], "browser": Required[Literal["received", "missing"]]}, total=False)

EvaluationsGetResponsePolicy = TypedDict("EvaluationsGetResponsePolicy", {"id": Required[str | None], "version": Required[float | None]}, total=False)

EvaluationsGetResponseAccessListEntryVariant0 = TypedDict("EvaluationsGetResponseAccessListEntryVariant0", {"id": Required[str | None], "kind": Required[Literal["allow", "block"]], "type": Required[str | None], "value": Required[str | None]}, total=False)

EvaluationsGetResponse = TypedDict("EvaluationsGetResponse", {"object": Required[Literal["evaluation"]], "id": Required[str], "benefit": Required[str | None], "claim_id": Required[str | None], "result": Required[Literal["allow", "deny"]], "reason": Required[EvaluationsGetResponseReasonVariant0 | None], "outcome": Required[EvaluationsGetResponseOutcome], "policy_version": Required[float | None], "created_at": Required[str | None], "mode": Required[Literal["protect", "observe"]], "observed_result": NotRequired[Literal["allow", "deny"] | None], "risk": Required[EvaluationsGetResponseRisk], "inputs": Required[EvaluationsGetResponseInputs], "browser_data": Required[Literal["collected", "consent_declined", "not_loaded", "blocked", "timed_out", "failed", "site_not_listed", "sdk_outdated", "expired", "not_passed_on", "not_sent"] | None], "policy": Required[EvaluationsGetResponsePolicy], "access_list_entry": Required[EvaluationsGetResponseAccessListEntryVariant0 | None]}, total=False)

EvaluationsGraphResponse = TypedDict("EvaluationsGraphResponse", {"object": Required[str]}, total=False)

EvaluationsEvidenceResponseReasonVariant0 = TypedDict("EvaluationsEvidenceResponseReasonVariant0", {"code": Required[str], "message": Required[str], "rule": NotRequired[str]}, total=False)

EvaluationsEvidenceResponseOutcome = TypedDict("EvaluationsEvidenceResponseOutcome", {"state": Required[str | None], "due_at": NotRequired[str | None]}, total=False)

EvaluationsEvidenceResponseRisk = TypedDict("EvaluationsEvidenceResponseRisk", {"score": Required[float | None], "band": Required[Literal["low", "elevated", "high", "not_assessed"]]}, total=False)

EvaluationsEvidenceResponseSignalsItem = TypedDict("EvaluationsEvidenceResponseSignalsItem", {"family": Required[Literal["identity", "device", "network", "benefit_history"]], "assessment": Required[Literal["clear", "elevated", "high", "unavailable"]]}, total=False)

EvaluationsEvidenceResponseInputs = TypedDict("EvaluationsEvidenceResponseInputs", {"email": Required[Literal["received", "missing"]], "ip": Required[Literal["received", "missing"]], "user_id": Required[Literal["received", "missing"]], "phone": Required[Literal["received", "missing"]], "payment": Required[Literal["received", "missing"]], "device": Required[Literal["received", "missing"]], "browser": Required[Literal["received", "missing"]]}, total=False)

EvaluationsEvidenceResponsePolicy = TypedDict("EvaluationsEvidenceResponsePolicy", {"id": Required[str | None], "version": Required[float | None]}, total=False)

EvaluationsEvidenceResponseAccessListEntryVariant0 = TypedDict("EvaluationsEvidenceResponseAccessListEntryVariant0", {"id": Required[str | None], "kind": Required[Literal["allow", "block"]], "type": Required[str | None], "value": Required[str | None]}, total=False)

EvaluationsEvidenceResponseEvidenceDeviceProfile = TypedDict("EvaluationsEvidenceResponseEvidenceDeviceProfile", {"status": Required[Literal["captured", "not_retained"]], "expires_at": Required[str | None]}, total=False)

EvaluationsEvidenceResponseEvidence = TypedDict("EvaluationsEvidenceResponseEvidence", {"request": Required[dict[str, Any] | None], "device_profile": Required[EvaluationsEvidenceResponseEvidenceDeviceProfile]}, total=False)

EvaluationsEvidenceResponse = TypedDict("EvaluationsEvidenceResponse", {"object": Required[Literal["evaluation"]], "id": Required[str], "benefit": Required[str | None], "claim_id": Required[str | None], "result": Required[Literal["allow", "deny"]], "reason": Required[EvaluationsEvidenceResponseReasonVariant0 | None], "outcome": Required[EvaluationsEvidenceResponseOutcome], "policy_version": Required[float | None], "created_at": Required[str | None], "mode": Required[Literal["protect", "observe"]], "observed_result": NotRequired[Literal["allow", "deny"] | None], "risk": Required[EvaluationsEvidenceResponseRisk], "signals": Required[list[EvaluationsEvidenceResponseSignalsItem]], "inputs": Required[EvaluationsEvidenceResponseInputs], "browser_data": Required[Literal["collected", "consent_declined", "not_loaded", "blocked", "timed_out", "failed", "site_not_listed", "sdk_outdated", "expired", "not_passed_on", "not_sent"] | None], "policy": Required[EvaluationsEvidenceResponsePolicy], "access_list_entry": Required[EvaluationsEvidenceResponseAccessListEntryVariant0 | None], "evidence": Required[EvaluationsEvidenceResponseEvidence]}, total=False)

OutcomesListInput = TypedDict("OutcomesListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

OutcomesListResponseDataItem = TypedDict("OutcomesListResponseDataItem", {"object": Required[str]}, total=False)

OutcomesListResponse = TypedDict("OutcomesListResponse", {"object": Required[Literal["list"]], "data": Required[list[OutcomesListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

OutcomesGetResponse = TypedDict("OutcomesGetResponse", {"object": Required[str]}, total=False)

OutcomesReportInput = TypedDict("OutcomesReportInput", {"outcome": Required[Literal["granted", "not_granted", "reversed"]], "reason": NotRequired[str], "external_outcome_id": NotRequired[str]}, total=False)

OutcomesReportResponse = TypedDict("OutcomesReportResponse", {"object": Required[str]}, total=False)

EvaluationsDryRunInputSubject = TypedDict("EvaluationsDryRunInputSubject", {"external_id": NotRequired[str], "email": Required[str], "email_verified": NotRequired[bool]}, total=False)

EvaluationsDryRunInputContextVariant0 = TypedDict("EvaluationsDryRunInputContextVariant0", {"ip": NotRequired[str | None], "user_agent": NotRequired[str], "session_id": NotRequired[str]}, total=False)

EvaluationsDryRunInputIdentifiersPayment = TypedDict("EvaluationsDryRunInputIdentifiersPayment", {"provider": Required[str], "scope": Required[str], "fingerprint": Required[str]}, total=False)

EvaluationsDryRunInputIdentifiersPhoneHash = TypedDict("EvaluationsDryRunInputIdentifiersPhoneHash", {"algorithm": Required[Literal["hmac-sha256"]], "key_version": Required[str], "value": Required[str]}, total=False)

EvaluationsDryRunInputIdentifiersCustomItemValueHash = TypedDict("EvaluationsDryRunInputIdentifiersCustomItemValueHash", {"algorithm": Required[Literal["hmac-sha256"]], "key_version": Required[str], "value": Required[str]}, total=False)

EvaluationsDryRunInputIdentifiersCustomItem = TypedDict("EvaluationsDryRunInputIdentifiersCustomItem", {"key": Required[str], "value_hash": Required[EvaluationsDryRunInputIdentifiersCustomItemValueHash]}, total=False)

EvaluationsDryRunInputIdentifiers = TypedDict("EvaluationsDryRunInputIdentifiers", {"device_id": NotRequired[str], "device_token": NotRequired[str], "browser_cookie_id": NotRequired[str], "payment": NotRequired[EvaluationsDryRunInputIdentifiersPayment], "phone_hash": NotRequired[EvaluationsDryRunInputIdentifiersPhoneHash], "phone_verified": NotRequired[bool], "custom": NotRequired[list[EvaluationsDryRunInputIdentifiersCustomItem]]}, total=False)

EvaluationsDryRunInputRequest = TypedDict("EvaluationsDryRunInputRequest", {"method": Required[str], "url": Required[str], "headers": Required[dict[str, Any]]}, total=False)

EvaluationsDryRunInput = TypedDict("EvaluationsDryRunInput", {"benefit": Required[str], "claim_id": Required[str], "subject": Required[EvaluationsDryRunInputSubject], "context": NotRequired[EvaluationsDryRunInputContextVariant0 | None], "identifiers": NotRequired[EvaluationsDryRunInputIdentifiers], "request": NotRequired[EvaluationsDryRunInputRequest]}, total=False)

EvaluationsDryRunResponseVariant0Risk = TypedDict("EvaluationsDryRunResponseVariant0Risk", {"score": Required[float | None], "band": Required[Literal["low", "elevated", "high", "not_assessed"]]}, total=False)

EvaluationsDryRunResponseVariant0ReasonVariant0 = TypedDict("EvaluationsDryRunResponseVariant0ReasonVariant0", {"code": Required[str], "message": Required[str], "rule": NotRequired[str]}, total=False)

EvaluationsDryRunResponseVariant0Inputs = TypedDict("EvaluationsDryRunResponseVariant0Inputs", {"email": Required[Literal["received", "missing"]], "ip": Required[Literal["received", "missing"]], "user_id": Required[Literal["received", "missing"]], "phone": Required[Literal["received", "missing"]], "payment": Required[Literal["received", "missing"]], "device": Required[Literal["received", "missing"]], "browser": Required[Literal["received", "missing"]]}, total=False)

EvaluationsDryRunResponseVariant0 = TypedDict("EvaluationsDryRunResponseVariant0", {"object": Required[Literal["evaluation_dry_run"]], "dry_run": Required[Literal[True]], "result": Required[Literal["allow", "deny"]], "risk": Required[EvaluationsDryRunResponseVariant0Risk], "reason": Required[EvaluationsDryRunResponseVariant0ReasonVariant0 | None], "inputs": Required[EvaluationsDryRunResponseVariant0Inputs]}, total=False)

EvaluationsDryRunResponseVariant1 = TypedDict("EvaluationsDryRunResponseVariant1", {"object": Required[Literal["evaluation_dry_run"]], "status": Required[Literal["skipped"]], "reason": Required[Literal["billing_overdue", "service_inactive", "insufficient_credits", "benefit_paused"]]}, total=False)

SimulationsSequenceInput = TypedDict("SimulationsSequenceInput", {"benefit_id": Required[str], "policy_key": Required[str]}, total=False)

SimulationsSequenceResponse = TypedDict("SimulationsSequenceResponse", {"object": Required[str]}, total=False)

SimulationsReplayInput = TypedDict("SimulationsReplayInput", {"benefit_id": Required[str], "policy_key": Required[str]}, total=False)

SimulationsReplayResponse = TypedDict("SimulationsReplayResponse", {"object": Required[str]}, total=False)

BenefitsListInput = TypedDict("BenefitsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

BenefitsListResponseDataItem = TypedDict("BenefitsListResponseDataItem", {"object": Required[str]}, total=False)

BenefitsListResponse = TypedDict("BenefitsListResponse", {"object": Required[Literal["list"]], "data": Required[list[BenefitsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

BenefitsCreateInputConfigEligibilityVariant0 = TypedDict("BenefitsCreateInputConfigEligibilityVariant0", {"kind": Required[Literal["once"]]}, total=False)

BenefitsCreateInputConfigEligibilityVariant1 = TypedDict("BenefitsCreateInputConfigEligibilityVariant1", {"kind": Required[Literal["calendar"]], "period": Required[Literal["day", "week", "month"]], "timezone": Required[str]}, total=False)

BenefitsCreateInputConfigEligibilityVariant2 = TypedDict("BenefitsCreateInputConfigEligibilityVariant2", {"kind": Required[Literal["rolling"]], "days": Required[int]}, total=False)

BenefitsCreateInputConfigValue = TypedDict("BenefitsCreateInputConfigValue", {"amount": Required[float], "currency": Required[Literal["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWG"]]}, total=False)

BenefitsCreateInputConfig = TypedDict("BenefitsCreateInputConfig", {"automation": NotRequired[Literal["allow_safe_automation", "allow_verified_agents", "deny_all_automation"]], "outcome_tracking": NotRequired[Literal["assume_granted", "report_outcome"]], "missing_outcome_behavior": NotRequired[Literal["hold_eligibility", "release_eligibility"]], "eligibility": NotRequired[BenefitsCreateInputConfigEligibilityVariant0 | BenefitsCreateInputConfigEligibilityVariant1 | BenefitsCreateInputConfigEligibilityVariant2], "value": NotRequired[BenefitsCreateInputConfigValue]}, total=False)

BenefitsCreateInput = TypedDict("BenefitsCreateInput", {"name": Required[str], "key": Required[str], "config": Required[BenefitsCreateInputConfig], "policy_key": Required[str], "protection_mode": Required[Literal["protect", "observe"]]}, total=False)

BenefitsCreateResponse = TypedDict("BenefitsCreateResponse", {"object": Required[str]}, total=False)

BenefitsGetResponse = TypedDict("BenefitsGetResponse", {"object": Required[str]}, total=False)

BenefitsUpdateInputConfigEligibilityVariant0 = TypedDict("BenefitsUpdateInputConfigEligibilityVariant0", {"kind": Required[Literal["once"]]}, total=False)

BenefitsUpdateInputConfigEligibilityVariant1 = TypedDict("BenefitsUpdateInputConfigEligibilityVariant1", {"kind": Required[Literal["calendar"]], "period": Required[Literal["day", "week", "month"]], "timezone": Required[str]}, total=False)

BenefitsUpdateInputConfigEligibilityVariant2 = TypedDict("BenefitsUpdateInputConfigEligibilityVariant2", {"kind": Required[Literal["rolling"]], "days": Required[int]}, total=False)

BenefitsUpdateInputConfigValue = TypedDict("BenefitsUpdateInputConfigValue", {"amount": Required[float], "currency": Required[Literal["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWG"]]}, total=False)

BenefitsUpdateInputConfig = TypedDict("BenefitsUpdateInputConfig", {"automation": NotRequired[Literal["allow_safe_automation", "allow_verified_agents", "deny_all_automation"]], "outcome_tracking": NotRequired[Literal["assume_granted", "report_outcome"]], "missing_outcome_behavior": NotRequired[Literal["hold_eligibility", "release_eligibility"]], "eligibility": NotRequired[BenefitsUpdateInputConfigEligibilityVariant0 | BenefitsUpdateInputConfigEligibilityVariant1 | BenefitsUpdateInputConfigEligibilityVariant2], "value": NotRequired[BenefitsUpdateInputConfigValue]}, total=False)

BenefitsUpdateInput = TypedDict("BenefitsUpdateInput", {"name": Required[str], "config": Required[BenefitsUpdateInputConfig], "policy_key": Required[str], "protection_mode": Required[Literal["protect", "observe"]], "revision": Required[int]}, total=False)

BenefitsUpdateResponse = TypedDict("BenefitsUpdateResponse", {"object": Required[str]}, total=False)

BenefitsDeleteResponse = TypedDict("BenefitsDeleteResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

PoliciesListInput = TypedDict("PoliciesListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

PoliciesListResponseDataItem = TypedDict("PoliciesListResponseDataItem", {"object": Required[str]}, total=False)

PoliciesListResponse = TypedDict("PoliciesListResponse", {"object": Required[Literal["list"]], "data": Required[list[PoliciesListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PoliciesCreateInputDefinitionRulesItem = TypedDict("PoliciesCreateInputDefinitionRulesItem", {"id": Required[str], "name": Required[str], "result": Required[Literal["allow", "deny"]], "when": Required[Any], "enabled": NotRequired[bool], "note": NotRequired[str]}, total=False)

PoliciesCreateInputDefinition = TypedDict("PoliciesCreateInputDefinition", {"base": NotRequired[Literal["balanced", "lenient", "strict"]], "risk_threshold": NotRequired[int | None], "default_result": Required[Literal["allow", "deny"]], "rules": Required[list[PoliciesCreateInputDefinitionRulesItem]]}, total=False)

PoliciesCreateInput = TypedDict("PoliciesCreateInput", {"name": Required[str], "key": Required[str], "definition": Required[PoliciesCreateInputDefinition]}, total=False)

PoliciesCreateResponse = TypedDict("PoliciesCreateResponse", {"object": Required[str]}, total=False)

PoliciesGetResponse = TypedDict("PoliciesGetResponse", {"object": Required[str]}, total=False)

PoliciesUpdateInputDefinitionRulesItem = TypedDict("PoliciesUpdateInputDefinitionRulesItem", {"id": Required[str], "name": Required[str], "result": Required[Literal["allow", "deny"]], "when": Required[Any], "enabled": NotRequired[bool], "note": NotRequired[str]}, total=False)

PoliciesUpdateInputDefinition = TypedDict("PoliciesUpdateInputDefinition", {"base": NotRequired[Literal["balanced", "lenient", "strict"]], "risk_threshold": NotRequired[int | None], "default_result": Required[Literal["allow", "deny"]], "rules": Required[list[PoliciesUpdateInputDefinitionRulesItem]]}, total=False)

PoliciesUpdateInput = TypedDict("PoliciesUpdateInput", {"name": Required[str], "definition": Required[PoliciesUpdateInputDefinition], "revision": Required[int], "restored_from": NotRequired[int]}, total=False)

PoliciesUpdateResponse = TypedDict("PoliciesUpdateResponse", {"object": Required[str]}, total=False)

PoliciesDeleteResponse = TypedDict("PoliciesDeleteResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

PoliciesDuplicateInput = TypedDict("PoliciesDuplicateInput", {"name": Required[str], "key": Required[str]}, total=False)

PoliciesDuplicateResponse = TypedDict("PoliciesDuplicateResponse", {"object": Required[str]}, total=False)

PoliciesVersionsResponseDataItem = TypedDict("PoliciesVersionsResponseDataItem", {"object": Required[str]}, total=False)

PoliciesVersionsResponse = TypedDict("PoliciesVersionsResponse", {"object": Required[Literal["list"]], "data": Required[list[PoliciesVersionsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

PoliciesVersionResponse = TypedDict("PoliciesVersionResponse", {"object": Required[str]}, total=False)

PoliciesSignalsResponseDataItem = TypedDict("PoliciesSignalsResponseDataItem", {"object": Required[str]}, total=False)

PoliciesSignalsResponse = TypedDict("PoliciesSignalsResponse", {"object": Required[Literal["list"]], "data": Required[list[PoliciesSignalsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

AccessListsListInput = TypedDict("AccessListsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "value": NotRequired[str]}, total=False)

AccessListsListResponseDataItem = TypedDict("AccessListsListResponseDataItem", {"object": Required[str]}, total=False)

AccessListsListResponse = TypedDict("AccessListsListResponse", {"object": Required[Literal["list"]], "data": Required[list[AccessListsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

AccessListsCreateInput = TypedDict("AccessListsCreateInput", {"kind": Required[Literal["allow", "block"]], "type": Required[Literal["email", "domain", "ip", "user", "device_id"]], "value": NotRequired[str], "values": NotRequired[list[str]], "benefit_ids": NotRequired[list[str]], "reason": Required[str], "expires_at": NotRequired[str | None], "expires_in_days": NotRequired[int | None]}, total=False)

AccessListsCreateResponse = TypedDict("AccessListsCreateResponse", {"object": Required[str]}, total=False)

AccessListsGetResponse = TypedDict("AccessListsGetResponse", {"object": Required[str]}, total=False)

AccessListsDeleteResponse = TypedDict("AccessListsDeleteResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

AccessListsUpdateInput = TypedDict("AccessListsUpdateInput", {"kind": NotRequired[Literal["allow", "block"]], "benefit_ids": NotRequired[list[str]], "reason": NotRequired[str], "expires_at": NotRequired[str | None], "expires_in_days": NotRequired[int | None]}, total=False)

AccessListsUpdateResponse = TypedDict("AccessListsUpdateResponse", {"object": Required[str]}, total=False)

IdentifiersLookupInput = TypedDict("IdentifiersLookupInput", {"value": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant0 = TypedDict("IdentifiersLookupResponseMatchesItemVariant0", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["evaluation"]], "id": Required[str], "result": Required[Literal["allow", "deny"] | None], "benefit": Required[str | None]}, total=False)

IdentifiersLookupResponseMatchesItemVariant1 = TypedDict("IdentifiersLookupResponseMatchesItemVariant1", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["evaluations"]], "count": Required[int], "capped": Required[bool], "days": Required[Literal[90]]}, total=False)

IdentifiersLookupResponseMatchesItemVariant2 = TypedDict("IdentifiersLookupResponseMatchesItemVariant2", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["claim_history"]], "count": Required[int], "capped": Required[bool]}, total=False)

IdentifiersLookupResponseMatchesItemVariant3 = TypedDict("IdentifiersLookupResponseMatchesItemVariant3", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["benefit"]], "id": Required[str], "key": Required[str], "name": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant4 = TypedDict("IdentifiersLookupResponseMatchesItemVariant4", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["policy"]], "id": Required[str], "key": Required[str], "name": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant5 = TypedDict("IdentifiersLookupResponseMatchesItemVariant5", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["protection_level"]], "id": Required[str], "key": Required[str], "name": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant6 = TypedDict("IdentifiersLookupResponseMatchesItemVariant6", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["access_list_entry"]], "id": Required[str], "list": Required[Literal["allow", "block"]], "type": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant7 = TypedDict("IdentifiersLookupResponseMatchesItemVariant7", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["api_key"]], "id": Required[str], "name": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant8 = TypedDict("IdentifiersLookupResponseMatchesItemVariant8", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["webhook_endpoint"]], "id": Required[str], "url": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant9 = TypedDict("IdentifiersLookupResponseMatchesItemVariant9", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["member"]], "id": Required[str], "email": Required[str]}, total=False)

IdentifiersLookupResponseMatchesItemVariant10 = TypedDict("IdentifiersLookupResponseMatchesItemVariant10", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["import"]], "id": Required[str], "file_name": Required[str | None]}, total=False)

IdentifiersLookupResponseMatchesItemVariant11 = TypedDict("IdentifiersLookupResponseMatchesItemVariant11", {"object": Required[Literal["lookup_match"]], "kind": Required[Literal["custom_identifier"]], "id": Required[str], "key": Required[str]}, total=False)

IdentifiersLookupResponse = TypedDict("IdentifiersLookupResponse", {"object": Required[Literal["lookup"]], "type": Required[Literal["id", "email", "ip"] | None], "matches": Required[list[IdentifiersLookupResponseMatchesItemVariant0 | IdentifiersLookupResponseMatchesItemVariant1 | IdentifiersLookupResponseMatchesItemVariant2 | IdentifiersLookupResponseMatchesItemVariant3 | IdentifiersLookupResponseMatchesItemVariant4 | IdentifiersLookupResponseMatchesItemVariant5 | IdentifiersLookupResponseMatchesItemVariant6 | IdentifiersLookupResponseMatchesItemVariant7 | IdentifiersLookupResponseMatchesItemVariant8 | IdentifiersLookupResponseMatchesItemVariant9 | IdentifiersLookupResponseMatchesItemVariant10 | IdentifiersLookupResponseMatchesItemVariant11]]}, total=False)

CustomIdentifiersListInput = TypedDict("CustomIdentifiersListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

CustomIdentifiersListResponseDataItem = TypedDict("CustomIdentifiersListResponseDataItem", {"object": Required[str]}, total=False)

CustomIdentifiersListResponse = TypedDict("CustomIdentifiersListResponse", {"object": Required[Literal["list"]], "data": Required[list[CustomIdentifiersListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

CustomIdentifiersCreateInput = TypedDict("CustomIdentifiersCreateInput", {"key": Required[str], "key_version": Required[str], "description": Required[str]}, total=False)

CustomIdentifiersCreateResponse = TypedDict("CustomIdentifiersCreateResponse", {"object": Required[str]}, total=False)

CustomIdentifiersGetResponse = TypedDict("CustomIdentifiersGetResponse", {"object": Required[str]}, total=False)

CustomIdentifiersDeleteResponse = TypedDict("CustomIdentifiersDeleteResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

ImportsListInput = TypedDict("ImportsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

ImportsListResponseDataItem = TypedDict("ImportsListResponseDataItem", {"object": Required[str]}, total=False)

ImportsListResponse = TypedDict("ImportsListResponse", {"object": Required[Literal["list"]], "data": Required[list[ImportsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

ImportsCreateInputRowsItemSubject = TypedDict("ImportsCreateInputRowsItemSubject", {"email": Required[str], "external_id": NotRequired[str]}, total=False)

ImportsCreateInputRowsItemIdentifiersPayment = TypedDict("ImportsCreateInputRowsItemIdentifiersPayment", {"provider": Required[str], "scope": Required[str], "fingerprint": Required[str]}, total=False)

ImportsCreateInputRowsItemIdentifiers = TypedDict("ImportsCreateInputRowsItemIdentifiers", {"payment": NotRequired[ImportsCreateInputRowsItemIdentifiersPayment]}, total=False)

ImportsCreateInputRowsItem = TypedDict("ImportsCreateInputRowsItem", {"benefit": NotRequired[str], "subject": Required[ImportsCreateInputRowsItemSubject], "granted_on": NotRequired[str], "granted_time": NotRequired[str], "occurred_at": NotRequired[str], "claim_id": NotRequired[str], "identifiers": NotRequired[ImportsCreateInputRowsItemIdentifiers]}, total=False)

ImportsCreateInput = TypedDict("ImportsCreateInput", {"rows": Required[list[ImportsCreateInputRowsItem]], "benefit": NotRequired[str], "time_zone": NotRequired[str], "file_name": NotRequired[str], "confirm": NotRequired[bool]}, total=False)

ImportsCreateResponse = TypedDict("ImportsCreateResponse", {"object": Required[str]}, total=False)

ImportsCsvInputPayment = TypedDict("ImportsCsvInputPayment", {"provider": Required[str], "scope": Required[str]}, total=False)

ImportsCsvInput = TypedDict("ImportsCsvInput", {"benefit": NotRequired[str], "time_zone": NotRequired[str], "file_name": NotRequired[str], "rows": NotRequired[int], "payment": NotRequired[ImportsCsvInputPayment], "confirm": NotRequired[bool]}, total=False)

ImportsCsvResponse = TypedDict("ImportsCsvResponse", {"object": Required[str]}, total=False)

ImportsGetResponse = TypedDict("ImportsGetResponse", {"object": Required[str]}, total=False)

ImportsProblemsInput = TypedDict("ImportsProblemsInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

ImportsProblemsResponseDataItem = TypedDict("ImportsProblemsResponseDataItem", {"object": Required[str]}, total=False)

ImportsProblemsResponse = TypedDict("ImportsProblemsResponse", {"object": Required[Literal["list"]], "data": Required[list[ImportsProblemsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

ImportsProblemsDownloadResponse = TypedDict("ImportsProblemsDownloadResponse", {"object": Required[Literal["import_problems_download"]], "url": Required[str]}, total=False)

ImportsConfirmResponse = TypedDict("ImportsConfirmResponse", {"object": Required[str]}, total=False)

ImportsDiscardResponse = TypedDict("ImportsDiscardResponse", {"object": Required[str]}, total=False)

ImportsFixRowInputCells = TypedDict("ImportsFixRowInputCells", {"email": NotRequired[str], "benefit": NotRequired[str], "granted_on": NotRequired[str], "granted_time": NotRequired[str], "occurred_at": NotRequired[str], "user_id": NotRequired[str], "claim_id": NotRequired[str], "payment_fingerprint": NotRequired[str]}, total=False)

ImportsFixRowInput = TypedDict("ImportsFixRowInput", {"row": Required[int], "cells": Required[ImportsFixRowInputCells]}, total=False)

ImportsFixRowResponse = TypedDict("ImportsFixRowResponse", {"object": Required[Literal["import_row"]], "import": Required[str], "row": Required[int], "state": Required[Literal["ready", "present", "attention", "skipped"]], "kind": Required[str | None], "field": Required[str | None]}, total=False)

ImportsSkipRowInput = TypedDict("ImportsSkipRowInput", {"row": Required[int]}, total=False)

ImportsSkipRowResponse = TypedDict("ImportsSkipRowResponse", {"object": Required[str]}, total=False)

ExportsListInput = TypedDict("ExportsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

ExportsListResponseDataItem = TypedDict("ExportsListResponseDataItem", {"object": Required[str]}, total=False)

ExportsListResponse = TypedDict("ExportsListResponse", {"object": Required[Literal["list"]], "data": Required[list[ExportsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

ExportsCreateInput = TypedDict("ExportsCreateInput", {"days": NotRequired[int], "include_evidence": NotRequired[bool]}, total=False)

ExportsCreateResponse = TypedDict("ExportsCreateResponse", {"object": Required[str], "id": Required[str], "status": Required[str], "status_url": Required[str]}, total=False)

ExportsGetResponse = TypedDict("ExportsGetResponse", {"object": Required[str]}, total=False)

ExportsDownloadResponse = TypedDict("ExportsDownloadResponse", {"object": Required[str]}, total=False)

WorkspaceExportsCreateInput = TypedDict("WorkspaceExportsCreateInput", {"password": Required[str], "encryption": NotRequired[Literal["standard", "aes256"]]}, total=False)

WorkspaceExportsCreateResponseExportVariant0 = TypedDict("WorkspaceExportsCreateResponseExportVariant0", {"id": Required[str], "state": Required[Literal["building", "complete", "expired", "failed", "deleted"]], "requested_by_you": Required[bool], "requested_at": Required[str | None], "completed_at": Required[str | None], "expires_at": Required[str | None], "parts": Required[int | None], "bytes": Required[int | None], "can_delete": Required[bool]}, total=False)

WorkspaceExportsCreateResponse = TypedDict("WorkspaceExportsCreateResponse", {"object": Required[Literal["workspace_export_status"]], "export": Required[WorkspaceExportsCreateResponseExportVariant0 | None], "next_allowed_at": Required[str | None]}, total=False)

WorkspaceExportsStatusResponseExportVariant0 = TypedDict("WorkspaceExportsStatusResponseExportVariant0", {"id": Required[str], "state": Required[Literal["building", "complete", "expired", "failed", "deleted"]], "requested_by_you": Required[bool], "requested_at": Required[str | None], "completed_at": Required[str | None], "expires_at": Required[str | None], "parts": Required[int | None], "bytes": Required[int | None], "can_delete": Required[bool]}, total=False)

WorkspaceExportsStatusResponse = TypedDict("WorkspaceExportsStatusResponse", {"object": Required[Literal["workspace_export_status"]], "export": Required[WorkspaceExportsStatusResponseExportVariant0 | None], "next_allowed_at": Required[str | None]}, total=False)

WorkspaceExportsDownloadResponsePartsItem = TypedDict("WorkspaceExportsDownloadResponsePartsItem", {"part": Required[int], "bytes": Required[int], "file_name": Required[str], "url": Required[str]}, total=False)

WorkspaceExportsDownloadResponse = TypedDict("WorkspaceExportsDownloadResponse", {"object": Required[Literal["workspace_export_download"]], "id": Required[str], "expires_at": Required[str | None], "links_expire_at": Required[str | None], "parts": Required[list[WorkspaceExportsDownloadResponsePartsItem]]}, total=False)

WorkspaceExportsDeleteResponseExportVariant0 = TypedDict("WorkspaceExportsDeleteResponseExportVariant0", {"id": Required[str], "state": Required[Literal["building", "complete", "expired", "failed", "deleted"]], "requested_by_you": Required[bool], "requested_at": Required[str | None], "completed_at": Required[str | None], "expires_at": Required[str | None], "parts": Required[int | None], "bytes": Required[int | None], "can_delete": Required[bool]}, total=False)

WorkspaceExportsDeleteResponse = TypedDict("WorkspaceExportsDeleteResponse", {"object": Required[Literal["workspace_export_status"]], "export": Required[WorkspaceExportsDeleteResponseExportVariant0 | None], "next_allowed_at": Required[str | None]}, total=False)

DeletionsDryRunInputSelectorVariant0 = TypedDict("DeletionsDryRunInputSelectorVariant0", {"kind": Required[Literal["subject"]], "user": Required[str], "email": Required[bool]}, total=False)

DeletionsDryRunInputSelectorVariant1 = TypedDict("DeletionsDryRunInputSelectorVariant1", {"kind": Required[Literal["workspace"]]}, total=False)

DeletionsDryRunInput = TypedDict("DeletionsDryRunInput", {"selector": Required[DeletionsDryRunInputSelectorVariant0 | DeletionsDryRunInputSelectorVariant1]}, total=False)

DeletionsDryRunResponse = TypedDict("DeletionsDryRunResponse", {"object": Required[str]}, total=False)

DeletionsListInput = TypedDict("DeletionsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

DeletionsListResponseDataItem = TypedDict("DeletionsListResponseDataItem", {"object": Required[str]}, total=False)

DeletionsListResponse = TypedDict("DeletionsListResponse", {"object": Required[Literal["list"]], "data": Required[list[DeletionsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

DeletionsCreateInputSelectorVariant0 = TypedDict("DeletionsCreateInputSelectorVariant0", {"kind": Required[Literal["subject"]], "user": Required[str], "email": Required[bool]}, total=False)

DeletionsCreateInputSelectorVariant1 = TypedDict("DeletionsCreateInputSelectorVariant1", {"kind": Required[Literal["workspace"]]}, total=False)

DeletionsCreateInput = TypedDict("DeletionsCreateInput", {"selector": Required[DeletionsCreateInputSelectorVariant0 | DeletionsCreateInputSelectorVariant1]}, total=False)

DeletionsCreateResponse = TypedDict("DeletionsCreateResponse", {"object": Required[str], "id": Required[str], "status": Required[str], "status_url": Required[str]}, total=False)

DeletionsGetResponse = TypedDict("DeletionsGetResponse", {"object": Required[str]}, total=False)

AnalyticsListInput = TypedDict("AnalyticsListInput", {"days": NotRequired[int]}, total=False)

AnalyticsListResponseDataItem = TypedDict("AnalyticsListResponseDataItem", {"object": Required[str]}, total=False)

AnalyticsListResponse = TypedDict("AnalyticsListResponse", {"object": Required[Literal["list"]], "data": Required[list[AnalyticsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

OverviewGetResponseEvaluations = TypedDict("OverviewGetResponseEvaluations", {"total": Required[int], "allowed": Required[int], "denied": Required[int], "waiting_for_confirmation": Required[int]}, total=False)

OverviewGetResponsePrevious = TypedDict("OverviewGetResponsePrevious", {"total": Required[int], "allowed": Required[int], "denied": Required[int], "waiting_for_confirmation": Required[int]}, total=False)

OverviewGetResponseApiRequests = TypedDict("OverviewGetResponseApiRequests", {"total": Required[int], "errors": Required[int]}, total=False)

OverviewGetResponseLatestEvaluationsItemReasonVariant0 = TypedDict("OverviewGetResponseLatestEvaluationsItemReasonVariant0", {"code": Required[str], "message": Required[str]}, total=False)

OverviewGetResponseLatestEvaluationsItemOutcome = TypedDict("OverviewGetResponseLatestEvaluationsItemOutcome", {"state": Required[str | None]}, total=False)

OverviewGetResponseLatestEvaluationsItem = TypedDict("OverviewGetResponseLatestEvaluationsItem", {"object": Required[Literal["evaluation"]], "id": Required[str], "benefit": Required[str], "claim_id": Required[str], "result": Required[Literal["allow", "deny"]], "mode": Required[Literal["protect", "observe"]], "observed_result": Required[Literal["allow", "deny"] | None], "reason": Required[OverviewGetResponseLatestEvaluationsItemReasonVariant0 | None], "outcome": Required[OverviewGetResponseLatestEvaluationsItemOutcome], "policy_version": Required[float | None], "browser_data": Required[Literal["collected", "consent_declined", "not_loaded", "blocked", "timed_out", "failed", "site_not_listed", "sdk_outdated", "expired", "not_passed_on", "not_sent"] | None], "created_at": Required[str | None]}, total=False)

OverviewGetResponse = TypedDict("OverviewGetResponse", {"object": Required[Literal["overview"]], "hours": Required[Literal[24]], "evaluations": Required[OverviewGetResponseEvaluations], "previous": Required[OverviewGetResponsePrevious], "api_requests": Required[OverviewGetResponseApiRequests], "last_evaluation_at": Required[str | None], "browser_issue": Required[Literal["not_passed_on", "site_not_listed", "sdk_outdated", "script_missing"] | None], "latest_evaluations": Required[list[OverviewGetResponseLatestEvaluationsItem]]}, total=False)

AnalyticsValueInput = TypedDict("AnalyticsValueInput", {"days": NotRequired[int], "currency": NotRequired[Literal["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWG"]], "benefit": NotRequired[str]}, total=False)

AnalyticsValueResponseBenefitsItemValueVariant0 = TypedDict("AnalyticsValueResponseBenefitsItemValueVariant0", {"amount": Required[float], "currency": Required[str]}, total=False)

AnalyticsValueResponseBenefitsItem = TypedDict("AnalyticsValueResponseBenefitsItem", {"benefit": Required[str | None], "value": Required[AnalyticsValueResponseBenefitsItemValueVariant0 | None], "delivered": Required[float], "saved": Required[float]}, total=False)

AnalyticsValueResponse = TypedDict("AnalyticsValueResponse", {"object": Required[Literal["benefit_value"]], "currency": Required[str], "from": Required[str], "to": Required[str], "delivered": Required[float], "saved": Required[float], "benefits": Required[list[AnalyticsValueResponseBenefitsItem]]}, total=False)

AnalyticsDenialReasonsInput = TypedDict("AnalyticsDenialReasonsInput", {"days": NotRequired[int], "benefit": NotRequired[str]}, total=False)

AnalyticsDenialReasonsResponseReasonsItem = TypedDict("AnalyticsDenialReasonsResponseReasonsItem", {"code": Required[str], "label": Required[str], "count": Required[int]}, total=False)

AnalyticsDenialReasonsResponse = TypedDict("AnalyticsDenialReasonsResponse", {"object": Required[Literal["denial_reasons"]], "benefit": Required[str | None], "from": Required[str], "to": Required[str], "denied": Required[int], "reasons": Required[list[AnalyticsDenialReasonsResponseReasonsItem]]}, total=False)

RequestLogsListInput = TypedDict("RequestLogsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "status": NotRequired[Literal["2xx", "4xx", "5xx"]], "key_id": NotRequired[str]}, total=False)

RequestLogsListResponseDataItem = TypedDict("RequestLogsListResponseDataItem", {"object": Required[str]}, total=False)

RequestLogsListResponse = TypedDict("RequestLogsListResponse", {"object": Required[Literal["list"]], "data": Required[list[RequestLogsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

RequestLogsGetResponse = TypedDict("RequestLogsGetResponse", {"object": Required[str]}, total=False)

AuditLogsListInput = TypedDict("AuditLogsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

AuditLogsListResponseDataItem = TypedDict("AuditLogsListResponseDataItem", {"object": Required[str]}, total=False)

AuditLogsListResponse = TypedDict("AuditLogsListResponse", {"object": Required[Literal["list"]], "data": Required[list[AuditLogsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

AuditLogsGetResponse = TypedDict("AuditLogsGetResponse", {"object": Required[str]}, total=False)

AccountStatusGetResponsePlan = TypedDict("AccountStatusGetResponsePlan", {"plan": Required[Literal["payg", "pro", "scale"]], "name": Required[str], "interval": Required[Literal["month", "year"] | None], "enterprise": Required[bool], "renews_at": Required[str | None], "ends_at": Required[str | None]}, total=False)

AccountStatusGetResponseCredits = TypedDict("AccountStatusGetResponseCredits", {"available": Required[int], "allowance": Required[int], "pay_as_you_go": Required[int], "per_evaluation": Required[int], "evaluations_left": Required[int], "state": Required[Literal["ok", "low", "exhausted"]]}, total=False)

AccountStatusGetResponseLimitsProtectedBenefits = TypedDict("AccountStatusGetResponseLimitsProtectedBenefits", {"used": Required[int], "limit": Required[int]}, total=False)

AccountStatusGetResponseLimitsCustomPolicies = TypedDict("AccountStatusGetResponseLimitsCustomPolicies", {"used": Required[int], "limit": Required[int]}, total=False)

AccountStatusGetResponseLimitsTeamSeats = TypedDict("AccountStatusGetResponseLimitsTeamSeats", {"used": Required[int], "limit": Required[int]}, total=False)

AccountStatusGetResponseLimits = TypedDict("AccountStatusGetResponseLimits", {"protected_benefits": Required[AccountStatusGetResponseLimitsProtectedBenefits], "custom_policies": Required[AccountStatusGetResponseLimitsCustomPolicies], "team_seats": Required[AccountStatusGetResponseLimitsTeamSeats], "retention_days": Required[int], "rate": Required[int]}, total=False)

AccountStatusGetResponseAutoReload = TypedDict("AccountStatusGetResponseAutoReload", {"enabled": Required[bool]}, total=False)

AccountStatusGetResponse = TypedDict("AccountStatusGetResponse", {"object": Required[Literal["account_status"]], "workspace": Required[str], "plan": Required[AccountStatusGetResponsePlan], "credits": Required[AccountStatusGetResponseCredits], "limits": Required[AccountStatusGetResponseLimits], "auto_reload": Required[AccountStatusGetResponseAutoReload]}, total=False)

IntegrationStatusGetResponseApiKeys = TypedDict("IntegrationStatusGetResponseApiKeys", {"state": Required[Literal["ok", "none", "expiring", "refused"]], "next_step": Required[str | None]}, total=False)

IntegrationStatusGetResponseBrowserScript = TypedDict("IntegrationStatusGetResponseBrowserScript", {"state": Required[Literal["ok", "not_set_up", "not_passed_on", "site_not_listed", "sdk_outdated", "script_missing"]], "next_step": Required[str | None]}, total=False)

IntegrationStatusGetResponseEvaluations = TypedDict("IntegrationStatusGetResponseEvaluations", {"state": Required[Literal["ok", "none_yet", "stopped", "idle"]], "next_step": Required[str | None]}, total=False)

IntegrationStatusGetResponseOutcomes = TypedDict("IntegrationStatusGetResponseOutcomes", {"state": Required[Literal["ok", "not_needed", "missing"]], "next_step": Required[str | None]}, total=False)

IntegrationStatusGetResponseWebhooks = TypedDict("IntegrationStatusGetResponseWebhooks", {"state": Required[Literal["ok", "not_set_up", "failing", "disabled", "daily_limit", "unavailable"]], "next_step": Required[str | None]}, total=False)

IntegrationStatusGetResponseCredits = TypedDict("IntegrationStatusGetResponseCredits", {"state": Required[Literal["ok", "low", "exhausted", "payment_overdue"]], "next_step": Required[str | None]}, total=False)

IntegrationStatusGetResponse = TypedDict("IntegrationStatusGetResponse", {"object": Required[Literal["integration_status"]], "status": Required[Literal["ok", "attention"]], "api_keys": Required[IntegrationStatusGetResponseApiKeys], "browser_script": Required[IntegrationStatusGetResponseBrowserScript], "evaluations": Required[IntegrationStatusGetResponseEvaluations], "outcomes": Required[IntegrationStatusGetResponseOutcomes], "webhooks": Required[IntegrationStatusGetResponseWebhooks], "credits": Required[IntegrationStatusGetResponseCredits], "checked_at": Required[str | None]}, total=False)

EventsListInput = TypedDict("EventsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "wait": NotRequired[int]}, total=False)

EventsListResponseDataItemDataVariant0 = TypedDict("EventsListResponseDataItemDataVariant0", {"object": Required[Literal["credits"]], "state": Required[Literal["low"]], "available": Required[int], "evaluations_left": Required[int], "days_left": Required[int | None]}, total=False)

EventsListResponseDataItemDataVariant1 = TypedDict("EventsListResponseDataItemDataVariant1", {"object": Required[Literal["credits"]], "state": Required[Literal["exhausted"]], "available": Required[int], "evaluations_left": Required[int], "days_left": Required[None]}, total=False)

EventsListResponseDataItemDataVariant2 = TypedDict("EventsListResponseDataItemDataVariant2", {"object": Required[Literal["payment"]], "status": Required[Literal["received"]], "purpose": Required[Literal["subscription", "credits", "auto_reload"]]}, total=False)

EventsListResponseDataItemDataVariant3 = TypedDict("EventsListResponseDataItemDataVariant3", {"object": Required[Literal["payment"]], "status": Required[Literal["failed"]], "purpose": Required[Literal["subscription", "credits", "auto_reload"]], "confirmation_required": Required[bool]}, total=False)

EventsListResponseDataItemDataVariant4PreviousVariant0 = TypedDict("EventsListResponseDataItemDataVariant4PreviousVariant0", {"plan": Required[Literal["payg", "pro", "scale"]], "name": Required[str], "interval": Required[Literal["month", "year"] | None]}, total=False)

EventsListResponseDataItemDataVariant4 = TypedDict("EventsListResponseDataItemDataVariant4", {"plan": Required[Literal["payg", "pro", "scale"]], "name": Required[str], "interval": Required[Literal["month", "year"] | None], "object": Required[Literal["plan"]], "previous": Required[EventsListResponseDataItemDataVariant4PreviousVariant0 | None]}, total=False)

EventsListResponseDataItemDataVariant5 = TypedDict("EventsListResponseDataItemDataVariant5", {"object": Required[Literal["workspace"]], "id": Required[str], "status": Required[Literal["suspended"]]}, total=False)

EventsListResponseDataItemDataVariant6 = TypedDict("EventsListResponseDataItemDataVariant6", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted"]], "expires_at": Required[str | None], "created_at": Required[str | None]}, total=False)

EventsListResponseDataItemDataVariant7 = TypedDict("EventsListResponseDataItemDataVariant7", {"object": Required[Literal["api_key"]], "id": Required[str], "name": Required[str], "type": Required[Literal["secret", "restricted"]], "expires_at": Required[str | None], "created_at": Required[str | None]}, total=False)

EventsListResponseDataItemDataVariant8 = TypedDict("EventsListResponseDataItemDataVariant8", {"object": Required[Literal["member"]], "id": Required[str], "name": Required[str | None], "role": Required[Literal["admin", "developer", "viewer"]], "joined_at": Required[str | None]}, total=False)

EventsListResponseDataItemDataVariant9OwnerVariant0 = TypedDict("EventsListResponseDataItemDataVariant9OwnerVariant0", {"id": Required[str], "name": Required[str | None]}, total=False)

EventsListResponseDataItemDataVariant9NewOwnerVariant0 = TypedDict("EventsListResponseDataItemDataVariant9NewOwnerVariant0", {"id": Required[str], "name": Required[str | None]}, total=False)

EventsListResponseDataItemDataVariant9 = TypedDict("EventsListResponseDataItemDataVariant9", {"object": Required[Literal["ownership_transfer"]], "status": Required[Literal["awaiting_owner", "awaiting_new_owner", "completed", "ended"]], "owner": Required[EventsListResponseDataItemDataVariant9OwnerVariant0 | None], "new_owner": Required[EventsListResponseDataItemDataVariant9NewOwnerVariant0 | None]}, total=False)

EventsListResponseDataItemDataVariant10 = TypedDict("EventsListResponseDataItemDataVariant10", {"object": Required[Literal["webhook_usage"]], "day": Required[str], "limit": Required[int]}, total=False)

EventsListResponseDataItem = TypedDict("EventsListResponseDataItem", {"object": Required[Literal["event"]], "id": Required[str], "type": Required[str], "api_version": Required[Literal["v1"]], "created_at": Required[str | None], "workspace": Required[str], "test": Required[Literal[False]], "data": Required[EventsListResponseDataItemDataVariant0 | EventsListResponseDataItemDataVariant1 | EventsListResponseDataItemDataVariant2 | EventsListResponseDataItemDataVariant3 | EventsListResponseDataItemDataVariant4 | EventsListResponseDataItemDataVariant5 | EventsListResponseDataItemDataVariant6 | EventsListResponseDataItemDataVariant7 | EventsListResponseDataItemDataVariant8 | EventsListResponseDataItemDataVariant9 | EventsListResponseDataItemDataVariant10 | dict[str, Any]]}, total=False)

EventsListResponse = TypedDict("EventsListResponse", {"object": Required[Literal["list"]], "data": Required[list[EventsListResponseDataItem]], "next_cursor": Required[str], "has_more": Required[bool]}, total=False)

BrowserCollectionGetResponseSitesItem = TypedDict("BrowserCollectionGetResponseSitesItem", {"origin": Required[str], "listed": Required[bool], "first_seen_at": Required[str | None], "last_seen_at": Required[str | None], "sdk_version": Required[str | None]}, total=False)

BrowserCollectionGetResponseCoverage = TypedDict("BrowserCollectionGetResponseCoverage", {"days": Required[Literal[7]], "total": Required[int], "collected": Required[int], "consent_declined": Required[int], "not_loaded": Required[int], "blocked": Required[int], "timed_out": Required[int], "failed": Required[int], "site_not_listed": Required[int], "sdk_outdated": Required[int], "expired": Required[int], "not_passed_on": Required[int], "not_sent": Required[int]}, total=False)

BrowserCollectionGetResponse = TypedDict("BrowserCollectionGetResponse", {"object": Required[Literal["browser_collection"]], "origins": Required[list[str]], "revision": Required[int], "sites": Required[list[BrowserCollectionGetResponseSitesItem]], "issue": Required[Literal["not_passed_on", "site_not_listed", "sdk_outdated", "script_missing"] | None], "issue_since": Required[str | None], "coverage": Required[BrowserCollectionGetResponseCoverage], "notices": Required[list[Literal["chrome", "edge", "firefox", "safari", "samsung", "opera", "other"]]]}, total=False)

BrowserCollectionUpdateInput = TypedDict("BrowserCollectionUpdateInput", {"origins": Required[list[str]], "revision": NotRequired[int]}, total=False)

BrowserCollectionUpdateResponseSitesItem = TypedDict("BrowserCollectionUpdateResponseSitesItem", {"origin": Required[str], "listed": Required[bool], "first_seen_at": Required[str | None], "last_seen_at": Required[str | None], "sdk_version": Required[str | None]}, total=False)

BrowserCollectionUpdateResponseCoverage = TypedDict("BrowserCollectionUpdateResponseCoverage", {"days": Required[Literal[7]], "total": Required[int], "collected": Required[int], "consent_declined": Required[int], "not_loaded": Required[int], "blocked": Required[int], "timed_out": Required[int], "failed": Required[int], "site_not_listed": Required[int], "sdk_outdated": Required[int], "expired": Required[int], "not_passed_on": Required[int], "not_sent": Required[int]}, total=False)

BrowserCollectionUpdateResponse = TypedDict("BrowserCollectionUpdateResponse", {"object": Required[Literal["browser_collection"]], "origins": Required[list[str]], "revision": Required[int], "sites": Required[list[BrowserCollectionUpdateResponseSitesItem]], "issue": Required[Literal["not_passed_on", "site_not_listed", "sdk_outdated", "script_missing"] | None], "issue_since": Required[str | None], "coverage": Required[BrowserCollectionUpdateResponseCoverage], "notices": Required[list[Literal["chrome", "edge", "firefox", "safari", "samsung", "opera", "other"]]]}, total=False)

BrowserCollectionScriptResponse = TypedDict("BrowserCollectionScriptResponse", {"object": Required[Literal["browser_script"]], "script": Required[str | None], "sdk_version": Required[str], "publishable_key": Required[str | None]}, total=False)

WebhookEndpointsListInput = TypedDict("WebhookEndpointsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

WebhookEndpointsListResponseDataItem = TypedDict("WebhookEndpointsListResponseDataItem", {"object": Required[str]}, total=False)

WebhookEndpointsListResponse = TypedDict("WebhookEndpointsListResponse", {"object": Required[Literal["list"]], "data": Required[list[WebhookEndpointsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

WebhookEndpointsCreateInput = TypedDict("WebhookEndpointsCreateInput", {"url": Required[str], "events": Required[list[Literal["evaluation.completed", "evaluation.skipped", "outcome.updated", "access_list_entry.created", "access_list_entry.updated", "access_list_entry.deleted", "import.completed", "export.completed", "data_deletion.completed", "credits.low", "credits.exhausted", "payment.received", "payment.failed", "plan.changed", "workspace.suspended", "api_key.created", "api_key.expiring", "member.joined", "ownership_transfer.updated", "webhook.daily_limit_reached"]]], "benefit_ids": NotRequired[list[str]], "denied_only": NotRequired[bool]}, total=False)

WebhookEndpointsCreateResponse = TypedDict("WebhookEndpointsCreateResponse", {"object": Required[Literal["webhook_endpoint"]], "id": Required[str | None], "url": Required[str], "description": Required[None], "events": Required[list[str]], "benefits": Required[list[str | None]], "denied_only": Required[bool], "status": Required[Literal["enabled", "disabled"]], "disabled_reason": Required[Literal["manual", "failures", "benefits_deleted"] | None], "last_success_at": Required[str | None], "revision": Required[int], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

WebhookEndpointsGetResponse = TypedDict("WebhookEndpointsGetResponse", {"object": Required[str]}, total=False)

WebhookEndpointsUpdateInput = TypedDict("WebhookEndpointsUpdateInput", {"revision": Required[int], "url": NotRequired[str], "events": NotRequired[list[Literal["evaluation.completed", "evaluation.skipped", "outcome.updated", "access_list_entry.created", "access_list_entry.updated", "access_list_entry.deleted", "import.completed", "export.completed", "data_deletion.completed", "credits.low", "credits.exhausted", "payment.received", "payment.failed", "plan.changed", "workspace.suspended", "api_key.created", "api_key.expiring", "member.joined", "ownership_transfer.updated", "webhook.daily_limit_reached"]]], "benefit_ids": NotRequired[list[str]], "denied_only": NotRequired[bool]}, total=False)

WebhookEndpointsUpdateResponse = TypedDict("WebhookEndpointsUpdateResponse", {"object": Required[Literal["webhook_endpoint"]], "id": Required[str | None], "url": Required[str], "description": Required[None], "events": Required[list[str]], "benefits": Required[list[str | None]], "denied_only": Required[bool], "status": Required[Literal["enabled", "disabled"]], "disabled_reason": Required[Literal["manual", "failures", "benefits_deleted"] | None], "last_success_at": Required[str | None], "revision": Required[int], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

WebhookEndpointsDeleteResponse = TypedDict("WebhookEndpointsDeleteResponse", {"object": Required[Literal["deleted"]], "id": Required[str | None], "deleted": Required[Literal[True]]}, total=False)

WebhookEndpointsTestInput = TypedDict("WebhookEndpointsTestInput", {"type": NotRequired[Literal["evaluation.completed", "evaluation.skipped", "outcome.updated", "access_list_entry.created", "access_list_entry.updated", "access_list_entry.deleted", "import.completed", "export.completed", "data_deletion.completed", "credits.low", "credits.exhausted", "payment.received", "payment.failed", "plan.changed", "workspace.suspended", "api_key.created", "api_key.expiring", "member.joined", "ownership_transfer.updated", "webhook.daily_limit_reached", "webhook.test"]]}, total=False)

WebhookEndpointsTestResponse = TypedDict("WebhookEndpointsTestResponse", {"object": Required[str]}, total=False)

WebhookEndpointsEnableResponse = TypedDict("WebhookEndpointsEnableResponse", {"object": Required[Literal["webhook_endpoint"]], "id": Required[str | None], "url": Required[str], "description": Required[None], "events": Required[list[str]], "benefits": Required[list[str | None]], "denied_only": Required[bool], "status": Required[Literal["enabled", "disabled"]], "disabled_reason": Required[Literal["manual", "failures", "benefits_deleted"] | None], "last_success_at": Required[str | None], "revision": Required[int], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

WebhookEndpointsDisableResponse = TypedDict("WebhookEndpointsDisableResponse", {"object": Required[Literal["webhook_endpoint"]], "id": Required[str | None], "url": Required[str], "description": Required[None], "events": Required[list[str]], "benefits": Required[list[str | None]], "denied_only": Required[bool], "status": Required[Literal["enabled", "disabled"]], "disabled_reason": Required[Literal["manual", "failures", "benefits_deleted"] | None], "last_success_at": Required[str | None], "revision": Required[int], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

WebhookEndpointsSecretResponse = TypedDict("WebhookEndpointsSecretResponse", {"object": Required[Literal["webhook_signing_secret"]], "endpoint": Required[str | None], "secret": Required[str]}, total=False)

WebhookEndpointsRotateSecretResponse = TypedDict("WebhookEndpointsRotateSecretResponse", {"object": Required[Literal["webhook_endpoint"]], "id": Required[str | None], "url": Required[str], "description": Required[None], "events": Required[list[str]], "benefits": Required[list[str | None]], "denied_only": Required[bool], "status": Required[Literal["enabled", "disabled"]], "disabled_reason": Required[Literal["manual", "failures", "benefits_deleted"] | None], "last_success_at": Required[str | None], "revision": Required[int], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

WebhookDeliveriesUsageResponse = TypedDict("WebhookDeliveriesUsageResponse", {"object": Required[Literal["webhook_usage"]], "day": Required[str], "deliveries": Required[int], "limit": Required[int], "limit_reached": Required[bool], "resets_at": Required[str | None]}, total=False)

WebhookDeliveriesListInput = TypedDict("WebhookDeliveriesListInput", {"cursor": NotRequired[str], "limit": NotRequired[int], "endpoint_id": NotRequired[str], "status": NotRequired[Literal["pending", "succeeded", "failed", "not_sent"]], "type": NotRequired[Literal["evaluation.completed", "evaluation.skipped", "outcome.updated", "access_list_entry.created", "access_list_entry.updated", "access_list_entry.deleted", "import.completed", "export.completed", "data_deletion.completed", "credits.low", "credits.exhausted", "payment.received", "payment.failed", "plan.changed", "workspace.suspended", "api_key.created", "api_key.expiring", "member.joined", "ownership_transfer.updated", "webhook.daily_limit_reached", "webhook.test"]], "event_id": NotRequired[str]}, total=False)

WebhookDeliveriesListResponseDataItem = TypedDict("WebhookDeliveriesListResponseDataItem", {"object": Required[str]}, total=False)

WebhookDeliveriesListResponse = TypedDict("WebhookDeliveriesListResponse", {"object": Required[Literal["list"]], "data": Required[list[WebhookDeliveriesListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

WebhookDeliveriesGetResponse = TypedDict("WebhookDeliveriesGetResponse", {"object": Required[str]}, total=False)

WebhookDeliveriesResendInput = TypedDict("WebhookDeliveriesResendInput", {"target": NotRequired[Literal["current", "original"]]}, total=False)

WebhookDeliveriesResendResponse = TypedDict("WebhookDeliveriesResendResponse", {"object": Required[str]}, total=False)

BillingPlanResponseScheduledChangeVariant0 = TypedDict("BillingPlanResponseScheduledChangeVariant0", {"plan": Required[Literal["payg", "pro", "scale"]], "name": Required[str], "interval": Required[Literal["month", "year"] | None], "at": Required[str | None]}, total=False)

BillingPlanResponsePayment = TypedDict("BillingPlanResponsePayment", {"state": Required[Literal["ok", "grace", "overdue"]], "due_at": Required[str | None]}, total=False)

BillingPlanResponseLimits = TypedDict("BillingPlanResponseLimits", {"protected_benefits": Required[int], "custom_policies": Required[int], "team_seats": Required[int], "retention_days": Required[int], "rate": Required[int]}, total=False)

BillingPlanResponseOverLimitVariant0ItemsItem = TypedDict("BillingPlanResponseOverLimitVariant0ItemsItem", {"kind": Required[Literal["benefit", "member"]], "id": Required[str | None], "name": Required[str], "paused": Required[bool], "will_pause": Required[bool]}, total=False)

BillingPlanResponseOverLimitVariant0 = TypedDict("BillingPlanResponseOverLimitVariant0", {"state": Required[Literal["grace", "enforced"]], "grace_until": Required[str | None], "items": Required[list[BillingPlanResponseOverLimitVariant0ItemsItem]]}, total=False)

BillingPlanResponse = TypedDict("BillingPlanResponse", {"object": Required[Literal["billing_plan"]], "plan": Required[Literal["payg", "pro", "scale"]], "name": Required[str], "interval": Required[Literal["month", "year"] | None], "subscribed": Required[bool], "renews_at": Required[str | None], "ends_at": Required[str | None], "scheduled_change": Required[BillingPlanResponseScheduledChangeVariant0 | None], "enterprise": Required[bool], "payment": Required[BillingPlanResponsePayment], "limits": Required[BillingPlanResponseLimits], "over_limit": Required[BillingPlanResponseOverLimitVariant0 | None]}, total=False)

BillingUsageResponseCredits = TypedDict("BillingUsageResponseCredits", {"available": Required[int], "allowance": Required[int], "pay_as_you_go": Required[int], "per_evaluation": Required[int]}, total=False)

BillingUsageResponseUsageAbsoluteAllowanceCredits = TypedDict("BillingUsageResponseUsageAbsoluteAllowanceCredits", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAbsolutePayAsYouGoCredits = TypedDict("BillingUsageResponseUsageAbsolutePayAsYouGoCredits", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAbsoluteProtectedBenefits = TypedDict("BillingUsageResponseUsageAbsoluteProtectedBenefits", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAbsoluteTeamSeats = TypedDict("BillingUsageResponseUsageAbsoluteTeamSeats", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAbsolute = TypedDict("BillingUsageResponseUsageAbsolute", {"allowance_credits": Required[BillingUsageResponseUsageAbsoluteAllowanceCredits], "pay_as_you_go_credits": Required[BillingUsageResponseUsageAbsolutePayAsYouGoCredits], "protected_benefits": Required[BillingUsageResponseUsageAbsoluteProtectedBenefits], "team_seats": Required[BillingUsageResponseUsageAbsoluteTeamSeats]}, total=False)

BillingUsageResponseUsageAllowanceVariant0AllowanceCredits = TypedDict("BillingUsageResponseUsageAllowanceVariant0AllowanceCredits", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAllowanceVariant0PayAsYouGoCredits = TypedDict("BillingUsageResponseUsageAllowanceVariant0PayAsYouGoCredits", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAllowanceVariant0ProtectedBenefits = TypedDict("BillingUsageResponseUsageAllowanceVariant0ProtectedBenefits", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAllowanceVariant0TeamSeats = TypedDict("BillingUsageResponseUsageAllowanceVariant0TeamSeats", {"used": Required[int], "total": Required[int]}, total=False)

BillingUsageResponseUsageAllowanceVariant0 = TypedDict("BillingUsageResponseUsageAllowanceVariant0", {"allowance_credits": Required[BillingUsageResponseUsageAllowanceVariant0AllowanceCredits], "pay_as_you_go_credits": Required[BillingUsageResponseUsageAllowanceVariant0PayAsYouGoCredits], "protected_benefits": Required[BillingUsageResponseUsageAllowanceVariant0ProtectedBenefits], "team_seats": Required[BillingUsageResponseUsageAllowanceVariant0TeamSeats]}, total=False)

BillingUsageResponseUsage = TypedDict("BillingUsageResponseUsage", {"absolute": Required[BillingUsageResponseUsageAbsolute], "allowance": Required[BillingUsageResponseUsageAllowanceVariant0 | None]}, total=False)

BillingUsageResponseAutoReload = TypedDict("BillingUsageResponseAutoReload", {"enabled": Required[bool], "capped": Required[bool], "threshold": Required[int | None], "amount_dollars": Required[int | None], "monthly_cap_dollars": Required[int | None]}, total=False)

BillingUsageResponse = TypedDict("BillingUsageResponse", {"object": Required[Literal["billing_usage"]], "credits": Required[BillingUsageResponseCredits], "usage": Required[BillingUsageResponseUsage], "auto_reload": Required[BillingUsageResponseAutoReload]}, total=False)

BillingCreditHistoryInput = TypedDict("BillingCreditHistoryInput", {"cursor": NotRequired[str], "activity": NotRequired[Literal["evaluations", "webhooks", "plan_credits", "temporary_plan_credits", "enterprise_plan_credits", "purchase", "first_purchase_bonus", "survey_credits", "yearly_conversion", "expired", "ended", "replaced", "enterprise_plan_removed", "refund", "dispute", "adjustment"]], "direction": NotRequired[Literal["added", "used"]], "days": NotRequired[Literal[7] | Literal[30] | Literal[90] | Literal[365]], "from": NotRequired[str], "to": NotRequired[str]}, total=False)

BillingCreditHistoryResponseDataItem = TypedDict("BillingCreditHistoryResponseDataItem", {"object": Required[Literal["credit_entry"]], "date": Required[str], "daily_total": Required[bool], "activity": Required[Literal["evaluations", "webhooks", "plan_credits", "temporary_plan_credits", "enterprise_plan_credits", "purchase", "first_purchase_bonus", "survey_credits", "yearly_conversion", "expired", "ended", "replaced", "enterprise_plan_removed", "refund", "dispute", "adjustment"]], "sources": Required[list[Literal["plan", "temporary_plan", "enterprise_plan", "purchased", "bonus", "survey", "converted", "adjustment", "negative_balance"]]], "credits": Required[int], "plans": Required[list[str]], "enterprise_plans": Required[list[str]]}, total=False)

BillingCreditHistoryResponse = TypedDict("BillingCreditHistoryResponse", {"object": Required[Literal["list"]], "data": Required[list[BillingCreditHistoryResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

BillingDailyUsageResponseDaysItemTopBenefitVariant0 = TypedDict("BillingDailyUsageResponseDaysItemTopBenefitVariant0", {"name": Required[str], "evaluations": Required[int]}, total=False)

BillingDailyUsageResponseDaysItem = TypedDict("BillingDailyUsageResponseDaysItem", {"day": Required[str], "credits": Required[int], "top_benefit": Required[BillingDailyUsageResponseDaysItemTopBenefitVariant0 | None]}, total=False)

BillingDailyUsageResponse = TypedDict("BillingDailyUsageResponse", {"object": Required[Literal["daily_usage"]], "time_zone": Required[str], "days": Required[list[BillingDailyUsageResponseDaysItem]]}, total=False)

BillingEnterprisePlansResponseDataItemGrants = TypedDict("BillingEnterprisePlansResponseDataItemGrants", {"credits": Required[int], "credit_cadence": Required[Literal["once", "month", "year"] | None], "credit_expiry": Required[Literal["never", "period_end", "days"] | None], "credit_expiry_days": Required[int | None], "team_seats": Required[int], "protected_benefits": Required[int], "custom_policies": Required[int | None], "rate": Required[int | None], "burst": Required[int | None], "concurrency": Required[int | None], "retention_days": Required[int | None]}, total=False)

BillingEnterprisePlansResponseDataItem = TypedDict("BillingEnterprisePlansResponseDataItem", {"object": Required[Literal["enterprise_plan"]], "name": Required[str], "active": Required[bool], "added_at": Required[str | None], "ends_at": Required[str | None], "grants": Required[BillingEnterprisePlansResponseDataItemGrants]}, total=False)

BillingEnterprisePlansResponse = TypedDict("BillingEnterprisePlansResponse", {"object": Required[Literal["list"]], "data": Required[list[BillingEnterprisePlansResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

BillingCodesPreviewInput = TypedDict("BillingCodesPreviewInput", {"code": Required[str]}, total=False)

BillingCodesPreviewResponsePlan = TypedDict("BillingCodesPreviewResponsePlan", {"name": Required[str], "description": Required[str | None], "credits": Required[int], "credit_cadence": Required[Literal["once", "month", "year"] | None], "credit_expiry": Required[Literal["never", "period_end", "days"] | None], "credit_expiry_days": Required[int | None], "team_seats": Required[int], "protected_benefits": Required[int], "custom_policies": Required[int | None], "rate": Required[int | None], "burst": Required[int | None], "concurrency": Required[int | None], "retention_days": Required[int | None], "duration_months": Required[int | None]}, total=False)

BillingCodesPreviewResponse = TypedDict("BillingCodesPreviewResponse", {"object": Required[Literal["enterprise_plan_code_preview"]], "plan": Required[BillingCodesPreviewResponsePlan]}, total=False)

BillingUpcomingResponseDataItem = TypedDict("BillingUpcomingResponseDataItem", {"object": Required[Literal["upcoming_charge"]], "kind": Required[Literal["plan"]], "amount_cents": Required[int], "at": Required[str | None], "payment_method": Required[str | None], "discounted": Required[bool]}, total=False)

BillingUpcomingResponse = TypedDict("BillingUpcomingResponse", {"object": Required[Literal["list"]], "data": Required[list[BillingUpcomingResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

BillingInvoicesInput = TypedDict("BillingInvoicesInput", {"cursor": NotRequired[str]}, total=False)

BillingInvoicesResponseDataItemPeriodVariant0 = TypedDict("BillingInvoicesResponseDataItemPeriodVariant0", {"start": Required[str | None], "end": Required[str | None]}, total=False)

BillingInvoicesResponseDataItem = TypedDict("BillingInvoicesResponseDataItem", {"object": Required[Literal["invoice"]], "number": Required[str | None], "created_at": Required[str | None], "status": Required[Literal["open", "paid", "void", "uncollectible"]], "description": Required[str], "period": Required[BillingInvoicesResponseDataItemPeriodVariant0 | None], "total_cents": Required[int], "paid_cents": Required[int], "due_cents": Required[int], "refunded_cents": Required[int], "payable": Required[bool], "url": Required[str | None]}, total=False)

BillingInvoicesResponse = TypedDict("BillingInvoicesResponse", {"object": Required[Literal["list"]], "data": Required[list[BillingInvoicesResponseDataItem]], "next_cursor": Required[str | None], "outstanding_cents": Required[int | None]}, total=False)

BillingPaymentMethodsResponseDataItem = TypedDict("BillingPaymentMethodsResponseDataItem", {"object": Required[Literal["payment_method"]], "id": Required[str | None], "type": Required[Literal["card", "bank_account", "link"]], "brand": Required[str | None], "last4": Required[str | None], "exp_month": Required[int | None], "exp_year": Required[int | None], "label": Required[str], "default": Required[bool], "backup": Required[int | None], "declined": Required[bool], "expired": Required[bool]}, total=False)

BillingPaymentMethodsResponse = TypedDict("BillingPaymentMethodsResponse", {"object": Required[Literal["list"]], "data": Required[list[BillingPaymentMethodsResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

BillingDetailsResponseAddressVariant0 = TypedDict("BillingDetailsResponseAddressVariant0", {"line1": Required[str], "line2": Required[str], "city": Required[str], "state": Required[str], "postal_code": Required[str], "country": Required[str]}, total=False)

BillingDetailsResponseTaxIdVariant0 = TypedDict("BillingDetailsResponseTaxIdVariant0", {"type": Required[str], "value": Required[str]}, total=False)

BillingDetailsResponse = TypedDict("BillingDetailsResponse", {"object": Required[Literal["billing_details"]], "name": Required[str], "email": Required[str], "uses_account_email": Required[bool], "address": Required[BillingDetailsResponseAddressVariant0 | None], "tax_id": Required[BillingDetailsResponseTaxIdVariant0 | None]}, total=False)

BillingDetailsUpdateInputAddress = TypedDict("BillingDetailsUpdateInputAddress", {"line1": Required[str], "line2": Required[str], "city": Required[str], "state": Required[str], "postal_code": Required[str], "country": Required[str | Literal[""]]}, total=False)

BillingDetailsUpdateInputTaxIdVariant0 = TypedDict("BillingDetailsUpdateInputTaxIdVariant0", {"type": Required[Literal["eu_vat", "gb_vat", "us_ein", "ca_bn", "au_abn", "in_gst", "ch_vat", "no_vat", "nz_gst", "sg_gst", "ae_trn", "za_vat", "br_cnpj", "mx_rfc", "jp_cn"]], "value": Required[str]}, total=False)

BillingDetailsUpdateInput = TypedDict("BillingDetailsUpdateInput", {"name": Required[str], "email": Required[str | Literal[""]], "address": Required[BillingDetailsUpdateInputAddress], "tax_id": Required[BillingDetailsUpdateInputTaxIdVariant0 | None]}, total=False)

BillingDetailsUpdateResponseAddressVariant0 = TypedDict("BillingDetailsUpdateResponseAddressVariant0", {"line1": Required[str], "line2": Required[str], "city": Required[str], "state": Required[str], "postal_code": Required[str], "country": Required[str]}, total=False)

BillingDetailsUpdateResponseTaxIdVariant0 = TypedDict("BillingDetailsUpdateResponseTaxIdVariant0", {"type": Required[str], "value": Required[str]}, total=False)

BillingDetailsUpdateResponse = TypedDict("BillingDetailsUpdateResponse", {"object": Required[Literal["billing_details"]], "name": Required[str], "email": Required[str], "uses_account_email": Required[bool], "address": Required[BillingDetailsUpdateResponseAddressVariant0 | None], "tax_id": Required[BillingDetailsUpdateResponseTaxIdVariant0 | None]}, total=False)

BillingPaymentsGetResponse = TypedDict("BillingPaymentsGetResponse", {"object": Required[Literal["billing_payment"]], "id": Required[str | None], "kind": Required[Literal["credit_purchase", "auto_reload", "plan_change", "invoice_payment"]], "status": Required[Literal["succeeded", "pending", "requires_action", "failed", "canceled"]], "payment_page_url": Required[str | None], "credits": Required[int | None], "bonus_credits": Required[int | None], "scheduled": Required[bool]}, total=False)

BillingQuotesCreateInput = TypedDict("BillingQuotesCreateInput", {"plan": Required[Literal["payg", "pro", "scale"]], "interval": NotRequired[Literal["month", "year"] | None], "promo_code": NotRequired[str]}, total=False)

BillingQuotesCreateResponseNextChargeVariant0 = TypedDict("BillingQuotesCreateResponseNextChargeVariant0", {"amount_cents": Required[int], "at": Required[str | None], "discounted": Required[bool]}, total=False)

BillingQuotesCreateResponsePromotionVariant0 = TypedDict("BillingQuotesCreateResponsePromotionVariant0", {"code": Required[str], "amount_cents": Required[int], "full_cents": Required[int], "duration": Required[str]}, total=False)

BillingQuotesCreateResponse = TypedDict("BillingQuotesCreateResponse", {"object": Required[Literal["plan_change_quote"]], "id": Required[str | None], "plan": Required[Literal["payg", "pro", "scale"]], "interval": Required[Literal["month", "year"] | None], "direction": Required[Literal["upgrade", "downgrade", "switch"]], "timing": Required[Literal["immediate", "period_end"]], "confirmable": Required[bool], "charge_now_cents": Required[int], "renewal_cents": Required[int], "credits_now": Required[int], "effective_at": Required[str | None], "expires_at": Required[str | None], "next_charge": Required[BillingQuotesCreateResponseNextChargeVariant0 | None], "promotion": Required[BillingQuotesCreateResponsePromotionVariant0 | None]}, total=False)

BillingLowCreditAlertUpdateInput = TypedDict("BillingLowCreditAlertUpdateInput", {"credits": Required[int | None]}, total=False)

BillingLowCreditAlertUpdateResponse = TypedDict("BillingLowCreditAlertUpdateResponse", {"object": Required[Literal["low_credit_alert"]], "credits": Required[int | None]}, total=False)

BillingOverLimitChooseInput = TypedDict("BillingOverLimitChooseInput", {"kind": Required[Literal["benefit", "member"]], "keep_active": Required[str], "pause": Required[str]}, total=False)

BillingOverLimitChooseResponse = TypedDict("BillingOverLimitChooseResponse", {"object": Required[Literal["over_limit_choice"]], "status": Required[Literal["chosen", "swapped", "unchanged"]]}, total=False)

BillingAutoReloadUpdateInput = TypedDict("BillingAutoReloadUpdateInput", {"enabled": Required[bool], "threshold": Required[int | None], "amount_dollars": Required[int | None], "monthly_cap_dollars": NotRequired[int | None]}, total=False)

BillingAutoReloadUpdateResponse = TypedDict("BillingAutoReloadUpdateResponse", {"object": Required[Literal["auto_reload"]], "enabled": Required[bool], "capped": Required[bool], "threshold": Required[int | None], "amount_dollars": Required[int | None], "monthly_cap_dollars": Required[int | None], "spent_this_month_dollars": Required[int]}, total=False)

BillingCreditsBuyInput = TypedDict("BillingCreditsBuyInput", {"amount_dollars": Required[int]}, total=False)

BillingCreditsBuyResponse = TypedDict("BillingCreditsBuyResponse", {"object": Required[Literal["billing_payment"]], "id": Required[str | None], "kind": Required[Literal["credit_purchase", "auto_reload", "plan_change", "invoice_payment"]], "status": Required[Literal["succeeded", "pending", "requires_action", "failed", "canceled"]], "payment_page_url": Required[str | None], "credits": Required[int | None], "bonus_credits": Required[int | None], "scheduled": Required[bool]}, total=False)

BillingCreditsRetryInput = TypedDict("BillingCreditsRetryInput", {"payment_method_id": NotRequired[str]}, total=False)

BillingCreditsRetryResponse = TypedDict("BillingCreditsRetryResponse", {"object": Required[Literal["billing_payment"]], "id": Required[str | None], "kind": Required[Literal["credit_purchase", "auto_reload", "plan_change", "invoice_payment"]], "status": Required[Literal["succeeded", "pending", "requires_action", "failed", "canceled"]], "payment_page_url": Required[str | None], "credits": Required[int | None], "bonus_credits": Required[int | None], "scheduled": Required[bool]}, total=False)

BillingPlanChangeInput = TypedDict("BillingPlanChangeInput", {"payment_method_id": NotRequired[str]}, total=False)

BillingPlanChangeResponse = TypedDict("BillingPlanChangeResponse", {"object": Required[Literal["billing_payment"]], "id": Required[str | None], "kind": Required[Literal["credit_purchase", "auto_reload", "plan_change", "invoice_payment"]], "status": Required[Literal["succeeded", "pending", "requires_action", "failed", "canceled"]], "payment_page_url": Required[str | None], "credits": Required[int | None], "bonus_credits": Required[int | None], "scheduled": Required[bool]}, total=False)

BillingDowngradeUndoResponse = TypedDict("BillingDowngradeUndoResponse", {"object": Required[Literal["subscription_change"]], "status": Required[Literal["succeeded", "pending"]]}, total=False)

BillingSubscriptionResumeResponse = TypedDict("BillingSubscriptionResumeResponse", {"object": Required[Literal["subscription_change"]], "status": Required[Literal["succeeded", "pending"]]}, total=False)

BillingOverduePayInput = TypedDict("BillingOverduePayInput", {"invoice_number": NotRequired[str], "payment_method_id": NotRequired[str]}, total=False)

BillingOverduePayResponse = TypedDict("BillingOverduePayResponse", {"object": Required[Literal["billing_payment"]], "id": Required[str | None], "kind": Required[Literal["credit_purchase", "auto_reload", "plan_change", "invoice_payment"]], "status": Required[Literal["succeeded", "pending", "requires_action", "failed", "canceled"]], "payment_page_url": Required[str | None], "credits": Required[int | None], "bonus_credits": Required[int | None], "scheduled": Required[bool]}, total=False)

BillingPaymentMethodsDefaultResponseOverdueInvoicesItem = TypedDict("BillingPaymentMethodsDefaultResponseOverdueInvoicesItem", {"number": Required[str | None], "amount_cents": Required[int], "status": Required[Literal["paid", "processing", "requires_action", "failed", "pending"]]}, total=False)

BillingPaymentMethodsDefaultResponse = TypedDict("BillingPaymentMethodsDefaultResponse", {"object": Required[Literal["payment_method_change"]], "status": Required[Literal["succeeded", "pending", "failed", "canceled"]], "overdue_invoices": Required[list[BillingPaymentMethodsDefaultResponseOverdueInvoicesItem]]}, total=False)

BillingPaymentMethodsMoveInput = TypedDict("BillingPaymentMethodsMoveInput", {"direction": Required[Literal["up", "down"]]}, total=False)

BillingPaymentMethodsMoveResponseOverdueInvoicesItem = TypedDict("BillingPaymentMethodsMoveResponseOverdueInvoicesItem", {"number": Required[str | None], "amount_cents": Required[int], "status": Required[Literal["paid", "processing", "requires_action", "failed", "pending"]]}, total=False)

BillingPaymentMethodsMoveResponse = TypedDict("BillingPaymentMethodsMoveResponse", {"object": Required[Literal["payment_method_change"]], "status": Required[Literal["succeeded", "pending", "failed", "canceled"]], "overdue_invoices": Required[list[BillingPaymentMethodsMoveResponseOverdueInvoicesItem]]}, total=False)

BillingPaymentMethodsRemoveResponseOverdueInvoicesItem = TypedDict("BillingPaymentMethodsRemoveResponseOverdueInvoicesItem", {"number": Required[str | None], "amount_cents": Required[int], "status": Required[Literal["paid", "processing", "requires_action", "failed", "pending"]]}, total=False)

BillingPaymentMethodsRemoveResponse = TypedDict("BillingPaymentMethodsRemoveResponse", {"object": Required[Literal["payment_method_change"]], "status": Required[Literal["succeeded", "pending", "failed", "canceled"]], "overdue_invoices": Required[list[BillingPaymentMethodsRemoveResponseOverdueInvoicesItem]]}, total=False)

BillingCodesRedeemInput = TypedDict("BillingCodesRedeemInput", {"code": Required[str]}, total=False)

BillingCodesRedeemResponse = TypedDict("BillingCodesRedeemResponse", {"object": Required[Literal["enterprise_plan_redemption"]], "status": Required[Literal["redeemed"]], "plan": Required[str | None]}, total=False)

BillingApprovalLinksCreateInput = TypedDict("BillingApprovalLinksCreateInput", {"kind": Required[Literal["add_payment_method", "upgrade"]], "plan": NotRequired[Literal["pro", "scale"]], "interval": NotRequired[Literal["month", "year"]]}, total=False)

BillingApprovalLinksCreateResponse = TypedDict("BillingApprovalLinksCreateResponse", {"object": Required[Literal["billing_approval_link"]], "id": Required[str], "kind": Required[Literal["add_payment_method", "upgrade"]], "plan": Required[Literal["pro", "scale"] | None], "interval": Required[Literal["month", "year"] | None], "status": Required[Literal["waiting", "completed", "declined", "expired"]], "approval_url": Required[str | None], "expires_at": Required[str | None], "completed_at": Required[str | None]}, total=False)

BillingApprovalLinksGetResponse = TypedDict("BillingApprovalLinksGetResponse", {"object": Required[Literal["billing_approval_link"]], "id": Required[str], "kind": Required[Literal["add_payment_method", "upgrade"]], "plan": Required[Literal["pro", "scale"] | None], "interval": Required[Literal["month", "year"] | None], "status": Required[Literal["waiting", "completed", "declined", "expired"]], "approval_url": Required[str | None], "expires_at": Required[str | None], "completed_at": Required[str | None]}, total=False)

AccountUpdateInput = TypedDict("AccountUpdateInput", {"name": Required[str]}, total=False)

AccountUpdateResponse = TypedDict("AccountUpdateResponse", {"object": Required[Literal["account"]], "name": Required[str]}, total=False)

AccountEmailPreferencesResponse = TypedDict("AccountEmailPreferencesResponse", {"object": Required[Literal["email_preferences"]], "members_and_invitations": Required[bool], "imports_and_exports": Required[bool], "integration_alerts": Required[bool], "weekly_summary": Required[bool]}, total=False)

AccountEmailPreferencesUpdateInput = TypedDict("AccountEmailPreferencesUpdateInput", {"members_and_invitations": NotRequired[bool], "imports_and_exports": NotRequired[bool], "integration_alerts": NotRequired[bool], "weekly_summary": NotRequired[bool]}, total=False)

AccountEmailPreferencesUpdateResponse = TypedDict("AccountEmailPreferencesUpdateResponse", {"object": Required[Literal["email_preferences"]], "members_and_invitations": Required[bool], "imports_and_exports": Required[bool], "integration_alerts": Required[bool], "weekly_summary": Required[bool]}, total=False)

NotificationsListInput = TypedDict("NotificationsListInput", {"filter": NotRequired[Literal["all", "unread"]], "cursor": NotRequired[str]}, total=False)

NotificationsListResponseDataItemActionsItem = TypedDict("NotificationsListResponseDataItemActionsItem", {"id": Required[str], "label": Required[str]}, total=False)

NotificationsListResponseDataItem = TypedDict("NotificationsListResponseDataItem", {"object": Required[Literal["notification"]], "id": Required[str], "workspace": Required[str | None], "kind": Required[str], "title": Required[str], "snippet": Required[str], "unread": Required[bool], "count": Required[int], "updated_at": Required[str | None], "actions": Required[list[NotificationsListResponseDataItemActionsItem]], "resolved": Required[str | None]}, total=False)

NotificationsListResponse = TypedDict("NotificationsListResponse", {"object": Required[Literal["list"]], "data": Required[list[NotificationsListResponseDataItem]], "next_cursor": Required[str | None], "unread_count": Required[int]}, total=False)

NotificationsUpdateInput = TypedDict("NotificationsUpdateInput", {"read": Required[bool]}, total=False)

NotificationsUpdateResponseActionsItem = TypedDict("NotificationsUpdateResponseActionsItem", {"id": Required[str], "label": Required[str]}, total=False)

NotificationsUpdateResponse = TypedDict("NotificationsUpdateResponse", {"object": Required[Literal["notification"]], "id": Required[str], "workspace": Required[str | None], "kind": Required[str], "title": Required[str], "snippet": Required[str], "unread": Required[bool], "count": Required[int], "updated_at": Required[str | None], "actions": Required[list[NotificationsUpdateResponseActionsItem]], "resolved": Required[str | None], "unread_count": Required[int]}, total=False)

NotificationsReadAllResponse = TypedDict("NotificationsReadAllResponse", {"object": Required[Literal["notifications_read"]], "unread_count": Required[int]}, total=False)

NotificationsRunActionInput = TypedDict("NotificationsRunActionInput", {"action": Required[str]}, total=False)

NotificationsRunActionResponseActionsItem = TypedDict("NotificationsRunActionResponseActionsItem", {"id": Required[str], "label": Required[str]}, total=False)

NotificationsRunActionResponse = TypedDict("NotificationsRunActionResponse", {"object": Required[Literal["notification"]], "id": Required[str], "workspace": Required[str | None], "kind": Required[str], "title": Required[str], "snippet": Required[str], "unread": Required[bool], "count": Required[int], "updated_at": Required[str | None], "actions": Required[list[NotificationsRunActionResponseActionsItem]], "resolved": Required[str | None], "unread_count": Required[int]}, total=False)

SupportTicketsCreateInput = TypedDict("SupportTicketsCreateInput", {"subject": Required[str], "message": Required[str], "topic": Required[Literal["account", "billing", "integration", "dashboard", "other"]], "request_id": NotRequired[str]}, total=False)

SupportTicketsCreateResponse = TypedDict("SupportTicketsCreateResponse", {"object": Required[Literal["support_ticket"]], "id": Required[str], "status": Required[Literal["received", "open", "resolved"]], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

SupportTicketsListInput = TypedDict("SupportTicketsListInput", {"cursor": NotRequired[str], "limit": NotRequired[int]}, total=False)

SupportTicketsListResponseDataItem = TypedDict("SupportTicketsListResponseDataItem", {"object": Required[Literal["support_ticket"]], "id": Required[str], "status": Required[Literal["received", "open", "resolved"]], "created_at": Required[str | None], "updated_at": Required[str | None]}, total=False)

SupportTicketsListResponse = TypedDict("SupportTicketsListResponse", {"object": Required[Literal["list"]], "data": Required[list[SupportTicketsListResponseDataItem]], "next_cursor": Required[str | None]}, total=False)

FeedbackCreateInput = TypedDict("FeedbackCreateInput", {"message": Required[str], "page": NotRequired[str]}, total=False)

FeedbackCreateResponse = TypedDict("FeedbackCreateResponse", {"object": Required[Literal["feedback"]], "sent": Required[Literal[True]]}, total=False)

class Evaluated(EvaluationsCreateResponseVariant0):
    source: Literal["abusezero"]

class Skipped(TypedDict):
    source: Literal["abusezero"]
    status: Literal["skipped"]
    reason: str
    object: NotRequired[str]

class LocalOutage(TypedDict):
    source: Literal["local_outage"]
    claim_id: str
    result: Literal["allow", "deny"]
    error: AbuseZeroError

Evaluation = Evaluated | Skipped | LocalOutage
