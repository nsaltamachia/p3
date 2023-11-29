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
    path('restaurants/<int:restaurant_id>/unassoc_seating/<int:seating_id>/', views.unassoc_seating, name='unassoc_seating'),
    path('seating/', views.SeatingList.as_view(), name='seating_index'),
    path('seating/create/', views.SeatingCreate.as_view(), name='seating_create'),
    # path('seating/<int:seating_id>/', views.seating_detail, name='detail'),
    path('seating/<int:pk>/update/', views.SeatingUpdate.as_view(), name='seating_update'),
    path('seating/<int:pk>/delete/', views.SeatingDelete.as_view(), name='seating_delete'),
]

