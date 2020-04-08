from django.conf.urls import url, include
from .views import reviewhome, detail


urlpatterns = [
    url(r'^$', reviewhome, name='reviewhome'),
    url(r'^details/(?P<pk>\d+)/$', detail, name='detail'),
]    
