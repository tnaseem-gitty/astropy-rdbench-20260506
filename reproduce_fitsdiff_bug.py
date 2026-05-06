import os
import sys
import site

# Add the site-packages directory to the Python path
site_packages = site.getsitepackages()[0]
sys.path.insert(0, site_packages)

from astropy.io import fits
import astropy

print(f"Using astropy version: {astropy.__version__}")

try:
    col = fits.Column('a', format='QD', array=[[0], [0, 0]])
    hdu = fits.BinTableHDU.from_columns([col])
    hdu.writeto('diffbug.fits', overwrite=True)

    diff = fits.FITSDiff('diffbug.fits', 'diffbug.fits')
    print(f"Identical: {diff.identical}")
    
    print("Detailed comparison report:")
    diff.report()

    # Clean up the file
    os.remove('diffbug.fits')

    print("Script completed successfully.")
except ImportError as e:
    print(f"ImportError: {str(e)}")
    print("Try running 'pip install astropy' to install the required package.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
