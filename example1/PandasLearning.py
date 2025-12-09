import xarray as xr
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Load dataset
ds = xr.open_dataset(
    "sresa1b_ncar_ccsm3-example.nc"
    )

# Plot outline of world map
fig = plt.figure(
    figsize=(10, 5)
    )
ax = plt.axes(
    projection=ccrs.PlateCarree()
    )
ax.coastlines()

# Initial Data
data_pressurelvl = ds.sel(plev=1000)
Data = data_pressurelvl["ua"].plot(
    ax=ax, cmap='viridis', add_colorbar=False
    )
ax.set_title(
        f"Eastward Wind at 1000 hPa", fontsize=14
        )

# Add colorbar
cbar = plt.colorbar(
    Data, ax=ax, orientation='vertical', pad=0.05, fraction = 0.023
    )
cbar.set_label(
    'Eastward Wind (m/s)'
    )
cbar.set_ticks([
    60, 40, 20, 0, -20, - 40, -60, 
    ])
# ([60, 40, 20, 0, -20, - 40, -60, ])

# Slider
ax_slide = plt.axes([
    0.12, 0.05, 0.65, 0.03
    ])
Slider_stepvalue = [
    1000, 2000, 3000, 5000, 7000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 85000, 92500, 100000
    ]
s_factor = Slider(
    ax_slide, "Pressure level", valmin=1000, valmax=100000, valinit=1000, valstep=Slider_stepvalue
    )

# Updating the plot 
def update(val):
    pressurelvl = s_factor.val
    data_pressurelvl = ds.sel(
        plev=pressurelvl
        )
    
    # Update Pressure level
    Data.set_array(
        data_pressurelvl["ua"].values.flatten()
        )
    ax.set_title(
        f"Eastward Wind at {pressurelvl} hPa", fontsize=14
        )
    
    # Redraw the canvas
    fig.canvas.draw_idle()

s_factor.on_changed(update)

# Improve layout
plt.tight_layout()
plt.show()
