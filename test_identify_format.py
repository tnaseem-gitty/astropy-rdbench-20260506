import sys
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())

# Mock the necessary parts of astropy
class Table:
    pass

class HDUList:
    pass

class TableHDU:
    pass

class BinTableHDU:
    pass

class GroupsHDU:
    pass

def is_fits(origin, filepath, fileobj, *args, **kwargs):
    if filepath is not None and isinstance(filepath, str):
        if filepath.lower().endswith((".fits", ".fits.gz", ".fit", ".fit.gz", ".fts", ".fts.gz")):
            return True
    # Check if args is empty before trying to access its first element
    if args and isinstance(args[0], (HDUList, TableHDU, BinTableHDU, GroupsHDU)):
        return True
    return False

def identify_format(origin, data_class, path, fileobj, args, kwargs):
    return is_fits(origin, path, fileobj, *args, **kwargs)

# Test the function
test_cases = [
    ("write", Table, "bububu.ecsv", None, [], {}),
    ("write", Table, "test.fits", None, [], {}),
    ("write", Table, None, None, [HDUList()], {}),
]

for case in test_cases:
    print(f"\nTesting case: {case}")
    result = identify_format(*case)
    print(f"Result: {result}")

print("\nScript completed.")
