from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<film_id>/', views.add_to_basket, name="add_to_basket"),
    path('remove/<film_id>/', views.remove_from, name="remove_from")
]
