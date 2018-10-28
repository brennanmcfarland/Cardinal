# Cardinal

## Cardinal is a Digital Assistant and Accessibility Tool written in Python. It is also the (cute) state bird of Ohio:
![Cardinal](https://d1ia71hq4oe7pn.cloudfront.net/photo/63667311-720px.jpg)

Cardinal receives user input via the device's microphone, and transforms the _speech to text_ using the __Microsoft Azure 
Cognitive Services Platform__. Cardinal can detect the intent of a message - the service being requested - 
and the entity to perform the service upon where relevant.

After the service code is executed, the text output is then sent back to the Cognitive Services Platform to request a 
_text to speech_ result from the Azure. Cardinal downloads the response .mp3 and plays back the audio.

Cardinal has four primary features as a digital assistant:

* Getting the time

* Getting current news headlines from Google News

* Getting the weather in a city
    * This will also open a web page to display more info than is spoken by the problem.

* Opening a requested Wikipedia page in a new browser


Here are some example commands:

Getting the time:
```
python main.py

...

'Recording audio'
User speaks: 'What is the time?'

...

The time is 04:07 AM, on Sunday, 28 of October, 2018 
```

Getting the news headlines:
```
User speaks: 'What's the news, baby?'

...

Here are the current news headlines.
 -Holt: Sale's rally cries 'lit a fire' under Red Sox
 -2 winners will split the $687 million Powerball jackpot
 -A look inside the journey of the US-bound caravan migrants
 -Here's what we know so far about Robert Bowers, the Pittsburgh synagogue shooting suspect
 -Leicester City owner's helicopter crashes after EPL match; report says he was on board
Headlines powered by News API
```

Getting the weather conditions of a city:
```
User speaks: 'How cold is it in Dallas?'

...

The weather in dallas is Clear, with a temperature of 60.5 F

<the webpage for weather in Dallas would be opened in the default browser>
```

Searching Wikipedia for Nelson Mandela:
```
User speaks: 'Search Wikipedia for Nelson Mandela?'

...

<the wikipedia webpage for Nelson Mandela would be opened in the default browser>
```


This project was developed by Brennan McFarland and Emilio Lopez for HackOHI/O 2018.  