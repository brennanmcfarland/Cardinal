import configparser
from cardinal.weather import get_weather_in_city

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('api.ini')    # not in the git repo

    owm_api = config.get('API', 'OWM')

    print(get_weather_in_city('London', owm_api))
