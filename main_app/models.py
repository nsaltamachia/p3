from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    
class Comment(models.Model):
    comment = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
    
    class Meta:
        ordering = ['-date']
