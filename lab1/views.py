# -*- coding: utf-8 -*-
import random
from django.views.generic.base import TemplateView

class Person:
    def __init__(self, fio):
        #конструктор класса Person
        self.fio = fio
class Student(Person):
     def __init__(self, id, group, age):
         #конструктор класса студенты
        self.id = id
        self.group = group
        self.age = age
class Subject:
    def __init__(self, id, name):
        #конструктор класса предмет
        self.id = id
        self.name = name
subject1 = Subject(1, 'terver')
subject2 = Subject(2, 'dm')
subject3 = Subject(3, 'bd')
subject4 = Subject(4, 'finansy')
subject5 = Subject(5, 'timp')
class Score:
    def __init__(self, student, subject, value):
        #конструктор класса Score
        self.student = student
        self.subject = subject
        self.value = value
class Statistics:
    def __init__(self):
        self.st = ()
    def student(self, id, group, age):
        self.student = Student(id, group, age)
    def score(self, terver, dm, bd, finansy, timp):
        self.terver = Score(self.student, subject1, terver)
        self.dm = Score(self.student, subject2, dm)
        self.bd = Score(self.student, subject3, bd)
        self.finansy = Score(self.student, subject4, finansy)
        self.timp = Score(self.student, subject5, timp)
    def average(self):
        self.average = float(self.timp.value + self.terver.value + self.dm.value + self.bd.value + self.finansy.value)/5
#Задание фио студентов,оценок, возраста, группы
st1 = Statistics()
st1.student = Student(1, 743, 18)
st1.student.fio = 'Алексеев Алексей Алексеевич'
st1.score(4, 4, 3, 3, 4)
st2 = Statistics()
st2.student = Student(2, 743, 19)
st2.student.fio = 'Иванов Иван Иванович'
st2.score(3, 4, 5, 5, 4)
st3 = Statistics()
st3.student = Student(3, 743, 21)
st3.student.fio = 'Михайлов Михаил Михайлович'
st3.score(5, 5, 5, 5, 5)
st4 = Statistics()
st4.student = Student(4, 743, 20)
st4.student.fio = 'Николаев Николай Николаевич'
st4.score(2, 3, 2, 2, 3)
st5 = Statistics()
st5.student = Student(5, 743, 19)
st5.student.fio = 'Петров Петр Петрович'
st5.score(2, 5, 4, 5, 3)
for s in [st1, st2, st3, st4, st5]:
    s.average()
excellent = [s.student.fio for s in [st1, st2, st3, st4, st5] if s.average >= 4.5]
bad = [s.student.fio for s in [st1, st2, st3, st4, st5] if s.average <= 3]
excellent_students = ', '.join(excellent)
bad_students = ', '.join(bad)
terver = 0
timp = 0
dm = 0
bd = 0
finansy = 0
for s in [st1, st2, st3, st4, st5]:
    terver += round(float(s.terver.value)/5,1)
    dm += round(float(s.dm.value)/5,1)
    bd += round(float(s.bd.value)/5,1)
    timp += round(float(s.timp.value)/5,1)
    finansy += round(float(s.finansy.value)/5,1)
sb = Statistics()
sb.student = Student(' ', 743, ' ')
sb.student.fio = 'Средний балл'
sb.score(terver, dm, bd, timp, finansy)
sb.average = ''

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                       'id': s.student.id,
                       'fio': s.student.fio,
                       'terver': s.terver.value,
                       'dm': s.dm.value,
                       'bd': s.bd.value,
                       'finansy': s.finansy.value,
                       'timp': s.timp.value,
                       'average': s.average,
                    }
                for s in [st1, st2, st3, st4, st5]
            ],
            'excellent_students': excellent_students,
            'bad_students': bad_students
            }
        )
        return context
