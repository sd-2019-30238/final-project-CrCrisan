from django.db import models
from Cont.models import Cont
from Cont.models import Cont
from django import forms
from django.core.exceptions import ValidationError
# Create your models here.
class Transfer1(models.Model):
    cont1 = models.ForeignKey(Cont, on_delete = None, null=True, blank=True, related_name='cont1')
    cont2 = models.ForeignKey(Cont, on_delete = None, null=True, blank=True, related_name='cont2')
    suma = models.IntegerField(default = 0)



class AddTransfer1(forms.ModelForm):
    class Meta:
        model = Transfer1
        fields = ['cont1', 'cont2', 'suma']
    
    def __init__(self, user, *args, **kwargs):
        super(AddTransfer1, self).__init__(*args, **kwargs)
        self.fields['cont1'].queryset = Cont.objects.filter(user=user)
        self.fields['cont2'].queryset = Cont.objects.filter(user=user)

    def clean(self):
        cd = self.cleaned_data
        cont1 = cd.get('cont1')
        suma = cd.get('suma')
        if cont1.sold < suma:
            raise ValidationError("Sold insuficient")
        return cd

class Transfer2(models.Model):
    cont1 = models.ForeignKey(Cont, on_delete = None, null=True, blank=True, related_name='cont12')
    cont2 = models.IntegerField(default = 0)
    suma = models.IntegerField(default = 0)

class AddTransfer2(forms.ModelForm):
    class Meta:
        model = Transfer2
        fields = ['cont1', 'cont2', 'suma']
    
    def __init__(self, user, *args, **kwargs):
        super(AddTransfer2, self).__init__(*args, **kwargs)
        self.fields['cont1'].queryset = Cont.objects.filter(user=user)

    def clean(self):
        cd = self.cleaned_data
        cont1 = cd.get('cont1')
        cont2 = cd.get('cont2')
        suma = cd.get('suma')
        if cont1.sold < suma:
            raise ValidationError("Sold insuficient")
        try:
            lista = Cont.objects.filter(id = cont2).first()
            if lista == [] or lista == None:
                raise ValidationError("Cont inexistent")
        except:
            raise ValidationError("Cont inexistent")
        return cd

class PlataFacturaF(models.Model):
    cont1 = models.ForeignKey(Cont, on_delete = None, null=True, blank=True, related_name='cont13')
    suma = models.IntegerField(default = 0)
    furnizor = models.CharField(max_length = 200, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    nrFactura = models.IntegerField(default = 0)


class PlataFactura(forms.ModelForm):
    class Meta:
        model = PlataFacturaF
        fields = ['cont1', 'furnizor', 'suma', 'data', 'nrFactura']
    
    def __init__(self, user, *args, **kwargs):
        super(PlataFactura, self).__init__(*args, **kwargs)
        self.fields['cont1'].queryset = Cont.objects.filter(user=user)

    def clean(self):
        try:
            cd = self.cleaned_data
            cont1 = cd.get('cont1')
            suma = cd.get('suma')
            if cont1.sold < suma:
                raise ValidationError("Sold insuficient")
        except:
            raise ValidationError("Erroare Date")
            
        return cd

        