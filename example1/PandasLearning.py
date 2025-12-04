import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ds = xr.open_dataset("sresa1b_ncar_ccsm3-example.nc")
# tempdata = ds.data_vars["tas"].values
# print(ds)
# print (dimension)
# print(tempdata)
# print(ds.tas)

pressurelvl = 7000
data_pressurelvl = ds.sel(plev = pressurelvl)

plt.figure(figsize=(10,5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

print(data_pressurelvl)
data_pressurelvl["ua"].plot()
plt.show()