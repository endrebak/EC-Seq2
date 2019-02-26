from django.views.generic import ListView, DetailView
from django.shortcuts import get_list_or_404
from .models import Gene

import random

from urllib.request import urlopen
from urllib.parse import quote_plus
import json

class HomePageView(ListView):
    model = Gene
    template_name = "home.html"

    def get_queryset(self):
        pks = random.sample(range(Gene.objects.count()), 5)
        return Gene.objects.filter(pk__in=pks)


from django.shortcuts import render

def search_mygene(term):

    url = "https://mygene.info/v3/query?q={name}&species=rat".format(name=quote_plus(term))
    response = urlopen(url).read()
    return json.loads(response)

class GeneListView(ListView):
    model = Gene
    template_name = "gene_list.html"

    def get_queryset(self):

        name = self.kwargs.get("name") or self.request.GET.get("name").strip()

        result = Gene.objects.filter(name__icontains=name)

        if not len(result):


            symbols = []
            result = search_mygene(name)
            for hit in result["hits"]:
                symbols.append(hit["symbol"])

            result = Gene.objects.filter(name__in=symbols)

        return result

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        object_list = data["object_list"]

        if len(object_list) == 1:
            name = object_list[0].name
            result = search_mygene(name)
            first_hit = result["hits"][0]
            data["gene_description"] = first_hit["name"]
            print(data)

        return data
