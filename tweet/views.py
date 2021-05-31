from django.http import JsonResponse
from django.shortcuts import render

from .models import Tweet
from django.core.exceptions import ObjectDoesNotExist


def home_view(request):
    return render(request, 'tweet/home.html')


def list_view(request, *args, **kwargs):
    try:
        qs = Tweet.objects.all()
        list_of_tweets = [{"pk": x.pk, "content": x.content, "img": x.image.url} for x in qs]
        data = {
            "data": list_of_tweets
        }
        return JsonResponse(data, status=200)
    except:
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
