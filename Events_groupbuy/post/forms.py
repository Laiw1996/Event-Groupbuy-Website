from django import forms
from events.models import Events
from django.core.exceptions import ValidationError
import datetime
import pytz


class event_created(forms.ModelForm):
	event_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
	deadline = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
	error_css_class = 'valid_error'

	class Meta:
		model = Events
		fields = ['title','location','event_type','price','discount_rate','expected_attendants','image_event','deadline','event_date','description']


	def clean(self):
		# cleaned_data = super().clean()
		super(event_created, self).clean() 
		open_date = self.cleaned_data.get('event_date')
		end_date = self.cleaned_data.get('deadline')
		now = datetime.datetime.now()
		now = pytz.utc.localize(now)
		# current = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
		if open_date and end_date:
			if open_date == end_date:
				raise forms.ValidationError("Cannot enter the same event date and dealine date")
			if open_date < end_date:
				raise forms.ValidationError("Cannot set the start the event before dealine")
			if (end_date) < now:
				raise forms.ValidationError("Cannot start in the past")

			return self.cleaned_data
	def __init__(self, *args, **kwargs):
		super(event_created, self).__init__(*args, **kwargs)
		self.fields['price'].label = "Price (CAD)" 
		self.fields['discount_rate'].label = "Discount (0% - 100%)" 
		self.fields['deadline'].label = "Dealine To Apply" 

	def clean_price(self,*args,**kwargs):
		p = self.cleaned_data.get('price')
		if p < 0:
			raise forms.ValidationError("Please enter a positive price")
		return p
	def clean_discount_rate(self,*args,**kwargs):
		dis_rate = self.cleaned_data.get('discount_rate')
		if dis_rate < 0 or dis_rate > 100:
			raise forms.ValidationError("Please enter a valid dicount rate")
		# if isinstance(dis_rate,float):
		# 	raise forms.ValidationError("Disocunt cannot be a floating number ")
		return dis_rate
	def clean_expected_attendants(self,*args,**kwargs):
		num = self.cleaned_data.get('expected_attendants')
		if num <= 0:
			raise forms.ValidationError("Attendants cannot be Zero")
		return num			

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title','location','event_type','discount_rate', 'expected_attendants','image_event','description']

    def clean_image_event(self):
    	t = self.cleaned_data.get('image_event')
    	if t:
    		return t
    	else:
    		raise forms.ValidationError("You cannot clear the image. You must have one image")