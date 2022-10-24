from rest_framework import serializers 
from info.models.Country import ems_country
 
 
class CountrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ems_country
        fields = ('id',
                  'name',
                  'shortCode')