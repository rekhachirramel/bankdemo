from .import views
from django.urls import path
urlpatterns=[
   path('register',views.register,name='demo'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),
   path('ernakulam',views.ernakulam,name='ernakulam'),
   path('idukki',views.idukki,name='idukki'),
   path('kottayam',views.kottayam,name='kottayam'),
   path('palakkad',views.palakkad,name='palakkad'),
   path('malapuram',views.malapuram,name='malapuram'),
   path('appform',views.appform,name='appform'),
   path('messageapp',views.messageapp,name='messageapp'),
   path('process',views.process,name='process'),
]
