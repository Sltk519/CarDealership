from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import Car,Review,Order

from .forms import FilterCarForm,ReviewForm,OrderForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def car_list(request):
    # Initialize the form
    form = FilterCarForm(request.GET or None)
    cars_query = Car.objects.all()
    brand = request.GET.get('brand')
    category = request.GET.get('category')
    year = request.GET.get('year')
    searchCar=request.GET.get('searchCar')
    
    # Apply filters if parameters exist
    if brand:
        cars_query = cars_query.filter(brand=brand)
    if category:
        cars_query = cars_query.filter(category__name=category)
    if year:
        cars_query = cars_query.filter(year=year)
    if searchCar:
        cars=Car.objects.filter(Q(brand__icontains=searchCar) | Q(category__name__icontains=searchCar))
    else:
        cars=cars_query
    # Execute the query and get the result set
    
    
    # Render the response
    return render(request, 'cars/car_list.html', {'cars': cars, "filter_form": form})


def detail(request,id):
    searchCar=request.GET.get('searchCar')
    if searchCar:
        car=Car.objects.filter(Q(brand__icontains=searchCar) | Q(category__name__icontains=searchCar)).first()
    else:
        car= get_object_or_404(Car,pk=id)
    reviews=Review.objects.filter(car=car)
    related_cars=Car.objects.filter(category=car.category,is_sold=False,).exclude(id=car.id)[0:6]
    return render(request,"cars/detail.html",{"car":car,"related_cars":related_cars,'reviews':reviews,"searchCar":searchCar})



def compare_cars(request, id):
    car1 = get_object_or_404(Car, pk=id)
    cars = Car.objects.exclude(id=car1.id)  # Exclude car1 from the list of cars
    
    selected_car = None
    selected_car_id = request.GET.get('selectedCars')
    if selected_car:
        selected_car = Car.objects.filter(id=selected_car_id).first()
    

    return render(request, "cars/compare.html", {"car1": car1, "cars": cars, "selected_car": selected_car})


@login_required
def createreview(request,id):
    car= get_object_or_404(Car,pk=id)
    if request.method=="GET":
        form=ReviewForm()
        return render(request,"cars/createreview.html",{"car":car,"form":form})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.car = car
            newReview.save()
            return redirect('car:detail',newReview.car.id)
        except ValueError:
            return render(request, 
            'cars/createreview.html', 
            {'form':ReviewForm(),'error':'bad data passed in'})
@login_required
def deletereview(request,id):
    review = get_object_or_404(Review, pk=id,user=request.user)
    review.delete()
    return redirect('car:detail',review.car.id)
@login_required
def updatereview(request,id):
    review = get_object_or_404(Review, pk=id,user=request.user)
    if request.method=="GET":
        form=ReviewForm(instance=review)
        return render(request,"cars/updatereview.html",{"form":form,"review":review})
    else:
        try:
            form = ReviewForm(request.POST,instance=review)
            form.save()
            return redirect('car:detail',review.car.id)
        except ValueError:
            return render(request,
                          'cars/updatereview.html',
                          {'form':ReviewForm(),'error':'bad data passed in'})
@login_required
def create_order(request,id):
    car=get_object_or_404(Car,pk=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user)
        if form.is_valid():
            # Update user's first and last name
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            
            order = form.save(commit=False)
            order.user = request.user
            order.car = car
            order.save()
            return redirect('core:dashboard',request.user)  # Redirect to a success page or the list of orders
    else:
        form = OrderForm(user=request.user)
    return render(request, 'cars/order.html', {'form': form})

@login_required
def deleteorder(request,id):
    order = get_object_or_404(Order, pk=id,user=request.user)
    order.delete()
    return redirect('core:dashboard',request.user)
    
    