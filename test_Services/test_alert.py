from Utilities.runner import SchemathesisRunner
from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.user_auth import get_access_token_for_user
import os


token = get_access_token_for_user()
os.makedirs("reports", exist_ok=True)

alerts_schema= ReadSchemaProperties.get_alerts_schema()

runner = SchemathesisRunner(token)

for name, url in alerts_schema.items():
    runner.run_test(name, url)