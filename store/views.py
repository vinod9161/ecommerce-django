from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.core.cache import cache
from .forms import ProductForm
from django.core.paginator import Paginator

# def store(request,category=None):
#     products = cache.get('products_cache_key')

#     if products is None:
#         products = Product.objects.all().filter(is_available=True)
#         cache.set('products_cache_key', products, 300)

#     # Pagination
#     paginator = Paginator(products, 8)  # Show 8 products per page
#     page_number = request.GET.get('page')  # Get page number from request query params
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,  # Pass the Page object to the template
#     }
#     return render(request, 'store/store.html', context)

def store(request, category_slug=None):
    if category_slug:
        # Suppose you have Category model and a slug field
        from .models import Category
        category = Category.objects.get(slug=category_slug)
        cache_key = f'products_cache_key_category_{category.slug}'
        products = cache.get(cache_key)
        if products is None:
            products = Product.objects.filter(category=category, is_available=True)
            cache.set(cache_key, products, 300)
    else:
        cache_key = 'products_cache_key_all'
        products = cache.get(cache_key)
        if products is None:
            products = Product.objects.filter(is_available=True)
            cache.set(cache_key, products, 300)
    
    # Pagination
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
    }   
    return render(request, 'store/product_detail.html',context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Clear cache after product is added
            cache.delete('products_cache_key')
            return redirect('dashboard')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

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

