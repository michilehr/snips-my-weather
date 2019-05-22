import requests
import pprint
import datetime

class OpenWeatherMap:

    def __init__(self, api_key, location_name, date: datetime):
        self.api_url = "https://api.openweathermap.org/data/2.5"
        self.api_key = api_key
        self.location_name = location_name
        self.date = date

    def get_forecast_data(self, requests: requests):
        forecast_url = "{}/forecast?q={}&appid={}&units=metric&lang=de".format(self.api_url, self.location_name, self.api_key)

        # try catch connection error  
        try:
            response = requests.get(forecast_url)
        except:
            raise Exception('connection error')

        if (response.status_code == 401):
            raise Exception('invalid api key')
        
        if (response.status_code == 404):
            raise Exception('location not found')

        response_json = response.json()

        date_formatted = self.date.strftime('%Y-%m-%d')

        data_day = list(filter(lambda forecast: forecast["dt_txt"].startswith(date_formatted), response_json["list"]))

        if (len(data_day) < 1):
            raise Exception('date not found')

        data = {}
        data["location"] = self.__get_location(response_json)
        data["temp_min"] = self.__get_temp_min(data_day)
        data["temp_max"] = self.__get_temp_max(data_day)
        data["condition"] = self.__get_condition(data_day)

        return data

    def __get_temp_min(self, data_day):
        """returns min temperature of day"""

        data_temp_min = [x["main"]["temp_min"] for x in data_day]

        return int(round(min(data_temp_min)-0.5))

    def __get_temp_max(self, data_day):
        """returns max temperature of day"""

        data_temp_max = [x["main"]["temp_max"] for x in data_day]

        return int(round(max(data_temp_max)+0.5))

    def __get_location(self, response):
        """returns location name from response"""

        return response["city"]["name"]

    def __get_condition(self, data_day):
        """
        returns conditions of day as list
        worst condition is first element, best condition is last element
        """
        
        all_conditions = [x["weather"][0] for x in data_day]
        all_conditions_sorted = sorted(all_conditions, key=lambda k: k['id']) 
        unique_conditions = list({k['id']:k for k in all_conditions_sorted}.values())

        unique_conditions_values = [k['description'] for k in unique_conditions]

        return unique_conditions_values
      