from django.conf.urls import url

from .views import IndexView, BoxCreate, FileboxCreate

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^box/add/$', BoxCreate.as_view(), name='add_box'),
    url(r'^filebox/add/$', FileboxCreate.as_view(), name='add_filebox'),
]
