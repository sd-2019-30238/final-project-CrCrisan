from django.db import models
from Cont.models import Cont
# Create your models here.
class Tranzactie(models.Model):
    CATEGORII = (
        ('Ne', 'Necunoscut'),
        ('Tr', 'Transport'),
        ('Al', 'Alimente'),
        ('Tra', 'Transfer'),
        ('Cu', 'Cumparaturi'), 
    )
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cont = models.ForeignKey(Cont, on_delete = models.CASCADE, null=True, blank=True)
    categorie = models.CharField(max_length = 100, choices = CATEGORII, default = 'Ne')
    total = models.IntegerField(default = 0)
    informatii = models.CharField(max_length = 200, null=True, blank=True)

    def __str__(self):
        return "Categoria " + str(self.categorie) + ", total : " + str(self.total)