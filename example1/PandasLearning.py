import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.widgets import Slider


ds = xr.open_dataset("sresa1b_ncar_ccsm3-example.nc")
# tempdata = ds.data_vars["tas"].values
# print(ds)
# print (dimension)
# print(tempdata)
# print(ds.tas)

# Plot outline of world map
plt.figure(figsize=(10,5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Selectinf pressure level
pressurelvl = 7000
data_pressurelvl = ds.sel(plev = pressurelvl)
print(data_pressurelvl)

# Plot Eastward wind values 
data_pressurelvl["ua"].plot()

# Slider
ax_slide = plt.axes([0.12,0.08,0.65,0.03]) # xpostion, yposition, width, height 
# Properties of slider
s_factor = Slider(
    ax_slide, "Pressure level", valmin = 1000, valmax= 10000, valinit= 1000, valstep= 1000
    )

# Updating the plot 
def update(val):
    current_v = s_factor.val 


plt.show()