
from django.db import models
from decimal import Decimal
import datetime


# Save model per 2 second period
class ModelPP(models.Model):  
    tid = models.IntegerField(default=0) #테스트 아이디
    vuser = models.IntegerField(default=0) # 총 vuser 수 
    tests = models.IntegerField(default=0) #총 테스트 수 
    sucessTest = models.IntegerField(default=0) #성공테스트수
    meanResp = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00)) #평균응답시간
    flag = models.CharField(max_length=20)  # 테스트 시작 S 끝 E 진행중 D
    dateTime = models.DateTimeField()

