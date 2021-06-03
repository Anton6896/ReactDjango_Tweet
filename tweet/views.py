import random
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet
from .forms import CreateTweetForm
from django.contrib import messages
from django.shortcuts import redirect


def home_view(request):
    """
    home view that have list of tweets and form for creating new tweet
    list and form handled by js requests
    """
    form = CreateTweetForm()
    return render(request, 'tweet/home.html', {'form': form})


def crete_view(request, *args, **kwargs):
    """
    creating new tweet thru the ajax and js
    """
    form = CreateTweetForm(request.POST or None)

    # get data from hidden field at tweet creation
    # next redirect to home page
    next_url = request.POST.get('next') or None
    if form.is_valid():
        form.save()

        if request.is_ajax():
            return JsonResponse({"msg": 'created'}, status=201)

        if next_url and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)

    # else
    form = CreateTweetForm()

    context = {
        "form": form
    }
    return render(request, 'tweet/create_tweet.html', context)


def list_view(request, *args, **kwargs):
    """
    get qs of all tweets and return as js list object
    or return error message
    """
    try:
        qs = Tweet.objects.all().order_by('-timestamp')
        list_of_tweets = [x.serializer() for x in qs]
        return JsonResponse({"data": list_of_tweets}, status=200)

    except Tweet.DoesNotExist:
        return JsonResponse({"msg": "not found"}, status=404)


def detail_view(request, pk):
    """
    get tweet by pk
    """
    status = None
    data = {
        "pk": pk,
    }

    try:
        tweet_obj = Tweet.objects.get(pk=pk)
        data['content'] = tweet_obj.content
        data['img'] = tweet_obj.image.url
        status = 200

    except Tweet.DoesNotExist:
        data['msg'] = 'not found'
        status = 404

    finally:
        return JsonResponse(data, status=status)
