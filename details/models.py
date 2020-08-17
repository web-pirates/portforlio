from django.db import models
from datetime import datetime

class Inquery(models.Model):
	name = models.CharField(max_length=100, blank=False)
	email = models.EmailField(max_length=100, blank=False)
	subject = models.CharField(max_length=120, blank=False)
	message = models.TextField(blank=False)
	created_at = models.DateTimeField(auto_now_add=True)

class News(models.Model):
	EMAIL = models.EmailField(max_length=200, blank=False)

