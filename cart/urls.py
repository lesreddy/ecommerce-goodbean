from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

'''All of the below urls were referenced from the e-commerce tutorial on the code institute Website, they are of not my own making'''

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]