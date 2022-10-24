
from rest_framework.response import Response
from rest_framework import status
 
from info.models.Tehsil import ems_tehsil
from info.Serializer.Tehsil import TehsilSerializer
from rest_framework.views import APIView 

class tehsil_view(APIView):

    def get(self,request,pk=None,format=None):
        try: 
         if pk is not None:
            tehsil = ems_tehsil.objects.get(pk=pk)
            tehsil_serializer = TehsilSerializer(tehsil) 
            return Response(tehsil_serializer.data)
         tehsil = ems_tehsil.objects.all()
         tehsil_serializer = TehsilSerializer(tehsil,many=True) 
        except ems_tehsil.DoesNotExist: 
             return Response({'message': 'The tehsil does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        return Response(tehsil_serializer.data)
    
    def post(self,request,format=None):
        tehsil_serializer = TehsilSerializer(data=request.data)
        if tehsil_serializer.is_valid():
            tehsil_serializer.save()
            return Response(tehsil_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(tehsil_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        if pk is not None:
            tehsil = ems_tehsil.objects.get(pk=pk)
            tehsil_serializer = TehsilSerializer(tehsil,data=request.data) 
            if tehsil_serializer.is_valid(): 
                tehsil_serializer.save() 
                return Response(tehsil_serializer.data) 
            return Response(tehsil_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response('Id not found', status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request, pk):
        try: 
         tehsil = ems_tehsil.objects.get(pk=pk) 
        except tehsil.DoesNotExist: 
            return Response({'message': 'The tehsil does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        tehsil.delete();
        return Response({'message': 'tehsil was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)