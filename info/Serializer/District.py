from rest_framework import serializers 
from info.models.District import ems_district
from info.Serializer.Province import ProvinceSerializer
class DistrictSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(many=False,read_only=True)
    class Meta:
        model = ems_district
        fields = ['id',
                  'name',
                  'shortCode','province']

