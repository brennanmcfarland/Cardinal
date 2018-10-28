import requests
import decimal
import webbrowser

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
decimal.getcontext().rounding = decimal.ROUND_DOWN


def __get_weather_request(city, owm_api):
    city_string = '?q=' + city
    app_id = 'APPID=' + owm_api
    request_url = WEATHER_URL + city_string + '&' + app_id

    return requests.get(request_url).json()


def __parse_fields(response):
    relevant_field_dict = dict(conditions=response['weather'][0]['main'],
                               temperature=__convert_kelvin_fahrenheit(response['main']['temp']),
                               id=response['id'])
    return relevant_field_dict


def __convert_kelvin_fahrenheit(kelvin_temp):
    kelvin_temp = int(kelvin_temp)
    fahrenheit_temp = round(decimal.Decimal((kelvin_temp - 273.15) * (9 / 5) + 32), 1)
    return str(fahrenheit_temp)


def __get_weather_in_city(city, owm_api):
    return __parse_fields(__get_weather_request(city, owm_api))


def __open_weather_page(city_id):
    url = 'https://openweathermap.org/city/' + str(city_id)
    webbrowser.open_new(url)


def weather_info(city, owm_api):
    weather_info_dict = __get_weather_in_city(city, owm_api)

    __open_weather_page(weather_info_dict['id'])
    return (f"The weather in {city} is {weather_info_dict['conditions']}, "
            f"with a temperature of {weather_info_dict['temperature']} F\n")

