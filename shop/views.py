from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product

# Metric: counts homepage visits
HOMEPAGE_VISITS = Counter('homepage_visits_total', 'Total homepage visits')

def home(request):
    HOMEPAGE_VISITS.inc()  # Increment counter whenever homepage is accessed
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

class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.html"
    context_object_name = "products"

# Metrics endpoint
def metrics(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
