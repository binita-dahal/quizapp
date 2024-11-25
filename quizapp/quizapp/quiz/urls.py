from django.contrib import admin
from django.urls import path, include
from quiz import views

urlpatterns = [
    path("", views.quizhome, name='quizhome'),
    path("play", views.playquiz, name='playquiz'),
    path('check-answer/', views.check_answer, name='check_answer'),
]