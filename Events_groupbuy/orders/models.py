from django.db import models
from carts.models import Cart
from billing.models import BillingProfile



ORDER_STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid')
)

class Order(models.Model):
	cart 		= models.ForeignKey(Cart, on_delete=models.CASCADE)
	status 		= models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	billing 	= models.OneToOneField(BillingProfile, null=True, on_delete=models.CASCADE)
	
def __str__(self):
    return {self.id}