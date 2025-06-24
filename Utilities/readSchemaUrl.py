import configparser
import json

configs = configparser.RawConfigParser()
configs.read(r"C:\Users\BAB AL SAFA\PycharmProjects\Schemathesis_Project\config.ini")


class ReadSchemaProperties:

    @staticmethod
    def get_alerts_schema():
        try:
            schema_string = configs.get("common Schema data", "Alerts_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'Alerts_Schema_Details' option not found.")
            return {}

    @staticmethod
    def get_user_management_schema():
        try:
            schema_string = configs.get("common Schema data", "User_Management_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'User_Management_Schema_Details' option not found.")

    @staticmethod
    def get_recommendation_schema():
        try:
            schema_string = configs.get("common Schema data", "Recommendation_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'Recommendation_Schema_Details' option not found.")

    @staticmethod
    def get_chats_schema():
        try:
            schema_string = configs.get("common Schema data", "Chats_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'Chats_Schema_Details' option not found.")

    @staticmethod
    def get_bytebox_schema():
        try:
            schema_string = configs.get("common Schema data", "bytebox_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'bytebox_Schema_Details' option not found.")

    @staticmethod
    def get_main_schema():
        try:
            schema_string = configs.get("common Schema data", "main_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'main_Schema_Details' option not found.")

    @staticmethod
    def get_feature_switch_schema():
        try:
            schema_string = configs.get("common Schema data", "feature_switch_Schema_Details")
            return json.loads(schema_string)
        except configparser.NoSectionError:
            print("Error: 'common Schema data' section not found in config.ini")
            return {}
        except configparser.NoOptionError:
            print("Error: 'feature_switch_Schema_Details' option not found.")