from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

def reviewhome(request):
    products = Product.objects.all()

    return render(request, 'review_content.html', {"products":products} )


def detail(request, pk):
    ''' A view which renders the specific product selected with more detail'''
    products = get_object_or_404(Product, pk=pk)

    return render(request, 'review_details.html', {"products":products})