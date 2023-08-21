from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

