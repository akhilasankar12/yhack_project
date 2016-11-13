from __future__ import unicode_literals

from django.db import models

class Login(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=100)

class User(models.Model):
	first_name = models.CharField(max_length=50, default='firstname')
	last_name = models.CharField(max_length=50, default='lastname')
	GENDER = (
		("M", 'Male'),
		("F", 'Female'))
	gender = models.CharField(
		max_length=1,
		choices=GENDER,
		default="M",
		)
	age = models.IntegerField(default=1)
	vegetarian = models.BooleanField(default=True)


class Meals(models.Model):
	item_id = models.CharField(max_length=50)
	brand_id = models.CharField(max_length=50)
	brand_name = models.CharField(max_length=37)
	item_name = models.CharField(max_length=80)
	price = models.FloatField()
	category = models.CharField(max_length=7)
	item_description=models.TextField()
	calories = models.FloatField()


	def _str_(self):
		return unicode(self).encode('utf-8')