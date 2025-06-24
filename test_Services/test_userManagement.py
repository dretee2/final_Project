
from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import SchemathesisRunner
from Utilities.user_auth import get_access_token_for_user
import os

token = get_access_token_for_user()
os.makedirs("reports", exist_ok=True)

user_management_schema= ReadSchemaProperties.get_user_management_schema()
runner = SchemathesisRunner(token)

for name, url in user_management_schema.items():
   runner.run_test(name, url)