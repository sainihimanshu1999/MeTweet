"""metweet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tweets.views import (
    local_tweets_list_view,
    local_tweets_detail_view,
    local_tweets_profile_view,
)
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', local_tweets_list_view),
    path('<int:tweet_id>', local_tweets_detail_view),
    path('profile/<str:username>', local_tweets_profile_view),
    path('api/tweets/', include('tweets.urls')),
    #old ways of using url just in django
    # path('react/', TemplateView.as_view(template_name='react.html')),
    # path('create-tweet/', tweet_create_view),
    # path('tweets/', tweet_list_view),
    # path('tweets/<int:tweet_id>', tweet_detail_view),
    # path('api/tweets/<int:tweet_id>/delete', tweet_delete_view),
    # path('api/tweets/action', tweet_action_view),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)