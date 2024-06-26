from rest_framework import serializers
from .models import Student

class Studentserializer(serializers.ModelSerializer):
    First_name=serializers.CharField(max_length=100,required=True)
    Last_name=serializers.CharField(max_length=100,required=True)
    address=serializers.CharField(max_length=250,required=True)
    roll_number=serializers.IntegerField(required=True)
    mobile_number=serializers.CharField(max_length=100,required=True)

class Meta:
    model=Student
    fields='__all__'
