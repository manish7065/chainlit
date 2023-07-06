# Import Necessary Libraries
import requests
import json
from chainlit import chat

# Define a function to get the weather data
def get_weather_data(city):
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = json.loads(response.text)
    return data

# Define the chatbot
bot = chat.ChatBot('WeatherBot')

# Create a function that provides weather information
@bot.listen('What is the weather like in {city}', intent='get_weather')
def get_weather(city):
    data = get_weather_data(city)
    if data["cod"] != "404":
        description = data["weather"][0]["description"]
        temp = round(data["main"]["temp"] - 273.15, 2)
        response = f'The weather in {city} is {description} with a temperature of {temp}°C.'
    else:
        response = f'Sorry, I could not find weather information for {city}.'
    return response

# Start the chatbot
bot.start()
