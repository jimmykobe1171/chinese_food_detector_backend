# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Food(models.Model):
    result = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food_images/')