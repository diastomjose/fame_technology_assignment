# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class roomsModel(models.Model):
	room_no = models.IntegerField()
	room_cost= models.CharField(max_length=100)
	room_status= models.CharField(max_length=100)


class bookingModel(models.Model):
	room_no = models.IntegerField()
	booker_name = models.CharField(max_length=100)
	