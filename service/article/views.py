# -*- coding: utf-8 -*-
from service.article.models import Article
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

class ProviderDetail(DetailView):
    model = Article

    def get_object(self):
        service = self.kwargs.get('service')
        article = self.kwargs.get('article')
        queryset = Article.objects.filter(service__slug=service)
        return get_object_or_404(queryset, slug=article)
