from django.conf.urls import url, include
from .views import all_products, about, searchresults



urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', searchresults, name='searchresults'),
    url(r'^about/$', about, name='about'),
]