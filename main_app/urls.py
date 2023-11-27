from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='detail'),
    path('restaurants/<int:restaurant_id>/add_comment/', views.add_comment, name='add_comment'),
]

