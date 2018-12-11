# -*- coding: utf-8 -*-
from service.provider.models import Provider
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

class ProviderDetail(DetailView):
    model = Provider

    def get_object(self):
        service = self.kwargs.get('service')
        provider = self.kwargs.get('provider')
        queryset = Provider.objects.filter(service__slug=service)
        return get_object_or_404(queryset, slug=provider)
