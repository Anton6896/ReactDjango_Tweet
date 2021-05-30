from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.core.exceptions import ObjectDoesNotExist


def home_view(request):
    data = {
        'msg': 'hello'
    }
    return JsonResponse(data)


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
