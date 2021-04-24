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
]
