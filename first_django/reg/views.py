from django.shortcuts import render, redirect, get_object_or_404
from .models import Reg
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.http import JsonResponse
from django import forms
def reg(request):
    if request.method == "POST":
        email=request.POST['email']  
        # password=request.POST['password']  
        data = Reg(email=email,password=make_password(request.POST['password']))
        data.save()
        return HttpResponse('Data save')
    else:  
       
        return render(request,'reg.html')
def login(request):
    if request.method == "POST":
        email=request.POST['email']  
        # password=request.POST['password']  
        data = Reg.objects.get(email=email)
        if check_password(request.POST['password'], data.password):
   
            return HttpResponse('Login ')
        else:
            return HttpResponse('P not correct ')

    else:  
       
        return render(request,'reg_login.html')  