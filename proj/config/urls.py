"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
# import the router of API requests 
from apps.inventory.api.v1.router import router as api_inventory
# from apps.inventory.api.v2.router import router as api_inventory_v2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('apps.home.urls')),
    path('inventory/', include('apps.inventory.urls')),  
    # redircet api request to router 
    path('api/v1/inventory/', include(api_inventory.urls)),
    path('api/v2/inventory/', include('apps.inventory.api.v2.urls_app')),
    # rest web auth
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
