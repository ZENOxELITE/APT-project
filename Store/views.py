from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    all_products = Product.objects.all().order_by('-created_at')
    return render(request, 'products.html', {'products': all_products})


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
