import subprocess
import os


class SchemathesisRunner:
    """
    A class to run Schemathesis contract tests with report generation.
    """

    def __init__(self, token: str):
        """
        Initialize the Schemathesis runner.

        :param token: API Authorization token
        """
        if not token:
            raise ValueError("❌ API token is not provided. Please set it.")
        self.token = token

    def run_test(self, url: str, name: str = "schemathesis_test"):
        """
        Run a Schemathesis test on the given OpenAPI schema URL.

        :param url: OpenAPI schema URL
        :param name: A unique name for report files (defaults to 'schemathesis_test')
        """

        report_name = name.replace("/", "_")
        html_report = f"{report_name}_report.html"
        junit_report = f"{report_name}_report.xml"

        cmd = [
            "schemathesis", "run", url,
            "-H", f"Authorization: Bearer {self.token}",
            "--checks", "all",
            "--workers", "4",
            "--report", html_report,
            "--junit-xml", junit_report,
            "--show-errors-tracebacks"
        ]

        print(f"\n🚀 Running Schemathesis test for: {name}")
        print(f"🔗 OpenAPI URL: {url}")
        print(f"📄 Reports will be saved as: {html_report} and {junit_report}")

        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Test completed successfully for {name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Test run failed for {name}")
            print(f"🔍 Error details: {e}")
        except Exception as ex:
            print(f"⚠️ Unexpected error occurred for {name}: {ex}")
