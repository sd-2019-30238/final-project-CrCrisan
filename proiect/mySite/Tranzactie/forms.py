from django import forms
from Tranzactie import models
from Cont.models import Cont

class AddTranzactie(forms.ModelForm):
    class Meta:
        model = models.Tranzactie
        fields = ['cont', 'categorie', 'total', 'informatii']
    
    def __init__(self, user, *args, **kwargs):
        super(AddTranzactie, self).__init__(*args, **kwargs)
        self.fields['cont'].queryset = Cont.objects.filter(user=user)