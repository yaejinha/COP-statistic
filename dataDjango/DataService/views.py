from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelPP
from django.views.decorators.csrf import csrf_exempt 
from django.http.response import JsonResponse
import json
from .DataSerializer import DataSerializer
from rest_framework.request import Request
from rest_framework.decorators import api_view
# Create your views here.


# 04.19 하예진
# agent 한테 2초에 한번씩 받은 내용 db 저장
@csrf_exempt
@api_view(['PUT', 'POST'])
def createModel(request): 

    inputTestdata= DataSerializer(data=request.data) # 전달받은 데이터 

    if inputTestdata.is_valid():  #모델 형식에 맞는 데이터면 저장 
        inputTestdata.save()

    return HttpResponse("OK")
    
# #
# def ReadModel():
# json 형태로 보낸다 

# def UpdateModel


# def DeleteModel 



