from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Cont(models.Model):
    MONEDA = (
        ('EUR', 'EURO'),
        ('RON', 'RON')
    )
    sold = models.IntegerField(default=0)
    nume = models.CharField(max_length = 20, default = "")
    credit = models.IntegerField(default=0)
    tipCont = models.CharField(max_length = 100, choices = MONEDA, default = "RON")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return "Id : " + str(self.id) + ", Name : " + str(self.nume)