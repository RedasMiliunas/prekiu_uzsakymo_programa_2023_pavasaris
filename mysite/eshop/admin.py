from django.contrib import admin
from .models import Order, OrderLine, Product, Status

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Product)
admin.site.register(Status)
