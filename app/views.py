from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def getHomePage(request):    
    products = Products.objects.all()

    # handle login :v
    # if request.user.is_authenticated:
    #     return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else :
            messages.info(request, "username or password not correct!!!")

    context = {"products": products, "hello": 123}
    return render(request, "app/home.html", context)

def logoutPage(request):
    logout(request)
    return redirect("/")

def getCheckoutsPage(request):    
    if request.user.is_authenticated:
        customer = request.user
        order, created = Orders.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0}

    context = {"items": items, "order": order}

    return render(request, "app/checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)

    productId = data["productId"]
    action = data["action"]
    customer = request.user
    product = Products.objects.get(id = productId)
    order, created = Orders.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0 :
        orderItem.delete()

    return JsonResponse("added", safe=False)

def getIntroduceFoodPage(request):    
    return render(request, "app/introduceFood.html")

def getMenuPage(request):    
    products = Products.objects.all()
    context = {"products": products}

    return render(request, "app/menu.html", context)

def getStorePage(request):    
    return render(request, "app/store.html")

def getCartPage(request): 
    if request.user.is_authenticated:
        customer = request.user
        order, created = Orders.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0}

    context = {"items": items, "order": order}
    return render(request, "app/cart.html", context)

def getProductDetailPage(request):    
    id = request.GET.get("id", "")
    products = Products.objects.filter(id=id)
    context = {"products": products}
    return render(request, "app/productDetail.html", context)

def getRegisterPage(request):   
    form = CreateUserForm()
    context = {"form": form} 

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/") 
    return render(request, "app/register.html", context)

def getBasePage(request):
    context = {} 
    return render(request, "app/base.html", context)

def index(request):
    return HttpResponse("this is pages test")

def getMenupage(request):
    users=Users.objects.all()
    context={"users" : users}
    return render(request, "app/menu.html", context)