from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import student_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=="POST":
        """
        Deserialization and insert data into database through DRF
        
        """
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=student_serializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created successfully'}
            json_data=JSONRenderer().render(res)

            return HttpResponse(json_data,content_type='application/json')
        

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

