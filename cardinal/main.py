import configparser
import datetime
from cardinal.weather import weather_info
from cardinal.news import news_headlines
from cardinal.wikipedia import get_wikipedia_page_for_topic
from cardinal.speech import get_command
from cardinal.intent import get_intent_from_text

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
    command_text = get_command()
    intent_json = get_intent_from_text(command_text)

    # intent json looks like this:
    #   'query': execute order 66
    #   'topScoringIntent': {
    #       'intent':'str'
    #       'score':float
    #    }
    #   entities: []



    # get_weather_info()
    # get_news_headlines()
    # get_local_time()
