from django.conf.urls import url
from .views import PersonList

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='list'),
]