import requests
import datetime
import locale
import calendar

class TextGenerator:

    def __init__(self):
        self.data = []
        locale.setlocale(locale.LC_ALL, 'de_DE')

    def get_forecast(self, data, date_today: datetime, date_requested: datetime):

        condition_text = self.__getConditonText(data)
        temperature_text = self.__getTemperatuerText(data)
        day_text = self.__getDayText(date_today, date_requested)
        location = data["location"]

        return "Wetter {} in {}: {} mit Temperaturen von {}.".format(day_text, location, condition_text, temperature_text)

    def __getConditonText(self, data):

        conditions = data["condition"]

        if(len(conditions) > 1):
            best_condition = conditions[0]
            worst_condition = conditions[len(conditions) - 1]
            return "{} bis {}".format(best_condition, worst_condition)
        else:
            return conditions[0]

    def __getTemperatuerText(self, data):

        temp_min = data["temp_min"]
        temp_max = data["temp_max"]

        if(temp_min != temp_max):
            return "{} bis {} Grad".format(temp_min, temp_max)
        else:
            return "{} Grad".format(temp_min)

    def __getDayText(self, date_today: datetime, date_requested: datetime):
        
        date_requested = date_requested.replace(hour=0, minute=0, second=0, microsecond=0)
        date_today = date_today.replace(hour=0, minute=0, second=0, microsecond=0)

        diff_in_days = (date_requested - date_today).days    

        if (diff_in_days <= 0):
            return "heute"
        elif (diff_in_days == 1):
            return "morgen"
        else:
            weekday_name = calendar.day_name[date_requested.weekday()]
            return "am {}".format(weekday_name)

    def get_location_not_found(self):
        return "Der angegebene Ort konnte nicht gefunden werden."

    def get_api_key_invalid(self):
        return "Der API Schlüssel ist ungültig."

    def get_date_not_found(self):
        return "Es liegen keine Wetterdaten zum angegebenen Datum vor."

    def get_connection_error(self):
        return "Es ist ein Verbindungsfehler aufgetreten."

    def get_unknown_error(self):
        return "Es ist ein unbekannter Fehler."