import requests
from src.DataProvider.OpenWeatherMap import OpenWeatherMap
from src.TextGenerator import TextGenerator
import datetime
from hermes_python.ontology.dialogue import IntentMessage
from snipsTools import SnipsConfigParser

class MyWeather:

    def __init__(self, config: SnipsConfigParser):
        try:
            self.api_key = config["secret"]["openweathermap_api_key"]
        except KeyError:
            self.api_key = "ABCDEFG"

        try:
            self.default_location = config["secret"]["default_location"]
        except KeyError:
            self.default_location = "New York"

    def get_my_weather_forecast(self, intentMessage: IntentMessage):

        date_requested = self.__get_date(intentMessage.slots)
        location_requested = self.__get_location(intentMessage.slots)
        text_generator = TextGenerator()

        data_provider = OpenWeatherMap(self.api_key, location_requested, date_requested)

        try:
            data = data_provider.get_forecast_data(requests)
        except Exception as e:

            error_messages = {
                'date not found': text_generator.get_date_not_found(), 
                'location not found': text_generator.get_location_not_found(),
                'invalid api key': text_generator.get_api_key_invalid(),
                'connection error': text_generator.get_connection_error()
                }
            error_message = error_messages.get(str(e), text_generator.get_unknown_error())

            return error_message

        date_today = datetime.datetime.today()

        return text_generator.get_forecast(data, date_today, date_requested)

    def __get_date(self, slots):
        if slots.forecast_date_time.first():
            date_requested_value = slots.forecast_date_time.first().value
            date_requested = datetime.datetime.strptime(date_requested_value[:-7], '%Y-%m-%d %H:%M:%S')
        else:
            date_requested = datetime.datetime.today()
        
        return date_requested

    def __get_location(self, slots):
        if slots.forecast_location.first():
            location = slots.forecast_location.first().value
        else:
            location = self.default_location
        
        return location