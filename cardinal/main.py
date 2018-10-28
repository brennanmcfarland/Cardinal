import configparser
import datetime
from cardinal.weather import weather_info
from cardinal.news import news_headlines
from cardinal.wikipedia import get_wikipedia_page_for_topic

config = configparser.ConfigParser()
config.read('api.ini')  # not in the git repo

owm_api = config.get('API', 'OWM')
news_api = config.get('API', 'NEWS')


def get_weather_info(city):
    print(weather_info(city, owm_api))


def get_news_headlines():
    print(news_headlines(news_api))


def get_wikipedia_page(topic):
    print(get_wikipedia_page_for_topic(topic))


def get_local_time():
    now = datetime.datetime.now()
    print(now.strftime("%A, %d of %B, %Y\n"))


if __name__ == '__main__':
    get_weather_info()
    get_news_headlines()
    get_local_time()
    get_wikipedia_page_for_topic('Dallas')
