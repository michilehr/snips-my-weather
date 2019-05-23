# Snips-Mein Wetter 🌤

This app is a skill for the the private-by-design self-hosted voice assistant Snips.ai](https://snips.ai/).

The skill uses the [OpenWeatherMap](https://openweathermap.org/) as data provider to say the current weather or weather forecast for a passed location. 

The skill currently supports following languages:
 - german

## Requirements

 - a configured [Snips.ai](https://snips.ai/) device ([Getting started](https://docs.snips.ai/getting-started))
 - an [OpenWeatherMap](https://openweathermap.org/) API key ([free for up to 60 calls / minute](https://openweathermap.org/price))

## Installation

1. In the german [app store](https://console.snips.ai/) add the app [Mein Wetter](https://console.snips.ai/store/de/skill_40MMMVlkDqV) to your assistant.

2. In the console execute the following command:
    ```bash
    sam install assistant
    ```
    You will be asked to enter two values:
    - `openweathermap_api_key`
    - `default_location`
        This is the default location which is used when you do not pass a location by speech
        

## Usage
At the moment you can ask for the current weather or a weather forecast for your default or a given location.

### Example sentences
- *Wie wird das Wetter am Donnerstag*
- *Wetter am Donnerstag*
- *Wettervorhersage für Neckarsulm am Samstag*

### Example responses
- *Wetter heute in Heilbronn: Klarer Himmel bis Starker Regen mit Temperaturen von 10 Grad.*
- *Wetter heute in Neckarsulm: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.*
- *Wetter morgen in Heilbronn: Klarer Himmel mit Temperaturen von 10 bis 20 Grad.*
- *Wetter morgen in Heilbronn: Klarer Himmel mit Temperaturen von 20 Grad.*

## Development

The app already has lots of unit tests which can be run by `./run_tests.py`
Feel free to fork and open up pull requests.
