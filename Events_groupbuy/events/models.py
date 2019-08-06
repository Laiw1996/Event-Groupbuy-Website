from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from PIL import Image

class Events(models.Model):

	EVENT_CHOICES = (
		("JANUARY", "Movie"),
    	("SPORTS", "Sports"),
    	("GAMES", "Games"),
    	("FOOD", "Food"),
    	("TRANSIT", "Transit"),
    	("MERCH", "Merch"),
    	("OTHER", "Other"),
    	)

	title = models.CharField(max_length=200)
	description = models.TextField(default = '')
	location = models.CharField(max_length=200)
	price = models.FloatField()
	event_date = models.DateTimeField()
	image_event = models.ImageField(default='default_image.jpg', upload_to='event_img',blank=True)

	event_type = models.CharField(max_length=50, choices=EVENT_CHOICES, default='OTHER')
	
	poster_image = models.ImageField(blank = True)

	status = models.PositiveSmallIntegerField(default=1, validators=[
	        MaxValueValidator(5),
	        MinValueValidator(1)
	    ])
	
	discount_rate = models.FloatField(validators=[
	        MaxValueValidator(100.0),
	        MinValueValidator(0.0)], default=10.0)
	
	# 1: pending(looking for people to buy stage)
	# 2: met expected number of people
	# 3: event owner cancelled(not expired yet)
	# 4: event dealine met, forced cancel
	# 5: event successfully processed 

	post_date = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()
	expected_attendants = models.PositiveSmallIntegerField()
	current_attendants = models.PositiveSmallIntegerField(default=0)

	participators = models.ManyToManyField(User, related_name='myEvents')
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Master', null=True)


	def save(self,force_insert=False, force_update=False, using=None):
		super().save()
		img = Image.open(self.image_event.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image_event.path)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Events"