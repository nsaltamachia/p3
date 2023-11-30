from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:restaurant_id>/add_comment/', views.add_comment, name='add_comment'),
    path('restaurants/<int:restaurant_id>/add_meal_had/', views.add_meal_had, name='add_meal_had'),
    path('restaurants/<int:restaurant_id>/assoc_seat/<int:seat_id>/', views.assoc_seat, name='assoc_seat'),
    path('restaurants/<int:restaurant_id>/unassoc_seat/<int:seat_id>/', views.unassoc_seat, name='unassoc_seat'),
    path('seats/', views.SeatList.as_view(), name='seats_index'),
    path('seats/<int:pk>/', views.SeatDetail.as_view(), name='seats_detail'),
    path('seats/create/', views.SeatCreate.as_view(), name='seats_create'),
    path('seats/<int:pk>/update/', views.SeatUpdate.as_view(), name='seats_update'),
    path('seats/<int:pk>/delete/', views.SeatDelete.as_view(), name='seats_delete'),
]


 

