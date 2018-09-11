from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^comment/comic/(?P<comic_pk>[0-9]+)/$', views.comic_comment, name='comic_comment'),
    url(r'^comment/poem/(?P<poem_pk>[0-9]+)/$', views.poem_comment, name='poem_comment'),
    url(r'^comment/nature/(?P<nature_pk>[0-9]+)/$', views.nature_comment, name='nature_comment'),
    url(r'^comment/funny/(?P<funny_pk>[0-9]+)/$', views.funny_comment, name='funny_comment'),
]