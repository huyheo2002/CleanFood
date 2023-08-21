from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getHomepage(request):
    context = {}
    return render(request, "app/home.html", context)

def index(request):
    return HttpResponse("this is pages test")

