import requests
import sys
import webbrowser

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

    topic = topic[:-2]
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
    __open_wikipedia_url(__get_wikipedia_page_url(topic))
