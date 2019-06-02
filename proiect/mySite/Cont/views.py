from django.shortcuts import render, redirect
from Tranzactie import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from Cont.models import Cont
from Cont.forms import AddTransfer1,AddTransfer2, PlataFactura
from Tranzactie.models import Tranzactie
from Cont.misc import *
# Create your views here.

@login_required()
def listCont(request):
    try:
        lista = Cont.objects.filter(user = request.user)
    except:
        lista = []
    print(lista)
    return render(request, 'Cont\ContPage.html', {'lista' : lista})

@login_required()
def listOp(request):
    return render(request, 'Operatii\ListOp.html')

@login_required()
def transfer(request):
    if request.method == 'POST':
        form = AddTransfer1(request.user, request.POST, request.FILES)
        if form.is_valid():
            cont1 = form.cleaned_data['cont1']
            cont2 = form.cleaned_data['cont2']
            suma = form.cleaned_data['suma']
            tranzactie = Tranzactie()
            tranzactie.cont = cont1
            tranzactie.categorie = 'Tra'
            tranzactie.total = -suma
            tranzactie.save()
            cont1.sold -= suma
            cont1.save()

            total = CURS_VALUTAR[cont1.tipCont]
            total = total[cont2.tipCont]
            total = int(total * suma)

            tranzactie = Tranzactie()
            tranzactie.categorie = 'Tra'
            tranzactie.cont = cont2
            tranzactie.total = total
            tranzactie.save()

            cont2.sold += total
            cont2.save()
            return redirect('HomePage')
        
        return render(request, 'Operatii\Transfer1.html', {'form':form})
    form = AddTransfer1(request.user)
    return render(request, 'Operatii\Transfer1.html', {'form':form})

@login_required()
def transfer2(request):
    if request.method == 'POST':
        form = AddTransfer2(request.user, request.POST, request.FILES)
        if form.is_valid():
            cont1 = form.cleaned_data['cont1']
            cont2 = form.cleaned_data['cont2']
            cont2 = Cont.objects.filter(id = cont2).first()
            suma = form.cleaned_data['suma']

            tranzactie = Tranzactie()
            tranzactie.cont = cont1
            tranzactie.categorie = 'Tra'
            tranzactie.total = -suma
            tranzactie.save()
            cont1.sold -= suma
            cont1.save()

            total = CURS_VALUTAR[cont1.tipCont]
            total = total[cont2.tipCont]
            total = int(total * suma)

            tranzactie = Tranzactie()
            tranzactie.categorie = 'Tra'
            tranzactie.cont = cont2
            tranzactie.total = total
            tranzactie.save()

            cont2.sold += total
            cont2.save()
            return redirect('HomePage')

        return render(request, 'Operatii\Transfer2.html', {'form':form})
    form = AddTransfer2(request.user)
    return render(request, 'Operatii\Transfer2.html', {'form':form})

@login_required()
def plataFactura(request):
    if request.method == 'POST':
        form = PlataFactura(request.user, request.POST, request.FILES)
        if form.is_valid():
            return redirect('HomePage')
        return render(request, 'Operatii\PlataFactura.html', {'form':form})
    form = PlataFactura(request.user)
    return render(request, 'Operatii\PlataFactura.html', {'form':form})