from rest_framework import serializers
from apps.inventory.models import Person, Location, TypeDevice, Device

#=================__PERSON__===========================
class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'fname',
            'sname'
        )
    
#=================__LOCATION__=========================
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'location'
        )

#=================__DIVECE_TYPE__========================
class TypeDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDevice
        fields = (
            'id',
            'dtype'
        )


#=================__DIVECE__============================
class DiveceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'id',
            'inventory_number',
            'person_id',
            'type_id',
            'location_id'
        )
