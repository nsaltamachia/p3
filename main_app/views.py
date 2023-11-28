from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import Meal_Had_Form
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def restaurants_index(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurants/index.html', 
    {
       'restaurants': restaurants
    }
  )

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant
    })


class RestaurantCreate(CreateView):
   model = Restaurant
   fields = '__all__'
   success_url = '/restaurants'


def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    meal_had_form = Meal_Had_Form()
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant, 'meal_had_form': meal_had_form
    })

def add_meal_had(request, restaurant_id):
    form = Meal_Had_Form(request.POST)
    if form.is_valid():
        new_meal_had = form.save(commit=False)
        new_meal_had.restaurant_id = restaurant_id
        new_meal_had.save()
    return redirect('detail', restaurant_id=restaurant_id)

class RestaurantUpdate(UpdateView):
  model = Restaurant
  fields = ['address', 'neighborhood', 'cuisine']

class RestaurantDelete(DeleteView):
  model = Restaurant
  success_url = '/restaurants'

