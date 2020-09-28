from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from .forms import TweetForm
from .models import Tweet
from rest_framework.response import Response
import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello Himanshu, Welcome back again</h1>')
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'pages/home.html', context={'username' :username}, status=200)


def tweets_list_view(request, *args, **kwargs):
    return render(request, 'tweets/list.html')


def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, 'tweets/detail.html', context={'tweet_id' :tweet_id})


# def tweets_profile_view(request,username, *args, **kwargs):
#     return render(request, 'tweets/profile.html', context={'profile_username' :username}, status=200)
#
#
# def tweet_create_view_pure_django(request, *args, **kwargs):
#     user = request.user
#     if not request.user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)
#     form = TweetForm(request.POST or None)
#     next_url = request.POST.get('next') or None
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = user
#         obj.save()
#         if request.is_ajax():
#             # 201 == created items
#             return JsonResponse(obj.serialize(), status=201)

#         if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
#             return redirect(next_url)
#         form = TweetForm()
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#     return render(request, 'components/form.html', context={'form': form})


# def tweet_list_view_pure_django(request, *args, **kwargs):
#     qs = Tweet.objects.all()
#     tweet_list = [x.serialize() for x in qs]
#     data = {
#         'isUser': False,
#         'response': tweet_list
#     }
#     return JsonResponse(data)


# def tweet_detail_view_pure_django(request, tweet_id, *args, **kwargs):
#     '''
#     REST API VIEW
#     return json data
#     to use javascript to show these views
#     '''

#     data = {
#         'id': tweet_id,

#     }
#     status = 200
#     try:
#         obj = Tweet.objects.get(id=tweet_id)
#         data['content'] = obj.content
#     except:
#         data['message'] = 'Not Found'
#         status = 404

#     return JsonResponse(data, status=status)
