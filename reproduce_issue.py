import numpy as np
from astropy.time import Time
from astropy.timeseries import TimeSeries

time = Time(np.arange(100000, 100003), format='jd')
ts = TimeSeries(time=time, data={"flux": [99.9, 99.8, 99.7]})
ts._required_columns = ["time", "flux"]

try:
    ts.remove_column("flux")
except ValueError as e:
    print(f"Exception raised: {str(e)}")

print("Script completed.")
