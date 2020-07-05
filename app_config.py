import os

CLIENT_ID = "e4db746d-7203-450c-9c10-12ea74faa2cc" # Application (client) ID of app registration

CLIENT_SECRET = "rOvpF.S93U-54QAhm-7l29I.To~Xsb~gsY" # Placeholder - for use ONLY during testing.
AUTHORITY = "https://login.microsoftonline.com/25e42d7e-cebb-4dd3-9a15-6e3060e48ee2"  # For multi-tenant app
REDIRECT_PATH = "/getAToken"
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
