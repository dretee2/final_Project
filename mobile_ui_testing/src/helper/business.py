import requests
import json
import random
import datetime
from mobile_ui_testing.settings import SLACK_TOKEN  # Make sure SLACK_TOKEN is defined in settings.py


def notify_slack():
    """
    Sends a formatted Slack message with test report summary.
    """
    web_hook_url = f'https://hooks.slack.com/services/{SLACK_TOKEN}'

    # Load the JSON report file (make sure it exists at this path after test run)
    with open("./report/json/report.json") as json_file:
        json_object = json.load(json_file)

    passed = int(status_count(json_object, 'passed'))
    failed = int(status_count(json_object, 'failed'))

    color = '#36a64f' if failed == 0 else '#a30001'
    text = "#✅ Build Passed" if failed == 0 else "#❌ Build Failed"

    slack_msg = {
        "attachments": [
            {
                "fallback": "Automation Test Summary",
                "color": color,
                "pretext": f"@here {quote()}",
                "author_name": "Mobile Automation Results",
                "author_icon": "https://avatars3.githubusercontent.com/u/2948696?s=460&v=4",
                "title": "📱 Your App - Android",
                "title_link": "https://your-test-results-url.com",  # Optional link to test results
                "text": text,
                "fields": [
                    {
                        "title": "AE",
                        "value": f":white_check_mark: {passed} Passed\n:exclamation: {failed} Failed",
                        "short": False
                    },
                    {
                        "title": "SA",
                        "value": f":white_check_mark: {passed} Passed\n:exclamation: {failed} Failed",
                        "short": False
                    }
                ],
                "footer": "Appium Test Framework",
                "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                "ts": int(datetime.datetime.now().timestamp())
            }
        ]
    }

    # Send message to Slack
    response = requests.post(web_hook_url, data=json.dumps(slack_msg))

    if response.status_code != 200:
        raise Exception(f"Slack notification failed: {response.status_code} - {response.text}")


def status_count(json_object, status):
    """
    Retrieves the count of passed or failed tests from the JSON report.
    Handles multiple report formats.
    """
    try:
        return json_object['report']['summary'][f'{status}']
    except KeyError:
        try:
            return json_object['data'][0]['attributes']['summary'][f'{status}']
        except KeyError:
            return 0
