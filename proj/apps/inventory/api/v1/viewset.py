from rest_framework.viewsets import ModelViewSet

from apps.inventory.models import Person
from .serializers import PersonSerializers

class PersonListAPIView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers