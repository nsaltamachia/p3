from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    neighborhood = models.TextField(max_length=150)
    cuisine = models.TextField(max_length=150)

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
    
    class Meta:
        ordering = ['-date']



