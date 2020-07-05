import os

CLIENT_ID = "d2d8b8d3-9538-4d3e-9acf-50e29a894a9e" # Application (client) ID of app registration

CLIENT_SECRET = "tZ.6lulkF5tGY0iQt8tdb_A.S7_eh3T~4y" # Placeholder - for use ONLY during testing.
AUTHORITY = "https://login.microsoftonline.com/2aced404-ed82-4fbd-b62b-692af0dc9836"  # For multi-tenant app
REDIRECT_PATH = "/getAToken"
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
