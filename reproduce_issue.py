from astropy.io.registry import identify_format
from astropy.table import Table

try:
    result = identify_format("write", Table, "bububu.ecsv", None, [], {})
    print("Unexpected success. Result:", result)
except IndexError as e:
    print("IndexError caught as expected:", str(e))
except Exception as e:
    print("Unexpected error:", str(e))

print("Script completed.")
