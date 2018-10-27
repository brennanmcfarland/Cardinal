import configparser
from cardinal.weather import weather_info
from cardinal.news import news_headlines

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('api.ini')    # not in the git repo

    owm_api = config.get('API', 'OWM')
    news_api = config.get('API', 'NEWS')

    print(weather_info('Dallas', owm_api))
    print(news_headlines(news_api))

