import os
import subprocess
import sys

def main():
    script = "start.sh"

    if not os.path.exists(script):
        print(f"Error: {script} not found.")
        sys.exit(1)

    os.chmod(script, 0o755)

    try:
        subprocess.run(["./" + script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script}: {e}")