import configparser
from cardinal.weather import weather_info
from cardinal.news import news_headlines

config = configparser.ConfigParser()
config.read('api.ini')  # not in the git repo

owm_api = config.get('API', 'OWM')
news_api = config.get('API', 'NEWS')


def get_weather_info():
    print(weather_info('Dallas', owm_api))


def get_news_headlines():
    print(news_headlines(news_api))


if __name__ == '__main__':
    get_weather_info()
    get_news_headlines()
