from django.db import models
from django.conf import settings

class carrinho(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	desenhos=models.ManyToMany
