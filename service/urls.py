# -*- coding: utf-8 -*-
from django.conf.urls import include, url  # noqa
from service.views import ServiceList
from service.views import ServiceDetail
from django.urls import include, path, re_path


urlpatterns = [
    #url(r'^$', ServiceList.as_view()),
    path('<slug>/', ServiceDetail.as_view()),
]
