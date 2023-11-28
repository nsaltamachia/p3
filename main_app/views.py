
import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Restaurant, MealPhoto, Comment, Meal_Had, Seating
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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
   fields = '__all__'
   success_url = '/restaurants'


def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    id_list = restaurant.seating.all().values_list('id')
    seating_restaurant_doesnt_have = Seating.objects.exclude(id__in=id_list)
    meal_had_form = Meal_Had_Form()
    comment_form = CommentForm()
    return render(request, 'restaurants/detail.html', {
      'restaurant': restaurant, 'meal_had_form': meal_had_form, 'comment_form' : comment_form,
      'seating': seating_restaurant_doesnt_have
    })
   

def add_photo(request, restaurant_id):
   photo_file = request.FILES.get('photo-file', None)
   if photo_file:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      try:
         bucket = os.environ['S3_bucket']
         s3.upload_fileobj(photo_file, bucket, key)
         url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
         MealPhoto.objects.create(url=url, meal_had_id=meal_had_id)
      except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
      return redirect('detail', meal_had_id=meal_had_id)
    
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

def assoc_seating(request, restaurant_id, seating_id):
  Restaurant.objects.get(id=restaurant_id).seating.add(seating_id)
  return redirect('detail', restaurant_id=restaurant_id)


