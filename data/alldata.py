import pandas as pd

nyc_crime_df = pd.read_csv('nyc_crime_from2020.csv')
seattle_crime_df = pd.read_csv('seattle_crime_from2020.csv')

crime = pd.read_csv('crime_from2020.csv')
crime_nyc = pd.read_csv('crime_from2020_nyc.csv')
crime_seattle = pd.read_csv('crime_from2020_seattle.csv')

crime_month = pd.read_csv('crime_month_from2020.csv')
crime_week = pd.read_csv('crime_week_from2020.csv')
crime_hour = pd.read_csv('crime_hour_from2020.csv')

print(crime.head())
# print('nyc table attributes:')
# print(nyc_crime_df.columns.tolist())
# print('seattle table attributes:')
# print(seattle_crime_df.columns.tolist())

# print('crime table all attributes:')
# print(crime.columns.tolist())
# print(crime_nyc.columns.tolist())
# print(crime_seattle.columns.tolist())

# print('month table :')
# print(crime_month.columns.tolist())
# print('week table :')
# print(crime_week.columns.tolist())
# print('hour table :')
# print(crime_hour.columns.tolist())
