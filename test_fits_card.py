from astropy.io import fits

# Create a Card object with the same contents as in the example
c = fits.Card('HIERARCH ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to avoid')

print("Original Card:")
print(repr(c))
print(str(c))

# Try to create a new Card with the same contents
new_c = fits.Card(f'HIERARCH {c.keyword}', c.value, c.comment)

print("\nNew Card:")
print(repr(new_c))
print(str(new_c))
