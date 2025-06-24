from gevent.libev.corecffi import recommended_backends

from Utilities.readSchemaUrl import ReadSchemaProperties
from Utilities.runner import run_schemathesis_test
from authentication import get_access_token
import os

token = get_access_token()
os.makedirs("reports", exist_ok=True)

recommendation_schema= ReadSchemaProperties.get_recommendation_schema()

for name, url in recommendation_schema.items():
    run_schemathesis_test(name, url, token)