from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from events.models import Events
from .forms import event_created,PostUpdateForm
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def showPost(request):

	return render(request, 'post/base.html')




def postNew(request):
	if request.user.is_anonymous:
		return redirect('/login/')
	print(request.user)
	if request.method == 'POST':
		e_form = event_created(request.POST,request.FILES)
		if e_form.is_valid():
			
			u_event = e_form.save()
			u_event.owner = request.user
			discount = float(request.POST.get('discount_rate'))
			discount = 100 - discount
			discount = discount/100
			print(discount)
			# u_event.discount_rate = discount
			u_event.save()

			print("Save event ")
			# messages.success(request, f'Your event has been updated!')
			now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
			print(now)
			return redirect('/events/started')
	else:
		e_form = event_created()
	return render(request, 'post/base.html', {
        'e_form': e_form
    })



def edit_post(request,edit_id):
	if request.user.is_anonymous:
		return redirect('/login/')
	if edit_id:
		p = Events.objects.get(pk=edit_id)
		if(p.owner != request.user):
			error = "You cannot edit this post since you are not the owner"
			return render(request, 'post/edit_post.html', {'error': error})
	else:
		p = None
	if request.method == 'POST':
		e_form = PostUpdateForm(request.POST,
                                   request.FILES,
                                   instance=p)
		if e_form.is_valid():
			e_form.save()
			print("Save img")
			messages.success(request, f'Your post got updated')
			return redirect('/events/started')
	else:
		e_form = PostUpdateForm(instance=p)
	return render(request, 'post/edit_post.html', {'e_form': e_form})
