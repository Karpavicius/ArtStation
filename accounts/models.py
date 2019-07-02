from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	cpf = models.CharField(max_length=16)
	def __str__(self):
		return '{} - {} '.format(self.username, self.email)