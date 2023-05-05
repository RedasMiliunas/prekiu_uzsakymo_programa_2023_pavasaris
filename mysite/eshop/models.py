from django.db import models

# Create your models here.
class Status(models.Model):
    #id stulpelis priskiriamas automatiskai (nereikia kurti, bet reikia zinoti, kad turi ID!)
    name = models.CharField(verbose_name='Pavadinimas', max_length=50)

class Product(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=50)
    price = models.FloatField(verbose_name='Kaina')

