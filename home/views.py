from django.shortcuts import render, redirect, reverse
from .forms import ContactForm

def home(request):
    """A view that renders the home page"""
    return render(request, "home.html")

def contact(request):
    """ return the contact.html page """
    return render(request, "contact.html")

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def contact(request):
    template = "contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, template, context)