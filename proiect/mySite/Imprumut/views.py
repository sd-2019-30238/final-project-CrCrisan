from django.shortcuts import render, redirect
from Tranzactie import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from Cont.forms import AddTransfer1,AddTransfer2, PlataFactura
from Tranzactie.models import Tranzactie
from Imprumut.forms import AddImprumut
from Imprumut.models import Imprumut
# Create your views here.
# Create your views here.

@login_required()
def addImprumut(request):
    if request.method == 'POST':
        form = AddImprumut(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
        return render(request, 'Imprumut\Imprumut.html', {'form':form})
    form = AddImprumut(request.user)
    return render(request, 'Imprumut\Imprumut.html', {'form':form})


def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def aprobareCredite(request):
    try:
        lista = Imprumut.objects.all()
    except:
        lista = []
    return render(request, 'Imprumut\ImprumutAll.html', {'lista' : lista})

@login_required()
@user_passes_test(isEmployee)
def editLoan(request, imprumutId):
    if request.method == 'POST':
        imprumut = Imprumut.objects.filter(id = imprumutId).first()
        imprumut.status = 'a'
        imprumut.save()

        cont = imprumut.cont
        cont.sold += imprumut.total
        cont.credit -= imprumut.total
        cont.save()

        return redirect('HomePage')
    else:
        imprumut = Imprumut.objects.filter(id = imprumutId).first()
        loanStatus = imprumut.status
    return render(request, 'Imprumut/EditareImprumut.html', {'imprumut' : imprumut, 'loanStatus' : loanStatus})
    # EditareImprumut.html