import xarray as xr

ds = xr.open_dataset("sresa1b_ncar_ccsm3-example.nc")
# print(ds)

print(ds.tas)