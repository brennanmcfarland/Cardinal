import sounddevice as sd
import configparser
import numpy as np
from scipy.signal import resample
import requests
import scipy.io.wavfile as wavfile
import io
import json

# TODO: tune the amplitude values

# 0. GET THE AUTHENTICATION KEY
config = configparser.ConfigParser()
config.read('api.ini')
msspeech_api = config.get('API', 'SPEECH')

# 1. GET THE AUDIO
fs=44100
duration = 3  # seconds
channels = 2 # number of channels
amplification = 10 # factor by which the volume is increased

recording = sd.rec(duration * fs, samplerate=fs, channels=channels,dtype='float64')

print("Recording Audio")
sd.wait()

print("Processing Audio")
print(recording.shape)

recording = [sum(r) / len(r) for r in recording]
recording = resample(recording, 16000*duration)
recording = recording * 32767 # *32767 cause we're converting to an int16 range from -1 - +1
recording *= amplification
recording = np.clip(recording, -32768, 32767)
recording = recording.astype('int16')
print("Resampled Audio")
print(recording.shape)
wav = io.BytesIO()
wavfile.write(wav, 16000, recording)

# 2. PUT IT IN A RESTFUL API REQUEST
print("sending REST request...")
msspeechurl = 'https://westus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-us'
headers = { 'Ocp-Apim-Subscription-Key': msspeech_api, 'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000' }
query_params = { 'language': 'en-US'}
response = requests.post(msspeechurl, params=query_params, headers=headers, data=wav)

# INTERPRET THE RESPONSE
print(response.text)
response = json.loads(response.text)
if response['RecognitionStatus'] == 'Success':
    recognized_text = response['DisplayText']
    print(recognized_text)
else:
    print('Did not understand command')