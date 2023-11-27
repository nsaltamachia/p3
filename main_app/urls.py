from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
	path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
 ]