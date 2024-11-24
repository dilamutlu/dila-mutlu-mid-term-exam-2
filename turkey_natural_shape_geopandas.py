import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("dila-mutlu-mid-term-exam-2/turkey-points-shape/points.shp")
print(gdf.head())

world = gpd.read_file("dila-mutlu-mid-term-exam-2/ne_110m_land/ne_110m_land.shp")

# We restrict to Türkiye.
ax = world.clip([24, 35, 45, 42]).plot(color="white", edgecolor="black")

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color="red")

plt.show()
