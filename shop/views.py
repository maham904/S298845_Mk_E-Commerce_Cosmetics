from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def cart(request):
    return render(request, 'cart.html', {'cart_items': []})

def checkout(request):
    return render(request, 'checkout.html')

def payment(request):
    return render(request, 'payment.html', {'total': 50})

def tracking(request):
    status = None
    if 'tracking_id' in request.GET:
        status = "Your order is being processed."
    return render(request, 'tracking.html', {'status': status})
# comment added