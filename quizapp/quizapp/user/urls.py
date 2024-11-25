from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("register", views.register, name='register')
    
]