import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.abspath('.'))

try:
    from astropy.io.fits.card import Card
    from astropy.io.fits.util import parse_card
except ImportError as e:
    print(f"Error importing astropy modules: {e}")
    sys.exit(1)

def test_card(n, suffix):
    try:
        card1 = Card('CONFIG', "x" * n + suffix)
        card2 = Card.fromstring(str(card1))
        print(n, len(card1.value), card1.value == card2.value)
        if card1.value != card2.value:
            print(card1.value)
            print(card2.value)
    except Exception as e:
        print(f"Error processing card with n={n}: {e}")

print("Test 1: Null string at the end")
for n in range(60, 70):
    test_card(n, "''")

print("\nTest 2: Null string in the middle")
for n in range(50, 70):
    test_card(n, "''x" * 10)

print("Script completed successfully, no errors.")
