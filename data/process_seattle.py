import pandas as pd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np

# Description: This file is used to process the data from the csv files and create a map of the crime data
nyc_crime_df = pd.read_csv('crime_from2020_seattle.csv').dropna()
non_zero_columns = nyc_crime_df[(nyc_crime_df['Latitude'] <= 50) & (nyc_crime_df['Longitude'] < -122)]
crime = non_zero_columns[['Longitude', 'Latitude']]

lo=crime['Longitude']
la=crime['Latitude']

delhi_map = gpd.read_file('shape2\Seattle_City_Council_District_2013.shp')
fig, ax = plt.subplots(figsize = (15,15))
delhi_map.plot(ax = ax, alpha=0.4, color='grey')
# plt.show()
geometry = [Point(xy) for xy in zip(lo, la)]
crs = {'init' : 'epsg:4326'}
geo_df = gpd.GeoDataFrame(crs=crs, geometry = geometry)
print(geo_df)

geo_df.plot(ax = ax, markersize = 2, color = 'blue',marker = '*',label = 'Delhi', alpha = 0.3)
plt.show()
plt.savefig('seattle_map.png', bbox_inches='tight')