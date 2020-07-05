import os

CLIENT_ID = "" # Application (client) ID of app registration

CLIENT_SECRET = "" # Placeholder - for use ONLY during testing.
AUTHORITY = "https://login.microsoftonline.com/tenant_id"  # For multi-tenant app
REDIRECT_PATH = "/getAToken"
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
