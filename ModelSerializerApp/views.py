from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import student_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.
@csrf_exempt
def studentmodel_api(request):
    
    if request.method=="GET":
        """
        Deserialization and insert data into database through DRF
        
        """
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id = python_data.get('id',None)
        serializer=student_serializer(data=python_data)

        if id is not None:
            stu=Student.objects.get(id=id)
            serializer= student_serializer(stu)
        
        
            json_data=JSONRenderer().render(serializer.data)

            return HttpResponse(json_data,content_type='application/json')
        

        #json_data=JSONRenderer().render(serializer.errors)
        stu=Student.objects.all()
        serializer= student_serializer(stu,many=True)
    
    
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')



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

    if request.method=="PUT":
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id = python_data.get('id',None)
        stu=Student.objects.get(id=id)
        #serializer= student_serializer(stu,data=python_data,partial=True)
        serializer= student_serializer(stu,data=python_data)

        if serializer.is_valid():
            serializer.save()
        
            res={'msg:"partially updated data'}
            json_data=JSONRenderer().render(res)

            return HttpResponse(json_data,content_type='application/json')
        

        json_data=JSONRenderer().render(serializer.errors)
      
    
    
        return HttpResponse(json_data,content_type='application/json')


    if request.method=="DELETE":
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id = python_data.get('id',None)
        stu=Student.objects.get(id=id)
        stu.delete()

      
    
        res={'msg':'Successfully Deleted data'}
        # json_data=JSONRenderer().render(res)
        """
        This is equvalent to jasoon response
        """

        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False) # safe = false becz res is not dictionary
        

        


