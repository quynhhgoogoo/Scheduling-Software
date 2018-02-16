# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Idol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
	
    def __str__(self):
        return self.id

class Tvshow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
		return self.id


