from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Seating(models.Model):
    TYPE_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('indoor_outdoor', 'Indoor & Outdoor'),
    ]
    YES_NO_CHOICES = [
        ('y', 'Yes'),
        ('n', 'No'),
    ]
    type = models.CharField(max_length=150)
    indoor = models.CharField(max_length=20, choices=TYPE_CHOICES)
    handicap = models.CharField(max_length=1, choices=YES_NO_CHOICES)

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    neighborhood = models.TextField(max_length=150)
    cuisine = models.TextField(max_length=150)
    seating = models.ManyToManyField(Seating)
    
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
      
class Comment(models.Model):
    comment = models.TextField(max_length=400)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
    



