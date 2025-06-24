import subprocess

class SchemathesisRunner:
    def __init__(self, token):
        self.token = token

    def run_test(self, name: str, url: str):
        print(f"Running Schemathesis for schema: {name}")
        cmd = [
            "schemathesis", "run",
            "-H", f"Authorization: Bearer {self.token}",
            "--checks", "all",
            "--workers", "4",
            url
        ]
        subprocess.run(cmd, check=True)
