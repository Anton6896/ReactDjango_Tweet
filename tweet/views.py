import random
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateTweetForm
from django.contrib import messages
from django.shortcuts import redirect


def home_view(request):
    form = CreateTweetForm()
    return render(request, 'tweet/home.html', {'form': form})


def crete_view(request, *args, **kwargs):
    form = CreateTweetForm(request.POST or None)

    # get data from hidden field at tweet creation
    # next redirect to home page
    next_url = request.POST.get('next') or None
    if form.is_valid():
        form.save()
        if next_url and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            messages.success(request, f'tweet created')
            return redirect(next_url)

    # else
    form = CreateTweetForm()

    context = {
        "form": form
    }
    return render(request, 'tweet/create_tweet.html', context)


# return list of js objects with all tweet data
def list_view(request, *args, **kwargs):
    try:
        qs = Tweet.objects.all().order_by('-timestamp')
        list_of_tweets = [{"pk": x.pk,
                           "content": x.content,
                           "img": x.image.url,
                           "like": random.randint(2, 100)} for x in qs]
        data = {
            "data": list_of_tweets
        }
        return JsonResponse(data, status=200)

    except Tweet.DoesNotExist:
        return JsonResponse({"msg": "not found"}, status=404)


def detail_view(request, pk):
    status = None
    data = {
        "pk": pk,
    }

    try:
        tweet_obj = Tweet.objects.get(pk=pk)
        data['content'] = tweet_obj.content
        data['img'] = tweet_obj.image.url
        status = 200

    except ObjectDoesNotExist:
        data['msg'] = 'not found'
        status = 404

    finally:
        return JsonResponse(data, status=status)
