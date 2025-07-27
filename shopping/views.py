from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product
from django.core.cache import cache
from django.core.paginator import Paginator

def dashboard(request):
    products = cache.get('products_cache_key')

    if products is None:
        products = Product.objects.all()
        cache.set('products_cache_key', products, 300)

    # Pagination
    paginator = Paginator(products, 8)  # Show 8 products per page
    page_number = request.GET.get('page')  # Get page number from request query params
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # Pass the Page object to the template
    }
    return render(request, 'dashboard.html', context)

