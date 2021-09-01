from django.shortcuts import render
from  store.models import Product
from store.views import ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    
        # Get the Reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'includes/about.html')

def contact(request):
    return render(request, 'includes/contact.html')
