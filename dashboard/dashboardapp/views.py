from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import forms     
from .forms import CustomUserCreationForm  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    return render(request,"dashboardapp/main.html")
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('mainpage')
        else:
            messages.info(request,'invalid credentials')
            return redirect('registerpage')
    return render(request,"dashboardapp/login.html")
def logoutfn(request):
    logout(request)
    return redirect('loginpage')
def registration(request):
    myform=UserCreationForm()
    if request.method=="POST":
        myform=UserCreationForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('mainpage')
        else:
            return render(request,"dashboardapp/register.html",{'form':myform})
    return render(request,"dashboardapp/register.html",{'form':myform})
    