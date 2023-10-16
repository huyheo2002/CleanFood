from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)

class Users(models.Model):
    username = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True,)
    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)

class Products(models.Model):
    name = models.CharField(max_length=200, null=False)
    desc = models.TextField(null=True, blank=True)
    price = models.FloatField(null=False)
    thumbnail = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    stay = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


