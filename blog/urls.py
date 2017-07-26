# author: lin,leo
# date: Jul 27, 2017

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list')    # map home url to post_list class in view
]