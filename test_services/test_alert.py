from Utilities.runner import SchemathesisRunner
from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.user_auth import get_access_token_for_user


token = get_access_token_for_user()

alerts_schema= ReadSchemaProperties.get_alerts_schema()

runner = SchemathesisRunner(token)

for name, url in alerts_schema.items():
    runner.run_test(name, url)