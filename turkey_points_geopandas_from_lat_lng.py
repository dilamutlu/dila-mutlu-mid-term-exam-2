import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file("dila-mutlu-mid-term-exam-2/turkey-points-shape/points.shp")
print(df.head())

# geometry sütunundan koordinatları ayıkla (nokta geometriler için)
df['longitude'] = df.geometry.x
df['latitude'] = df.geometry.y

# Ayrıştırılmış DataFrame
xdf = df[['osm_id', 'name', 'type', 'longitude', 'latitude']]

gdf = gpd.GeoDataFrame(
    xdf, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326"
)

world = gpd.read_file("dila-mutlu-mid-term-exam-2/ne_110m_land/ne_110m_land.shp")

# We restrict to Türkiye.
ax = world.clip([24, 35, 45, 42]).plot(color="white", edgecolor="black")

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color="red")

plt.show()
