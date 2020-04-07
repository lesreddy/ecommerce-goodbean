from django.conf.urls import url, include
from .views import reviewhome

urlpatterns = [
    url(r'^$', reviewhome, name='reviewhome'),
]    
