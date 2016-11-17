from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
	trainer = 'trainer'
	dietitian = 'dietitian'
	both = 'both'
	none = 'none'


	service_choices = (
		(trainer, trainer),
		(dietitian, dietitian),
		(both, both),
		(none, none),
		)

	service = models.CharField(
		max_length=30,
		choices=service_choices,
		default=none,
		)

	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	#profileppic = models.ImageField(upload_to="profile_pics")

	def __str__(self):
		return self.firstname
