import pandas as pd
from datetime import datetime

crime = pd.read_csv('crime_from2020.csv')
crime_nyc = pd.read_csv('crime_from2020_nyc.csv')
crime_seattle = pd.read_csv('crime_from2020_seattle.csv')

crime['Date'] = pd.to_datetime(crime['Date'], errors='raise')
crime['Time'] = pd.to_datetime(crime['Time'], errors='raise')
crime_nyc['Date'] = pd.to_datetime(crime_nyc['Date'], errors='raise')
crime_nyc['Time'] = pd.to_datetime(crime_nyc['Time'], errors='raise')
crime_seattle['Date'] = pd.to_datetime(crime_seattle['Date'], errors='raise')
crime_seattle['Time'] = pd.to_datetime(crime_seattle['Time'], errors='raise')

crime['Month'] = crime['Date'].dt.month
crime['Week_Day'] = crime['Date'].dt.day_name()
crime['Hour'] = crime['Time'].dt.hour

# Create the 'crime_month' DataFrame
crime_month = crime.groupby('Month').size().reset_index(name='Month_Count')
crime_month_se = crime_seattle['Date'].dt.month.value_counts().reset_index().rename(columns={'index': 'Month', 'Date': 'Month_Count_SE'})
crime_month_ny = crime_nyc['Date'].dt.month.value_counts().reset_index().rename(columns={'index': 'Month', 'Date': 'Month_Count_NY'})
crime_month = crime_month.merge(crime_month_se, on='Month', how='left').merge(crime_month_ny, on='Month', how='left')

# Create the 'crime_week' DataFrame
crime_week = crime.groupby('Week_Day').size().reset_index(name='Week_Day_Count')
crime_week_se = crime_seattle['Date'].dt.day_name().value_counts().reset_index().rename(columns={'index': 'Week_Day', 'Date': 'Week_Day_Count_SE'})
crime_week_ny = crime_nyc['Date'].dt.day_name().value_counts().reset_index().rename(columns={'index': 'Week_Day', 'Date': 'Week_Day_Count_NY'})
crime_week = crime_week.merge(crime_week_se, on='Week_Day', how='left').merge(crime_week_ny, on='Week_Day', how='left')

# Create the 'crime_time' DataFrame
crime_hour = crime.groupby('Hour').size().reset_index(name='Hour_Count')
crime_hour_se = crime_seattle['Time'].dt.hour.value_counts().reset_index().rename(columns={'index': 'Hour', 'Time': 'Hour_Count_SE'})
crime_hour_ny = crime_nyc['Time'].dt.hour.value_counts().reset_index().rename(columns={'index': 'Hour', 'Time': 'Hour_Count_NY'})
crime_hour = crime_hour.merge(crime_hour_se, on='Hour', how='left').merge(crime_hour_ny, on='Hour', how='left')

crime_month.to_csv('crime_month_from2020.csv', index=False)
crime_week.to_csv('crime_week_from2020.csv', index=False)
crime_hour.to_csv('crime_hour_from2020.csv', index=False)
