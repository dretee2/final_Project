import subprocess
import os
from datetime import datetime
from Utilities.logger_config import setup_logger

class SchemathesisRunner:
    def __init__(self, token: str):
        if not token:
            raise ValueError("❌ Token environment variable not set!")
        self.token = token
        self.logger = setup_logger("SchemathesisRunner")

    def run_test(self, name:str , url: str):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        service_name = name

        # Use fixed directory name directly (NO report_dir passed or created)
        report_dir = "schemathesis_reports"
        junit_report = os.path.join(report_dir, f"{service_name}_{timestamp}_report.xml")

        cmd = [
            "schemathesis", "run", url,
            "-H", f"Authorization: Bearer {self.token}",
            "--checks", "all",
            "--workers", "4",
            "--report", "junit"
        ]

        self.logger.info(f"🚀 Running Schemathesis test for: {name}")

        try:
            subprocess.run(cmd, check=True)

            if os.path.exists("schemathesis.junit.xml"):
                os.rename("schemathesis.junit.xml", junit_report)
                self.logger.info(f"✅ Report saved as {junit_report}")
            else:
                self.logger.error("❌ Report file not found after run!")

        except subprocess.CalledProcessError as e:
            self.logger.error(f"❌ Test run failed for {name} with exit code {e.returncode}")
            self.logger.error("Check logs and report for details.")
