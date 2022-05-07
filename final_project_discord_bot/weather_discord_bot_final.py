#weather discord bot final

#------------------------------------------------
#Weather functions


### Working with weather API section ---------------------------------

#This part of the program gathers information from the openweathermap.org API. This API provides information about the weather for cities worldwide.

#Weather API
import requests
import json


API_KEY = "d5fcf285d0a6978fc98628b41e510d86"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

 
### Weather bot functions -------------------

## current_weather_in_city()
# This function provides temperature, humidity, pressure, and conditions information for the city provided as the argument
def current_weather_in_city(CITY):
  BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
  API_KEY = "d5fcf285d0a6978fc98628b41e510d86"

  URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=imperial"

  response = requests.get(URL)


  if response.status_code == 200:
    data = response.json()
    main_dict = data['main']
    temperature = main_dict['temp']
    humidity = main_dict['humidity']
    pressure = main_dict['pressure']
    report = data['weather']
    current_weather_f = 'Today, in ' + CITY + f" the temperature is {temperature} degrees fahrenheit with {humidity}% humidity and a pressure of {pressure} inHG. There will be {report[0]['description']}."
    output_message = current_weather_f
  else:
     output_message = "<Error in the HTTP request> It is possible that you misspelled the name of the city."
  print(output_message)
  return output_message


## is_it_windy()
# This function provides information about the wind conditions in the city provided. Instead of returning wind in mph, it responds with more consumer friendly terms.
def is_it_windy(CITY):
  BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
  API_KEY = "d5fcf285d0a6978fc98628b41e510d86"

  windy_URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=imperial"

  wind_response = requests.get(windy_URL)

  if wind_response.status_code == 200:
    data = wind_response.json()
    wind_dict = data['wind']
    wind_speed = wind_dict['speed']
    if wind_speed <= 2:
      output_message = 'There is no wind.'
    elif wind_speed > 2 and wind_speed <= 10:
      output_message = 'There is a gentle breeze.'
    elif wind_speed > 10 and wind_speed <= 20:
      output_message = 'It is windy, with winds between 10 and 20 mph.'
    elif wind_speed > 25:
      output_message = 'Winds are expected to be in excess of 25 mph with heavy gusts.'
  else:
    output_message = "<Error in the HTTP request> It is possible that you misspelled the name of the city."
  print(output_message)
  return output_message
    
    
    
## sunrise_sunset_time()
#This function provides information about the time of the sunset in the city provided as the argument.
import datetime

def sunset_time(CITY):
  BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
  API_KEY = "d5fcf285d0a6978fc98628b41e510d86"

  sunset_URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=imperial"

  sunset_response = requests.get(sunset_URL)
  
  if sunset_response.status_code == 200:
    sunset_data = sunset_response.json()
    sys_dict = sunset_data['sys']
    
    #sunset times are recorded in UTC
    sunset_utc = sys_dict['sunset']
    print(sunset_utc)
    
    #timezone is recorded as the shift in seconds from UTC time
    city_timezone = sunset_data['timezone']
    print(city_timezone)
    
    #sunset_time_local_raw = sunset_utc + city_timezone
    sunset_time_local_raw = sunset_utc
    #print(f" the sunset local time is {local_sunset_time_raw}")
    local_sunset_datetime = datetime.datetime.fromtimestamp(sunset_time_local_raw)
    
    output_message = f"Time of the sunset for today, {local_sunset_datetime}"
  else:
    output_message = "<Error in the HTTP request> It is possible that you misspelled the name of the city."
  print(output_message)
  return output_message

### Testing weather bot functions
#current_weather_in_city('Charlottesville')
#is_it_windy('Charlottesville')
#sunset_time('Charlottesville')


### ----------------------------------------


#-------------------------------------------------
# Preparing discord bot to respond to user

import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')
#TOKEN = 'OTY2Mzc5NjczMzU5NjQyNjY0.GSHYuT.gGLQJrG65SWO2V_BTBstbss-4_8eH6SDUejvqY'
GUILD = os.getenv('DISCORD_GUILD')
#GUILD = 'Parker_D_bot_lab_server'

greeting_triggers = ['Hello' , 'Hey' ,]
greeting_responses = ['Greetings, what can I do for you?' , "What's up, how can I help?"]

help_triggers = ["I need help", "I have a question", "I am having trouble", "help","Help!","Help", "I have a problem"]
help_response = 'I can help. I am a weather bot, so I can answer questions like "What is the weather in Charlottesville" (or any other city you choose). Or you can ask me "Is it windy in Charlottesville" or "When is the sunset today in Charlottesville" Hope that helps!'

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged in as')
    print(self.user.name)
    print(self.user.id)
    
  async def on_message(self, message):
    if message.author.id == self.user.id:
      return
    
    else:
      msg = message.content
      
      if any(word in msg for word in greeting_triggers):
        await message.channel.send(random.choice(greeting_responses))
    
      if any(word in msg for word in help_triggers):
        await message.channel.send(help_response)
        
      #Activating weather functions
      if msg[0:22] == 'What is the weather in':
        current_weather_city = msg[22:]
        current_weather = current_weather_city.strip()
        print('current_weather')
        current_weather_response = current_weather_in_city(current_weather_city)
        await message.channel.send(current_weather_response)
        return

      #This if statement takes in the question about wind conditions and responds with the wind conditions
      if msg[0:14] == 'Is it windy in':
        windy_city = msg[14:]
        windy_city = windy_city.strip()
        print('windy_city')
        windy_city_response = is_it_windy(windy_city)
        await message.channel.send(windy_city_response)
        return

      #This if statement responds to the question about sunset time and responds with the sunset time
      if msg[0:27] == 'When is the sunset today in':
        sunset_city = msg[27:]
        sunset_city = sunset_city.strip()
        print('sunset_city')
        sunset_city_response = sunset_time(sunset_city)
        await message.channel.send(sunset_city_response)
        return
        
      #This else clause responds in the event that the bot does not understand the user's request 
      else:
        error_message = "I didn't quite get that, can you reiterate your request?"
        await message.channel.send(error_message)
        return
        

      
client = MyClient()
client.run('OTY2Mzc5NjczMzU5NjQyNjY0.GQPsQP.-AfjuWqeVGq-j2O8jZf1OnttmvasB4W0LguagI')
    





