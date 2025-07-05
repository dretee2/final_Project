

from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import SchemathesisRunner
from Utilities.user_auth import get_access_token_for_user
import os

def test_recommendation():
    token = get_access_token_for_user()
    os.makedirs("reports", exist_ok=True)

    recommendation_schema= ReadSchemaProperties.get_recommendation_schema()
    runner = SchemathesisRunner(token)

    for name, url in recommendation_schema.items():
        runner.run_test(name, url)