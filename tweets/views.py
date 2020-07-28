import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello Himanshu, Welcome back again</h1>')
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{'id': x.id, 'content': x.content,
                   "likes": random.randint(0, 122)} for x in qs]
    data = {
        'isUser': False,
        'response': tweet_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API VIEW
    return json data
    to use javascript to show these views
    '''

    data = {
        'id': tweet_id,

    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404

    return JsonResponse(data, status=status)
