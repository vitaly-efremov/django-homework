# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


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
                        'timp': s.timp.value,
                        'eis': s.eis.value,
                        'philosophy': s.fil.value,
                        'english': s.eis.value,
                        'sport': s.fiz.value,
                        'average': s.average,
                    }
                    for s in [stat1, stat2, stat3, stat4, stat5, stat6, stat7]
                ],
                'excellent_students': excellent_students,
                'bad_students': bad_students
            }
        )
        return context


class Person:
    def __init__(self, fio):
        self.fio = fio


class Student(Person):
     def __init__(self, id, group, age):
        self.id = id
        self.group = group
        self.age = age


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

sub1 = Subject(1, 'timp')
sub2 = Subject(2, 'eis')
sub3 = Subject(3, 'fil')
sub4 = Subject(4, 'inz')
sub5 = Subject(5, 'fiz')


class Score:
    def __init__(self, student, subject, value):
        self.student = student
        self.subject = subject
        self.value = value


class Statistics:
    def __init__(self):
        self.stat = ()

    def student(self, id, group, age):
        self.student = Student(id, group, age)

    def score(self, timp, eis, fil, inz, fiz):
        self.timp = Score(self.student, sub1, timp)                 #студент, которого задали выше
        self.eis = Score(self.student, sub2, eis)
        self.fil = Score(self.student, sub3, fil)
        self.inz = Score(self.student, sub4, inz)
        self.fiz = Score(self.student, sub5, fiz)

    def average(self):
        self.average = float(self.fiz.value + self.eis.value + self.fil.value + self.inz.value + self.inz.value)/5


stat1 = Statistics()
stat1.student = Student(1, 743, 19)
stat1.student.fio = 'Алексин Павел'
stat1.score(4, 4, 5, 5, 4)

stat2 = Statistics()
stat2.student = Student(2, 743, 19)
stat2.student.fio = 'Вершинин Артем'
stat2.score(3, 2, 4, 2, 2)

stat3 = Statistics()
stat3.student = Student(3, 743, 19)
stat3.student.fio = 'Зарипов Данил'
stat3.score(4, 4, 4, 4, 4)

stat4 = Statistics()
stat4.student = Student(4, 743, 19)
stat4.student.fio = 'Звягинцев Евгений'
stat4.score(5, 4, 5, 4, 5)

stat5 = Statistics()
stat5.student = Student(5, 743, 20)
stat5.student.fio = 'Кайзер Екатерина'
stat5.score(5, 5, 5, 5, 5)

stat6 = Statistics()
stat6.student = Student(6, 743, 19)
stat6.student.fio = 'Ковалев Вячеслав'
stat6.score(5, 5, 5, 5, 5)

stat7 = Statistics()
stat7.student = Student(7, 743, 19)
stat7.student.fio = 'Койшинов Тимур'
stat7.score(5, 3, 2, 5, 5)

for s in [stat1, stat2, stat3, stat4, stat5, stat6, stat7]:
    s.average()
excellent = [s.student.fio for s in [stat1, stat2, stat3, stat4, stat5, stat6, stat7] if s.average >= 4.5]
bad = [s.student.fio for s in [stat1, stat2, stat3, stat4, stat5, stat6, stat7] if s.average <= 2.5]
excellent_students = ', '.join(excellent)
bad_students = ', '.join(bad)