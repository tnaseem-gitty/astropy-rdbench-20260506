import numpy as np
import astropy.units as u

# Attempt to reproduce the issue
try:
    result = (1 * u.m) + (1 * u.mm)
    print("Operation successful:", result)
except ValueError as e:
    print("ValueError caught:", str(e))

print("Script completed.")
