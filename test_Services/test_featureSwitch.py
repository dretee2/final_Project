from Utilities.runner import run_schemathesis_test
from Utilities.readSchemaUrl import ReadSchemaProperties
from authentication import get_access_token
import os


token = get_access_token()
os.makedirs("reports", exist_ok=True)

feature_switch_schema= ReadSchemaProperties.get_feature_switch_schema()


for name, url in feature_switch_schema.items():
    run_schemathesis_test(name, url, token)