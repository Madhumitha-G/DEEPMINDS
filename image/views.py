from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as log
from django.contrib import auth
from django.contrib import messages
from django.db.models import Q
from .form import CreateUserForm
def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"index.html",{"obj":obj})
    else:
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html",{"img":img,"form":form})

def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Welcome' + user + 'your registration is successful'+ 'Kindly login , to explore more!!')
            return redirect('login')
    context={'form':form}
    return render(request,'authentication/register.html',context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username , password = password)
        if user is not None:
            log(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,'authentication/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
# def upload(request):
#     return render(request, 'upload.html')
def search(request):
    query=None
    result=[]
    if request.method == 'GET':
            query=request.GET.get('search')
            result=Image.objects.filter(Q(caption__icontains=query))
    return render(request,'search.html',{'query':query,'result':result})

