import sys
import os

# Add the current directory to Python's module search path
sys.path.insert(0, os.getcwd())

from astropy.io.fits.tests.test_card_float_precision import test_card_float_precision

if __name__ == "__main__":
    try:
        test_card_float_precision()
        print("Test passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
