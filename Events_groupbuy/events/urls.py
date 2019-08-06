from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('event_details/<int:id>', views.details, name='details'),
	path('event_details/purchase/<int:id>', views.purchase, name='purchase'),
]
