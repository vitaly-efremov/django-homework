from django.db import models
from datetime import datetime

class Teacher(models.Model):
    fio = models.TextField()
    date = models.DateField(default = datetime.now)
    WE = models.TextField()

    def __str__(self):
        return '{}, date:{}, WE: {}'.format(
            self.fio,
            self.date,
            self.WE
        )

class Subject(models.Model):
    subject_name = models.TextField()
    cycle = models.TextField()

    def __str__(self):
        return '{}, cycle: {}'.format(
         self.subject_name,
         self.cycle
        )


class Workload(models.Model):

    #fio = models.ForeignKey(Teacher, related_name='fio')
   # subject = models.ForeignKey(Subject)
    quarter = models.TextField(default = 1)
    number_of_hours = models.TextField(default = 120)

    def __str__(self):
        return 'quarter: {}, number_of_hours: {}'.format(
         
         self.quarter,
         self.number_of_hours
        )

