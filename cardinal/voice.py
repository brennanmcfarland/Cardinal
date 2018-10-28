import io
import subprocess

import requests
<<<<<<< HEAD
import soundfile as sf
import sounddevice as sd
import configparser
import wave
import scipy.io.wavfile as wavfile
import pyaudio
import simpleaudio as sa
from pydub import AudioSegment
import numpy as np
from scipy.signal import resample
=======
import vlc
import configparser
from mutagen.mp3 import MP3
import time
>>>>>>> audio-output


config = configparser.ConfigParser()
config.read('api.ini')
msspeech_api = config.get('API', 'SPEECH')
<<<<<<< HEAD
=======

>>>>>>> audio-output

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

    return requests.post(WEB_URL, data=xml, headers=headers).text


def __save_audio_file(response):
    local_filename = './voice.mp3'
    print(response)
    recording = np.array(bytearray(response, encoding='UTF-8'))
    newrecording = []
    for i in range(0, len(recording), 2):
        newrecording.append(int((recording[i] * 256) + recording[i+1]))
    newrecording = np.array(newrecording, dtype='int16')
    # convert from 16000 to 44100 Hz
    print(44100 * len(newrecording) / 16000)
    recording = resample(newrecording, int(44100 * len(newrecording) / 16000))
    sd.play(newrecording, 44100)
    sd.wait()


def text_to_speech(text, api_key):
<<<<<<< HEAD
    __save_audio_file(__send_output_text(text, __get_token(api_key)))


if __name__ == '__main__':
    text_to_speech("This is a test of the text to speech", msspeech_api)
=======
    filename = __save_audio_file(__send_output_text(text, __get_token(api_key)))
    audio = MP3(filename)
    player = vlc.MediaPlayer(filename)
    player.play()
    time.sleep(audio.info.length)


if __name__ == '__main__':
    text_to_speech("This is a test", msspeech_api)
>>>>>>> audio-output
