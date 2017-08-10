from django.db import models

class Estimate(models.Model):
	title = models.CharField(max_length=40)
	customer = models.CharField(max_length=40)
	price = models.IntegerField(default=0)
	date = models.DateField(auto_now_add=True)