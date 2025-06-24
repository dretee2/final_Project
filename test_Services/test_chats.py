
from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import SchemathesisRunner
from Utilities.user_auth import get_access_token_for_user
import os

token = get_access_token_for_user()
os.makedirs("reports", exist_ok=True)

Chats_schema= ReadSchemaProperties.get_chats_schema()

runner = SchemathesisRunner(token)

for name, url in Chats_schema.items():
    runner.run_test(name, url)