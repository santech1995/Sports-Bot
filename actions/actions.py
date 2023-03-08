# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database_connection import DataInsertion
import requests

#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.get_slot("city")
        dispatcher.utter_message(text=f"You chose {city}")
        api_address = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=bcb59ece5810e1272e46ade32b2ef8ed"
        json_data = requests.get(api_address).json()
        temp = int(json_data['main']['temp_min'] - 273)
        description = json_data['weather'][0]['description']
        # print(json_data)
        # temp= json_data['main']['temp']
        
        dispatcher.utter_message(text=f"The temperature in {city} today is {temp} degrees celcius with {description}")
        DataInsertion(tracker.get_slot("city"),temp)
        dispatcher.utter_message("Data has been inserted to database")
        return []

class ActionGetNewsOption(Action):

    def name(self) -> Text:
        return "action_news_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        news_option=tracker.get_slot("news_option")
        dispatcher.utter_message(text=f"You chose {news_option}")

        entities = tracker.latest_message['entities']
        print("last message was ",entities)

        for e in entities:
            if e['entity'] == 'news_option':
                user_resp = e['value']
                dispatcher.utter_message(text=f"User response is {user_resp}")

            if user_resp == 'weather':
                dispatcher.utter_message(response = "utter_city")

            if user_resp == 'sports':
                dispatcher.utter_message(response = "utter_sport_name")
        
        # print(json_data)
        # temp= json_data['main']['temp']
        
        # dispatcher.utter_message(text=f"The temperature in {city} today is {temp} degrees celcius with {description}")

        return []

class ActionGetSportsNews(Action):

    def name(self) -> Text:
        return "action_sports_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("inside get sports news")
        game_name=tracker.get_slot("game")
        print(game_name)
        dispatcher.utter_message(text=f"You chose {game_name}")

        api_url = 'https://newsapi.org/v2/everything?q=' + game_name + '&apiKey=491c2f82f26045a39a0a164e41557798'
        json_resp = requests.get(api_url).json()
        dispatcher.utter_message("The following are the top 5 headlines for " + game_name +":")
        for i in range(5):
            result = json_resp["articles"][i]["title"]
            dispatcher.utter_message(text=f" {i+1}. {result}")

        return []
