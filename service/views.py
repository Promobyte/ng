# -*- coding: utf-8 -*-
from django.views.generic import ListView
from service.models import Service
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpRequest
from django.http import HttpResponse
class ServiceList(ListView):
    model = Service

class ServiceDetail(DetailView):

    model = Service
    queryset = model.objects.all()


class IndexView(ListView):
    template_name = 'index.html'
    model = Service


