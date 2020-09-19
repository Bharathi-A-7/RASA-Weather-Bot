
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
    def run(self,dispatcher,tracker,domain):
        from apixu.client import ApixuClient
        api_key = '5cb0e26bd5b315edabbc1252518cf8f6'
        client = ApixuClient(api_key,lang="en")
        
        loc = tracker.get_slot('location')
        api_address='http://api.weatherstack.com/current?access_key={}&query={}'.format(api_key,loc)
        current = requests.get(api_address).json()
        
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['weather_descriptions'][0]
        temperature_c = current['current']['temperature']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_speed']
        
        response =""" It is currently {} in {} at the moment . The temperature is {} degrees,the humidity is {}% and the wind speed is {} mph.""".format(condition,city,temperature_c,humidity,wind_mph)
        
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]
    
