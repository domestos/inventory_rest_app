
from django.contrib import admin
from django.urls import path
from apps.inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.main, name='inventory_main'),
    
]
