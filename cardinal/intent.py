import configparser
import requests

config = configparser.ConfigParser()
config.read('api.ini')
msspeech_api = config.get('API', 'SPEECH')
luis_api = config.get('API', 'INTENT')
luis_utterances = config.get('API', 'UTTERANCES')
luisurl = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/' + luis_utterances
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
    return response.json()


if __name__ == '__main__':
    get_intent_from_text("go to New York today")
