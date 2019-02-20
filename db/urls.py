from django.urls import path

from .views import HomePageView, GeneDetailView

urlpatterns = [
    path('gene/<str:name>/', GeneDetailView.as_view(), name="gene"),
    path('search/', GeneDetailView.as_view(), name="gene"),
    path('', HomePageView.as_view(), name="home"),
]
