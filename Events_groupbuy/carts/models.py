from django.contrib.auth.models import User
from django.db import models
from events.models import Events
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	products 	= models.ManyToManyField(Events, blank=True)
	total 		= models.DecimalField(default=0.0, max_digits=100, decimal_places=2, blank=True)
	updated		= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	
def __str__(self):
    return {self.id}