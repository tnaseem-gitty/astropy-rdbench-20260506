import numpy as np
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation, ITRS, AltAz, HADec
from astropy.tests.helper import assert_quantity_allclose

def test_itrs_to_altaz():
    # Create an ITRS coordinate
    itrs = ITRS(x=6371*u.km, y=0*u.km, z=100*u.km)
    
    # Create an observer location
    location = EarthLocation(lon=0*u.deg, lat=45*u.deg, height=0*u.m)
    
    # Create an AltAz frame
    altaz_frame = AltAz(obstime=Time('2021-01-01T00:00:00'), location=location)
    
    # Transform ITRS to AltAz
    altaz = itrs.transform_to(altaz_frame)
    
    # Check the results (these values are approximate and may need adjustment)
    assert_quantity_allclose(altaz.alt, 44.427*u.deg, atol=1e-3*u.deg)
    assert_quantity_allclose(altaz.az, 0*u.deg, atol=1e-3*u.deg)
    
    # Transform back to ITRS
    itrs_back = altaz.transform_to(ITRS)
    
    # Check that we get back to the original ITRS coordinates
    assert_quantity_allclose(itrs_back.x, itrs.x, atol=1e-3*u.km)
    assert_quantity_allclose(itrs_back.y, itrs.y, atol=1e-3*u.km)
    assert_quantity_allclose(itrs_back.z, itrs.z, atol=1e-3*u.km)

def test_itrs_to_hadec():
    # Create an ITRS coordinate
    itrs = ITRS(x=6371*u.km, y=0*u.km, z=100*u.km)
    
    # Create an observer location
    location = EarthLocation(lon=0*u.deg, lat=45*u.deg, height=0*u.m)
    
    # Create a HADec frame
    hadec_frame = HADec(obstime=Time('2021-01-01T00:00:00'), location=location)
    
    # Transform ITRS to HADec
    hadec = itrs.transform_to(hadec_frame)
    
    # Check the results (these values are approximate and may need adjustment)
    assert_quantity_allclose(hadec.ha, 0*u.deg, atol=1e-3*u.deg)
    assert_quantity_allclose(hadec.dec, 44.427*u.deg, atol=1e-3*u.deg)
    
    # Transform back to ITRS
    itrs_back = hadec.transform_to(ITRS)
    
    # Check that we get back to the original ITRS coordinates
    assert_quantity_allclose(itrs_back.x, itrs.x, atol=1e-3*u.km)
    assert_quantity_allclose(itrs_back.y, itrs.y, atol=1e-3*u.km)
    assert_quantity_allclose(itrs_back.z, itrs.z, atol=1e-3*u.km)

