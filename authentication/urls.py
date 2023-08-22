from django.contrib import admin
from django.urls import path, include
from . import views

from authentication.views import removeitem
from authentication.views import mylist

urlpatterns = [
    #path('',views.home, name="home"),
    path('',views.loginPage, name="login"),
    path('mylist', views.mylist, name="mylist"),
    path('mylist/<int:id>', removeitem),

    #path('register', views.registerPage, name="register"),
    #path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
]