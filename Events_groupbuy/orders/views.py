from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
import stripe
from carts.models import Cart
from events.models import Events


stripe.api_key = settings.STRIPE_SECRET_KEY


def helper(request):
	current_cartID = request.session.get("cartID", None)
	if current_cartID is None:					  # session cart id does not exist

		if request.user.is_authenticated:
			the_Cart = Cart.objects.create(user=request.user)
		else :
			the_Cart = Cart.objects.create(user=None)
		
		request.session['cartID'] = the_Cart.id   #each cart session id will be set yo equal 
		print("cartID doesnt exist")			  #to newly created cart object id

	else:										  # session cart id exist!
		print("cartID already exist")
		print(current_cartID)
		the_Cart = Cart.objects.get(id=current_cartID)
		if request.user.is_authenticated and the_Cart.user is None: #if an user created a cart not 
																	 #logged in previously, 
																	 #then logged in, we need to 
																	 #add the user to the cart
			the_Cart.user = request.user
			the_Cart.save()

	return the_Cart

def pay(request):
	if request.method == 'POST':
		charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
		the_Cart = helper(request)

		for event in the_Cart.products.all():
			event.current_attendants = event.current_attendants + 1;
			event.participators.add(request.user)
			event.save()
 
		the_Cart.products.clear()

		return render(request, "orders/confirmed.html")







