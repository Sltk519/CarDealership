from django.shortcuts import render,redirect,get_object_or_404

from django.db.models import Count

from cars.models import Car,Category,Order

from .forms import SignupForm

from django.contrib.auth import logout

from .models import Favorite
from django.contrib.auth.models import  User
from django.http import  JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from django.http import  HttpResponse
from django.views.decorators.http import require_POST


def index(request):
    # Get the first 6 car objects that are not sold yet
    cars = Car.objects.filter(is_sold=False)[:6]
    
    # Annotate categories with the number of cars associated with each
    categories = Category.objects.annotate(num_cars=Count('car'))
    
    # # Get the favorite cars for the logged-in user
    # favorites = Favorite.objects.filter(user=request.user).values_list('item_id', flat=True)
    # favorites=Favorite.objects.filter(user=request.user)
    
    # Pass the context to the template
    context = {
        "cars": cars,
        "categories": categories,
        # 'favorites': favorites
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request,"core/contact.html")

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
    
        form=SignupForm()
    return render(request,"core/signup.html",{'form':form})
def logoutaccount(request):
    logout(request)
    return redirect('/')

@login_required
def add_to_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, item=car)
    if created:
        messages.success(request,"The car successfully was added to favourites")
    else:
        # The item was already in favorites, handle as you wish
        messages.warning(request,"This item is already in your favorites.")
    return redirect('/')
 
@login_required
def remove_from_favorites(request,car_id):
    car = get_object_or_404(Favorite, user=request.user,item_id=car_id).item
    Favorite.objects.filter(user=request.user,item=car).delete()
    messages.success(request, "Succesfully removed from favorites")
    # return redirect("dashboard",user=request.user.username)  
    return redirect("/")  
@login_required
def dashboard(request,user):
    user = User.objects.get(username=user)
    order=Order.objects.filter(user=user)
    fav_list = Favorite.objects.filter(user=user)[0:6]
    context={'favs':fav_list,"orders":order}
    return render(request,'core/dashboard.html',context)