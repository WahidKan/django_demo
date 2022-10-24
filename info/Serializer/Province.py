from rest_framework import serializers 
from info.models.Province import ems_province
from info.Serializer.Country import CountrySerializer
class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False,read_only=True)
    class Meta:
        model = ems_province
        fields = ['id',
                  'name',
                  'shortCode','country']

