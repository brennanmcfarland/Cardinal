import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
import urllib.request as urllib

WIKI_URL = 'https://en.wikipedia.org/w/api.php'


def __wikipedia_page_exists(topic):

    params = {
        'action': "query",
        'list': "search",
        'srsearch': topic,
        'format': "json"
    }

    response = requests.get(WIKI_URL, params)

    if response.status_code != 200:
        print("error, exiting")
        return False

    response = response.json()

    try:
        if response['query']['search'][0]['title'].lower() in topic:
            return True
    except IndexError:
        return False



def __get_wikipedia_page_url(topic):

    # topic = topic[:-2]
    if __wikipedia_page_exists(topic):
        # /w/api.php?action=parse&format=json&page=Pet_door
        response = requests.get(WIKI_URL + '?action=parse&format=json&page=' + topic).json()

        return 'http://en.wikipedia.org/?curid=' + str(response['parse']['pageid'])
    else:
        print(topic + ' not found')
        sys.exit(1)


def __open_wikipedia_url(full_url):
    webbrowser.open_new(full_url)


def get_wikipedia_page_for_topic(topic):
    wikipedia_url = __get_wikipedia_page_url(topic)
    __open_wikipedia_url(wikipedia_url)
    return get_wikipedia_page_blurb(wikipedia_url)


def get_wikipedia_page_blurb(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    blurb = soup.find('div', class_='mw-parser-output').p.find_next("p").get_text()
    blurb = blurb.split('.')[0]
    return blurb


if __name__ == '__main__':
    get_wikipedia_page_for_topic('green. ')
