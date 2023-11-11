import pandas as pd
from datetime import datetime

# 读取CSV文件
nyc_crime_df = pd.read_csv('nyc_crime_from2020.csv')
seattle_crime_df = pd.read_csv('seattle_crime_from2020.csv')

# 将字符串日期转换为datetime对象
nyc_crime_df['CMPLNT_FR_DT'] = pd.to_datetime(nyc_crime_df['CMPLNT_FR_DT'], errors='raise').dt.date
seattle_crime_df['Offense Start DateTime'] = pd.to_datetime(seattle_crime_df['Offense Start DateTime'], errors='raise')

# 创建六个新表的结构
# seattle_crime_type = pd.DataFrame(columns=['Crime_Type_ID', 'Offense_Description'])
# newyork_crime_type = pd.DataFrame(columns=['Crime_Type_ID', 'Offense_Description'])
# crime = pd.DataFrame(columns=['Crime_ID', 'Date', 'Time', 'Crime_Type', 'Longitude', 'Latitude', 'City'])
crime_month = pd.DataFrame(columns=['Month', 'Month_Count', 'Month_Count_SE', 'Month_Count_NY'])
crime_week = pd.DataFrame(columns=['Week_Day', 'Week_Day_Count', 'Week_Day_Count_SE', 'Week_Day_Count_NY'])
crime_time = pd.DataFrame(columns=['Hour', 'Hour_Count', 'Hour_Count_SE', 'Hour_Count_NY'])

# 填充Seattle和New York的犯罪类型表
seattle_crime_type = seattle_crime_df[['Offense Code', 'Offense']].drop_duplicates().rename(columns={'Offense Code': 'Crime_Type_ID', 'Offense': 'Offense_Description'})
newyork_crime_type = nyc_crime_df[['KY_CD', 'OFNS_DESC']].drop_duplicates().rename(columns={'PD_CD': 'Crime_Type_ID', 'PD_DESC': 'Offense_Description'})

# 填充犯罪表
crime_nyc = nyc_crime_df[['CMPLNT_NUM', 'CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'PD_CD', 'Latitude', 'Longitude']]
crime_nyc.columns = ['Crime_ID', 'Date', 'Time', 'Crime_Type', 'Longitude', 'Latitude']
crime_nyc['City'] = 'New York'
crime_nyc['Time'] = pd.to_datetime(crime_nyc['Time'], format='%H:%M:%S').dt.time

crime_seattle = seattle_crime_df[['Offense ID', 'Offense Code', 'Longitude', 'Latitude']]
crime_seattle.columns = ['Crime_ID', 'Crime_Type', 'Longitude', 'Latitude']
crime_seattle['City'] = 'Seattle'
crime_seattle['Date'] = seattle_crime_df['Offense Start DateTime'].dt.date
crime_seattle['Time'] = seattle_crime_df['Offense Start DateTime'].dt.time

crime = pd.concat([crime_nyc, crime_seattle], ignore_index=True)
crime.to_csv('crime_from2020.csv', index=False)
crime_nyc.to_csv('crime_from2020_nyc.csv', index=False)
crime_seattle.to_csv('crime_from2020_seattle.csv', index=False)

