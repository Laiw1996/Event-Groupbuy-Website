from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart_home, name='cart_home'),
	path('update', views.cart_update, name='cart_update'),
	path('remove/<int:id>', views.cart_remove, name='cart_remove'),
	path('checkout', views.checkout_home, name='checkout_home'),
] 