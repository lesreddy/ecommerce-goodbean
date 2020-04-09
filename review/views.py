from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product, Review
from .forms import *

def reviewhome(request):
    products = Product.objects.all()

    return render(request, 'review_content.html', {"products":products} )


def detail(request, pk):
    ''' A view which renders the specific product selected with more detail'''
    products = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=pk)

    return render(request, 'review_details.html', {"products":products})


def add_review(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=pk)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.product = product
                data.save()
                return redirect("detail", pk)
        else:
            form = ReviewForm()
        return render(request, 'review_details.html', {"form": form})
    else:
        return redirect("accounts:login")