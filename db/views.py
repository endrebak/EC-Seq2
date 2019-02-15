from django.views.generic import ListView
from .models import Gene


class HomePageView(ListView):
    model = Gene
    template_name = "home.html"
