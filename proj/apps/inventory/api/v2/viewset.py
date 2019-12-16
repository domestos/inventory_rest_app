from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from apps.inventory.models import Person, Location, TypeDevice, Device
from .serializers import PersonSerializers, LocationSerializer, TypeDeviceSerializer, DeviceSerializer

#=================__PERSON__===========================
""" Example APIView """
@permission_classes((permissions.AllowAny,))
class PersonViewSet(APIView):
    def get(self,request):
        person = Person.objects.all()
        serializer = PersonSerializers(person, many=True)
        return Response({"person":serializer.data})
       
    def post(self, request):
        person = request.data.get('person')
        # Create an person from the above data
        serializer = PersonSerializers(data=person)
        if serializer.is_valid(raise_exception=True):
            # for saving a new object, the Person Serializers have to has the method create
            person_saved = serializer.save() 
        return Response({"success": "Person '{}' created successfully".format(person_saved.fname)})

    def put(self, request, pk):
        saved_person = get_object_or_404(Person.objects.all(), pk=pk)
        data = request.data.get('person')
        # Ми передаємо partial = True в серіалізатор, оскільки хочемо мати можливість оновлювати тільки деякі поля, але не обов'язково всі відразу.
        serializer = PersonSerializers(instance=saved_person, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            person_saved = serializer.save()
        return Response({
            "success": "Person '{}' updated successfully".format(person_saved.fname)
        })

    def delete(self, request, pk):
        # Get object with this pk
        person = get_object_or_404(Person.objects.all(), pk=pk)
        person.delete()
        return Response({
            "message": "Person with id `{}` has been deleted.".format(pk)
        }, status=204)

#=================__LOCATION__=========================
""" Example APIView """
@permission_classes((permissions.AllowAny,))
class LocationViewSet(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response({"location":serializer.data})

    def post(self, request):
        location = request.data.get('location')
        serializer = LocationSerializer(data=location)
        if serializer.is_valid(raise_exception=True):
            saved_location=serializer.save()
        return Response({'success':"Location '{}' created successfull.".format(saved_location.location)})

    def put(self,request, pk):
        location= get_object_or_404(Location.objects.get(pk=pk)) 
        data = request.data.get('location')
        serializer = LocationSerializer(initial=location, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_location = serializer.save()
        return Response({
            "success":"Location {} was updated successfull.".format(updated_location.location)
        })

    def delete(self, request, pk):
        location = get_object_or_404(Location.objects.get(pk=pk))
        location.delete()
        return Response({
            "message": "Location with id `{}` has been deleted.".format(pk)
        }, status=204)

#=================__DIVECE_TYPE__========================
""" Example APIView """
@permission_classes((permissions.AllowAny,))
class TypeDeviceViewSet(APIView):
    def get(self, request):
        type_device=TypeDevice.objects.all()
        serializer = TypeDeviceSerializer(type_device, many=True)
        return Response({"type_device":serializer.data})

    def post(self, request):
        type_device = request.data.get("type_device")
        serializer = TypeDeviceSerializer(data=type_device)
        if serializer.is_valid(raise_exception=True):
            saved_type_device = serializer.save()
        return Response({
            "success":"Type Device {} was saved successfull."
        })

    def put(self, request, pk):
        type_device = get_object_or_404(TypeDevice.objects.get(pk=pk))
        data = request.data.get('type_device')
        serializer = TypeDeviceSerializer(instance=type_device, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_type_device=serializer.save()
        return Response({
            "success":"Type Device {} was updated successfull.".format(updated_type_device.location)
        })
   

#=================__DIVECE__============================
""" Example APIView """
@permission_classes((permissions.AllowAny,))
class DeviceViewSet(APIView):

    def get(self, request, pk=None):
        if (pk==None):
            devices = Device.objects.all()
        else:
            devices = get_object_or_404(Device.objects.get(pk=pk))
        serializer = DeviceSerializer(devices, many=True)
        return Response({"device": serializer.data})
    
    
    def detail(self, request, pk):
        devices = get_object_or_404(Device.objects.get(pk=pk))
        serializer = DeviceSerializer(devices, many=True)
        return Response({"device": serializer.data})
        # filter_backends = [filters.SearchFilter]   
        # search_fields = ['inventory_number']

    def put(self, request, pk):
        device = get_object_or_404(Device.objects.get(pk=pk))
        data = request.data.get('device')
        serializer = DeviceSerializer(instance=device, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            update_device = serializer.save()
        return Response({
            "seccess":"Device whit this id '{}' was updated successfull.".format(update_device.id)
        })
