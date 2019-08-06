from django.shortcuts import render, redirect
from .models import Cart
from events.models import Events
from orders.models import Order
from billing.forms import AddressForm
from django.conf import settings
from decimal import *
from django.contrib.auth.decorators import login_required

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

def cart_home(request):
	the_Cart = helper(request)

	events = the_Cart.products.all()
	total = 0
	for i in events:
		total += i.price
	the_Cart.total = total
	the_Cart.save()
	cartTax = round(total * 0.1, 2)
	cartTotal_withTax = total + cartTax
	context = {
		'current_cart': the_Cart,
		'events': events,
		'cartTax':cartTax,
		'cartTotal_withTax':cartTotal_withTax
	}
	return render(request, "carts/home.html", context)

def cart_update(request):
	product_id = request.POST.get('productID')
	the_event = Events.objects.get(id=product_id)
	the_Cart = helper(request)
	the_Cart.products.add(the_event)
	the_Cart.save()
	return redirect('/carts/')


def cart_remove(request, id):
	the_Cart = helper(request)
	tobeRemoved = the_Cart.products.all().get(id=id)
	the_Cart.products.remove(tobeRemoved)
	the_Cart.save()
	return redirect('/carts/')

@login_required
def checkout_home(request):
	the_Cart = helper(request)
	if the_Cart.products.count() == 0:
		return redirect('/carts/')
	else:
		order, new_order = Order.objects.get_or_create(cart=the_Cart)
		billing_address_form = AddressForm(request.POST or None)

		if billing_address_form.is_valid():
			the_billing = billing_address_form.save()
			order.billing = the_billing
			order.save()
			key = settings.STRIPE_PUBLISHABLE_KEY
			orderTax = round(order.cart.total * Decimal('0.1'), 2)
			orderTotal_withTax = order.cart.total + orderTax
			orderTotal_forStripe = orderTotal_withTax * 100
			context = {
				'the_order': order,
				'key':key,
				'orderTax':orderTax,
				'orderTotal_withTax':orderTotal_withTax,
				'orderTotal_forStripe':orderTotal_forStripe
			}
			return render(request, 'orders/order_review.html', context)

		context = {
			'billing_address_form': billing_address_form
		}
		return render(request, "orders/billing_address_filling.html", context)
	
	




