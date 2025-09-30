"""
Script for testing that there are no errors in examples
Run each example, only print if an error is raised
"""

import os
from pathlib import Path

hide_output = True

folderpath = Path("../examples")

examples = sorted(folderpath.glob("*.abyz"))
print("Examples:", [e.stem for e in examples])

for example in examples:
    print(f"Running example: {example}")
    run_command = f"abyz -s {example} -x"
    if hide_output: run_command += " > testfiles"
    os.system(run_command)
    os.remove(folderpath / Path(str(example.stem)+".py"))
    if hide_output: os.remove("testfiles")
