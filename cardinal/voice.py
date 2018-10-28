import requests
import vlc
import configparser
from mutagen.mp3 import MP3
import time


config = configparser.ConfigParser()
config.read('api.ini')
msspeech_api = config.get('API', 'SPEECH')


TOKEN_URL = 'https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
WEB_URL = 'https://westus.tts.speech.microsoft.com/cognitiveservices/v1'


def __get_token(speech_api):
    headers = {
        "Ocp-Apim-Subscription-Key": speech_api,
        "Content-type": 'application/x-www-form-urlencoded'
        "Content-Length: 0"
    }

    return requests.post(TOKEN_URL, data='', headers=headers).text


def __send_output_text(text, token):
    headers = {
        "Content-Type": 'application/ssml+xml',
        "X-Microsoft-OutputFormat": 'audio-16khz-32kbitrate-mono-mp3',
        "User-Agent": 'Cardinal Digital Assitant',
        "Authorization": token
    }

    first_xml_line = "<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Female' "
    second_xml_line = "name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>"
    third_xml_line = text
    fourth_xml_line = "</voice></speak>"

    xml = (first_xml_line + second_xml_line + third_xml_line + fourth_xml_line)

    return requests.post(WEB_URL, data=xml.encode('utf-8'), headers=headers)


def __save_audio_file(response):
    local_filename = './voice.mp3'
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    return local_filename


def text_to_speech(text, api_key):
    filename = __save_audio_file(__send_output_text(text, __get_token(api_key)))
    audio = MP3(filename)
    player = vlc.MediaPlayer(filename)
    player.play()
    time.sleep(audio.info.length)


if __name__ == '__main__':
    text_to_speech("This is a test of the text to speech", msspeech_api)
