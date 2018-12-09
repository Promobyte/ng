# -*- coding: utf-8 -*-
from django.conf.urls import include, url  # noqa
from service.views import ServiceList
from django.urls import include, path, re_path


urlpatterns = [
    url(r'^$', ServiceList.as_view()),
    path('<slug>/', ServiceList.as_view()),
]
