import requests

NEWS_URL = 'https://newsapi.org/v2/top-headlines'


def __get_headlines(news_api):
    country = '?country=us'
    url = NEWS_URL + country + '&apiKey=' + news_api
    return requests.get(url).json()


def __parse_titles(response, number=5):
    titles = []
    articles = response['articles']

    collected_headlines = 0
    for article in articles:
        if collected_headlines < number:
            titles.append(article['title'])
            collected_headlines += 1
        else:
            break

    return titles


def news_headlines(news_api):
    headlines = __parse_titles(__get_headlines(news_api))

    output = "Here are the current news headlines.\n"
    for headline in headlines:
        output += (' -' + headline + '\n')

    return output + 'Headlines powered by News API\n'

