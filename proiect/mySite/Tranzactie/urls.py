
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Tranzactie'

urlpatterns = [
    path('add-tranzactie/', views.addTranzactie, name = "add-tranzactie"),
    path('', views.listTranzactii, name = "list-tranzactii")
]