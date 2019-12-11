from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from apps.inventory.models import Person, Location, TypeDevice, Device
from .serializers import PersonSerializers, LocationSerializer, TypeDeviceSerializer, DiveceSerializer

#=================__PERSON__===========================
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

#=================__LOCATION__=========================
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

#=================__DIVECE_TYPE__========================
class TypeDeviceViewSet(ModelViewSet):
    queryset = TypeDevice.objects.all()
    serializer_class = TypeDeviceSerializer

#=================__DIVECE__============================
class DiveceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DiveceSerializer

    filter_backends = [filters.SearchFilter]   
    search_fields = ['inventory_number']
