import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Restaurant, MealPhoto
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

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant
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
