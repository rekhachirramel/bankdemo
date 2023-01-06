from django.urls import path
from  .import views
urlpatterns=[
    path('',views.demo,name='demo'),
    #path('',views.ernakulam,name='ernakulam')

    #path('',views.login,name='login'),


]