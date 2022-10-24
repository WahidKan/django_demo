
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
 
from info.models.District import ems_district
from info.Serializer.District import DistrictSerializer
from rest_framework.decorators import api_view,schema
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView 

class district_view(APIView):

    def get(self,request,pk=None,format=None):
        try: 
         if pk is not None:
            district = ems_district.objects.get(pk=pk)
            district_serializer = DistrictSerializer(district) 
            return Response(district_serializer.data)
         district = ems_district.objects.all()
         district_serializer = DistrictSerializer(district,many=True) 
        except ems_district.DoesNotExist: 
             return Response({'message': 'The district does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        return Response(district_serializer.data)
    
    def post(self,request,format=None):
        district_serializer = DistrictSerializer(data=request.data)
        if district_serializer.is_valid():
            district_serializer.save()
            return Response(district_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(district_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        if pk is not None:
            district = ems_district.objects.get(pk=pk)
            district_serializer = DistrictSerializer(district,data=request.data) 
            if district_serializer.is_valid(): 
                district_serializer.save() 
                return Response(district_serializer.data) 
            return Response(district_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response('Id not found', status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request, pk):
        try: 
         district = ems_district.objects.get(pk=pk) 
        except district.DoesNotExist: 
            return Response({'message': 'The district does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        district.delete();
        return Response({'message': 'district was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

