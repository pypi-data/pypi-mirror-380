<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control
*ApplicationsApi* | [**create_application**](docs/ApplicationsApi.md#create_application) | **POST** /api/applications | [EARLY ACCESS] CreateApplication: Create Application
*ApplicationsApi* | [**delete_application**](docs/ApplicationsApi.md#delete_application) | **DELETE** /api/applications/{id} | [EARLY ACCESS] DeleteApplication: Delete Application
*ApplicationsApi* | [**get_application**](docs/ApplicationsApi.md#get_application) | **GET** /api/applications/{id} | GetApplication: Get Application
*ApplicationsApi* | [**list_applications**](docs/ApplicationsApi.md#list_applications) | **GET** /api/applications | ListApplications: List Applications
*ApplicationsApi* | [**rotate_application_secrets**](docs/ApplicationsApi.md#rotate_application_secrets) | **POST** /api/applications/{id}/lifecycle/$newsecret | [EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets
*AuthenticationApi* | [**get_authentication_information**](docs/AuthenticationApi.md#get_authentication_information) | **GET** /api/authentication/information | GetAuthenticationInformation: Gets AuthenticationInformation
*AuthenticationApi* | [**get_password_policy**](docs/AuthenticationApi.md#get_password_policy) | **GET** /api/authentication/password-policy/{userType} | GetPasswordPolicy: Gets password policy for a user type
*AuthenticationApi* | [**get_support_access_history**](docs/AuthenticationApi.md#get_support_access_history) | **GET** /api/authentication/support | GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination
*AuthenticationApi* | [**get_support_roles**](docs/AuthenticationApi.md#get_support_roles) | **GET** /api/authentication/support-roles | GetSupportRoles: Get mapping of support roles, the internal representation to a human friendly representation
*AuthenticationApi* | [**grant_support_access**](docs/AuthenticationApi.md#grant_support_access) | **POST** /api/authentication/support | GrantSupportAccess: Grants FINBOURNE support access to your account
*AuthenticationApi* | [**invalidate_support_access**](docs/AuthenticationApi.md#invalidate_support_access) | **DELETE** /api/authentication/support | InvalidateSupportAccess: Revoke any FINBOURNE support access to your account
*AuthenticationApi* | [**update_password_policy**](docs/AuthenticationApi.md#update_password_policy) | **PUT** /api/authentication/password-policy/{userType} | UpdatePasswordPolicy: Updates password policy for a user type
*ExternalTokenIssuersApi* | [**create_external_token_issuer**](docs/ExternalTokenIssuersApi.md#create_external_token_issuer) | **POST** /api/externaltokenissuers | [EARLY ACCESS] CreateExternalTokenIssuer: Create an External Token Issuer
*ExternalTokenIssuersApi* | [**delete_external_token_issuer**](docs/ExternalTokenIssuersApi.md#delete_external_token_issuer) | **DELETE** /api/externaltokenissuers/{code} | [EARLY ACCESS] DeleteExternalTokenIssuer: Deletes an External Token Issuer by code
*ExternalTokenIssuersApi* | [**get_external_token_issuer**](docs/ExternalTokenIssuersApi.md#get_external_token_issuer) | **GET** /api/externaltokenissuers/{code} | [EARLY ACCESS] GetExternalTokenIssuer: Gets an External Token Issuer with code
*ExternalTokenIssuersApi* | [**list_external_token_issuers**](docs/ExternalTokenIssuersApi.md#list_external_token_issuers) | **GET** /api/externaltokenissuers | [EARLY ACCESS] ListExternalTokenIssuers: Lists all External Token Issuers for a domain
*ExternalTokenIssuersApi* | [**update_external_token_issuer**](docs/ExternalTokenIssuersApi.md#update_external_token_issuer) | **PUT** /api/externaltokenissuers/{code} | [EARLY ACCESS] UpdateExternalTokenIssuer: Updates an existing External Token Issuer
*IdentityLogsApi* | [**list_logs**](docs/IdentityLogsApi.md#list_logs) | **GET** /api/logs | [BETA] ListLogs: Lists system logs for a domain
*IdentityLogsApi* | [**list_user_logs**](docs/IdentityLogsApi.md#list_user_logs) | **GET** /api/logs/me | ListUserLogs: Lists user logs
*IdentityProviderApi* | [**add_scim**](docs/IdentityProviderApi.md#add_scim) | **PUT** /api/identityprovider/scim | AddScim: Add SCIM
*IdentityProviderApi* | [**remove_scim**](docs/IdentityProviderApi.md#remove_scim) | **DELETE** /api/identityprovider/scim | RemoveScim: Remove SCIM
*MeApi* | [**get_user_info**](docs/MeApi.md#get_user_info) | **GET** /api/me | GetUserInfo: Get User Info
*MeApi* | [**set_password**](docs/MeApi.md#set_password) | **PUT** /api/me/password | SetPassword: Set password of current user
*NetworkZonesApi* | [**create_network_zone**](docs/NetworkZonesApi.md#create_network_zone) | **POST** /api/networkzones | [EARLY ACCESS] CreateNetworkZone: Creates a network zone
*NetworkZonesApi* | [**delete_network_zone**](docs/NetworkZonesApi.md#delete_network_zone) | **DELETE** /api/networkzones/{code} | [EARLY ACCESS] DeleteNetworkZone: Deletes a network zone
*NetworkZonesApi* | [**get_network_zone**](docs/NetworkZonesApi.md#get_network_zone) | **GET** /api/networkzones/{code} | [EARLY ACCESS] GetNetworkZone: Retrieve a Network Zone
*NetworkZonesApi* | [**list_network_zones**](docs/NetworkZonesApi.md#list_network_zones) | **GET** /api/networkzones | [EARLY ACCESS] ListNetworkZones: Lists all network zones for a domain
*NetworkZonesApi* | [**update_network_zone**](docs/NetworkZonesApi.md#update_network_zone) | **PUT** /api/networkzones/{code} | [EARLY ACCESS] UpdateNetworkZone: Updates an existing network zone
*PersonalAuthenticationTokensApi* | [**create_api_key**](docs/PersonalAuthenticationTokensApi.md#create_api_key) | **POST** /api/keys | CreateApiKey: Create a Personal Access Token
*PersonalAuthenticationTokensApi* | [**delete_api_key**](docs/PersonalAuthenticationTokensApi.md#delete_api_key) | **DELETE** /api/keys/{id} | DeleteApiKey: Invalidate a Personal Access Token
*PersonalAuthenticationTokensApi* | [**list_own_api_keys**](docs/PersonalAuthenticationTokensApi.md#list_own_api_keys) | **GET** /api/keys | ListOwnApiKeys: Gets the meta data for all of the user's existing Personal Access Tokens.
*RolesApi* | [**add_user_to_role**](docs/RolesApi.md#add_user_to_role) | **PUT** /api/roles/{id}/users/{userId} | AddUserToRole: Add User to Role
*RolesApi* | [**create_role**](docs/RolesApi.md#create_role) | **POST** /api/roles | CreateRole: Create Role
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /api/roles/{id} | DeleteRole: Delete Role
*RolesApi* | [**get_role**](docs/RolesApi.md#get_role) | **GET** /api/roles/{id} | GetRole: Get Role
*RolesApi* | [**list_roles**](docs/RolesApi.md#list_roles) | **GET** /api/roles | ListRoles: List Roles
*RolesApi* | [**list_users_in_role**](docs/RolesApi.md#list_users_in_role) | **GET** /api/roles/{id}/users | ListUsersInRole: Get the users in the specified role.
*RolesApi* | [**remove_user_from_role**](docs/RolesApi.md#remove_user_from_role) | **DELETE** /api/roles/{id}/users/{userId} | RemoveUserFromRole: Remove User from Role
*RolesApi* | [**update_role**](docs/RolesApi.md#update_role) | **PUT** /api/roles/{id} | UpdateRole: Update Role
*TokensApi* | [**invalidate_token**](docs/TokensApi.md#invalidate_token) | **DELETE** /api/tokens | InvalidateToken: Invalidate current JWT token (sign out)
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /api/users | CreateUser: Create User
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /api/users/{id} | DeleteUser: Delete User
*UsersApi* | [**expire_password**](docs/UsersApi.md#expire_password) | **POST** /api/users/{id}/lifecycle/$expirepassword | ExpirePassword: Reset the user's password to a temporary one
*UsersApi* | [**find_users_by_id**](docs/UsersApi.md#find_users_by_id) | **GET** /api/directory | FindUsersById: Find users by id endpoint
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /api/users/{id} | GetUser: Get User
*UsersApi* | [**get_user_schema**](docs/UsersApi.md#get_user_schema) | **GET** /api/users/schema | [EARLY ACCESS] GetUserSchema: Get User Schema
*UsersApi* | [**list_runnable_users**](docs/UsersApi.md#list_runnable_users) | **GET** /api/users/$runnable | [EARLY ACCESS] ListRunnableUsers: List Runable Users
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /api/users | ListUsers: List Users
*UsersApi* | [**reset_factors**](docs/UsersApi.md#reset_factors) | **POST** /api/users/{id}/lifecycle/$resetfactors | ResetFactors: Reset MFA factors
*UsersApi* | [**reset_password**](docs/UsersApi.md#reset_password) | **POST** /api/users/{id}/lifecycle/$resetpassword | ResetPassword: Reset Password
*UsersApi* | [**send_activation_email**](docs/UsersApi.md#send_activation_email) | **POST** /api/users/{id}/lifecycle/$activate | SendActivationEmail: Sends an activation email to the User
*UsersApi* | [**unlock_user**](docs/UsersApi.md#unlock_user) | **POST** /api/users/{id}/lifecycle/$unlock | UnlockUser: Unlock User
*UsersApi* | [**unsuspend_user**](docs/UsersApi.md#unsuspend_user) | **POST** /api/users/{id}/lifecycle/$unsuspend | [EXPERIMENTAL] UnsuspendUser: Unsuspend user
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /api/users/{id} | UpdateUser: Update User
*UsersApi* | [**update_user_schema**](docs/UsersApi.md#update_user_schema) | **PUT** /api/users/schema | [EARLY ACCESS] UpdateUserSchema: Update User Schema


<a id="documentation-for-models"></a>
## Documentation for Models

 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [ActionId](docs/ActionId.md)
 - [AddScimResponse](docs/AddScimResponse.md)
 - [ApiKey](docs/ApiKey.md)
 - [AuthenticationInformation](docs/AuthenticationInformation.md)
 - [ClaimMappings](docs/ClaimMappings.md)
 - [CreateApiKey](docs/CreateApiKey.md)
 - [CreateApplicationRequest](docs/CreateApplicationRequest.md)
 - [CreateExternalTokenIssuerRequest](docs/CreateExternalTokenIssuerRequest.md)
 - [CreateNetworkZoneRequest](docs/CreateNetworkZoneRequest.md)
 - [CreateRoleRequest](docs/CreateRoleRequest.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreatedApiKey](docs/CreatedApiKey.md)
 - [CurrentUserResponse](docs/CurrentUserResponse.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [ExternalTokenIssuerResponse](docs/ExternalTokenIssuerResponse.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [IdentifierPartSchema](docs/IdentifierPartSchema.md)
 - [IpAddressDefinition](docs/IpAddressDefinition.md)
 - [Link](docs/Link.md)
 - [ListUsersResponse](docs/ListUsersResponse.md)
 - [LogActor](docs/LogActor.md)
 - [LogAuthenticationContext](docs/LogAuthenticationContext.md)
 - [LogClientInfo](docs/LogClientInfo.md)
 - [LogDebugContext](docs/LogDebugContext.md)
 - [LogGeographicalContext](docs/LogGeographicalContext.md)
 - [LogGeolocation](docs/LogGeolocation.md)
 - [LogIpChainEntry](docs/LogIpChainEntry.md)
 - [LogIssuer](docs/LogIssuer.md)
 - [LogOutcome](docs/LogOutcome.md)
 - [LogRequest](docs/LogRequest.md)
 - [LogSecurityContext](docs/LogSecurityContext.md)
 - [LogSeverity](docs/LogSeverity.md)
 - [LogTarget](docs/LogTarget.md)
 - [LogTransaction](docs/LogTransaction.md)
 - [LogUserAgent](docs/LogUserAgent.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [NetworkZoneDefinitionResponse](docs/NetworkZoneDefinitionResponse.md)
 - [NetworkZonesApplyRules](docs/NetworkZonesApplyRules.md)
 - [OAuthApplication](docs/OAuthApplication.md)
 - [PasswordPolicyResponse](docs/PasswordPolicyResponse.md)
 - [PasswordPolicyResponseAge](docs/PasswordPolicyResponseAge.md)
 - [PasswordPolicyResponseComplexity](docs/PasswordPolicyResponseComplexity.md)
 - [PasswordPolicyResponseConditions](docs/PasswordPolicyResponseConditions.md)
 - [PasswordPolicyResponseLockout](docs/PasswordPolicyResponseLockout.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [ResourceListOfSystemLog](docs/ResourceListOfSystemLog.md)
 - [RoleId](docs/RoleId.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [SetPassword](docs/SetPassword.md)
 - [SetPasswordResponse](docs/SetPasswordResponse.md)
 - [SupportAccessExpiry](docs/SupportAccessExpiry.md)
 - [SupportAccessExpiryWithRole](docs/SupportAccessExpiryWithRole.md)
 - [SupportAccessRequest](docs/SupportAccessRequest.md)
 - [SupportAccessResponse](docs/SupportAccessResponse.md)
 - [SupportRole](docs/SupportRole.md)
 - [SupportRolesResponse](docs/SupportRolesResponse.md)
 - [SystemLog](docs/SystemLog.md)
 - [TemporaryPassword](docs/TemporaryPassword.md)
 - [UpdateExternalTokenIssuerRequest](docs/UpdateExternalTokenIssuerRequest.md)
 - [UpdateNetworkZoneRequest](docs/UpdateNetworkZoneRequest.md)
 - [UpdatePasswordPolicyRequest](docs/UpdatePasswordPolicyRequest.md)
 - [UpdatePasswordPolicyRequestAge](docs/UpdatePasswordPolicyRequestAge.md)
 - [UpdatePasswordPolicyRequestComplexity](docs/UpdatePasswordPolicyRequestComplexity.md)
 - [UpdatePasswordPolicyRequestConditions](docs/UpdatePasswordPolicyRequestConditions.md)
 - [UpdatePasswordPolicyRequestLockout](docs/UpdatePasswordPolicyRequestLockout.md)
 - [UpdateRoleRequest](docs/UpdateRoleRequest.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateUserSchemaRequest](docs/UpdateUserSchemaRequest.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserSchemaProperty](docs/UserSchemaProperty.md)
 - [UserSchemaResponse](docs/UserSchemaResponse.md)
 - [UserSummary](docs/UserSummary.md)

