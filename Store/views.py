from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Service
from .forms import ProductForm, ServiceForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    all_products = Product.objects.all().order_by('-created_at')
    return render(request, 'products.html', {'products': all_products})

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