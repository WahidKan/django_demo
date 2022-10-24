
from rest_framework.response import Response
from rest_framework import status
 
from info.models.type import ems_type
from info.Serializer.type import TypeSerializer
from rest_framework.views import APIView 

class type_view(APIView):

    def get(self,request,pk=None,format=None):
        try: 
         if pk is not None:
            type = ems_type.objects.get(pk=pk)
            type_serializer = TypeSerializer(type) 
            return Response(type_serializer.data)
         type = ems_type.objects.all()
         type_serializer = TypeSerializer(type,many=True) 
        except ems_type.DoesNotExist: 
             return Response({'message': 'The type does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        return Response(type_serializer.data)
    
    def post(self,request,format=None):
        type_serializer = TypeSerializer(data=request.data)
        if type_serializer.is_valid():
            type_serializer.save()
            return Response(type_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        if pk is not None:
            type = ems_type.objects.get(pk=pk)
            type_serializer = TypeSerializer(type,data=request.data) 
            if type_serializer.is_valid(): 
                type_serializer.save() 
                return Response(type_serializer.data) 
            return Response(type_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response('Id not found', status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request, pk):
        try: 
         type = ems_type.objects.get(pk=pk) 
        except type.DoesNotExist: 
            return Response({'message': 'The type does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        type.delete();
        return Response({'message': 'type was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)