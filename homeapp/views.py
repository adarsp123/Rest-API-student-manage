from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Student  
from .serializer import Studentserializer  
# Create your views here.  

class StudentView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Student.objects.all()  
        serializers = Studentserializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = Studentserializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 