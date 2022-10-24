
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
 
from info.models.Country import ems_country
from info.Serializer.Country import CountrySerializer
from rest_framework.decorators import api_view,schema
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView 

class country_view(APIView):

    def get(self,request,pk=None,format=None):
        try: 
         if pk is not None:
            country = ems_country.objects.get(pk=pk)
            country_serializer = CountrySerializer(country) 
            return Response(country_serializer.data)
         country = ems_country.objects.all()
         country_serializer = CountrySerializer(country,many=True) 
        except ems_country.DoesNotExist: 
             return Response({'message': 'The country does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        return Response(country_serializer.data)
    
    def post(self,request,format=None):
        country_serializer = CountrySerializer(data=request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(country_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        if pk is not None:
            country = ems_country.objects.get(pk=pk)
            country_serializer = CountrySerializer(country,data=request.data) 
            if country_serializer.is_valid(): 
                country_serializer.save() 
                return Response(country_serializer.data) 
            return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response('Id not found', status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request, pk):
        try: 
         country = ems_country.objects.get(pk=pk) 
        except country.DoesNotExist: 
            return Response({'message': 'The country does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        country.delete();
        return Response({'message': 'country was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

