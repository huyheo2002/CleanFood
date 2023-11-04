from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getHomePage),
    path("checkout", views.getCheckoutsPage),
    path("introduceFood", views.getIntroduceFoodPage),
    path("menu", views.getMenuPage),
    path("store", views.getStorePage),
    path("cart", views.getCartPage),
    path("productDetail", views.getProductDetailPage),
    path("register", views.getRegisterPage),
    path("update_item", views.updateItem),
    path("logout", views.logoutPage),

    # path("/1", views.index),
]