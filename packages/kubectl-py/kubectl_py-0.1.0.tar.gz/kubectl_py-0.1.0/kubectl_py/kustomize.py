from __future__ import annotations

import subprocess
import sys


def main():
    envs = sys.argv[1:]
    for env in envs:
        print(f">>> Building {env}")
        subprocess.run(
            ['kubectl', 'kustomize', env],
            check=True,
        )
