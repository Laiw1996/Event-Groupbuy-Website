from django.contrib import admin
from django.urls import path, include
from post.views import postNew, showPost,edit_post
from events.views import Started, Joined, show_user, Merch, Movie, Game, Food, Sport, Transit, Other, sortByDate, saveTheMost, lowToHigh, highToLow

urlpatterns = [
	path('', include('main.urls')),
	path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('post/', postNew),
    path('create/', postNew),

    path('events/joined', Joined),
    path('events/started', Started),

    path('events/merch', Merch),
    path('events/movie', Movie),
    path('events/game', Game),
    path('events/food', Food),
    path('events/sport', Sport),
    path('events/transit', Transit),
    path('events/other', Other),

    path('events/sortbydate', sortByDate),
    path('events/savethemost', saveTheMost),
    path('events/lowtohigh', lowToHigh),
    path('events/hightolow', highToLow),
    
    path('editpost/<int:edit_id>', edit_post),

    path('show/<int:u_id>',show_user),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls'))
]
