from astropy.coordinates import SkyCoord

class custom_coord(SkyCoord):
    @property
    def prop(self):
        return self.random_attr

c = custom_coord('00h42m30s', '+41d12m00s', frame='icrs')
try:
    c.prop
except AttributeError as e:
    print(f"AttributeError: {str(e)}")

print("Script completed successfully.")
