from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import News
from aylienapiclient import textapi
# Create your views here.

client = textapi.Client("b94c4409", "344364c0cb2eae76d7f4337c8b996ef3")


def news(request):
    data_old = list(News.objects.values_list('id', flat=True))
    data_new = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()
    items = list((set(data_new) - set(data_old)))

    if len(items) > 0:
        news_list = []
        for item in items:
            urlgetbyid = 'https://hacker-news.firebaseio.com/v0/item/' + str(item) + '.json?print=pretty'
            story = requests.get(urlgetbyid).json()
            sentiment = client.Sentiment({'text': story.get('title', '')})
            news_obj = News(id=story['id'], title=story.get('title', ''), url=story.get('url', ''),
                        score=story.get('score', ''), username=story.get('by', ''),
                        sentiment=sentiment['polarity'], sentiment_confidence=sentiment['polarity_confidence'])
            news_list.append(news_obj)
        News.objects.bulk_create(news_list)

    news = News.objects.all()
    return render(request, 'newsapp/index.html', {'news': news})


def search(request):
    query = request.GET.get('query')
    if query != '':
        news = News.objects.filter(title__search=query)
        return render(request, 'newsapp/index.html', {'news':news, 'query':query})
    return redirect('news')
