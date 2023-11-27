from django.shortcuts import render
from .models import Restaurant
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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
       'restaurants' : restaurants
    }
  )

class RestaurantCreate(CreateView):
   model = Restaurant
   fields = '__all__'

   success_url = '/restaurants'

   
