from Utilities.runner import SchemathesisRunner
from Utilities.readSchemaUrl import ReadSchemaProperties
from authentication import get_access_token
import os


token = get_access_token()
os.makedirs("reports", exist_ok=True)

main_schema= ReadSchemaProperties.get_main_schema()

for name, url in main_schema.items():
    SchemathesisRunner.run_test(name, url, token)