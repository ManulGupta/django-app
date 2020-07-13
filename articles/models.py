# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=100)
	category=models.CharField(max_length=50,default='Life')
	slug=models.SlugField()
	story=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	thumb=models.ImageField(default='default.png',blank=True)
	author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	#thumbnail
	#author
	def __str__(self):
		return self.title

	def snippet(self):
		return self.story[0:50]+"..."
