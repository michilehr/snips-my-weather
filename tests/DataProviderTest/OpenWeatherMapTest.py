from src.DataProvider.OpenWeatherMap import OpenWeatherMap
import unittest
import requests
from mock import MagicMock
from mock import PropertyMock
from mock import Mock
import json
import datetime

class DataProviderOpenWeatherMapTest(unittest.TestCase):
    def setUp(self):
       pass

    def test_constructor_properties_assigned(self):
        api_key = "ABCDEF"
        location_name = "Heilbronn"
        date = datetime.datetime(2019, 1, 1)

        data_provider = OpenWeatherMap(api_key, location_name, date)

        self.assertEqual(api_key, data_provider.api_key)
        self.assertEqual(location_name, data_provider.location_name)
        self.assertEqual(date, data_provider.date)

    def test_request_wrong_api_key(self):
        api_key = "ABCDEF"
        location_name = "Heilbronn"
        date = datetime.datetime(2019, 5, 19)

        data_provider = OpenWeatherMap(api_key, location_name, date)

        try:
            data_provider.get_forecast_data(self._get_mock_request(401, "{}"))
        except Exception as e:
            self.assertEqual(str(e), "invalid api key")

    def test_request_unknown_city(self):
        api_key = "ABCDEF"
        location_name = "ABCDEF"
        date = datetime.datetime(2019, 5, 19)

        data_provider = OpenWeatherMap(api_key, location_name, date)

        try:
            data_provider.get_forecast_data(self._get_mock_request(404, "{}"))
        except Exception as e:
            self.assertEqual(str(e), "location not found")


    def test_request_connection_error(self):
        api_key = "ABCDEF"
        location_name = "ABCDEF"
        date = datetime.datetime(2019, 5, 19)

        data_provider = OpenWeatherMap(api_key, location_name, date)


        request_mock = MagicMock()
        request_mock.get.side_effect = Exception('Boom!')

        try:
            data_provider.get_forecast_data(request_mock)
        except Exception as e:
            self.assertEqual(str(e), "connection error")

    def test_request_success_day_found(self):
        api_key = "ABCDEF"
        location_name = "ABCDEF"
        date = datetime.datetime(2019, 5, 19)

        data_provider = OpenWeatherMap(api_key, location_name, date)

        f = open("tests/DataProviderTest/response_ok.txt", "r")

        data = data_provider.get_forecast_data(self._get_mock_request(200, json.loads(f.read())))

        self.assertEqual("Heilbronn", data["location"])
        self.assertEqual(10, data["temp_min"])
        self.assertEqual(22, data["temp_max"])
        self.assertEqual("Leichter Regen", data["condition"][0])
        self.assertEqual("Mäßiger Regen", data["condition"][1])

    def test_request_success_day_not_found(self):
        api_key = "ABCDEF"
        location_name = "ABCDEF"
        date = datetime.datetime(2019, 5, 31)

        data_provider = OpenWeatherMap(api_key, location_name, date)

        f = open("tests/DataProviderTest/response_ok.txt", "r")

        try:
            data_provider.get_forecast_data(self._get_mock_request(200, json.loads(f.read())))
        except Exception as e:
            self.assertEqual(str(e), "date not found")


    def _get_mock_request(self, status_code, return_value):
        response_mock = MagicMock()
        type(response_mock).status_code = PropertyMock(return_value=status_code)
        response_mock.json.return_value = return_value

        request_mock = MagicMock()
        request_mock.get.return_value = response_mock

        return request_mock