
from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import SchemathesisRunner
from authentication import get_access_token
import os

token = get_access_token()
os.makedirs("reports", exist_ok=True)

user_management_schema= ReadSchemaProperties.get_user_management_schema()

for name, url in user_management_schema.items():
    SchemathesisRunner.run_test(name, url, token)