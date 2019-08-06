from django.db import models


class BillingProfile(models.Model):
	email			= models.EmailField()
	address_line_1  = models.CharField(max_length=120, default='')
	address_line_2  = models.CharField(max_length=120, default='', null=True, blank=True)
	city            = models.CharField(max_length=120, default='')
	country         = models.CharField(max_length=120, default='')
	state           = models.CharField(max_length=120, default='')
	postal_code     = models.CharField(max_length=120, default='')
	
def __str__(self):
    return {self.id}