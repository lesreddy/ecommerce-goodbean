from django.conf.urls import url, include
from .views import reviewhome, detail, add_review

urlpatterns = [
    url(r'^$', reviewhome, name='reviewhome'),
    url(r'^details/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^addreview/(?P<id>\d+)/', add_review, name='add_review'),
]    
