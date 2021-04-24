from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>/',
         views.orderHistory, name='order_history'),
]
