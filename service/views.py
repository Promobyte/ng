# -*- coding: utf-8 -*-
from django.views.generic import ListView
from service.models import Service

class ServiceList(ListView):
    context_object_name = 'title'
    queryset = Service.objects.all()

