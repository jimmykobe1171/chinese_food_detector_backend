# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from .models import Food

# Create your views here.

@csrf_exempt
def upload_food_image_view(request):
    if request.method == 'POST':
        image = request.FILES.get('file')
        if image:
            # create new food
            try:
                food = Food(image=image)
                food.save()
            except Exception as e:
                print e
                return HttpResponseServerError()

            data = {
                'id': food.id,
                'image': food.image.url
            }
            return JsonResponse(data)
        else:
            return HttpResponseBadRequest()
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