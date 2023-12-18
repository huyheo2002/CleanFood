from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from .forms import *
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
        shipping_address_form = ShippingAddressForm()
    else:
        items = []
        order = {"get_cart_total": 0}
        shipping_address_form = ShippingAddressForm()

    context = {"items": items, "order": order, "shipping_address_form": shipping_address_form}

    if request.method == 'POST':
        shipping_address_form = ShippingAddressForm(request.POST)
        if shipping_address_form.is_valid():
            shipping_address = shipping_address_form.save(commit=False)
            shipping_address.customer = request.user if request.user.is_authenticated else None
            shipping_address.order = order
            shipping_address.save()
            
            order.complete = True
            order.save()
            return render(request, 'app/order_success.html')

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

def getSystemPage(request):        
    context = {}
    return render(request, "app/system/index.html", context)

# component page
# charts
def getChartjs(request):
    context = {}
    return render(request, "app/pages/charts/chartjs.html", context)

def getChartflot(request):
    context = {}
    return render(request, "app/pages/charts/flot.html", context)

def getChartinline(request):
    context = {}
    return render(request, "app/pages/charts/inline.html", context)

def getChartuplot(request):
    context = {}
    return render(request, "app/pages/charts/uplot.html", context)

# forms
def getFormsAdvanced(request):
    context = {}
    return render(request, "app/pages/forms/advanced.html", context)

def getFormEditors(request):
    context = {}
    return render(request, "app/pages/forms/editors.html", context)

def getFormGeneral(request):
    context = {}
    return render(request, "app/pages/forms/general.html", context)

def getFormValidation(request):
    context = {}
    return render(request, "app/pages/forms/validation.html", context)

# big
def getCalendar(request):
    context = {}
    return render(request, "app/pages/calendar.html", context)

def getGallery(request):
    context = {}
    return render(request, "app/pages/gallery.html", context)

def getKanban(request):
    context = {}
    return render(request, "app/pages/kanban.html", context)

def getWidgets(request):
    context = {}
    return render(request, "app/pages/widgets.html", context)

# table 
def getTableInvoice(request):
    context = {}
    return render(request, "app/pages/examples/invoice.html", context)

def getProfile(request):
    context = {}
    return render(request, "app/pages/examples/profile.html", context)

def getTableTest(request):
    context = {}
    return render(request, "app/pages/tables/data.html", context)

def getTableUserManagement(request):
    users = User.objects.all()
    paginator = Paginator(users, 5)
    page = request.GET.get('page')
    users = paginator.get_page(page)

    form = CreateUserForm()    
    context = {"users": users, "form": form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/system/table-user-management")
    return render(request, "app/system/userManagement.html", context)

def update_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('updateUserId')
        username = request.POST.get('updateUsername')
        email = request.POST.get('updateEmail')
        first_name = request.POST.get('updateFirstName')
        last_name = request.POST.get('updateLastName')

        try:
            user = User.objects.get(id=user_id)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('/system/table-user-management')
        except User.DoesNotExist:
            return HttpResponseBadRequest('Người dùng không tồn tại.')

    return HttpResponseBadRequest('Phương thức không hợp lệ.')

def delete_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('/system/table-user-management')

    return HttpResponseBadRequest('Phương thức không hợp lệ.')


def getTableProductManagement(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    form = ProductForm()
    context = {"products": products, "form": form, "categories": categories}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/system/table-product-management")
    return render(request, "app/system/productManagement.html", context)

def update_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('updateProductId')
        updateProductName = request.POST.get('updateProductName')
        updateProductDesc = request.POST.get('updateProductDesc')
        updateProductPrice = request.POST.get('updateProductPrice')
        updateProductCategory = request.POST.get('updateProductCategory')

        try:
            product = Products.objects.get(id=product_id)
            product.name = updateProductName
            product.desc = updateProductDesc
            product.price = updateProductPrice
            # product.category = updateProductCategory
            # Kiểm tra xem category có tồn tại không
            if updateProductCategory:
                category = Category.objects.get(id=updateProductCategory)
                product.category = category
            else:
                product.category = None  # Giữ nguyên giá trị hiện tại (nếu có)
                # Hoặc bạn có thể gán một category mặc định:
                # default_category = Category.objects.get(name='Tên mặc định')
                # product.category = default_category
            
            product.save()
            return redirect('/system/table-product-management')
        except User.DoesNotExist:
            return HttpResponseBadRequest('Người dùng không tồn tại.')

    return HttpResponseBadRequest('Phương thức không hợp lệ.')    

def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Products, id=product_id)
        product.delete()
        return redirect('/system/table-product-management')

    return HttpResponseBadRequest('Phương thức không hợp lệ.')

def getTablePaymentManagement(request):
    orders = Orders.objects.select_related('customer').prefetch_related('shippingaddress_set').all()     
    context = {'orders': orders}
    return render(request, "app/system/paymentManagement.html", context)

def get_order_items(request, order_id):
    try:
        order = Orders.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        items = [{'product': item.product.name, 'quantity': item.quantity, 'price': item.product.price} for item in order_items]
        return JsonResponse(items, safe=False)
    except Orders.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Orders, id=order_id)

        # Xóa các order items và shipping addresses liên quan đến đơn hàng
        order.orderitem_set.all().delete()
        order.shippingaddress_set.all().delete()

        # Xóa đơn hàng
        order.delete()

        return JsonResponse({'message': 'Order deleted successfully'})

    return HttpResponseBadRequest('Phương thức không hợp lệ.')
    
def getOrderSuccessPage(request):        
    context = {}
    return render(request, "app/order_success.html", context)