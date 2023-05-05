from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    #id stulpelis priskiriamas automatiskai (nereikia kurti, bet reikia zinoti, kad turi ID!)
    name = models.CharField(verbose_name='Pavadinimas', max_length=50)

class Product(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=50)
    price = models.FloatField(verbose_name='Kaina')

#kuriam pagrindine lentele 'order' (i ja yra 2 foreign key, taip pat reikia import User), is orderio puses many to one rysys:
class Order(models.Model):
    customer = models.ForeignKey(to=User, verbose_name='Vartotojas', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    status = models.ForeignKey(to='Status', verbose_name='Busena', on_delete=models.SET_NULL, null=True, blank=True)
