# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', store, name='store'),
    path('<slug:category_slug>/', store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-product/', add_product, name='add_product'),
]