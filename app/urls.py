from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getHomepage),
    path("menu/", views.getMenupage,name='menu'),
]