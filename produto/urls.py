from django.urls import path
from .views import *

urlpatterns=[
    path('', lista_produtos, name='lista_produtos'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
]