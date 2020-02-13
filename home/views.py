from django.shortcuts import render, redirect, reverse


# Create your views here.
def home(request):
    """A view that renders the home page"""
    return render(request, "home.html")


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})