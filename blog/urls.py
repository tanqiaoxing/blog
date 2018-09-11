from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^comic/(?P<pk>[0-9]+)/$', views.comic, name='comic'),
    url(r'^poem/(?P<pk>[0-9]+)/$', views.poem, name='poem'),
    url(r'^nature/(?P<pk>[0-9]+)/$', views.nature, name='nature'),
    url(r'^funny/(?P<pk>[0-9]+)/$', views.funny, name='funny'),
]
