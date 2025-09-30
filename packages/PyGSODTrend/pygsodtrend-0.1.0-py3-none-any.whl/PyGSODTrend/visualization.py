import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import warnings
import cartopy.crs as ccrs
import cartopy.feature as cfeature

warnings.filterwarnings("ignore", message="Downloading: https://naturalearth")

def create_scatter(df, filename, lat_col='LATITUDE', lon_col='LONGITUDE', value_col='SLOPE', title="Geographic Map"):
    """
    Creates and saves a static scatter plot of a given attribute colored onto the data points 
    using Matplotlib and Cartopy, showing political boundaries.

    Args:
        df (pd.DataFrame): DataFrame containing geographic data and values.
        filename (str): Name of the file to save the image to (e.g., 'scatter.png').
        lat_col (str): Name of the latitude column.
        lon_col (str): Name of the longitude column.
        value_col (str): Name of the column to color the points by.
        title (str): Title listed on plot.
    """
    # check if required columns are in place
    required_cols = [lat_col, lon_col, value_col]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain columns: {required_cols}")

    lats = df[lat_col].values
    lons = df[lon_col].values
    values = df[value_col].values

    # create bounds for geographical map
    lon_min, lon_max = lons.min() - 0.1, lons.max() + 0.1
    lat_min, lat_max = lats.min() - 0.2, lats.max() + 0.2

    # define the map projection
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

    # add political boundaries and geographical context
    ax.add_feature(cfeature.STATES, linestyle='-', edgecolor='gray',
                   linewidth=0.5, zorder=1)  # State boundaries
    ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black',
                   linewidth=1.0, zorder=1)  # Country borders
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8, zorder=1)
    ax.add_feature(cfeature.LAND, facecolor='lightgray', zorder=0)

    # Plot the data points, colored by the value_col (SLOPE)
    # The 'c' argument takes the array of values for coloring
    # The 'cmap' defines the colormap
    scatter = ax.scatter(lons, lats,
                         c=values,
                         cmap='coolwarm',
                         marker='o',
                         s=100,
                         edgecolor='black',
                         linewidths=0.5,
                         transform=ccrs.PlateCarree(),
                         label=value_col,
                         zorder=3)

    # add color bar
    cbar = fig.colorbar(
        scatter, ax=ax, orientation='vertical', pad=0.05, aspect=20)
    match(df['ATTRIBUTE'][0]):
        case "PRCP":
            cbar.set_label(f'PRCP Trend (mm/day)', fontsize=12)
        case "MAX":
            cbar.set_label(f'MAX Trend (°F/day)', fontsize=12)
        case "MIN":
            cbar.set_label(f'MIN Trend (°F/day)', fontsize=12)

    # Add gridlines and labels
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False

    # add title, lat & long labels
    plt.title(title, fontsize=14)
    plt.xlabel('Longitude', fontsize=12)
    plt.ylabel('Latitude', fontsize=12)

    output_dir = 'src/resources'  # Change to src/resources
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
    full_path = os.path.join(output_dir, filename)
    
    plt.savefig(full_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    
    print(f"Static scatter plot saved successfully as: {full_path}")