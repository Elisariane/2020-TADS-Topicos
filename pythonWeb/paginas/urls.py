from django.urls import path
from .views import PaginaInicialView, SobreView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]