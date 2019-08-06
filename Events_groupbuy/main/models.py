from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from events.models import Events

MAJOR_CHOICES = (
    ('Applied Sciences','FAS'),
    ('Arts and Social Sciences','ART'),
    ('Beedie School of Business','BUS'),
    ('Communication','CMNS'),
    ('Faculty of Education','EDUC'),
	('Faculty of Environment','ENVC'),
	('Health Sciences','HEALTH'),
	('Faculty of Science','SCI'),
)
YEAR_IN_SCHOOL_CHOICES = (
    ('Freshman','1st Year'),
    ('Sophomore','2nd Year'),
    ('Junior','3rd Year'),
    ('Senior','4th Year'),
)
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	# age = models.IntegerField(default=0)
	# age = models.CharField(default=0)
	image = models.ImageField(default='default.jpg', upload_to='profile_img')
	major = models.CharField(max_length=30, choices=MAJOR_CHOICES, default='Applied Sciences')
	age = models.IntegerField(default=0)
	year_in_school = models.CharField(max_length=10,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default='Freshman')
	note = models.TextField(default='write something')

	# purchased_events = models.ManyToManyField(Events)

	def save(self,force_insert=False, force_update=False, using=None):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 200 or img.width > 200:
			output_size = (200,200)
			img.thumbnail(output_size)
			img.save(self.image.path)

def __str__(self):
    return {self.user.username}
