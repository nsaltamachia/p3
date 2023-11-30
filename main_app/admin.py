from django.contrib import admin
from .models import Restaurant, Comment, Meal_Had, Seat

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Meal_Had)
admin.site.register(Seat)


