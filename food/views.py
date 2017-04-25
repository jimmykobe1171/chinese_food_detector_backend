# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Food

# Create your views here.

def upload_food_image_view(request):
    data = [
        {'foo':'bar'},
        {'foo':'bar'},
        {'foo':'bar'}
    ]
    if request.method == 'POST':
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseNotAllowed(['POST'])


def foods_view(request):
    foods = Food.objects.all()
    data = []
    for food in foods:
        data.append({
            'id': food.id,
            'image': food.image.url
            })
    if request.method == 'GET':
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseNotAllowed(['GET'])