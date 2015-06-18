from django.db import models

class Client(models.Model):
    nomer_id = models.IntegerField()
    familia = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    otchestvo = models.CharField(max_length=30)

    pol = models.CharField(max_length=7)
    data = models.DateField()
    mobile = models.IntegerField()
    nomer_dogovora = models.IntegerField()


class Dogov(models.Model):
    iddog = models.IntegerField()
    uslov = models.TextField()
    data1 = models.DateField()
    idcard = models.IntegerField()


class Card(models.Model):
    idcard = models.IntegerField()
    valid = models.BooleanField()
    data2 = models.DateField()
    nomer_oper = models.IntegerField()


class Oper(models.Model):
    nomer_oper = models.IntegerField()
    opera = models.TextField()
    data3 = models.DateField()

# Create your models here.