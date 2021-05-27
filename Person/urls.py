from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PersonDetail.as_view(), name='detail'),
    url(r'^nuevo$', PersonCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', PersonUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', PersonDelete.as_view(), name='delete'),
]