
import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Restaurant, Comment, Meal_Had, Seat
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Comment, Meal_Had, Seat
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import CommentForm, Meal_Had_Form

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

class RestaurantCreate(CreateView):
   model = Restaurant
   fields = ['name', 'address', 'neighborhood', 'cuisine']
   success_url = '/restaurants'

class RestaurantUpdate(UpdateView):
  model = Restaurant
  fields = ['address', 'neighborhood', 'cuisine']

class RestaurantDelete(DeleteView):
  model = Restaurant
  success_url = '/restaurants'

class SeatCreate(CreateView):
  model = Seat
  fields = ['table_type', 'table_capacity', 'indoor_or_outdoor']
  success_url = '/seats/'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'seat_id': self.id})
class SeatList(ListView):
  model = Seat

class SeatDetail(DetailView):
  model = Seat

class SeatUpdate(UpdateView):
  model = Seat
  fields = ['table_type', 'table_capacity', 'indoor_or_outdoor']
  success_url = '/seats/'

class SeatDelete(DeleteView):
  model = Seat
  success_url = '/seats'

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    id_list = restaurant.seats.all().values_list('id')
    seats_restaurant_doesnt_have = Seat.objects.exclude(id__in=id_list)
    meal_had_form = Meal_Had_Form()
    comment_form = CommentForm()
    return render(request, 'restaurants/detail.html', {
      'restaurant': restaurant, 'meal_had_form': meal_had_form, 'comment_form' : comment_form,
      'seats': seats_restaurant_doesnt_have
    })

def add_comment(request, restaurant_id):
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.restaurant_id = restaurant_id
      new_comment.save()
    return redirect('detail', restaurant_id = restaurant_id)
  else:
    form = CommentForm()

def update_comment(request, restaurant_id):
  restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
  if comment_id:
     comment = get_object_or_404(Comment, pk=comment_id)
     if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
           form.save()
           return redirect('detail', restaurant_id=restaurant_id)
  else:
    form = CommentForm
  return render(request, 'comment_form.html', {
     'form': form,
     'restaurant': restaurant,
     'comment_id': comment_id
  })

# def update_comment(request, restaurant_id, pk):
#   update_comment = Comment.objects.get(id = pk)
#   if request.method == 'POST':
#     form = CommentForm(request.POST)
#     if form.is_valid():
#       update_comment = form.save(commit=False)
#       update_comment.restaurant_id = restaurant_id
#       update_comment.save()
#       return redirect('detail', restaurant_id = restaurant_id)
#   else:
#         form = CommentForm()
#   return render(request, 'comment_form.html', {'form': form})

def delete_comment(request, comment_id, restaurant_id):
  if request.method == 'DELETE':
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
  return redirect('detail', restaurant_id=restaurant_id)

def add_meal_had(request, restaurant_id):
    form = Meal_Had_Form(request.POST)
    if form.is_valid():
        new_meal_had = form.save(commit=False)
        new_meal_had.restaurant_id = restaurant_id
        new_meal_had.save()
    return redirect('detail', restaurant_id=restaurant_id)

def assoc_seat(request, restaurant_id, seat_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Restaurant.objects.get(id=restaurant_id).seats.add(seat_id)
  return redirect('detail', restaurant_id=restaurant_id)

def unassoc_seat(request, restaurant_id, seat_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Restaurant.objects.get(id=restaurant_id).seats.remove(seat_id)
  return redirect('detail', restaurant_id=restaurant_id)


