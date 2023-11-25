import pandas as pd
from datetime import datetime

# Reading the CSV File
nyc_crime_df = pd.read_csv('Crime_Map_.csv')
seattle_crime_df = pd.read_csv('SPD_Crime_Data__2008-Present_20231020.csv')

# Convert string date to datetime object and filter out data from 2020 to present
nyc_crime_df['CMPLNT_FR_DT'] = pd.to_datetime(nyc_crime_df['CMPLNT_FR_DT'], errors='coerce')
seattle_crime_df['Offense Start DateTime'] = pd.to_datetime(seattle_crime_df['Offense Start DateTime'], errors='coerce')

# We only care about data after 2020
# nyc_crime_df = nyc_crime_df[nyc_crime_df['CMPLNT_FR_DT'].dt.year >= 2020]
nyc_crime_df = nyc_crime_df[
    (nyc_crime_df['CMPLNT_FR_DT'].dt.year >= 2020) &
    ~(
        (nyc_crime_df['CMPLNT_FR_DT'].dt.year == 2023) &
        (nyc_crime_df['CMPLNT_FR_DT'].dt.month >= 7)
    )
]
# seattle_crime_df = seattle_crime_df[seattle_crime_df['Offense Start DateTime'].dt.year >= 2020]
seattle_crime_df = seattle_crime_df[
    (seattle_crime_df['Offense Start DateTime'].dt.year >= 2020) &
    ~(
        (seattle_crime_df['Offense Start DateTime'].dt.year == 2023) &
        (seattle_crime_df['Offense Start DateTime'].dt.month >= 7)
    )
]
nyc_crime_df.to_csv('nyc_crime_from2020.csv', index=False)
seattle_crime_df.to_csv('seattle_crime_from2020.csv', index=False)