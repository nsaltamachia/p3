
import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Restaurant, Comment, Meal_Had, Seat, Meal, Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import CommentForm, Meal_Had_Form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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















class MealCreate(LoginRequiredMixin, CreateView):
  model = Meal
  fields = ['date', 'description', 'image']
  success_url = '/meals/'

  def form_valid(self, form):
      form.instance.restaurant_id = self.kwargs['restaurant_id']
      return super().form_valid(form)

  def get_success_url(self):
      return reverse('restaurant_detail', kwargs={'restaurant_id': self.kwargs['restaurant_id']})

  def get_absolute_url(self):
    return reverse('detail', kwargs={'meal_id': self.id, 'restaurant': restaurant})


def add_photo(request, meal_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to meal_id or meal (if you have a meal object)
      photo = Photo(url=url, meal_id=meal_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', meal_id=meal_id)


def meals_index(request):
  meals = Meal.objects.all()
  return render(request, 'meals/index.html', { 'meals': meals })

  def get_absolute_url(self):
    return reverse('detail', kwargs={'meal_id': self.id})

def meals_detail(request, meal_id):
  meal = Meal.objects.get(id=meal_id)
  return render(request, 'meals/detail.html', {
    'meal': meal
  })

class MealList(LoginRequiredMixin, ListView):
  model = Meal

class MealDetail(LoginRequiredMixin, DetailView):
  model = Meal

class MealUpdate(LoginRequiredMixin, UpdateView):
  model = Meal
  fields = ['date', 'description', 'image']
  success_url = '/meals/'

class MealDelete(LoginRequiredMixin, DeleteView):
  model = Meal
  success_url = '/meals'















@login_required
def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    id_list = restaurant.seats.all().values_list('id')
    seats_restaurant_doesnt_have = Seat.objects.exclude(id__in=id_list)
    meal_had_form = Meal_Had_Form()
    comment_form = CommentForm()
    return render(request, 'restaurants/detail.html', {
      'restaurant': restaurant, 'meal_had_form': meal_had_form, 'comment_form' : comment_form,
      'seats': seats_restaurant_doesnt_have, 
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
