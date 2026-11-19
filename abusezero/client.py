from __future__ import annotations
from typing import Any
from .models import *
from .core import Core, AsyncCore

class AbuseZero(Core):
    _public = False

    def workspaces(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspacesListResponse:
        "List workspaces available to this identity."
        return self._call("workspaces.list", input, path, idempotency_key)

    def me(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MeGetResponse:
        "Read who this connection acts for: the person, their role and permissions, the workspace and the granted scopes."
        return self._call("me.get", input, path, idempotency_key)

    def api_keys(self, input: ApiKeysListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysListResponse:
        "List API keys with their type, scopes, last use and expiry. Secrets are never returned."
        return self._call("api-keys.list", input, path, idempotency_key)

    def create_api_key(self, input: ApiKeysCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysCreateResponse:
        "Create a secret or restricted key. Its secret is shown once, in the response."
        return self._call("api-keys.create", input, path, idempotency_key)

    def update_api_key(self, input: ApiKeysUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysUpdateResponse:
        "Change an API key's name, scopes or expiry."
        return self._call("api-keys.update", input, path, idempotency_key)

    def roll_api_key(self, input: ApiKeysRollInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysRollResponse:
        "Roll an API key. The old key keeps working for 1 hour, 24 hours or 7 days, and the new secret is shown once."
        return self._call("api-keys.roll", input, path, idempotency_key)

    def show_api_key_replacement(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysReplacementResponse:
        "Show a key's replacement once, when AbuseZero replaced the key for you."
        return self._call("api-keys.replacement", input, path, idempotency_key)

    def revoke_api_key(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysRevokeResponse:
        "Revoke an API key. It stops working at once."
        return self._call("api-keys.revoke", input, path, idempotency_key)

    def machine_clients(self, input: MachineClientsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsListResponse:
        "List machine clients."
        return self._call("machine-clients.list", input, path, idempotency_key)

    def create_machine_client(self, input: MachineClientsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsCreateResponse:
        "Create a machine client. Its secret is shown once, in the response."
        return self._call("machine-clients.create", input, path, idempotency_key)

    def rotate_machine_client_secret(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsRotateSecretResponse:
        "Rotate a machine client's secret. The old secret stops working at once, and the new one is shown once."
        return self._call("machine-clients.rotate_secret", input, path, idempotency_key)

    def revoke_machine_client(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsRevokeResponse:
        "Revoke a machine client. Its secret and access tokens stop working at once."
        return self._call("machine-clients.revoke", input, path, idempotency_key)

    def authorized_apps(self, input: AuthorizedAppsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuthorizedAppsListResponse:
        "List the apps and agents members authorized with OAuth."
        return self._call("authorized-apps.list", input, path, idempotency_key)

    def disconnect_authorized_app(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuthorizedAppsDisconnectResponse:
        "Disconnect one of your authorized apps. It loses access at once."
        return self._call("authorized-apps.disconnect", input, path, idempotency_key)

    def members(self, input: MembersListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MembersListResponse:
        "List the workspace's members with their roles and permissions."
        return self._call("members.list", input, path, idempotency_key)

    def update_member(self, input: MembersUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MembersUpdateResponse:
        "Change a member's role or permissions."
        return self._call("members.update", input, path, idempotency_key)

    def remove_member(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MembersRemoveResponse:
        "Remove a member from the workspace. They lose access at once."
        return self._call("members.remove", input, path, idempotency_key)

    def invitations(self, input: InvitationsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsListResponse:
        "List pending invitations."
        return self._call("invitations.list", input, path, idempotency_key)

    def invite_member(self, input: InvitationsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsCreateResponse:
        "Invite someone to the workspace by email, up to the plan's team seats."
        return self._call("invitations.create", input, path, idempotency_key)

    def resend_invitation(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsResendResponse:
        "Send a pending invitation again, as a new invitation that replaces it."
        return self._call("invitations.resend", input, path, idempotency_key)

    def cancel_invitation(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsCancelResponse:
        "Cancel a pending invitation."
        return self._call("invitations.cancel", input, path, idempotency_key)

    def workspace_settings(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceGetResponse:
        "Read the workspace's settings: name, icon, time zone, website, product type and data retention."
        return self._call("workspace.get", input, path, idempotency_key)

    def update_workspace_settings(self, input: WorkspaceUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceUpdateResponse:
        "Rename the workspace, or change its website, product type or time zone."
        return self._call("workspace.update", input, path, idempotency_key)

    def upload_workspace_icon(self, input: WorkspaceIconUploadInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceIconUploadResponse:
        "Upload a new workspace icon. It's checked before it's used."
        return self._call("workspace.icon_upload", input, path, idempotency_key)

    def remove_workspace_icon(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceIconRemoveResponse:
        "Remove the workspace icon."
        return self._call("workspace.icon_remove", input, path, idempotency_key)

    def workspace_icon_upload(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceIconUploadGetResponse:
        "Read whether an uploaded workspace icon is ready."
        return self._call("workspace.icon_upload_get", input, path, idempotency_key)

    def set_data_retention(self, input: WorkspaceRetentionInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceRetentionResponse:
        "Change how long evaluation evidence is kept. Shortening it deletes older evidence for good."
        return self._call("workspace.retention", input, path, idempotency_key)

    def setup_progress(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceSetupResponse:
        "Read setup progress: which Get started steps are done."
        return self._call("workspace.setup", input, path, idempotency_key)

    def finish_setup(self, input: WorkspaceSetupFinishInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceSetupFinishResponse:
        "Finish setting up the workspace, with its website, product type and time zone. Workspace owner only."
        return self._call("workspace.setup_finish", input, path, idempotency_key)

    def dismiss_setup_guide(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceSetupDismissResponse:
        "Stop Get started opening by itself for you."
        return self._call("workspace.setup_dismiss", input, path, idempotency_key)

    def leave_workspace(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceLeaveResponse:
        "Leave the workspace. Your access ends, and so does this sign-in's."
        return self._call("workspace.leave", input, path, idempotency_key)

    def evaluations(self, input: EvaluationsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsListResponse:
        "List evaluations."
        return self._call("evaluations.list", input, path, idempotency_key)

    def evaluate(self, input: EvaluationsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> Evaluation:
        "Evaluate a benefit claim."
        return self._call("evaluations.create", input, path, idempotency_key)

    def evaluation_filters(self, input: EvaluationsFiltersInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsFiltersResponse:
        "Read the benefits, results and reasons found in recent evaluations."
        return self._call("evaluations.filters", input, path, idempotency_key)

    def get_evaluation(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsGetResponse:
        "Read an evaluation."
        return self._call("evaluations.get", input, path, idempotency_key)

    def evaluation_graph(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsGraphResponse:
        "Read an evaluation association graph."
        return self._call("evaluations.graph", input, path, idempotency_key)

    def evaluation_evidence(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsEvidenceResponse:
        "Read retained evaluation evidence."
        return self._call("evaluations.evidence", input, path, idempotency_key)

    def outcomes(self, input: OutcomesListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OutcomesListResponse:
        "List outcomes."
        return self._call("outcomes.list", input, path, idempotency_key)

    def get_outcome(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OutcomesGetResponse:
        "Read an outcome."
        return self._call("outcomes.get", input, path, idempotency_key)

    def outcome(self, input: OutcomesReportInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OutcomesReportResponse:
        "Record a known outcome, including a benefit delivered after a deny."
        return self._call("outcomes.report", input, path, idempotency_key)

    def dry_run_evaluation(self, input: EvaluationsDryRunInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsDryRunResponseVariant0 | EvaluationsDryRunResponseVariant1:
        "Run a dry-run evaluation without writing claim history. Completed dry-run evaluations consume usage."
        return self._call("evaluations.dry_run", input, path, idempotency_key)

    def simulate(self, input: SimulationsSequenceInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SimulationsSequenceResponse:
        "Simulate a retained sequence."
        return self._call("simulations.sequence", input, path, idempotency_key)

    def replay(self, input: SimulationsReplayInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SimulationsReplayResponse:
        "Replay retained evaluations against a saved policy."
        return self._call("simulations.replay", input, path, idempotency_key)

    def benefits(self, input: BenefitsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsListResponse:
        "List benefits."
        return self._call("benefits.list", input, path, idempotency_key)

    def create_benefit(self, input: BenefitsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsCreateResponse:
        "Create a benefit."
        return self._call("benefits.create", input, path, idempotency_key)

    def get_benefit(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsGetResponse:
        "Read a benefit."
        return self._call("benefits.get", input, path, idempotency_key)

    def update_benefit(self, input: BenefitsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsUpdateResponse:
        "Update a benefit."
        return self._call("benefits.update", input, path, idempotency_key)

    def delete_benefit(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsDeleteResponse:
        "Permanently delete a benefit. This cannot be reversed."
        return self._call("benefits.delete", input, path, idempotency_key)

    def policies(self, input: PoliciesListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesListResponse:
        "List policies."
        return self._call("policies.list", input, path, idempotency_key)

    def create_policy(self, input: PoliciesCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesCreateResponse:
        "Create a policy."
        return self._call("policies.create", input, path, idempotency_key)

    def get_policy(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesGetResponse:
        "Read a policy."
        return self._call("policies.get", input, path, idempotency_key)

    def update_policy(self, input: PoliciesUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesUpdateResponse:
        "Update a policy."
        return self._call("policies.update", input, path, idempotency_key)

    def delete_policy(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesDeleteResponse:
        "Permanently delete an unused custom policy. This cannot be reversed."
        return self._call("policies.delete", input, path, idempotency_key)

    def duplicate_policy(self, input: PoliciesDuplicateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesDuplicateResponse:
        "Duplicate a policy."
        return self._call("policies.duplicate", input, path, idempotency_key)

    def policy_versions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesVersionsResponse:
        "List saved policy versions."
        return self._call("policies.versions", input, path, idempotency_key)

    def get_policy_version(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesVersionResponse:
        "Read a saved policy version."
        return self._call("policies.version", input, path, idempotency_key)

    def policy_signals(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesSignalsResponse:
        "List signals available to policy rules."
        return self._call("policies.signals", input, path, idempotency_key)

    def access_lists(self, input: AccessListsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsListResponse:
        "List access lists."
        return self._call("access-lists.list", input, path, idempotency_key)

    def add_access_list_entries(self, input: AccessListsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsCreateResponse:
        "Create an access list entry."
        return self._call("access-lists.create", input, path, idempotency_key)

    def get_access_list_entry(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsGetResponse:
        "Read an access list entry."
        return self._call("access-lists.get", input, path, idempotency_key)

    def delete_access_list_entry(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsDeleteResponse:
        "Permanently delete an access list entry. This cannot be reversed."
        return self._call("access-lists.delete", input, path, idempotency_key)

    def update_access_list_entry(self, input: AccessListsUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsUpdateResponse:
        "Update an access list entry's list, benefits, reason or expiry."
        return self._call("access-lists.update", input, path, idempotency_key)

    def look_up_identifier(self, input: IdentifiersLookupInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> IdentifiersLookupResponse:
        "Look up an ID, email address or IP address."
        return self._call("identifiers.lookup", input, path, idempotency_key)

    def custom_identifiers(self, input: CustomIdentifiersListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersListResponse:
        "List custom identifiers."
        return self._call("custom-identifiers.list", input, path, idempotency_key)

    def register_custom_identifier(self, input: CustomIdentifiersCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersCreateResponse:
        "Create a custom identifier."
        return self._call("custom-identifiers.create", input, path, idempotency_key)

    def get_custom_identifier(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersGetResponse:
        "Read a custom identifier."
        return self._call("custom-identifiers.get", input, path, idempotency_key)

    def delete_custom_identifier(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersDeleteResponse:
        "Permanently delete a custom identifier. This cannot be reversed."
        return self._call("custom-identifiers.delete", input, path, idempotency_key)

    def imports(self, input: ImportsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsListResponse:
        "List imports."
        return self._call("imports.list", input, path, idempotency_key)

    def import_claim_history(self, input: ImportsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsCreateResponse:
        "Import claim history: benefits you granted before AbuseZero. The rows wait for review unless the request sends confirm."
        return self._call("imports.create", input, path, idempotency_key)

    def create_csv_import(self, input: ImportsCsvInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsCsvResponse:
        "Start a claim history import from a CSV file, and get its upload link."
        return self._call("imports.csv", input, path, idempotency_key)

    def get_import(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsGetResponse:
        "Read an import: its state, its rows' counts and its progress."
        return self._call("imports.get", input, path, idempotency_key)

    def list_import_problems(self, input: ImportsProblemsInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsProblemsResponse:
        "List an import's rows that can't be added, with each row's problem and field."
        return self._call("imports.problems", input, path, idempotency_key)

    def import_problems_download(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsProblemsDownloadResponse:
        "Create a short-lived download link for an import's rows with problems."
        return self._call("imports.problems_download", input, path, idempotency_key)

    def confirm_import(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsConfirmResponse:
        "Add an import that's ready to review. Rows that need attention are skipped."
        return self._call("imports.confirm", input, path, idempotency_key)

    def discard_import(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsDiscardResponse:
        "Discard an import before it's confirmed. Nothing from it is added, and its rows are deleted."
        return self._call("imports.discard", input, path, idempotency_key)

    def fix_import_row(self, input: ImportsFixRowInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsFixRowResponse:
        "Fix one row that needs attention in an import that's ready to review."
        return self._call("imports.fix_row", input, path, idempotency_key)

    def skip_import_row(self, input: ImportsSkipRowInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsSkipRowResponse:
        "Skip one row that needs attention in an import that's ready to review."
        return self._call("imports.skip_row", input, path, idempotency_key)

    def exports(self, input: ExportsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsListResponse:
        "List exports."
        return self._call("exports.list", input, path, idempotency_key)

    def request_export(self, input: ExportsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsCreateResponse:
        "Create an evaluation export."
        return self._call("exports.create", input, path, idempotency_key)

    def get_export(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsGetResponse:
        "Read export status."
        return self._call("exports.get", input, path, idempotency_key)

    def export_download(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsDownloadResponse:
        "Create a short-lived export download URL."
        return self._call("exports.download", input, path, idempotency_key)

    def request_workspace_export(self, input: WorkspaceExportsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsCreateResponse:
        "Request a workspace data export, with the password for its ZIP files."
        return self._call("workspace-exports.create", input, path, idempotency_key)

    def workspace_export(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsStatusResponse:
        "Read the workspace's latest data export, and when the next one can be requested."
        return self._call("workspace-exports.status", input, path, idempotency_key)

    def workspace_export_download(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsDownloadResponse:
        "Get short-lived links to the files of a workspace data export you requested."
        return self._call("workspace-exports.download", input, path, idempotency_key)

    def delete_workspace_export(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsDeleteResponse:
        "Delete a workspace data export. Its files are removed for good."
        return self._call("workspace-exports.delete", input, path, idempotency_key)

    def dry_run_data_deletion(self, input: DeletionsDryRunInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsDryRunResponse:
        "Run a dry run of user-history deletion."
        return self._call("deletions.dry_run", input, path, idempotency_key)

    def data_deletions(self, input: DeletionsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsListResponse:
        "List data deletions."
        return self._call("deletions.list", input, path, idempotency_key)

    def request_data_deletion(self, input: DeletionsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsCreateResponse:
        "Permanently delete user history. This cannot be reversed."
        return self._call("deletions.create", input, path, idempotency_key)

    def get_data_deletion(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsGetResponse:
        "Read data-deletion status."
        return self._call("deletions.get", input, path, idempotency_key)

    def analytics(self, input: AnalyticsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AnalyticsListResponse:
        "Read analytics."
        return self._call("analytics.list", input, path, idempotency_key)

    def overview(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OverviewGetResponse:
        "Read the overview of the last 24 hours."
        return self._call("overview.get", input, path, idempotency_key)

    def benefit_value(self, input: AnalyticsValueInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AnalyticsValueResponse:
        "Read benefit value: what delivered claims were worth and what AbuseZero saved, in any supported currency."
        return self._call("analytics.value", input, path, idempotency_key)

    def denial_reasons(self, input: AnalyticsDenialReasonsInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AnalyticsDenialReasonsResponse:
        "Read why claims were denied: denied claims by reason, largest first."
        return self._call("analytics.denial_reasons", input, path, idempotency_key)

    def request_logs(self, input: RequestLogsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> RequestLogsListResponse:
        "Read request logs."
        return self._call("request-logs.list", input, path, idempotency_key)

    def get_request_log(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> RequestLogsGetResponse:
        "Read a request log."
        return self._call("request-logs.get", input, path, idempotency_key)

    def audit_logs(self, input: AuditLogsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuditLogsListResponse:
        "Read audit logs."
        return self._call("audit-logs.list", input, path, idempotency_key)

    def get_audit_log(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuditLogsGetResponse:
        "Read an audit log."
        return self._call("audit-logs.get", input, path, idempotency_key)

    def account_status(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountStatusGetResponse:
        "Read account status: credits, plan, limits and auto-reload."
        return self._call("account_status.get", input, path, idempotency_key)

    def integration_status(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> IntegrationStatusGetResponse:
        "Read integration status: whether keys, the browser script, evaluations, outcomes, webhooks and credits are working, and what to do next."
        return self._call("integration_status.get", input, path, idempotency_key)

    def events(self, input: EventsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EventsListResponse:
        "Read account events after a cursor, oldest first, waiting for the next one if you ask."
        return self._call("events.list", input, path, idempotency_key)

    def browser_collection(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BrowserCollectionGetResponse:
        "Read browser protection: your sites, where the script was seen, and what recent checks received."
        return self._call("browser_collection.get", input, path, idempotency_key)

    def update_browser_collection(self, input: BrowserCollectionUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BrowserCollectionUpdateResponse:
        "Update the sites listed for browser protection."
        return self._call("browser_collection.update", input, path, idempotency_key)

    def browser_script(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BrowserCollectionScriptResponse:
        "Get the browser script tag, with your publishable key filled in."
        return self._call("browser_collection.script", input, path, idempotency_key)

    def webhook_endpoints(self, input: WebhookEndpointsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsListResponse:
        "List webhook endpoints."
        return self._call("webhook-endpoints.list", input, path, idempotency_key)

    def create_webhook_endpoint(self, input: WebhookEndpointsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsCreateResponse:
        "Add a webhook endpoint. Its signing secret isn't in the response."
        return self._call("webhook-endpoints.create", input, path, idempotency_key)

    def get_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsGetResponse:
        "Read a webhook endpoint."
        return self._call("webhook-endpoints.get", input, path, idempotency_key)

    def update_webhook_endpoint(self, input: WebhookEndpointsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsUpdateResponse:
        "Change a webhook endpoint's URL, events or benefits."
        return self._call("webhook-endpoints.update", input, path, idempotency_key)

    def delete_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsDeleteResponse:
        "Permanently delete a webhook endpoint and its delivery log. This cannot be reversed."
        return self._call("webhook-endpoints.delete", input, path, idempotency_key)

    def send_webhook_test(self, input: WebhookEndpointsTestInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsTestResponse:
        "Send a test event to a webhook endpoint."
        return self._call("webhook-endpoints.test", input, path, idempotency_key)

    def enable_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsEnableResponse:
        "Enable a webhook endpoint."
        return self._call("webhook-endpoints.enable", input, path, idempotency_key)

    def disable_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsDisableResponse:
        "Disable a webhook endpoint. It gets only test events until it's enabled again."
        return self._call("webhook-endpoints.disable", input, path, idempotency_key)

    def webhook_signing_secret(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsSecretResponse:
        "Show a webhook endpoint's signing secret. Every read is recorded in the audit trail."
        return self._call("webhook-endpoints.secret", input, path, idempotency_key)

    def rotate_webhook_signing_secret(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsRotateSecretResponse:
        "Rotate a webhook endpoint's signing secret. The previous secret keeps signing for 24 hours."
        return self._call("webhook-endpoints.rotate_secret", input, path, idempotency_key)

    def webhook_usage(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesUsageResponse:
        "Read today's webhook deliveries against the daily limit."
        return self._call("webhook-deliveries.usage", input, path, idempotency_key)

    def webhook_deliveries(self, input: WebhookDeliveriesListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesListResponse:
        "List webhook deliveries."
        return self._call("webhook-deliveries.list", input, path, idempotency_key)

    def get_webhook_delivery(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesGetResponse:
        "Read a webhook delivery with its request body and attempts."
        return self._call("webhook-deliveries.get", input, path, idempotency_key)

    def resend_webhook_delivery(self, input: WebhookDeliveriesResendInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesResendResponse:
        "Send a webhook delivery's event again, to the endpoint's current URL or the URL it was first sent to."
        return self._call("webhook-deliveries.resend", input, path, idempotency_key)

    def plan(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPlanResponse:
        "Read the plan, its billing period and renewal date, and the workspace's limits."
        return self._call("billing.plan", input, path, idempotency_key)

    def usage(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingUsageResponse:
        "Read credits and usage: allowance credits, pay-as-you-go credits, protected benefits and team seats."
        return self._call("billing.usage", input, path, idempotency_key)

    def credit_history(self, input: BillingCreditHistoryInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCreditHistoryResponse:
        "List credit history: credits added, used and removed."
        return self._call("billing.credit_history", input, path, idempotency_key)

    def daily_usage(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDailyUsageResponse:
        "Read credits used each day of the last 30 days."
        return self._call("billing.daily_usage", input, path, idempotency_key)

    def enterprise_plans(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingEnterprisePlansResponse:
        "List the workspace's Enterprise plans and what each one adds."
        return self._call("billing.enterprise_plans", input, path, idempotency_key)

    def preview_enterprise_plan_code(self, input: BillingCodesPreviewInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCodesPreviewResponse:
        "Preview what an Enterprise plan code adds, without redeeming it."
        return self._call("billing.codes.preview", input, path, idempotency_key)

    def upcoming_charge(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingUpcomingResponse:
        "Read the next charge: its amount, date and payment method."
        return self._call("billing.upcoming", input, path, idempotency_key)

    def invoices(self, input: BillingInvoicesInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingInvoicesResponse:
        "List invoices, newest first, each with its secure payment page link."
        return self._call("billing.invoices", input, path, idempotency_key)

    def payment_methods(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsResponse:
        "List saved payment methods: the default first, then the backup payment methods in order."
        return self._call("billing.payment_methods", input, path, idempotency_key)

    def billing_details(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDetailsResponse:
        "Read billing details: name, billing email, address and tax ID."
        return self._call("billing.details", input, path, idempotency_key)

    def update_billing_details(self, input: BillingDetailsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDetailsUpdateResponse:
        "Save billing details: name, billing email, address and tax ID."
        return self._call("billing.details.update", input, path, idempotency_key)

    def get_payment(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentsGetResponse:
        "Read a payment's progress."
        return self._call("billing.payments.get", input, path, idempotency_key)

    def quote_plan_change(self, input: BillingQuotesCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingQuotesCreateResponse:
        "Get a quote for a plan or billing period change: what it costs now and at renewal. Nothing changes."
        return self._call("billing.quotes.create", input, path, idempotency_key)

    def set_low_credit_alert(self, input: BillingLowCreditAlertUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingLowCreditAlertUpdateResponse:
        "Set the low-credit alert level, or clear it to be alerted by your usage pace."
        return self._call("billing.low_credit_alert.update", input, path, idempotency_key)

    def choose_what_stays_active(self, input: BillingOverLimitChooseInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingOverLimitChooseResponse:
        "Choose what stays active over your plan limits: keep one benefit or member active and pause another."
        return self._call("billing.over_limit.choose", input, path, idempotency_key)

    def set_auto_reload(self, input: BillingAutoReloadUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingAutoReloadUpdateResponse:
        "Set up, change or turn off auto-reload. When it's on, it charges the default payment method on its own."
        return self._call("billing.auto_reload.update", input, path, idempotency_key)

    def buy_credits(self, input: BillingCreditsBuyInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCreditsBuyResponse:
        "Buy credits with a saved payment method."
        return self._call("billing.credits.buy", input, path, idempotency_key)

    def retry_credit_purchase(self, input: BillingCreditsRetryInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCreditsRetryResponse:
        "Try a declined credit purchase again, with the default or another saved payment method."
        return self._call("billing.credits.retry", input, path, idempotency_key)

    def confirm_plan_change(self, input: BillingPlanChangeInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPlanChangeResponse:
        "Confirm a quote to move to a higher plan on the same or a longer billing period, Builder to Pro or Scale included, or yearly billing on the same plan, with a saved payment method."
        return self._call("billing.plan.change", input, path, idempotency_key)

    def undo_scheduled_downgrade(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDowngradeUndoResponse:
        "Undo a scheduled downgrade, so the subscription renews on the current plan."
        return self._call("billing.downgrade.undo", input, path, idempotency_key)

    def resume_subscription(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingSubscriptionResumeResponse:
        "Resume a canceled subscription before it ends, so it renews again."
        return self._call("billing.subscription.resume", input, path, idempotency_key)

    def pay_overdue_invoice(self, input: BillingOverduePayInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingOverduePayResponse:
        "Pay an overdue invoice with a saved payment method."
        return self._call("billing.overdue.pay", input, path, idempotency_key)

    def set_default_payment_method(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsDefaultResponse:
        "Make a saved payment method the default. It then pays anything overdue."
        return self._call("billing.payment_methods.default", input, path, idempotency_key)

    def move_backup_payment_method(self, input: BillingPaymentMethodsMoveInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsMoveResponse:
        "Move a backup payment method up or down one place in the order."
        return self._call("billing.payment_methods.move", input, path, idempotency_key)

    def remove_payment_method(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsRemoveResponse:
        "Remove a saved payment method. The default can't be removed."
        return self._call("billing.payment_methods.remove", input, path, idempotency_key)

    def redeem_enterprise_plan_code(self, input: BillingCodesRedeemInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCodesRedeemResponse:
        "Redeem an Enterprise plan code. It adds the plan to the workspace for good."
        return self._call("billing.codes.redeem", input, path, idempotency_key)

    def create_billing_approval_link(self, input: BillingApprovalLinksCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingApprovalLinksCreateResponse:
        "Make a link for the owner to add a payment method, or to add one and pay for an upgrade, when the workspace has none saved."
        return self._call("billing.approval_links.create", input, path, idempotency_key)

    def billing_approval_link(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingApprovalLinksGetResponse:
        "Read whether the owner finished a billing approval link, declined it or let it expire."
        return self._call("billing.approval_links.get", input, path, idempotency_key)

    def update_account_name(self, input: AccountUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountUpdateResponse:
        "Change your name."
        return self._call("account.update", input, path, idempotency_key)

    def email_preferences(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountEmailPreferencesResponse:
        "Read which optional emails you get."
        return self._call("account.email_preferences", input, path, idempotency_key)

    def update_email_preferences(self, input: AccountEmailPreferencesUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountEmailPreferencesUpdateResponse:
        "Choose which optional emails you get. Sign-in, security and billing emails always go."
        return self._call("account.email_preferences_update", input, path, idempotency_key)

    def notifications(self, input: NotificationsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsListResponse:
        "List your notifications, and how many are unread."
        return self._call("notifications.list", input, path, idempotency_key)

    def mark_notification(self, input: NotificationsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsUpdateResponse:
        "Mark a notification as read or unread."
        return self._call("notifications.update", input, path, idempotency_key)

    def mark_all_notifications_read(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsReadAllResponse:
        "Mark all your notifications as read."
        return self._call("notifications.read_all", input, path, idempotency_key)

    def run_notification_action(self, input: NotificationsRunActionInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsRunActionResponse:
        "Run one of a notification's actions. It also needs the scope of the action it runs."
        return self._call("notifications.run_action", input, path, idempotency_key)

    def contact_support(self, input: SupportTicketsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SupportTicketsCreateResponse:
        "Contact AbuseZero support about this workspace. Support replies to your account email."
        return self._call("support-tickets.create", input, path, idempotency_key)

    def support_tickets(self, input: SupportTicketsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SupportTicketsListResponse:
        "List the support tickets you sent about this workspace."
        return self._call("support-tickets.list", input, path, idempotency_key)

    def send_feedback(self, input: FeedbackCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> FeedbackCreateResponse:
        "Send product feedback to the AbuseZero team."
        return self._call("feedback.create", input, path, idempotency_key)
class AbuseZeroPublic(Core):
    _public = True

    def pricing(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicPricingResponse:
        "Read AbuseZero's plans and prices, what each plan includes and what every plan shares."
        return self._call("public.pricing", input, path, idempotency_key)

    def price_quote(self, input: PublicPricingQuoteInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicPricingQuoteResponse:
        "Get the exact price of a plan for a month or a year, or of a credit pack."
        return self._call("public.pricing_quote", input, path, idempotency_key)

    def docs(self, input: PublicDocsInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicDocsResponse:
        "List the developer docs pages, with each page's title, path and last update."
        return self._call("public.docs", input, path, idempotency_key)

    def search_docs(self, input: PublicDocsSearchInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicDocsSearchResponse:
        "Search the developer docs."
        return self._call("public.docs_search", input, path, idempotency_key)

    def public_docs_page(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicDocsPageResponse:
        "Read a developer docs page as Markdown."
        return self._call("public.docs_page", input, path, idempotency_key)

    def help_articles(self, input: PublicHelpInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicHelpResponse:
        "List the help center's articles, with each article's title, path and last update."
        return self._call("public.help", input, path, idempotency_key)

    def search_help(self, input: PublicHelpSearchInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicHelpSearchResponse:
        "Search the help center."
        return self._call("public.help_search", input, path, idempotency_key)

    def public_help_article(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicHelpArticleResponse:
        "Read a help center article as Markdown."
        return self._call("public.help_article", input, path, idempotency_key)

    def openapi(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicOpenapiResponse:
        "Read the OpenAPI document for the AbuseZero API."
        return self._call("public.openapi", input, path, idempotency_key)

    def actions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicActionsResponse:
        "List every API action with its MCP tool, CLI command and scope."
        return self._call("public.actions", input, path, idempotency_key)

    def error_codes(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicErrorsResponse:
        "List the API's error codes: what each means, whether to retry and what to do next."
        return self._call("public.errors", input, path, idempotency_key)

    def reason_codes(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicReasonsResponse:
        "List the reason codes evaluations return."
        return self._call("public.reasons", input, path, idempotency_key)

    def webhook_event_types(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicWebhookEventsResponse:
        "List the webhook event types, each with an example payload."
        return self._call("public.webhook_events", input, path, idempotency_key)

    def conditions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicConditionsResponse:
        "List the conditions the rules in custom policies can use."
        return self._call("public.conditions", input, path, idempotency_key)

    def glossary(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicGlossaryResponse:
        "Read the glossary and the developer FAQ."
        return self._call("public.glossary", input, path, idempotency_key)

    def legal_documents(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicLegalResponse:
        "List AbuseZero's legal documents, with each one's version and effective date."
        return self._call("public.legal", input, path, idempotency_key)

    def legal_document(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicLegalDocumentResponse:
        "Read a legal document as Markdown."
        return self._call("public.legal_document", input, path, idempotency_key)

    def changelog(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicChangelogResponse:
        "Read the product changelog."
        return self._call("public.changelog", input, path, idempotency_key)

    def blog_posts(self, input: PublicBlogInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicBlogResponse:
        "List blog posts."
        return self._call("public.blog", input, path, idempotency_key)

    def blog_post(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicBlogPostResponse:
        "Read a blog post as Markdown."
        return self._call("public.blog_post", input, path, idempotency_key)

    def versions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicVersionsResponse:
        "Read the latest npm package version and the browser script address."
        return self._call("public.versions", input, path, idempotency_key)

    def service_status(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicStatusResponse:
        "Read whether AbuseZero is operational or degraded."
        return self._call("public.status", input, path, idempotency_key)

    def contacts(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicContactsResponse:
        "Read how to reach AbuseZero's support, sales and security."
        return self._call("public.contacts", input, path, idempotency_key)

    def contact_sales(self, input: PublicContactSalesInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicContactSalesResponse:
        "Send a message to AbuseZero's sales team about an Enterprise plan."
        return self._call("public.contact_sales", input, path, idempotency_key)

    def contact_support(self, input: PublicContactSupportInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicContactSupportResponse:
        "Send a request to AbuseZero support without an account."
        return self._call("public.contact_support", input, path, idempotency_key)

    def start_onboarding(self, input: PublicOnboardingStartInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicOnboardingStartResponse:
        "Start agent onboarding for a new workspace: returns the approval link for the person, and a secret only this agent keeps."
        return self._call("public.onboarding_start", input, path, idempotency_key)

    def onboarding_status(self, input: PublicOnboardingStatusInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicOnboardingStatusResponse:
        "Read whether the person finished onboarding, optionally waiting up to 25 seconds, and how to collect the sign-in."
        return self._call("public.onboarding_status", input, path, idempotency_key)
class AsyncAbuseZero(AsyncCore):
    _public = False

    async def workspaces(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspacesListResponse:
        "List workspaces available to this identity."
        return await self._call("workspaces.list", input, path, idempotency_key)

    async def me(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MeGetResponse:
        "Read who this connection acts for: the person, their role and permissions, the workspace and the granted scopes."
        return await self._call("me.get", input, path, idempotency_key)

    async def api_keys(self, input: ApiKeysListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysListResponse:
        "List API keys with their type, scopes, last use and expiry. Secrets are never returned."
        return await self._call("api-keys.list", input, path, idempotency_key)

    async def create_api_key(self, input: ApiKeysCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysCreateResponse:
        "Create a secret or restricted key. Its secret is shown once, in the response."
        return await self._call("api-keys.create", input, path, idempotency_key)

    async def update_api_key(self, input: ApiKeysUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysUpdateResponse:
        "Change an API key's name, scopes or expiry."
        return await self._call("api-keys.update", input, path, idempotency_key)

    async def roll_api_key(self, input: ApiKeysRollInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysRollResponse:
        "Roll an API key. The old key keeps working for 1 hour, 24 hours or 7 days, and the new secret is shown once."
        return await self._call("api-keys.roll", input, path, idempotency_key)

    async def show_api_key_replacement(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysReplacementResponse:
        "Show a key's replacement once, when AbuseZero replaced the key for you."
        return await self._call("api-keys.replacement", input, path, idempotency_key)

    async def revoke_api_key(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ApiKeysRevokeResponse:
        "Revoke an API key. It stops working at once."
        return await self._call("api-keys.revoke", input, path, idempotency_key)

    async def machine_clients(self, input: MachineClientsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsListResponse:
        "List machine clients."
        return await self._call("machine-clients.list", input, path, idempotency_key)

    async def create_machine_client(self, input: MachineClientsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsCreateResponse:
        "Create a machine client. Its secret is shown once, in the response."
        return await self._call("machine-clients.create", input, path, idempotency_key)

    async def rotate_machine_client_secret(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsRotateSecretResponse:
        "Rotate a machine client's secret. The old secret stops working at once, and the new one is shown once."
        return await self._call("machine-clients.rotate_secret", input, path, idempotency_key)

    async def revoke_machine_client(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MachineClientsRevokeResponse:
        "Revoke a machine client. Its secret and access tokens stop working at once."
        return await self._call("machine-clients.revoke", input, path, idempotency_key)

    async def authorized_apps(self, input: AuthorizedAppsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuthorizedAppsListResponse:
        "List the apps and agents members authorized with OAuth."
        return await self._call("authorized-apps.list", input, path, idempotency_key)

    async def disconnect_authorized_app(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuthorizedAppsDisconnectResponse:
        "Disconnect one of your authorized apps. It loses access at once."
        return await self._call("authorized-apps.disconnect", input, path, idempotency_key)

    async def members(self, input: MembersListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MembersListResponse:
        "List the workspace's members with their roles and permissions."
        return await self._call("members.list", input, path, idempotency_key)

    async def update_member(self, input: MembersUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MembersUpdateResponse:
        "Change a member's role or permissions."
        return await self._call("members.update", input, path, idempotency_key)

    async def remove_member(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> MembersRemoveResponse:
        "Remove a member from the workspace. They lose access at once."
        return await self._call("members.remove", input, path, idempotency_key)

    async def invitations(self, input: InvitationsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsListResponse:
        "List pending invitations."
        return await self._call("invitations.list", input, path, idempotency_key)

    async def invite_member(self, input: InvitationsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsCreateResponse:
        "Invite someone to the workspace by email, up to the plan's team seats."
        return await self._call("invitations.create", input, path, idempotency_key)

    async def resend_invitation(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsResendResponse:
        "Send a pending invitation again, as a new invitation that replaces it."
        return await self._call("invitations.resend", input, path, idempotency_key)

    async def cancel_invitation(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> InvitationsCancelResponse:
        "Cancel a pending invitation."
        return await self._call("invitations.cancel", input, path, idempotency_key)

    async def workspace_settings(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceGetResponse:
        "Read the workspace's settings: name, icon, time zone, website, product type and data retention."
        return await self._call("workspace.get", input, path, idempotency_key)

    async def update_workspace_settings(self, input: WorkspaceUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceUpdateResponse:
        "Rename the workspace, or change its website, product type or time zone."
        return await self._call("workspace.update", input, path, idempotency_key)

    async def upload_workspace_icon(self, input: WorkspaceIconUploadInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceIconUploadResponse:
        "Upload a new workspace icon. It's checked before it's used."
        return await self._call("workspace.icon_upload", input, path, idempotency_key)

    async def remove_workspace_icon(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceIconRemoveResponse:
        "Remove the workspace icon."
        return await self._call("workspace.icon_remove", input, path, idempotency_key)

    async def workspace_icon_upload(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceIconUploadGetResponse:
        "Read whether an uploaded workspace icon is ready."
        return await self._call("workspace.icon_upload_get", input, path, idempotency_key)

    async def set_data_retention(self, input: WorkspaceRetentionInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceRetentionResponse:
        "Change how long evaluation evidence is kept. Shortening it deletes older evidence for good."
        return await self._call("workspace.retention", input, path, idempotency_key)

    async def setup_progress(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceSetupResponse:
        "Read setup progress: which Get started steps are done."
        return await self._call("workspace.setup", input, path, idempotency_key)

    async def finish_setup(self, input: WorkspaceSetupFinishInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceSetupFinishResponse:
        "Finish setting up the workspace, with its website, product type and time zone. Workspace owner only."
        return await self._call("workspace.setup_finish", input, path, idempotency_key)

    async def dismiss_setup_guide(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceSetupDismissResponse:
        "Stop Get started opening by itself for you."
        return await self._call("workspace.setup_dismiss", input, path, idempotency_key)

    async def leave_workspace(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceLeaveResponse:
        "Leave the workspace. Your access ends, and so does this sign-in's."
        return await self._call("workspace.leave", input, path, idempotency_key)

    async def evaluations(self, input: EvaluationsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsListResponse:
        "List evaluations."
        return await self._call("evaluations.list", input, path, idempotency_key)

    async def evaluate(self, input: EvaluationsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> Evaluation:
        "Evaluate a benefit claim."
        return await self._call("evaluations.create", input, path, idempotency_key)

    async def evaluation_filters(self, input: EvaluationsFiltersInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsFiltersResponse:
        "Read the benefits, results and reasons found in recent evaluations."
        return await self._call("evaluations.filters", input, path, idempotency_key)

    async def get_evaluation(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsGetResponse:
        "Read an evaluation."
        return await self._call("evaluations.get", input, path, idempotency_key)

    async def evaluation_graph(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsGraphResponse:
        "Read an evaluation association graph."
        return await self._call("evaluations.graph", input, path, idempotency_key)

    async def evaluation_evidence(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsEvidenceResponse:
        "Read retained evaluation evidence."
        return await self._call("evaluations.evidence", input, path, idempotency_key)

    async def outcomes(self, input: OutcomesListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OutcomesListResponse:
        "List outcomes."
        return await self._call("outcomes.list", input, path, idempotency_key)

    async def get_outcome(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OutcomesGetResponse:
        "Read an outcome."
        return await self._call("outcomes.get", input, path, idempotency_key)

    async def outcome(self, input: OutcomesReportInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OutcomesReportResponse:
        "Record a known outcome, including a benefit delivered after a deny."
        return await self._call("outcomes.report", input, path, idempotency_key)

    async def dry_run_evaluation(self, input: EvaluationsDryRunInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EvaluationsDryRunResponseVariant0 | EvaluationsDryRunResponseVariant1:
        "Run a dry-run evaluation without writing claim history. Completed dry-run evaluations consume usage."
        return await self._call("evaluations.dry_run", input, path, idempotency_key)

    async def simulate(self, input: SimulationsSequenceInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SimulationsSequenceResponse:
        "Simulate a retained sequence."
        return await self._call("simulations.sequence", input, path, idempotency_key)

    async def replay(self, input: SimulationsReplayInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SimulationsReplayResponse:
        "Replay retained evaluations against a saved policy."
        return await self._call("simulations.replay", input, path, idempotency_key)

    async def benefits(self, input: BenefitsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsListResponse:
        "List benefits."
        return await self._call("benefits.list", input, path, idempotency_key)

    async def create_benefit(self, input: BenefitsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsCreateResponse:
        "Create a benefit."
        return await self._call("benefits.create", input, path, idempotency_key)

    async def get_benefit(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsGetResponse:
        "Read a benefit."
        return await self._call("benefits.get", input, path, idempotency_key)

    async def update_benefit(self, input: BenefitsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsUpdateResponse:
        "Update a benefit."
        return await self._call("benefits.update", input, path, idempotency_key)

    async def delete_benefit(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BenefitsDeleteResponse:
        "Permanently delete a benefit. This cannot be reversed."
        return await self._call("benefits.delete", input, path, idempotency_key)

    async def policies(self, input: PoliciesListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesListResponse:
        "List policies."
        return await self._call("policies.list", input, path, idempotency_key)

    async def create_policy(self, input: PoliciesCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesCreateResponse:
        "Create a policy."
        return await self._call("policies.create", input, path, idempotency_key)

    async def get_policy(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesGetResponse:
        "Read a policy."
        return await self._call("policies.get", input, path, idempotency_key)

    async def update_policy(self, input: PoliciesUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesUpdateResponse:
        "Update a policy."
        return await self._call("policies.update", input, path, idempotency_key)

    async def delete_policy(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesDeleteResponse:
        "Permanently delete an unused custom policy. This cannot be reversed."
        return await self._call("policies.delete", input, path, idempotency_key)

    async def duplicate_policy(self, input: PoliciesDuplicateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesDuplicateResponse:
        "Duplicate a policy."
        return await self._call("policies.duplicate", input, path, idempotency_key)

    async def policy_versions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesVersionsResponse:
        "List saved policy versions."
        return await self._call("policies.versions", input, path, idempotency_key)

    async def get_policy_version(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesVersionResponse:
        "Read a saved policy version."
        return await self._call("policies.version", input, path, idempotency_key)

    async def policy_signals(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PoliciesSignalsResponse:
        "List signals available to policy rules."
        return await self._call("policies.signals", input, path, idempotency_key)

    async def access_lists(self, input: AccessListsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsListResponse:
        "List access lists."
        return await self._call("access-lists.list", input, path, idempotency_key)

    async def add_access_list_entries(self, input: AccessListsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsCreateResponse:
        "Create an access list entry."
        return await self._call("access-lists.create", input, path, idempotency_key)

    async def get_access_list_entry(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsGetResponse:
        "Read an access list entry."
        return await self._call("access-lists.get", input, path, idempotency_key)

    async def delete_access_list_entry(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsDeleteResponse:
        "Permanently delete an access list entry. This cannot be reversed."
        return await self._call("access-lists.delete", input, path, idempotency_key)

    async def update_access_list_entry(self, input: AccessListsUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccessListsUpdateResponse:
        "Update an access list entry's list, benefits, reason or expiry."
        return await self._call("access-lists.update", input, path, idempotency_key)

    async def look_up_identifier(self, input: IdentifiersLookupInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> IdentifiersLookupResponse:
        "Look up an ID, email address or IP address."
        return await self._call("identifiers.lookup", input, path, idempotency_key)

    async def custom_identifiers(self, input: CustomIdentifiersListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersListResponse:
        "List custom identifiers."
        return await self._call("custom-identifiers.list", input, path, idempotency_key)

    async def register_custom_identifier(self, input: CustomIdentifiersCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersCreateResponse:
        "Create a custom identifier."
        return await self._call("custom-identifiers.create", input, path, idempotency_key)

    async def get_custom_identifier(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersGetResponse:
        "Read a custom identifier."
        return await self._call("custom-identifiers.get", input, path, idempotency_key)

    async def delete_custom_identifier(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> CustomIdentifiersDeleteResponse:
        "Permanently delete a custom identifier. This cannot be reversed."
        return await self._call("custom-identifiers.delete", input, path, idempotency_key)

    async def imports(self, input: ImportsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsListResponse:
        "List imports."
        return await self._call("imports.list", input, path, idempotency_key)

    async def import_claim_history(self, input: ImportsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsCreateResponse:
        "Import claim history: benefits you granted before AbuseZero. The rows wait for review unless the request sends confirm."
        return await self._call("imports.create", input, path, idempotency_key)

    async def create_csv_import(self, input: ImportsCsvInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsCsvResponse:
        "Start a claim history import from a CSV file, and get its upload link."
        return await self._call("imports.csv", input, path, idempotency_key)

    async def get_import(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsGetResponse:
        "Read an import: its state, its rows' counts and its progress."
        return await self._call("imports.get", input, path, idempotency_key)

    async def list_import_problems(self, input: ImportsProblemsInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsProblemsResponse:
        "List an import's rows that can't be added, with each row's problem and field."
        return await self._call("imports.problems", input, path, idempotency_key)

    async def import_problems_download(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsProblemsDownloadResponse:
        "Create a short-lived download link for an import's rows with problems."
        return await self._call("imports.problems_download", input, path, idempotency_key)

    async def confirm_import(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsConfirmResponse:
        "Add an import that's ready to review. Rows that need attention are skipped."
        return await self._call("imports.confirm", input, path, idempotency_key)

    async def discard_import(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsDiscardResponse:
        "Discard an import before it's confirmed. Nothing from it is added, and its rows are deleted."
        return await self._call("imports.discard", input, path, idempotency_key)

    async def fix_import_row(self, input: ImportsFixRowInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsFixRowResponse:
        "Fix one row that needs attention in an import that's ready to review."
        return await self._call("imports.fix_row", input, path, idempotency_key)

    async def skip_import_row(self, input: ImportsSkipRowInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ImportsSkipRowResponse:
        "Skip one row that needs attention in an import that's ready to review."
        return await self._call("imports.skip_row", input, path, idempotency_key)

    async def exports(self, input: ExportsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsListResponse:
        "List exports."
        return await self._call("exports.list", input, path, idempotency_key)

    async def request_export(self, input: ExportsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsCreateResponse:
        "Create an evaluation export."
        return await self._call("exports.create", input, path, idempotency_key)

    async def get_export(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsGetResponse:
        "Read export status."
        return await self._call("exports.get", input, path, idempotency_key)

    async def export_download(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> ExportsDownloadResponse:
        "Create a short-lived export download URL."
        return await self._call("exports.download", input, path, idempotency_key)

    async def request_workspace_export(self, input: WorkspaceExportsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsCreateResponse:
        "Request a workspace data export, with the password for its ZIP files."
        return await self._call("workspace-exports.create", input, path, idempotency_key)

    async def workspace_export(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsStatusResponse:
        "Read the workspace's latest data export, and when the next one can be requested."
        return await self._call("workspace-exports.status", input, path, idempotency_key)

    async def workspace_export_download(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsDownloadResponse:
        "Get short-lived links to the files of a workspace data export you requested."
        return await self._call("workspace-exports.download", input, path, idempotency_key)

    async def delete_workspace_export(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WorkspaceExportsDeleteResponse:
        "Delete a workspace data export. Its files are removed for good."
        return await self._call("workspace-exports.delete", input, path, idempotency_key)

    async def dry_run_data_deletion(self, input: DeletionsDryRunInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsDryRunResponse:
        "Run a dry run of user-history deletion."
        return await self._call("deletions.dry_run", input, path, idempotency_key)

    async def data_deletions(self, input: DeletionsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsListResponse:
        "List data deletions."
        return await self._call("deletions.list", input, path, idempotency_key)

    async def request_data_deletion(self, input: DeletionsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsCreateResponse:
        "Permanently delete user history. This cannot be reversed."
        return await self._call("deletions.create", input, path, idempotency_key)

    async def get_data_deletion(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> DeletionsGetResponse:
        "Read data-deletion status."
        return await self._call("deletions.get", input, path, idempotency_key)

    async def analytics(self, input: AnalyticsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AnalyticsListResponse:
        "Read analytics."
        return await self._call("analytics.list", input, path, idempotency_key)

    async def overview(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> OverviewGetResponse:
        "Read the overview of the last 24 hours."
        return await self._call("overview.get", input, path, idempotency_key)

    async def benefit_value(self, input: AnalyticsValueInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AnalyticsValueResponse:
        "Read benefit value: what delivered claims were worth and what AbuseZero saved, in any supported currency."
        return await self._call("analytics.value", input, path, idempotency_key)

    async def denial_reasons(self, input: AnalyticsDenialReasonsInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AnalyticsDenialReasonsResponse:
        "Read why claims were denied: denied claims by reason, largest first."
        return await self._call("analytics.denial_reasons", input, path, idempotency_key)

    async def request_logs(self, input: RequestLogsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> RequestLogsListResponse:
        "Read request logs."
        return await self._call("request-logs.list", input, path, idempotency_key)

    async def get_request_log(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> RequestLogsGetResponse:
        "Read a request log."
        return await self._call("request-logs.get", input, path, idempotency_key)

    async def audit_logs(self, input: AuditLogsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuditLogsListResponse:
        "Read audit logs."
        return await self._call("audit-logs.list", input, path, idempotency_key)

    async def get_audit_log(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AuditLogsGetResponse:
        "Read an audit log."
        return await self._call("audit-logs.get", input, path, idempotency_key)

    async def account_status(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountStatusGetResponse:
        "Read account status: credits, plan, limits and auto-reload."
        return await self._call("account_status.get", input, path, idempotency_key)

    async def integration_status(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> IntegrationStatusGetResponse:
        "Read integration status: whether keys, the browser script, evaluations, outcomes, webhooks and credits are working, and what to do next."
        return await self._call("integration_status.get", input, path, idempotency_key)

    async def events(self, input: EventsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> EventsListResponse:
        "Read account events after a cursor, oldest first, waiting for the next one if you ask."
        return await self._call("events.list", input, path, idempotency_key)

    async def browser_collection(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BrowserCollectionGetResponse:
        "Read browser protection: your sites, where the script was seen, and what recent checks received."
        return await self._call("browser_collection.get", input, path, idempotency_key)

    async def update_browser_collection(self, input: BrowserCollectionUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BrowserCollectionUpdateResponse:
        "Update the sites listed for browser protection."
        return await self._call("browser_collection.update", input, path, idempotency_key)

    async def browser_script(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BrowserCollectionScriptResponse:
        "Get the browser script tag, with your publishable key filled in."
        return await self._call("browser_collection.script", input, path, idempotency_key)

    async def webhook_endpoints(self, input: WebhookEndpointsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsListResponse:
        "List webhook endpoints."
        return await self._call("webhook-endpoints.list", input, path, idempotency_key)

    async def create_webhook_endpoint(self, input: WebhookEndpointsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsCreateResponse:
        "Add a webhook endpoint. Its signing secret isn't in the response."
        return await self._call("webhook-endpoints.create", input, path, idempotency_key)

    async def get_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsGetResponse:
        "Read a webhook endpoint."
        return await self._call("webhook-endpoints.get", input, path, idempotency_key)

    async def update_webhook_endpoint(self, input: WebhookEndpointsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsUpdateResponse:
        "Change a webhook endpoint's URL, events or benefits."
        return await self._call("webhook-endpoints.update", input, path, idempotency_key)

    async def delete_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsDeleteResponse:
        "Permanently delete a webhook endpoint and its delivery log. This cannot be reversed."
        return await self._call("webhook-endpoints.delete", input, path, idempotency_key)

    async def send_webhook_test(self, input: WebhookEndpointsTestInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsTestResponse:
        "Send a test event to a webhook endpoint."
        return await self._call("webhook-endpoints.test", input, path, idempotency_key)

    async def enable_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsEnableResponse:
        "Enable a webhook endpoint."
        return await self._call("webhook-endpoints.enable", input, path, idempotency_key)

    async def disable_webhook_endpoint(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsDisableResponse:
        "Disable a webhook endpoint. It gets only test events until it's enabled again."
        return await self._call("webhook-endpoints.disable", input, path, idempotency_key)

    async def webhook_signing_secret(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsSecretResponse:
        "Show a webhook endpoint's signing secret. Every read is recorded in the audit trail."
        return await self._call("webhook-endpoints.secret", input, path, idempotency_key)

    async def rotate_webhook_signing_secret(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookEndpointsRotateSecretResponse:
        "Rotate a webhook endpoint's signing secret. The previous secret keeps signing for 24 hours."
        return await self._call("webhook-endpoints.rotate_secret", input, path, idempotency_key)

    async def webhook_usage(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesUsageResponse:
        "Read today's webhook deliveries against the daily limit."
        return await self._call("webhook-deliveries.usage", input, path, idempotency_key)

    async def webhook_deliveries(self, input: WebhookDeliveriesListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesListResponse:
        "List webhook deliveries."
        return await self._call("webhook-deliveries.list", input, path, idempotency_key)

    async def get_webhook_delivery(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesGetResponse:
        "Read a webhook delivery with its request body and attempts."
        return await self._call("webhook-deliveries.get", input, path, idempotency_key)

    async def resend_webhook_delivery(self, input: WebhookDeliveriesResendInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> WebhookDeliveriesResendResponse:
        "Send a webhook delivery's event again, to the endpoint's current URL or the URL it was first sent to."
        return await self._call("webhook-deliveries.resend", input, path, idempotency_key)

    async def plan(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPlanResponse:
        "Read the plan, its billing period and renewal date, and the workspace's limits."
        return await self._call("billing.plan", input, path, idempotency_key)

    async def usage(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingUsageResponse:
        "Read credits and usage: allowance credits, pay-as-you-go credits, protected benefits and team seats."
        return await self._call("billing.usage", input, path, idempotency_key)

    async def credit_history(self, input: BillingCreditHistoryInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCreditHistoryResponse:
        "List credit history: credits added, used and removed."
        return await self._call("billing.credit_history", input, path, idempotency_key)

    async def daily_usage(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDailyUsageResponse:
        "Read credits used each day of the last 30 days."
        return await self._call("billing.daily_usage", input, path, idempotency_key)

    async def enterprise_plans(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingEnterprisePlansResponse:
        "List the workspace's Enterprise plans and what each one adds."
        return await self._call("billing.enterprise_plans", input, path, idempotency_key)

    async def preview_enterprise_plan_code(self, input: BillingCodesPreviewInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCodesPreviewResponse:
        "Preview what an Enterprise plan code adds, without redeeming it."
        return await self._call("billing.codes.preview", input, path, idempotency_key)

    async def upcoming_charge(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingUpcomingResponse:
        "Read the next charge: its amount, date and payment method."
        return await self._call("billing.upcoming", input, path, idempotency_key)

    async def invoices(self, input: BillingInvoicesInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingInvoicesResponse:
        "List invoices, newest first, each with its secure payment page link."
        return await self._call("billing.invoices", input, path, idempotency_key)

    async def payment_methods(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsResponse:
        "List saved payment methods: the default first, then the backup payment methods in order."
        return await self._call("billing.payment_methods", input, path, idempotency_key)

    async def billing_details(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDetailsResponse:
        "Read billing details: name, billing email, address and tax ID."
        return await self._call("billing.details", input, path, idempotency_key)

    async def update_billing_details(self, input: BillingDetailsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDetailsUpdateResponse:
        "Save billing details: name, billing email, address and tax ID."
        return await self._call("billing.details.update", input, path, idempotency_key)

    async def get_payment(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentsGetResponse:
        "Read a payment's progress."
        return await self._call("billing.payments.get", input, path, idempotency_key)

    async def quote_plan_change(self, input: BillingQuotesCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingQuotesCreateResponse:
        "Get a quote for a plan or billing period change: what it costs now and at renewal. Nothing changes."
        return await self._call("billing.quotes.create", input, path, idempotency_key)

    async def set_low_credit_alert(self, input: BillingLowCreditAlertUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingLowCreditAlertUpdateResponse:
        "Set the low-credit alert level, or clear it to be alerted by your usage pace."
        return await self._call("billing.low_credit_alert.update", input, path, idempotency_key)

    async def choose_what_stays_active(self, input: BillingOverLimitChooseInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingOverLimitChooseResponse:
        "Choose what stays active over your plan limits: keep one benefit or member active and pause another."
        return await self._call("billing.over_limit.choose", input, path, idempotency_key)

    async def set_auto_reload(self, input: BillingAutoReloadUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingAutoReloadUpdateResponse:
        "Set up, change or turn off auto-reload. When it's on, it charges the default payment method on its own."
        return await self._call("billing.auto_reload.update", input, path, idempotency_key)

    async def buy_credits(self, input: BillingCreditsBuyInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCreditsBuyResponse:
        "Buy credits with a saved payment method."
        return await self._call("billing.credits.buy", input, path, idempotency_key)

    async def retry_credit_purchase(self, input: BillingCreditsRetryInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCreditsRetryResponse:
        "Try a declined credit purchase again, with the default or another saved payment method."
        return await self._call("billing.credits.retry", input, path, idempotency_key)

    async def confirm_plan_change(self, input: BillingPlanChangeInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPlanChangeResponse:
        "Confirm a quote to move to a higher plan on the same or a longer billing period, Builder to Pro or Scale included, or yearly billing on the same plan, with a saved payment method."
        return await self._call("billing.plan.change", input, path, idempotency_key)

    async def undo_scheduled_downgrade(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingDowngradeUndoResponse:
        "Undo a scheduled downgrade, so the subscription renews on the current plan."
        return await self._call("billing.downgrade.undo", input, path, idempotency_key)

    async def resume_subscription(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingSubscriptionResumeResponse:
        "Resume a canceled subscription before it ends, so it renews again."
        return await self._call("billing.subscription.resume", input, path, idempotency_key)

    async def pay_overdue_invoice(self, input: BillingOverduePayInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingOverduePayResponse:
        "Pay an overdue invoice with a saved payment method."
        return await self._call("billing.overdue.pay", input, path, idempotency_key)

    async def set_default_payment_method(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsDefaultResponse:
        "Make a saved payment method the default. It then pays anything overdue."
        return await self._call("billing.payment_methods.default", input, path, idempotency_key)

    async def move_backup_payment_method(self, input: BillingPaymentMethodsMoveInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsMoveResponse:
        "Move a backup payment method up or down one place in the order."
        return await self._call("billing.payment_methods.move", input, path, idempotency_key)

    async def remove_payment_method(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingPaymentMethodsRemoveResponse:
        "Remove a saved payment method. The default can't be removed."
        return await self._call("billing.payment_methods.remove", input, path, idempotency_key)

    async def redeem_enterprise_plan_code(self, input: BillingCodesRedeemInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingCodesRedeemResponse:
        "Redeem an Enterprise plan code. It adds the plan to the workspace for good."
        return await self._call("billing.codes.redeem", input, path, idempotency_key)

    async def create_billing_approval_link(self, input: BillingApprovalLinksCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingApprovalLinksCreateResponse:
        "Make a link for the owner to add a payment method, or to add one and pay for an upgrade, when the workspace has none saved."
        return await self._call("billing.approval_links.create", input, path, idempotency_key)

    async def billing_approval_link(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> BillingApprovalLinksGetResponse:
        "Read whether the owner finished a billing approval link, declined it or let it expire."
        return await self._call("billing.approval_links.get", input, path, idempotency_key)

    async def update_account_name(self, input: AccountUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountUpdateResponse:
        "Change your name."
        return await self._call("account.update", input, path, idempotency_key)

    async def email_preferences(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountEmailPreferencesResponse:
        "Read which optional emails you get."
        return await self._call("account.email_preferences", input, path, idempotency_key)

    async def update_email_preferences(self, input: AccountEmailPreferencesUpdateInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> AccountEmailPreferencesUpdateResponse:
        "Choose which optional emails you get. Sign-in, security and billing emails always go."
        return await self._call("account.email_preferences_update", input, path, idempotency_key)

    async def notifications(self, input: NotificationsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsListResponse:
        "List your notifications, and how many are unread."
        return await self._call("notifications.list", input, path, idempotency_key)

    async def mark_notification(self, input: NotificationsUpdateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsUpdateResponse:
        "Mark a notification as read or unread."
        return await self._call("notifications.update", input, path, idempotency_key)

    async def mark_all_notifications_read(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsReadAllResponse:
        "Mark all your notifications as read."
        return await self._call("notifications.read_all", input, path, idempotency_key)

    async def run_notification_action(self, input: NotificationsRunActionInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> NotificationsRunActionResponse:
        "Run one of a notification's actions. It also needs the scope of the action it runs."
        return await self._call("notifications.run_action", input, path, idempotency_key)

    async def contact_support(self, input: SupportTicketsCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SupportTicketsCreateResponse:
        "Contact AbuseZero support about this workspace. Support replies to your account email."
        return await self._call("support-tickets.create", input, path, idempotency_key)

    async def support_tickets(self, input: SupportTicketsListInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> SupportTicketsListResponse:
        "List the support tickets you sent about this workspace."
        return await self._call("support-tickets.list", input, path, idempotency_key)

    async def send_feedback(self, input: FeedbackCreateInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> FeedbackCreateResponse:
        "Send product feedback to the AbuseZero team."
        return await self._call("feedback.create", input, path, idempotency_key)
class AsyncAbuseZeroPublic(AsyncCore):
    _public = True

    async def pricing(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicPricingResponse:
        "Read AbuseZero's plans and prices, what each plan includes and what every plan shares."
        return await self._call("public.pricing", input, path, idempotency_key)

    async def price_quote(self, input: PublicPricingQuoteInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicPricingQuoteResponse:
        "Get the exact price of a plan for a month or a year, or of a credit pack."
        return await self._call("public.pricing_quote", input, path, idempotency_key)

    async def docs(self, input: PublicDocsInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicDocsResponse:
        "List the developer docs pages, with each page's title, path and last update."
        return await self._call("public.docs", input, path, idempotency_key)

    async def search_docs(self, input: PublicDocsSearchInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicDocsSearchResponse:
        "Search the developer docs."
        return await self._call("public.docs_search", input, path, idempotency_key)

    async def public_docs_page(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicDocsPageResponse:
        "Read a developer docs page as Markdown."
        return await self._call("public.docs_page", input, path, idempotency_key)

    async def help_articles(self, input: PublicHelpInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicHelpResponse:
        "List the help center's articles, with each article's title, path and last update."
        return await self._call("public.help", input, path, idempotency_key)

    async def search_help(self, input: PublicHelpSearchInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicHelpSearchResponse:
        "Search the help center."
        return await self._call("public.help_search", input, path, idempotency_key)

    async def public_help_article(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicHelpArticleResponse:
        "Read a help center article as Markdown."
        return await self._call("public.help_article", input, path, idempotency_key)

    async def openapi(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicOpenapiResponse:
        "Read the OpenAPI document for the AbuseZero API."
        return await self._call("public.openapi", input, path, idempotency_key)

    async def actions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicActionsResponse:
        "List every API action with its MCP tool, CLI command and scope."
        return await self._call("public.actions", input, path, idempotency_key)

    async def error_codes(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicErrorsResponse:
        "List the API's error codes: what each means, whether to retry and what to do next."
        return await self._call("public.errors", input, path, idempotency_key)

    async def reason_codes(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicReasonsResponse:
        "List the reason codes evaluations return."
        return await self._call("public.reasons", input, path, idempotency_key)

    async def webhook_event_types(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicWebhookEventsResponse:
        "List the webhook event types, each with an example payload."
        return await self._call("public.webhook_events", input, path, idempotency_key)

    async def conditions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicConditionsResponse:
        "List the conditions the rules in custom policies can use."
        return await self._call("public.conditions", input, path, idempotency_key)

    async def glossary(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicGlossaryResponse:
        "Read the glossary and the developer FAQ."
        return await self._call("public.glossary", input, path, idempotency_key)

    async def legal_documents(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicLegalResponse:
        "List AbuseZero's legal documents, with each one's version and effective date."
        return await self._call("public.legal", input, path, idempotency_key)

    async def legal_document(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicLegalDocumentResponse:
        "Read a legal document as Markdown."
        return await self._call("public.legal_document", input, path, idempotency_key)

    async def changelog(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicChangelogResponse:
        "Read the product changelog."
        return await self._call("public.changelog", input, path, idempotency_key)

    async def blog_posts(self, input: PublicBlogInput | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicBlogResponse:
        "List blog posts."
        return await self._call("public.blog", input, path, idempotency_key)

    async def blog_post(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicBlogPostResponse:
        "Read a blog post as Markdown."
        return await self._call("public.blog_post", input, path, idempotency_key)

    async def versions(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicVersionsResponse:
        "Read the latest npm package version and the browser script address."
        return await self._call("public.versions", input, path, idempotency_key)

    async def service_status(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicStatusResponse:
        "Read whether AbuseZero is operational or degraded."
        return await self._call("public.status", input, path, idempotency_key)

    async def contacts(self, input: dict[str, Any] | None = None, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicContactsResponse:
        "Read how to reach AbuseZero's support, sales and security."
        return await self._call("public.contacts", input, path, idempotency_key)

    async def contact_sales(self, input: PublicContactSalesInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicContactSalesResponse:
        "Send a message to AbuseZero's sales team about an Enterprise plan."
        return await self._call("public.contact_sales", input, path, idempotency_key)

    async def contact_support(self, input: PublicContactSupportInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicContactSupportResponse:
        "Send a request to AbuseZero support without an account."
        return await self._call("public.contact_support", input, path, idempotency_key)

    async def start_onboarding(self, input: PublicOnboardingStartInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicOnboardingStartResponse:
        "Start agent onboarding for a new workspace: returns the approval link for the person, and a secret only this agent keeps."
        return await self._call("public.onboarding_start", input, path, idempotency_key)

    async def onboarding_status(self, input: PublicOnboardingStatusInput, *, path: dict[str, str | int] | None = None, idempotency_key: str | None = None) -> PublicOnboardingStatusResponse:
        "Read whether the person finished onboarding, optionally waiting up to 25 seconds, and how to collect the sign-in."
        return await self._call("public.onboarding_status", input, path, idempotency_key)
