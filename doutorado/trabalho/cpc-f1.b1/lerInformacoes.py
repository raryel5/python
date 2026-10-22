import xarray as xr

ds = xr.open_dataset('maoaafcpcF1.b1.20140222.143709.nc')
print(ds)
ds.close()
