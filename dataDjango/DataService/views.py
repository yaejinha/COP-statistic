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
# 수정할 컬럼, 수정할 값, 조건 (컬럼 값 상황)
# param : 조건절 (컬럼, 값, 조건 기호 =,!, >,<), 변경목표값 (컬럼, 값)
# UpdateModel(dict, dict)
def UpdateModel(condition, target):
    condColumn= condition['col'] #조건절 where condColumn = condValue
    condValue=condition['val']
    condFlag= condition['flag'] # =, ! , > , < , >=, <= , in

    targetColumn= target['col'] #변경목표값 set targetColumn= targetValue
    targetValue=target['val']

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