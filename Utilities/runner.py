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
            "--hypothesis-max-examples", "50",
            "--junit-xml", f"reports/{name}-report.xml",
            "--report", f"reports/{name}-report.html",
            "--report", f"reports/{name}-report.json",
            url
        ]
        subprocess.run(cmd, check=True)
