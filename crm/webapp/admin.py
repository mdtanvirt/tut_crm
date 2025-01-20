from django.contrib import admin
from .models import Client, Order, Rent, Service, Product

class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "created_at")

admin.site.register(Client, ClientAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "order_date", "amount")

admin.site.register(Order, OrderAdmin)

class RentAdmin(admin.ModelAdmin):
    list_display = ("client", "rent_receive_amount", "receive_date")

admin.site.register(Rent, RentAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("client", "service_name", "amount")

admin.site.register(Service, ServiceAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('client', 'product_name', 'price')

admin.site.register(Product, ProductAdmin)