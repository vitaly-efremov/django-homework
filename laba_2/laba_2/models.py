# -*- coding: utf-8 -*-
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    otch = models.CharField(max_length=50)
    passport = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, blank=True)

    def client_name(self):
        return self.fam + ' ' + self.name[0] + '. ' + self.otch[0] + '.'


class Master(models.Model):
    name = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    otch = models.CharField(max_length=50)
    qualification = models.CharField(max_length=35)
    birth = models.DateField()

    def master_name(self):
        return self.fam + ' ' + self.name[0] + '. ' + self.otch[0] + '., ' + self.qualification

class Repairing(models.Model):
    client = models.ForeignKey(Client)
    master = models.ForeignKey(Master)
    min_cost = models.FloatField()
    description = models.CharField(max_length=600)
    date = models.DateField()