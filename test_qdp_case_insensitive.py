from astropy.table import Table

# Test data
qdp_data = """
read serr 1 2 
1 0.5 1 0.5
"""

# Try to read the table
try:
    table = Table.read(qdp_data, format='ascii.qdp')
    print("Table read successfully:")
    print(table)
except Exception as e:
    print(f"Error reading table: {str(e)}")

print("Test completed.")
