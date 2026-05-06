from astropy.utils import minversion
from packaging.version import Version, parse

print("Testing minversion:")
try:
    result = minversion('numpy', '1.14dev')
    print(f"minversion('numpy', '1.14dev') = {result}")
except Exception as e:
    print(f"Error in minversion: {type(e).__name__}: {str(e)}")

print("\nTesting Version:")
try:
    result = Version('1.14.3') >= Version('1.14dev')
    print(f"Version('1.14.3') >= Version('1.14dev') = {result}")
except Exception as e:
    print(f"Error in Version: {type(e).__name__}: {str(e)}")

print("\nTesting parse:")
try:
    result = parse('1.14.3') >= parse('1.14dev')
    print(f"parse('1.14.3') >= parse('1.14dev') = {result}")
except Exception as e:
    print(f"Error in parse: {type(e).__name__}: {str(e)}")

print("\nScript completed successfully.")
