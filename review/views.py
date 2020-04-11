from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm
from django.db.models import Avg



def reviewhome(request):
    ''' A view to render the home page of the review section showing all products'''
    products = Product.objects.all()

    return render(request, 'review_content.html', {"products":products} )


def detail(request, id):
    ''' A view which renders the specific product selected with more detail'''
    product = Product.objects.get(id=id) 
    reviews = Review.objects.filter(product=id).order_by("-comment")
    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "product": product,
        "reviews": reviews,
        "average": average,
    }

    return render(request, 'review_details.html', context)


def add_review(request, id):
    """
    View for adding reviews via use of the ReviewForm whilst implementing checks to see if user is authenticated
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
        messages.info(request, "You need to log in to post a review!")
        return redirect(reverse('login'))


   