from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Gene

import random

class HomePageView(ListView):
    model = Gene
    template_name = "home.html"

    def get_queryset(self):
        pks = random.sample(range(Gene.objects.count()), 5)
        return Gene.objects.filter(pk__in=pks)


from django.shortcuts import render

class GeneDetailView(DetailView):
    model = Gene
    template_name = "gene_detail.html"

    def get_object(self):
        gene = get_object_or_404(Gene, name__iexact=self.kwargs['name'])
        return gene
