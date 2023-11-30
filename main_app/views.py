
import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Restaurant, Comment, Meal_Had, Seat
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import CommentForm, Meal_Had_Form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def restaurants_index(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurants/index.html', 
    {
       'restaurants': restaurants
    }
  )


class RestaurantCreate(LoginRequiredMixin, CreateView):
   model = Restaurant
   fields = ['name', 'address', 'neighborhood', 'cuisine']
   success_url = '/restaurants'

   def form_valid(self, form):
     # Assign the logged in user (self.request.user)
     form.instance.user = self.request.user
     return super().form_valid(form)


class RestaurantUpdate(LoginRequiredMixin, UpdateView):
  model = Restaurant
  fields = ['address', 'neighborhood', 'cuisine']


class RestaurantDelete(LoginRequiredMixin, DeleteView):
  model = Restaurant
  success_url = '/restaurants'

class SeatCreate(LoginRequiredMixin, CreateView):
  model = Seat
  fields = ['table_type', 'table_capacity', 'indoor_or_outdoor']
  success_url = '/seats/'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'seat_id': self.id})

class SeatList(LoginRequiredMixin, ListView):
  model = Seat

class SeatDetail(LoginRequiredMixin, DetailView):
  model = Seat

class SeatUpdate(LoginRequiredMixin, UpdateView):
  model = Seat
  fields = ['table_type', 'table_capacity', 'indoor_or_outdoor']
  success_url = '/seats/'

class SeatDelete(LoginRequiredMixin, DeleteView):
  model = Seat
  success_url = '/seats'

@login_required
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

@login_required
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
  return render(request, 'comment_form.html', {'form': form})

@login_required
def add_meal_had(request, restaurant_id):
    form = Meal_Had_Form(request.POST)
    if form.is_valid():
        new_meal_had = form.save(commit=False)
        new_meal_had.restaurant_id = restaurant_id
        new_meal_had.save()
    return redirect('detail', restaurant_id=restaurant_id)

@login_required
def assoc_seat(request, restaurant_id, seat_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Restaurant.objects.get(id=restaurant_id).seats.add(seat_id)
  return redirect('detail', restaurant_id=restaurant_id)

@login_required
def unassoc_seat(request, restaurant_id, seat_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Restaurant.objects.get(id=restaurant_id).seats.remove(seat_id)
  return redirect('detail', restaurant_id=restaurant_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'

    # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  
