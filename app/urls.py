from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getHomepage),
    path("news", views.getNewspage),
    path("introduceFood", views.getIntroduceFoodpage),
    path("menu", views.getMenupage),
    path("store", views.getStorepage),
    path("cart", views.getCartpage),
    path("productDetail", views.getProductDetailpage),
    # path("/1", views.index),
    
]