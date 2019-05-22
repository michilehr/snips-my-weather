import unittest
import datetime
from src.TextGenerator import TextGenerator

class TextGeneratorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_weather_forecast_different_temperatures(self):

        data = {}
        data["location"] = "Heilbronn"
        data["temp_min"] = "10"
        data["temp_max"] = "20"
        data["condition"] = ["Klarer Himmel"]

        text_generator = TextGenerator()

        date_today = datetime.datetime(2019, 5, 17)
        date_requested = datetime.datetime(2019, 5, 17)

        self.assertEqual(
            "Wetter heute in Heilbronn: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def testweather_forecast_different_conditions(self):

        data = {}
        data["location"] = "Heilbronn"
        data["temp_min"] = "10"
        data["temp_max"] = "10"
        data["condition"] = ["Klarer Himmel", "Starker Regen"]

        text_generator = TextGenerator()

        date_today = datetime.datetime(2019, 5, 17)
        date_requested = datetime.datetime(2019, 5, 17)

        self.assertEqual(
            "Wetter heute in Heilbronn: Klarer Himmel bis Starker Regen mit Temperaturen von 10 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def test_weather_forecast_different_temperatures_and_different_conditions(self):

        data = {}
        data["location"] = "Neckarsulm"
        data["temp_min"] = "10"
        data["temp_max"] = "20"
        data["condition"] = ["Klarer Himmel", "Starker Regen"]

        date_today = datetime.datetime(2019, 5, 17)
        date_requested = datetime.datetime(2019, 5, 17)

        text_generator = TextGenerator()

        self.assertEqual(
            "Wetter heute in Neckarsulm: Klarer Himmel bis Starker Regen mit Temperaturen von 10 bis 20 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def test_weather_forecast_for_today(self):

        data = {}
        data["location"] = "Neckarsulm"
        data["temp_min"] = "10"
        data["temp_max"] = "20"
        data["condition"] = ["Klarer Himmel"]

        date_today = datetime.datetime(2019, 5, 17)
        date_requested = datetime.datetime(2019, 5, 17)

        text_generator = TextGenerator()

        self.assertEqual(
            "Wetter heute in Neckarsulm: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def test_weather_forecast_for_tomorrow(self):

        data = {}
        data["location"] = "Heilbronn"
        data["temp_min"] = "10"
        data["temp_max"] = "20"
        data["condition"] = ["Klarer Himmel"]

        date_today = datetime.datetime(2019, 5, 17, 10, 10, 10, 10)
        date_requested = datetime.datetime(2019, 5, 18, 5, 5, 5, 5)

        text_generator = TextGenerator()

        self.assertEqual(
            "Wetter morgen in Heilbronn: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def test_weather_forecast_for_sunday(self):

        data = {}
        data["location"] = "Heilbronn"
        data["temp_min"] = "10"
        data["temp_max"] = "20"
        data["condition"] = ["Klarer Himmel"]

        date_today = datetime.datetime(2019, 5, 17)
        date_requested = datetime.datetime(2019, 5, 19)

        text_generator = TextGenerator()

        self.assertEqual(
            "Wetter am Sonntag in Heilbronn: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def test_weather_forecast_for_monday(self):

        data = {}
        data["location"] = "Heilbronn"
        data["temp_min"] = "10"
        data["temp_max"] = "20"
        data["condition"] = ["Klarer Himmel"]

        date_today = datetime.datetime(2019, 5, 17)
        date_requested = datetime.datetime(2019, 5, 20)

        text_generator = TextGenerator()

        self.assertEqual(
            "Wetter am Montag in Heilbronn: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.", 
            text_generator.get_forecast(data, date_today, date_requested)
            )

    def test_location_not_found(self):

        text_generator = TextGenerator()

        self.assertEqual(
            "Der angegebene Ort konnte nicht gefunden werden.", 
            text_generator.get_location_not_found()
            )

    def test_api_key_invalid(self):

        text_generator = TextGenerator()

        self.assertEqual(
            "Der API Schlüssel ist ungültig.", 
            text_generator.get_api_key_invalid()
            )

    def test_date_not_found(self):

        text_generator = TextGenerator()

        self.assertEqual(
            "Es liegen keine Wetterdaten zum angegebenen Datum vor.", 
            text_generator.get_date_not_found()
            )

    def test_connection_error(self):

        text_generator = TextGenerator()

        self.assertEqual(
            "Es ist ein Verbindungsfehler aufgetreten.", 
            text_generator.get_connection_error()
            )