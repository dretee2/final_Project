import subprocess
import os
from datetime import datetime

class SchemathesisRunner:
    def __init__(self, token: str, report_dir: str = "reports"):
        if not token:
            raise ValueError("❌ token environment variable not set!")
        self.token = token
        self.report_dir = report_dir

    def run_test(self, name: str, url: str):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        safe_name = name.replace("/", "_")

        html_report = os.path.join(self.report_dir, f"{safe_name}_{timestamp}_report.html")

        cmd = [
            "schemathesis", "run", url,
            "-H", f"Authorization: Bearer {self.token}",
            "--checks", "all",
            "--workers", "4",
            "--report", html_report,
            "--show-errors-tracebacks"
        ]

        print(f"\n🚀 Running Schemathesis test for: {name}")

        try:
            subprocess.run(cmd, check=False)
            print(f"✅ Test completed successfully for {name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Test run failed for {name} with exit code {e.returncode}")
            print(f"Check report files for details.")
