from django.urls import path
from .viewset import PersonViewSet
app_name = "inventory"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('person/<int:pk>', PersonViewSet.as_view()),
    path('person', PersonViewSet.as_view()),
   

]