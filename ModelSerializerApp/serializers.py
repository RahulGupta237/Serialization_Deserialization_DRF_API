from .models import Student
from rest_framework import serializers

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        