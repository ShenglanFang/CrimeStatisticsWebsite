import pandas as pd
from datetime import datetime

# 读取CSV文件
nyc_crime_df = pd.read_csv('Crime_Map_.csv')
seattle_crime_df = pd.read_csv('SPD_Crime_Data__2008-Present_20231020.csv')

# 将字符串日期转换为datetime对象，并过滤出2020年至今的数据
nyc_crime_df['CMPLNT_FR_DT'] = pd.to_datetime(nyc_crime_df['CMPLNT_FR_DT'], errors='coerce')
seattle_crime_df['Offense Start DateTime'] = pd.to_datetime(seattle_crime_df['Offense Start DateTime'], errors='coerce')

# 我们只关心2020年以后的数据
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