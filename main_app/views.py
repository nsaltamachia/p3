from django.shortcuts import render, redirect
from .models import Restaurant
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentForm

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

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    comment_form = CommentForm()
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant, 'comment_form' : comment_form
    })

def add_comment(request, restaurant_id):
  form = CommentForm(request.POST)
  if form.is_valid():
     new_comment = form.save(commit=False)
     new_comment.restaurant_id = restaurant_id
     new_comment.save()
  return redirect('detail', restaurant_id=restaurant_id)