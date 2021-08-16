# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather
import requests

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot('location')
        temperature = round(Weather(city)['main']['temp']-273.15)
        print("tis is city",city)
        desc = Weather(city)['weather'][0]['description']
        hum = Weather(city)['main']['humidity']
        wind_spd = Weather(city)['wind']['speed']

        response = f"The current temperature at {city} is {temperature} degree Celsius. Weather is {desc}. The humidity is {hum}% and wind speed is {wind_spd}kph"
        dispatcher.utter_message(response)

        return [SlotSet('location', city)]
