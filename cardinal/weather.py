import requests

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather_in_city(city, owm_api):
    city_string = '?q=' + city
    app_id = 'APPID=' + owm_api
    request_url = WEATHER_URL + city_string + '&' + app_id

    return requests.get(request_url).text
