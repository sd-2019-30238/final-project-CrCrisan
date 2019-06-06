from django.db import models
from Cont.models import Cont

# Create your models here.
class Imprumut(models.Model):
    STATUS = (
        ('p', 'p'),
        ('a', 'a'),
        ('r', 'r'),
    )
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cont = models.ForeignKey(Cont, on_delete = models.CASCADE, null=True, blank=True)
    total = models.IntegerField(default = 0)
    informatii = models.CharField(max_length = 200, null=True, blank=True)
    moneda = models.CharField(max_length = 100, choices = Cont.MONEDA, default = "RON")
    status = models.CharField(max_length = 100, choices = STATUS, default = 'p')
    def __str__(self):
        return "Id " + str(self.id) + ", total : " + str(self.total) + " client : " + str(self.cont)