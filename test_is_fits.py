import sys
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())

from astropy.io.fits.connect import is_fits
from astropy.table import Table
from astropy.io.fits import HDUList, TableHDU, BinTableHDU, GroupsHDU

# Test cases
test_cases = [
    ("bububu.ecsv", None),
    ("test.fits", None),
]

for case in test_cases:
    print(f"\nTesting case: {case}")
    result = is_fits("read", *case)
    print(f"Result: {result}")

# Special case for HDUList
print("\nTesting case: (None, HDUList())")
try:
    result = is_fits("read", None, HDUList())
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {str(e)}")

print("\nScript completed.")
