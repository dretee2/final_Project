from Utilities.runner import SchemathesisRunner
from Utilities.readSchemaUrl import ReadSchemaProperties


alerts_schema= ReadSchemaProperties.get_alerts_schema()

for  name, url in alerts_schema.items():
    print(name, url)