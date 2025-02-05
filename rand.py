"""
Module for sorting algorithms with debugging improvements.
"""

import subprocess

def random_array(arr):
    """Generates a shuffled array using system command."""
    for i, _ in enumerate(arr):  # Using enumerate for cleaner iteration
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
