
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render



# Create your views here.
def demo(request):
   #obj=Place.objects.all()

   return render(request,"index.html")


