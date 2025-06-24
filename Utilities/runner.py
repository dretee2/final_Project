import subprocess

def run_schemathesis_test(name, url, token):
    print(f"Running Schemathesis for schema: {name}")
    cmd = [
        "schemathesis", "run",
        "-H", f"Authorization: Bearer {token}",
        "--checks", "all",
        "--workers", "4",
        url,
    ]
    subprocess.run(cmd, check=True)