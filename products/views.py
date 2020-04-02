from django.shortcuts import render, redirect, reverse
from .models import Product, Review

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


def get_reviews(request):
    """
    Create a view that will return a list
    of reviews
    """
    products = Product.objects.all()
    reviews = Review.objects.all()
    return render(request, "reviews.html", {'products': products}, {'reviews': reviews})

