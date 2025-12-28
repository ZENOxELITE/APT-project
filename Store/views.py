from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Service, Api_product
from .forms import ProductForm, ServiceForm, ApiProductForm
import requests
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    manual_products = Product.objects.all().order_by('-created_at')
    api_products = Api_product.objects.all().order_by('-created_at')
    
    # Add is_api flag to each product
    for product in manual_products:
        product.is_api = False
    for product in api_products:
        product.is_api = True
    
    # Combine both querysets
    all_products = list(manual_products) + list(api_products)
    
    # Sort combined list by creation date, newest first
    all_products.sort(key=lambda x: x.created_at, reverse=True)
    
    return render(request, 'products.html', {
        'products': all_products
    })

def services(request):
    all_services = Service.objects.all().order_by('-created_at')
    return render(request, 'services.html', {'services' : all_services})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})


# --- Product detail / edit / delete ---
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form, 'submit_label': 'Update Product'})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('products')
    return render(request, 'product_detail.html', {'product': product})


# --- Service detail / edit / delete ---
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})


def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'add_service.html', {'form': form, 'submit_label': 'Update Service'})


def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully!')
        return redirect('services')
    return render(request, 'service_detail.html', {'service': service})

def fetch_api(request):
    if request.method == 'POST':
        api_url = request.POST.get('api_url', 'https://fakestoreapi.com/products')
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for bad status codes
            api_products = response.json()
            
            if not isinstance(api_products, list):
                messages.error(request, 'The API should return an array of products')
                return redirect('products')
                
            for item in api_products:
                Api_product.objects.update_or_create(
                    title=item.get('title', 'Untitled Product'),
                    defaults={
                        'price': item.get('price', 0),
                        'description': item.get('description', 'No description available'),
                        'image': item.get('image', ''),
                        'category': item.get('category', 'uncategorized'),
                    }
                )
            messages.success(request, f'Successfully fetched {len(api_products)} products from the API!')
        except requests.RequestException as e:
            messages.error(request, f'Error fetching products: {str(e)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    
    return redirect('products')

def api_product_details(request, pk):
    api_product = get_object_or_404(Api_product, pk=pk)
    return render(request, 'api_product_details.html', {'api_product': api_product})

def edit_api_product(request, pk):
    product = get_object_or_404(Api_product, pk=pk)
    if request.method == 'POST':
        form = ApiProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'API Product updated successfully!')
            return redirect('api_product_details', pk=product.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ApiProductForm(instance=product)
    return render(request, 'edit_api_product.html', {
        'form': form,
        'product': product,
        'submit_label': 'Update Product'
    })

def delete_api_product(request, pk):
    api_product = get_object_or_404(Api_product, pk=pk)
    if request.method == 'POST':
        api_product.delete()
        messages.success(request, 'API Product deleted successfully!')
        return redirect('fetch_api')
    return render(request, 'api_product_details.html', {'api_product': api_product})
