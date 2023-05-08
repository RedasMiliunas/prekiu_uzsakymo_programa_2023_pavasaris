from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('products/<int:product_id>', views.product, name='product'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
]
