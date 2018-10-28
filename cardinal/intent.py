import configparser
import requests

config = configparser.ConfigParser()
config.read('api.ini')
msspeech_api = config.get('API', 'SPEECH')
luis_api = config.get('API', 'INTENT')
luisurl = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/df67dcdb-c37d-46af-88e1-8b97951ca1c2'
headers = { 'Ocp-Apim-Subscription-Key': luis_api}


def get_intent_from_text(recognized_text):
    query_params = {
        'q': recognized_text,
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false' }
    response = requests.get(luisurl, headers=headers, params=query_params)
    print(response.text)


if __name__ == '__main__':
    get_intent_from_text("Turn off the lights")