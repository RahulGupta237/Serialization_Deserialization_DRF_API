
from django.contrib import admin
from django.urls import path
from drf1 import views
from CRUDAPI import views as v1
from ModelSerializerApp import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stucreat/',views.student_create),
     path('stuget/',v1.student_api),
      path('stumodel/',v2.studentmodel_api),
]
