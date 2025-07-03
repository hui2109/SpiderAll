import subprocess
import sys

cmd = [
    sys.executable, "-m", "pip",
    "install",
    "pyexecjs2",
    "requests",
    "jupyterlab",
    "notebook",
    "pycryptodome",
]

subprocess.run(cmd, check=True)
