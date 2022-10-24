
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
 
from info.models.Province import ems_province
from info.Serializer.Province import ProvinceSerializer
from rest_framework.decorators import api_view,schema
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView 

class province_view(APIView):

    def get(self,request,pk=None,format=None):
        try: 
         if pk is not None:
            province = ems_province.objects.get(pk=pk)
            country_serializer = ProvinceSerializer(province) 
            return Response(country_serializer.data)
         province = ems_province.objects.all()
         country_serializer = ProvinceSerializer(province,many=True) 
        except ems_province.DoesNotExist: 
             return Response({'message': 'The province does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        return Response(country_serializer.data)
    
    def post(self,request,format=None):
        country_serializer = ProvinceSerializer(data=request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(country_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        if pk is not None:
            province = ems_province.objects.get(pk=pk)
            country_serializer = ProvinceSerializer(province,data=request.data) 
            if country_serializer.is_valid(): 
                country_serializer.save() 
                return Response(country_serializer.data) 
            return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response('Id not found', status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request, pk):
        try: 
         province = ems_province.objects.get(pk=pk) 
        except province.DoesNotExist: 
            return Response({'message': 'The province does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        province.delete();
        return Response({'message': 'province was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

