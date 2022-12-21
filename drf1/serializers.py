from .models import Student
from rest_framework import serializers


# CUstom Validators
def start_with_r(value):
    if value['0'].lower()!='r':
        raise serializers.ValidationError("Name should be start with r")




class student_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    city=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    # Fields Level Validation
    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError("Seat full")
        return value

    # OBject Level Validation

    def validate(self,data):
        """
    Validation required for multiple felds
    """
        nm=data.get('name')
        cf=data.get('city')
        if nm.lower()== 'rohit' and cf.lower()!='ranchi':
            raise serializers.ValidationError("City Must be Ranchi")

        return data

