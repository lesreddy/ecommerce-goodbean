from django.shortcuts import render
from products.models import Product

# Create your views here.

'''Part of the below view was referenced from the e-commerce tutorial on the code institute Website, they are of not my own making, all I changed was the name of the page rendered'''

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "searchresults.html", {"products": products})