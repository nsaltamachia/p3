from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Seat(models.Model):
    table_type = models.CharField(max_length=50)
    table_capacity = models.IntegerField()
    indoor_or_outdoor = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.table_type}"
    
class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    neighborhood = models.TextField(max_length=150)
    cuisine = models.TextField(max_length=150)
    seats = models.ManyToManyField(Seat)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})

class Meal_Had(models.Model):
    date = models.DateField('meal date')
    description = models.TextField(max_length=250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.description} on {self.date}'










class Meal(models.Model):
    date = models.DateField('meal date')
    description = models.TextField(max_length=250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meal_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.description} on {self.date}'
      

class Photo(models.Model):
    url = models.CharField(max_length=200)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for meal_id: {self.meal_id} @{self.url}"







class Comment(models.Model):
    comment = models.TextField(max_length=400)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
    



