from django.shortcuts import render
from .models import ModelPP
from .forms import ModelPPForm
# Create your views here.


# post 로 받은 내용 저장 
def createModel(request):  # form 으로 빼기
    # tid =  request.POST.get("tid")
    # vuser = request.POST.get("vuser")
    # tests = request.POST.get("tests")
    # sucessTest =request.POST.get("successTest")
    # meanResp =request.POST.get("successTest")
    # flag =request.POST.get("flag")
    form = ModelPPForm.forms(request.POST, request.FILE) 
    form.save()
    print(form.cleaned_data)
    return HttpResponse("nn")
    
# #
# def ReadModel():
# json 형태로 보낸다 

# def UpdateModel


# def DeleteModel 



