from rest_framework import serializers 
from info.models.Tehsil import ems_tehsil
from info.Serializer.District import DistrictSerializer
class TehsilSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(many=False,read_only=True)
    class Meta:
        model = ems_tehsil
        fields = ['id',
                  'name',
                  'shortCode',
                  'district'
                 ]