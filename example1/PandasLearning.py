import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.widgets import Slider


ds = xr.open_dataset("sresa1b_ncar_ccsm3-example.nc")
# tempdata = ds.data_vars["tas"].values


# Plot outline of world map
fig = plt.figure(figsize=(10,5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Slider
ax_slide = plt.axes([0.12,0.08,0.65,0.03]) # xpostion, yposition, width, height 
# Properties of slider
s_factor = Slider(
    ax_slide, "Pressure level", valmin = 1000, valmax= 10000, valinit= 1000, valstep= 1000
    )

# Updating the plot 
def update(val):
    pressurelvl = s_factor.val

    # UPDATING Pressure level
    data_pressurelvl = ds.sel(
        plev = pressurelvl
        )
    # Plot Eastward wind values 
    data_pressurelvl["ua"].plot(ax=ax)
    fig.canvas.draw()


s_factor.on_changed(update)
plt.show()