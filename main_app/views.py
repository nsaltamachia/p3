from django.shortcuts import render
from .models import Restaurant
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

class RestaurantUpdate(UpdateView):
  model = Restaurant
  fields = ['address', 'neighborhood', 'cuisine']

class RestaurantDelete(DeleteView):
  model = Restaurant
  success_url = '/restaurants'