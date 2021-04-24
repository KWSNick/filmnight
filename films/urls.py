from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='films'),
    path('<film_id>', views.filmpage, name='filmpage'),
    path('watch/<film_id>', views.watch, name='watch'),
    path('admin_area/', views.admin_area, name='admin_area'),
    path('admin_area/edit_price/<price_id>/',
         views.edit_price, name='edit_price'),
    path('admin_area/add_film/',
         views.add_film, name='add_film'),
    path('admin_area/edit_film/<film_id>/',
         views.edit_film, name='edit_film'),
    path('admin_area/delete_film/<film_id>/',
         views.delete_film, name='delete_film'),
]
