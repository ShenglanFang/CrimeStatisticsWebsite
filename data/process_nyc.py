import pandas as pd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import geopandas as gpd

# Description: This file is used to process the data from the csv files and create a map of the crime data
nyc_crime_df = pd.read_csv('crime_from2020_nyc.csv').dropna()
non_zero_columns = nyc_crime_df.loc[nyc_crime_df['Longitude'] != 0]
crime = non_zero_columns[['Longitude', 'Latitude']]

lo=crime['Latitude']
la=crime['Longitude']

delhi_map = gpd.read_file('shape1\geo_export_82534e18-e1ab-40a5-b8b1-537e723e567c.shp')
fig, ax = plt.subplots(figsize = (15,15))
delhi_map.plot(ax = ax, alpha=0.4, color='grey')

geometry = [Point(xy) for xy in zip(lo, la)]
crs = {'init' : 'epsg:4326'}
geo_df = gpd.GeoDataFrame(crs=crs, geometry = geometry)
print(geo_df)

geo_df.plot(ax = ax, markersize = 2, color = 'blue',marker = '*',label = 'Delhi', alpha = 0.3)
