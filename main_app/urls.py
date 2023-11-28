from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='detail'),
    path('restaurants/<int:restaurant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('restaurants/<int:restaurant_id>/add_comment/', views.add_comment, name='add_comment'),
    path('restaurants/<int:restaurant_id>/add_meal_had/', views.add_meal_had, name='add_meal_had'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:restaurant_id>/assoc_seating/<int:seating_id>/', views.assoc_seating, name='assoc_seating'),
]

