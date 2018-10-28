import configparser
import datetime
import sys
from cardinal.weather import weather_info
from cardinal.news import news_headlines
from cardinal.wikipedia import get_wikipedia_page_for_topic
from cardinal.speech import get_command
from cardinal.intent import get_intent_from_text
from cardinal.voice import text_to_speech

config = configparser.ConfigParser()
config.read('api.ini')  # not in the git repo

owm_api = config.get('API', 'OWM')
news_api = config.get('API', 'NEWS')
tts_api = config.get('API', 'SPEECH')


def get_weather_info(city):
    return weather_info(city, owm_api)


def get_news_headlines():
    return news_headlines(news_api)


def get_wikipedia_page(topic):
    return get_wikipedia_page_for_topic(topic)


def get_local_time():
    now = datetime.datetime.now()
    return now.strftime("%A, %d of %B, %Y\n")


if __name__ == '__main__':
    command_text = get_command()
    intent_json = get_intent_from_text(command_text)
    intent = intent_json['topScoringIntent']['intent']

    output = ''
    if intent == 'weather':
        output = get_weather_info(intent_json['entities'][0]['entity'])
    elif intent == 'wikipedia':
        output = get_wikipedia_page(intent_json['entities'][0]['entity'])
    elif intent == 'time':
        output = get_local_time()
    elif intent == 'news':
        output = get_news_headlines()
    else:
        print('Unknown intent, exiting')
        sys.exit(1)

    text_to_speech(output, tts_api)
