import os
import pymysql
import pandas as pd
from datetime import datetime
import numpy as np



host = '127.0.0.1'
port = '3306'
user = 'root'
password = 'MyNewPass'
database = 'MBTAdb'

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user="root",
    passwd=password,
    db=database,
    charset='utf8mb4')

df = pd.read_sql_query("SELECT * FROM mbta_buses",
    conn)

df

def trip_info(df,dist):
    trips=pd.DataFrame(columns=['id', 'direction_id', 'start', 'end', 'total_time', 'AVG_speed'])
    FMT="%Y-%m-%dT%H:%M:%S%z"   
    for trip in df['trip_id'].sort_values().drop_duplicates():
        direction=df[(df['trip_id']==trip)]['direction_id'].iloc[0]
        sorted_trip=df[(df['trip_id']==trip) & (df['current_stop_sequence']==2)].sort_values('updated_at')
        #print(sorted_trip.loc[:,['trip_id','direction_id','current_stop_sequence','updated_at']])
        if len(sorted_trip['updated_at'])>=1:
            start_time=sorted_trip['updated_at'].iloc[0]
            start_time_formated=datetime.strptime(start_time, FMT)
        else:
            start_time=None
        #print(f"start time: {start_time}")
        sorted_trip=df[(df['trip_id']==trip) & (df['current_stop_sequence']==24)].sort_values('updated_at')
        #print(sorted_trip.loc[:,['trip_id','direction_id','current_stop_sequence','updated_at']])
        if len(sorted_trip['updated_at'])>=1:
            end_time=sorted_trip['updated_at'].iloc[0]
            end_time_formated=datetime.strptime(end_time, FMT)
        else:
            end_time=None
        #print(f"end time:   {end_time}")
        if start_time!=None and end_time!=None:

            delta_t=end_time_formated-start_time_formated
            if delta_t.total_seconds()<=0:
                delta_t=None
                speed=None
            else:
                delta_t=delta_t.total_seconds()/60
                speed=dist/delta_t*60
        else:
            delta_t=None
            speed=None

        temp={'id':trip, 'direction_id':direction ,'start':start_time, 'end':end_time,'total_time':delta_t, 'AVG_speed':speed}
        #print(temp)
        trips=trips.append(temp, ignore_index=True)
        #print(trips)

    trips.dropna(inplace=True)
    trips["start"] = pd.to_datetime(trips["start"], yearfirst=True, errors='coerce', dayfirst=False, format=FMT)
    trips["end"] = pd.to_datetime(trips["end"], yearfirst=True, errors='coerce', dayfirst=False, format=FMT)
    return trips
test=trip_info(df,20)
print(test)