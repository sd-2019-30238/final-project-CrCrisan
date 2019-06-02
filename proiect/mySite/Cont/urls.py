from django.contrib import admin
from django.urls import path
from Cont.views import listCont, listOp,transfer, transfer2,plataFactura

app_name = 'Cont'

urlpatterns = [
    path('', listCont, name = "Home"),
    path('op', listOp, name = "ListOp"),
    path('tr1', transfer, name = "Tr1"),
    path('tr2', transfer2, name = "Tr2"),
    path('PlataFactura', plataFactura, name = "PlataFactura"),
    
]
