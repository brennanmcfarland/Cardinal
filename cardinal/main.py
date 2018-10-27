import configparser
from cardinal.weather import weather_info

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('api.ini')    # not in the git repo

    owm_api = config.get('API', 'OWM')

    print(weather_info('Dallas', owm_api))
