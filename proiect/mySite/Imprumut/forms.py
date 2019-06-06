from django import forms
from Tranzactie import models
from Cont.models import Cont
from Imprumut.models import Imprumut

class AddImprumut(forms.ModelForm):
    class Meta:
        model = Imprumut
        fields = ['cont', 'total', 'informatii', 'moneda']
    
    def __init__(self, user, *args, **kwargs):
        super(AddImprumut, self).__init__(*args, **kwargs)
        self.fields['cont'].queryset = Cont.objects.filter(user=user)