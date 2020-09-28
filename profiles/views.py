from django.shortcuts import render 
from django.http import Http404
from .models import Profile
from django.db.models.signals import post_save

def profile_detail_view(request, username, *args, **kwargs):
    # get the profile for the passed username
    qs = Profile.objects.filter(user__username = username)
    if not qs.exists():
        raise Http404
    profile_obj = qs.first()
    context = {
        'username':username,
        'profile': profile_obj
    }
    return render(request, "profiles/detail.html", context)





