import numpy as np
from astropy.nddata import NDDataRef

array = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
mask = np.array([[0, 1, 64], [8, 0, 1], [2, 1, 0]])

nref_nomask = NDDataRef(array)
nref_mask = NDDataRef(array, mask=mask)

print("1. Multiply no mask by constant:")
try:
    result = nref_nomask.multiply(1., handle_mask=np.bitwise_or).mask
    print(result)
except Exception as e:
    print(f"Error: {e}")

print("\n2. Multiply no mask by itself:")
try:
    result = nref_nomask.multiply(nref_nomask, handle_mask=np.bitwise_or).mask
    print(result)
except Exception as e:
    print(f"Error: {e}")

print("\n3. Multiply mask by constant:")
try:
    result = nref_mask.multiply(1., handle_mask=np.bitwise_or).mask
    print(result)
except Exception as e:
    print(f"Error: {e}")

print("\n4. Multiply mask by itself:")
try:
    result = nref_mask.multiply(nref_mask, handle_mask=np.bitwise_or).mask
    print(result)
except Exception as e:
    print(f"Error: {e}")

print("\n5. Multiply mask by no mask:")
try:
    result = nref_mask.multiply(nref_nomask, handle_mask=np.bitwise_or).mask
    print(result)
except Exception as e:
    print(f"Error: {e}")

print("\nScript completed.")
