import numpy as np
from astropy import units as u

print("Testing float16:")
print("float16(1):", np.float16(1))
print("float16(1) * km:", (np.float16(1) * u.km))
print("(float16(1) * km).dtype:", (np.float16(1) * u.km).dtype)
print("float16(1.5) * km:", (np.float16(1.5) * u.km))
print("(float16(1.5) * km).dtype:", (np.float16(1.5) * u.km).dtype)
print("(float16(1) * km).to(m):", (np.float16(1) * u.km).to(u.m))
print("(float16(1) * km).to(m).dtype:", (np.float16(1) * u.km).to(u.m).dtype)

print("\nTesting other float types:")
print("float32:", (np.float32(1) * u.km).dtype)
print("float64:", (np.float64(1) * u.km).dtype)
print("float128:", (np.float128(1) * u.km).dtype)
print("float:", (float(1) * u.km).dtype)

print("\nScript completed successfully, no errors.")
