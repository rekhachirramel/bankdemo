from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.forms import ProcessDataForm
from credentials.models import Branch,District,ProcessData


# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"YOu are logged in as {username},")
            return redirect('appform')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("User created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def ernakulam(request):
   return render(request,"ernakulam.html")
def idukki(request):
   return render(request,"idukki.html")
def kottayam(request):
   return render(request,"kottayam.html")
def palakkad(request):
   return render(request,"palakkad.html")
def malapuram(request):
   return render(request,"malapuram.html")

def appform(request):
    districtobj=District.objects.all()
    branchobj=Branch.objects.all()

    return render(request,"appform.html",{"district":districtobj,"branch":branchobj})
   # return redirect('process')
def messageapp(request):
    return render(request,"messageapp.html")
def process(request):
    # if request.method=='POST':
    #     username=request.POST['username']
    #     dob=request.POST['dob']
    #     age=request.POST['age']
    #     gender=request.POST['gender']
    #     phone=request.POST['phone']
    #     email=request.POST['email']
    #     address = request.POST['address']
    #     dist=request.POST['dist']
    #     branc=request.POST['branc']
    #     pdata=ProcessData.objects.Cre(request.POST or None)
    # # if pdata.is_valid():
    # #     pdata.save()
    # #     return redirect('thankyou')
    # # return render(request,'appform.html')
    if request.method=="POST":
        pdata=ProcessDataForm(request.POST)
        if pdata.is_valid():
            pdata.save()
            return redirect('thankyou')

    return render(request, 'appform.html')
def thankyou(request):
    return render(request,'messageapp.html')
