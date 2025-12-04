import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as crs

ds = xr.open_dataset("sresa1b_ncar_ccsm3-example.nc")
# tempdata = ds.data_vars["tas"].values
# print(ds)
# print (dimension)
# print(tempdata)
# print(ds.tas)

pressurelvl = 7000
data_pressurelvl = ds.sel(plev = pressurelvl)
print(data_pressurelvl)
data_pressurelvl["ua"].plot()
print(ds["ua"].dims)
# ds['tas'].plot() 
plt.show()