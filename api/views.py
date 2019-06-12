
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from api import models
# Create your views here.
class RegisteredView(APIView):
    def post(self,request,*args,**kwargs):
        ret = {'code': 1000}
        name = request.data.get('name')
        sex = request.data.get('sex')
        age = request.data.get('age')
        print(name,sex,age)
        models.Verify.objects.create(name=name,sex=sex,age=age)
        return Response(ret)
