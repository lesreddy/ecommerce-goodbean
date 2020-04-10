from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from products.models import Product
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def reviewhome(request):
    products = Product.objects.all()

    return render(request, 'review_content.html', {"products":products} )


def detail(request, id):
    ''' A view which renders the specific product selected with more detail'''
    product = Product.objects.get(id=id) 
    reviews = Review.objects.filter(product=id).order_by("-comment")

    context = {
        "product": product,
        "reviews": reviews,
    }

    return render(request, 'review_details.html', context)


def add_review(request, id):
    """
    View for adding reviews via use of the ReviewForm.
    """
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.product = product
                data.save()
                return redirect("detail", id)
            else:
                if not form.is_valid():
                    return redirect("detail", id)
        else:
            form = ReviewForm()
        return render(request, 'review_details.html', {"form": form})
    else:
        return redirect(reverse('login'))


   