from django.shortcuts import render, redirect
from Tranzactie import forms
from Tranzactie.models import Tranzactie
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required()
def addTranzactie(request):
    if request.method == 'POST':
        form = forms.AddTranzactie(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
        else:
            return render(request, 'Tranzactie/AddTranzactie.html', {'form':form})
    else:
        form = forms.AddTranzactie(request.user)
    return render(request, 'Tranzactie/AddTranzactie.html', {'form':form})

@login_required()
def listTranzactii(request):
    lista = Tranzactie.objects.all().order_by('-data')
    return render(request, 'Tranzactie/ListAll.html', {'lista' : lista})

def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def aprobareCredite(request):
    return redirect('HomePage')