from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelPP
from django.views.decorators.csrf import csrf_exempt 
from django.http.response import JsonResponse
import json
from .DataSerializer import DataSerializer
from rest_framework.request import Request
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# 04.19 하예진
# agent 한테 2초에 한번씩 받은 내용 db 저장
@csrf_exempt
@api_view(['POST'])
def createModel(request): 
    if request.method == 'POST':
        inputTestdata= DataSerializer(data=request.data) # 전달받은 데이터 

        if inputTestdata.is_valid():  #모델 형식에 맞는 데이터면 저장 
            inputTestdata.save()
            return Response(status=status.HTTP_201_CREATED) # success createModel 
        else:
            return Response(inputTestdata.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_303_SEE_OTHER) # redirect custom error page
    
# #
# def ReadModel():


# 04.19 하예진
# get conditions by post request and update database
# @input    
# @output   Response    RESET_CONTENT
@csrf_exempt
@api_view(['POST'])
@parser_classes([JSONParser])
def updateModel(request):

    if request.method == 'POST':
        condColumn = request.data.get('condColumn')
        condValue = request.data.get('condValue')
        condFlag = request.data.get('condFlag')
        targetColumn = request.data.get('targetColumn')
        targetValue = request.data.get('targetValue')

        if condFlag =='=':
            ModelPP.objects.filter(**{condColumn : condValue}).update(**{targetColumn:targetValue})
        elif condFlag == '!':
            ModelPP.objects.filter(~Q(**{condColumn : condValue})).update(**{targetColumn:targetValue})
        elif condFlag =='>=':
            ModelPP.objects.filter(**{condColumn+'__gte' : condValue}).update(**{targetColumn:targetValue})
        elif condFlag =='>':
            ModelPP.objects.filter(**{condColumn+'__gt' : condValue}).update(**{targetColumn:targetValue})
        elif condFlag =='<=':
            ModelPP.objects.filter(**{condColumn+'__lte' : condValue}).update(**{targetColumn:targetValue})
        elif condFlag =='<':
            ModelPP.objects.filter(**{condColumn+'__lt' : condValue}).update(**{targetColumn:targetValue})
        elif condFlag =='in':
            ModelPP.objects.filter(**{condColumn+'__in' : condValue}).update(**{targetColumn:targetValue})

        return Response(status=status.HTTP_205_RESET_CONTENT)

    else:
        return Response(status=status.HTTP_303_SEE_OTHER)
    

# 200419 qyu
# get request parameter(tid) using url and remove objects from database filtered by tid
# @input    tid         test id
# @output   Response    NO_CONTENT
@csrf_exempt
@api_view(['GET'])
def deleteModel(request, tid):
    
    if request.method == 'GET':
        model = ModelPP.objects.filter(tid=tid)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_303_SEE_OTHER)