from django.contrib import admin
from django.urls import path
from Imprumut.views import addImprumut, aprobareCredite, editLoan

app_name = 'Imprumut'

urlpatterns = [
    path('add', addImprumut, name = "AddImprumut"),
    path('edit', aprobareCredite, name = "AprobareImprumut"),
    path('edit-imp/<int:imprumutId>', editLoan, name = "EditLoan" )
]
