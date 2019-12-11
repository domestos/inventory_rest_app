from rest_framework import serializers
from apps.inventory.models import Device, Person, Location, TypeDivece

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'fname',
            'sname'
        )