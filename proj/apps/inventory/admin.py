from django.contrib import admin
from .models import Location, TypeDevice, Device, Person 
# Register your models here.
admin.site.register(Person)
admin.site.register(Device)
admin.site.register(TypeDevice)
admin.site.register(Location)