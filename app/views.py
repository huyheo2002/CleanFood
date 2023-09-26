from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def getHomepage(request):
    products = Products.objects.all()
    users=Users.objects.all()
    context = {"products": products,"users" : users}
    return render(request, "app/home.html", context)

def getNewspage(request):    
    return render(request, "app/news.html")

def getIntroduceFoodpage(request):    
    return render(request, "app/introduceFood.html")

def getMenupage(request):    
    return render(request, "app/menu.html")

def getStorepage(request):    
    return render(request, "app/store.html")

def getCartpage(request):    
    return render(request, "app/cart.html")

def getProductDetailpage(request):    
    return render(request, "app/productDetail.html")

def index(request):
    return HttpResponse("this is pages test")

def getMenupage(request):
    users=Users.objects.all()
    context={"users" : users}
    return render(request, "app/menu.html", context)