from astropy.io import fits

def test_card_float_precision():
    # Test case for the issue with float precision in Card
    c = fits.Card('HIERARCH ESO IFM CL RADIUS', 0.009125, '[m] radius arround actuator to avoid')
    
    # Check that the original card is formatted correctly
    assert str(c) == 'HIERARCH ESO IFM CL RADIUS = 0.009125 / [m] radius arround actuator to avoid    '
    
    # Create a new card with the same contents
    new_c = fits.Card(f'HIERARCH {c.keyword}', c.value, c.comment)
    
    # Check that the new card is identical to the original
    assert str(new_c) == str(c)
    
    # Check that the value is preserved exactly
    assert new_c.value == 0.009125
    
    # Check that the comment is not truncated
    assert new_c.comment == '[m] radius arround actuator to avoid'

