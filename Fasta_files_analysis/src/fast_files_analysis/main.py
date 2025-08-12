"""This module is for measuring the execution time of the program from the first code to the last code."""

import time

from main_ranners import mrn

if __name__ == "__main__":
    # Processing time file.
    start_time = time.time()
    mrn()
    elapsed = time.time() - start_time
    print(f"\n>>>>>> ⚪ 🔴 🟢 🟡 Processing time: {elapsed:.3f}s 🟡 🟢 🔴 ⚪ <<<<<<")
