from django.conf.urls import url, include
from .views import all_products
from .views import about

urlpatterns = [
    url(r'^products/$', all_products, name='products'),
    url(r'^about/$', about, name='about')
]