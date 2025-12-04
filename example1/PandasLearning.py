import xarray as xr
import matplotlib.pyplot as plt

# dimension = ds.dims
# tempdata = ds.data_vars["tas"].values
# print(ds)
# print (dimension)
# print(tempdata)
# print(ds.tas)
ds = xr.open_dataset("sresa1b_ncar_ccsm3-example.nc")

ds['tas'].plot() 
plt.show()