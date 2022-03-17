#!/usr/bin/env python
# coding: utf-8

# In[133]:


#OpenSky API Project
# Author: Parker Driscoll fpd4fv
#Assignment: DS3002 Data Project 1


# In[ ]:


import json
import requests

import csv
import pandas as pd

import datetime


# In[134]:


def epoch_utc_filename_convert(epoch_time):
    utc_filename_format = datetime.datetime.utcfromtimestamp(epoch_time).strftime("%Y_%m_%d-%I_%M_%S_%p")
    return(utc_filename_format)


# In[135]:


###Operation 2 from assignment doc
#This function uses an anonymous API key to pull data on all aircraft in the world being tracked via ADS-b transponders. This function pulls data from the OpenSky network API.
#This functions converts the json response from the API and returns the data as a pandas dataframe

def all_current_aircraft_df_function():
    url_anon_aca = "https://opensky-network.org/api/states/all"
    pull_all_current_aircraft = requests.request("GET",url_anon_aca)
    pull_aca_json_format = pull_all_current_aircraft.json()
    df_aca = pd.DataFrame(pull_aca_json_format["states"], columns = ['icao24','callsign','origin_country','time_position','last_contact','longitude','latitude','baro_altitude','on_ground','velocity','true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source','MLAT'])
    return df_aca

df_aca = all_current_aircraft_df_function()


# In[136]:


### Operation 3 from assignment doc
#Dropping columns

df_aca.drop(['sensors','geo_altitude','squawk','spi','position_source','MLAT'], axis = 1, inplace = True)
df_aca


# In[137]:


### Operation 5 from assignment doc
#Producing summary of data taken in from API

print('This data set represents', df_aca.shape[0], 'aircraft that are currently being tracked via their ADS-b transponders worldwide. This data set has', df_aca.shape[1] ,  'columns which provide information about the identity of the aircraft, its position, and its track.')
      
      


# In[139]:


### Try / Catch producing informative errors example
# This function takes input as the unique icao24 code assigned to a specific aircraft and tells the user how fast that aircraft is traveling. 
#If the icao24 code is invalid or it is valid but that aircraft is not being tracked at the time that the API was called, then an error will be produced

def specific_aircraft_speed_finder(icao24):
    str_icao = str(icao24)
    info = df_aca.loc[df_aca['icao24']==icao24]
    try:
        speed = int(info['velocity'])
        print('The speed of this aircraft is ' + str(speed) + ' m/s')
    except:
        print('ICAO24 code was invalid. Either this aircraft is not currently in flight, or this code does not exist.')
        
# The lines of code below demonstrate the function's ability to produce errors. ICAO24 codes are only 6 characters long, so a string longer than 6 characters will trigger the error.
error_producing_icao24_code = 'led_zeppelin'
specific_aircraft_speed_finder(error_producing_icao24_code)


# In[82]:


#This function converts epoch time into a filename friendly UTC time format
def epoch_utc_filename_convert(epoch_time):
    utc_filename_format1 = datetime.datetime.utcfromtimestamp(epoch_time).strftime("%Y_%m_%d-%I_%M_%S_%p")
    utc_filename_format2 = str(utc_filename_format1)
    return(utc_filename_format2)


# In[83]:


### Operation 4 from assignment doc
#Converting modified pandas dataframe to csv file saved to pwd of user 
#Filename has timestamp that represents the time that the data was most recently received from an aircraft when the API was called.  


def df_to_csv_file_function(dataframe):
    # filename = all_current_aircraft_TIMESTAMP.csv
    timestamp = epoch_utc_filename_convert(dataframe['time_position'].max())
    filename = 'all_current_aircraft_' + timestamp + '.csv'
    df_as_csv = dataframe.to_csv(filename , encoding = 'utf-8' , index=False)
    return df_as_csv

df_to_csv_file_function(df_aca)

