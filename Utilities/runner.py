import subprocess
import os
from datetime import datetime


class SchemathesisRunner:
    def __init__(self, token: str, report_dir: str = "reports"):
        if not token:
            raise ValueError("❌ Token environment variable not set!")
        self.token = token
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)

    def run_test(self, name: str, url: str):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        safe_name = name.replace("/", "_")

        # File path where we will move the generated JUnit report
        junit_report = os.path.join(self.report_dir, f"{safe_name}_{timestamp}_report.xml")

        cmd = [
            "schemathesis", "run", url,
            "-H", f"Authorization: Bearer {self.token}",
            "--checks", "all",
            "--workers", "4",
            "--report", "junit"
        ]

        print(f"\n🚀 Running Schemathesis test for: {name}")

        try:
            subprocess.run(cmd, check=True)

            # Rename default output file to the desired report path
            if os.path.exists("schemathesis.junit.xml"):
                os.rename("schemathesis.junit.xml", junit_report)
                print(f"✅ Report saved as {junit_report}")
            else:
                print("❌ Report file not found after run!")

        except subprocess.CalledProcessError as e:
            print(f"❌ Test run failed for {name} with exit code {e.returncode}")
            print(f"Check logs and report for details.")
