from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def amn(request):
    if request.method=='GET':
        form=trekform()
        bese=trek.objects.all()
        return render(request,'him.html',{'form':form,'bese':bese})
    else:
         form=trekform(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('amn')
    
def index(request):
    bese=trek.objects.all()

    return render(request,'index.html',{'bese':bese})

@login_required(login_url='login')
def read(request,id):
    bese=trek.objects.get(id=id)
    return render(request,'read.html',{'bese':bese})



def up(request,id):
     emp = trek.objects.get(id=id)  
     if request.method=='GET':
          form=trekform(instance=emp)
          bese=trek.objects.all()
          return render(request,'him.html',{'form':form,'bese':bese})
     else:
         form=trekform(request.POST,request.FILES,instance=emp)
         if form.is_valid():
            form.save()
         return redirect('index')
     
def sig(request):
    if request.method=='GET':
        return render(request,'sign.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        pass4=request.POST['pass1']
        pass5=request.POST['pass2']
 
        if pass4==pass5:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'username already exists')
                return redirect('sig')
            
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'email already exists')
                return redirect('sig')
            else:
                User.objects.create_user(username=username,email=email,password=pass5)
                messages.success(request,'Account Has Been Created')
                return redirect('login')
        else:
            return redirect('sig')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    else:
        username=request.POST['username']
        password=request.POST['pass1']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'invalid userame or password')
            return redirect('login')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def sear(request):
    if request.method=='POST':
        search=request.POST['search']
        if trek.objects.filter(name__contains=search).exists():
            bese=trek.objects.filter(name__contains=search)
            return render(request,'index.html',{'bese':bese})

        else:
          messages.warning(request,'Not found')
          return redirect('index')
    else:
        return redirect('index')    

        
        




