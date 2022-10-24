from rest_framework import serializers 
from info.models.type import ems_type
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ems_type
        fields = ['id',
                  'code'
                 ]