from django.shortcuts import render
from .models import Events
from django.contrib.auth.models import User
from main.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import datetime


def index(request):
	AllEvents = Events.objects.all()
	
	# me = request.user
	# my_events = me.profile.myEvents.all()
	
	context = {
	'AllEvents': AllEvents
	
	# 'AllEvents': my_events
	}

	return render(request, 'events/index.html', context)

def Joined(request):
	# AllEvents = Events.objects.all()
	me = request.user
	
	my_events = me.myEvents.all()

	now = datetime.datetime.now()
	
	context = {
	# 'AllEvents': AllEvents
	'AllEvents': my_events,
	'flag': 0,
	'now': now,
	}

	return render(request, 'events/index2.html', context)


def Started(request):
	# AllEvents = Events.objects.all()
	me = request.user
	
	my_starts = Events.objects.filter(owner_id=me.id)
	
	context = {
	# 'AllEvents': AllEvents
	'AllEvents': my_starts,
	'flag': 1,
	}

	return render(request, 'events/index2.html', context)

def Merch(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='MERCH')
	count = Events.objects.filter(event_type='MERCH').count()
	context = {
	'AllEvents': AllEvents,
	'type': 'Merch',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def Movie(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='MOVIE')
	count = Events.objects.filter(event_type='MOVIE').count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Movie',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def Game(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='GAMES')
	count = Events.objects.filter(event_type='GAMES').count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Game',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def Food(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='FOOD')
	count = Events.objects.filter(event_type='FOOD').count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Food',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def Sport(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='SPORTS')
	count = Events.objects.filter(event_type='SPORTS').count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Sport',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def Transit(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='TRANSIT')
	count = Events.objects.filter(event_type='TRANSIT').count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Transit',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def Other(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.filter(event_type='OTHER')
	count = Events.objects.filter(event_type='OTHER').count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Other',
	'sorting': 0,
	'filtering': 1,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def sortByDate(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.all().order_by('-post_date')
	count = Events.objects.all().count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Most recently',
	'sorting': 1,
	'filtering': 0,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def saveTheMost(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.all().order_by('-discount_rate')
	count = Events.objects.all().count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Save the most',
	'sorting': 1,
	'filtering': 0,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def lowToHigh(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.all().order_by('price')
	count = Events.objects.all().count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Price: Low to high',
	'sorting': 1,
	'filtering': 0,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def highToLow(request):
	# AllEvents = Events.objects.all()

	AllEvents = Events.objects.all().order_by('-price')
	count = Events.objects.all().count()
	
	context = {
	'AllEvents': AllEvents,
	'type': 'Price: High to low',
	'sorting': 1,
	'filtering': 0,
	'count': count,
	}

	return render(request, 'events/index.html', context)

def details(request, id):
	eventDetail = Events.objects.get(id=id)
	price = eventDetail.price * ((100 - eventDetail.discount_rate)/100)
	price = round(price,1);
	context = {
	'eventDetail': eventDetail,
	'cur': eventDetail.participators.all(),
	'discount_price': price
	}
	# buyerProfile = Profile.objects.get(user=request.user)
	print(eventDetail.participators.all())
	return render(request, 'events/details.html', context)

@login_required
def purchase(request, id):
	selected_event = Events.objects.get(id=id)
	selected_event.current_attendants = selected_event.current_attendants + 1;

	
	# buyerProfile = Profile.objects.get(user=request.user)

	participator = request.user

	# print(request.user.username)

	selected_event.save()
	selected_event.participators.add(participator)
	

	return redirect('/events/')



def show_user(request,u_id):
	show_user = User.objects.get(id=u_id)
	return render(request, 'events/participant.html', context={"user":show_user})

