from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.lista_productos, name='lista_productos'),
]