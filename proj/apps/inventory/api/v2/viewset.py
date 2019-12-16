from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from apps.inventory.models import Person, Location, TypeDevice, Device
from .serializers import PersonSerializers, LocationSerializer, TypeDeviceSerializer, DiveceSerializer

#=================__PERSON__===========================
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
        return Response({"success": "Article '{}' created successfully".format(person_saved.fname)})

    def put(self, request, pk):
        saved_person = get_object_or_404(Person.objects.all(), pk=pk)
        data = request.data.get('person')
        # Ми передаємо partial = True в серіалізатор, оскільки хочемо мати можливість оновлювати тільки деякі поля, але не обов'язково всі відразу.
        serializer = PersonSerializers(instance=saved_person, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            person_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(person_saved.fname)
        })

    def delete(self, request, pk):
        # Get object with this pk
        person = get_object_or_404(Person.objects.all(), pk=pk)
        person.delete()
        return Response({
            "message": "Person with id `{}` has been deleted.".format(pk)
        }, status=204)

#=================__LOCATION__=========================
class LocationViewSet(APIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

#=================__DIVECE_TYPE__========================


class TypeDeviceViewSet(APIView):
    queryset = TypeDevice.objects.all()
    serializer_class = TypeDeviceSerializer

#=================__DIVECE__============================


class DiveceViewSet(APIView):
    queryset = Device.objects.all()
    serializer_class = DiveceSerializer

    # filter_backends = [filters.SearchFilter]   
    # search_fields = ['inventory_number']
