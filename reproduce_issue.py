from astropy import units as u

x = u.Unit('asdf', parse_strict='silent')

try:
    result = x == None
    print(f"x == None resulted in: {result}")
except TypeError as e:
    print(f"TypeError occurred: {str(e)}")

print("Script completed successfully.")
