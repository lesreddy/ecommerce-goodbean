from django.shortcuts import render, redirect, reverse
from .models import Product, Review
from .forms import ReviewForm

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
    reviews = Review.objects.all()
    return render(request, "reviews.html", {'reviews': reviews})

def create_or_edit_review(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(get_reviews, review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviewform.html', {'form': form})