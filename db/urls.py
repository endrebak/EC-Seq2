from django.urls import path

from .views import HomePageView, GeneListView

urlpatterns = [
    path('gene/<str:name>/', GeneListView.as_view(), name="gene"),
    path('search/', GeneListView.as_view(), name="search"),
    path('', HomePageView.as_view(), name="home"),
]
