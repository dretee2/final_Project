

from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import SchemathesisRunner
from authentication import get_access_token
import os

token = get_access_token()
os.makedirs("reports", exist_ok=True)

recommendation_schema= ReadSchemaProperties.get_recommendation_schema()
runner = SchemathesisRunner(token)

for name, url in recommendation_schema.items():
    runner.run_test(name, url)