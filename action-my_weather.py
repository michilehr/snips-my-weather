#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
from src.MyWeather import MyWeather
import io

CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Template(object):

    def __init__(self):
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        self.start_blocking()

    def getMyWeatherForecast(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "")

        print('[Received] intent: {}'.format(intent_message.intent.intent_name))
        
        my_weather = MyWeather(self.config)

        ret = my_weather.get_my_weather_forecast(intent_message)

        hermes.publish_start_session_notification(intent_message.site_id, ret)

    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'getMyWeatherForecast':
            self.getMyWeatherForecast(hermes, intent_message)

    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Template()
