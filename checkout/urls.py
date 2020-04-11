from django.conf.urls import url
from .views import checkout

'''All of the below urls were referenced from the e-commerce tutorial on the code institute Website, they are of not my own making'''

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]