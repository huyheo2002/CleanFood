from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def getHomepage(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, "app/home.html", context)

def index(request):
    return HttpResponse("this is pages test")

