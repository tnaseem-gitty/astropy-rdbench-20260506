from astropy.io import fits

for n in range(60, 70):
    card1 = fits.Card('CONFIG', "x" * n + "''")
    card2 = fits.Card.fromstring(str(card1))  # Should be the same as card1
    print(n, card1.value == card2.value)
    if card1.value != card2.value:
        print(card1.value)
        print(card2.value)
