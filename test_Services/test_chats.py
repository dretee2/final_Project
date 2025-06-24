
from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import SchemathesisRunner
from authentication import get_access_token
import os

token = get_access_token()
os.makedirs("reports", exist_ok=True)

Chats_schema= ReadSchemaProperties.get_chats_schema()

for name, url in Chats_schema.items():
    SchemathesisRunner.run_test(name, url, token)