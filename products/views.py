from django.shortcuts import render, redirect, reverse
from .models import Product
from review.models import Review

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def about(request):
    """ return the about.html page """
    return render(request, "about.html")

def searchresults(request):
    """ return the product search page """
    products = Product.objects.all()
    return render(request, "searchresults.html")


