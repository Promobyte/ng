# -*- coding: utf-8 -*-
from django.views.generic import ListView
from service.models import Service
from django.views.generic.detail import DetailView
from django.utils import timezone

class ServiceList(ListView):
    context_object_name = 'title'
    queryset = Service.objects.all()

class ServiceDetail(DetailView):

    model = Service
    queryset = model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
