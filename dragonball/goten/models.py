from django.db import models

# Create your models here.

class goku(models.Model):
	name 	 = models.CharField(max_length=64)
	number	 = models.CharField(max_length=64)
	location = models.CharField(max_length=64)