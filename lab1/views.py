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
                        'philosophy': s.philosophy.value,
                        'english': s.english.value,
                        'sport': s.sport.value,
                        'average': s.average,

                    }
                    for s in [statis1, statis2, statis3, statis4, statis5, statsred]
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


class Score:
    def __init__(self, student, subject, value):
        self.student = student
        self.subject = subject
        self.value = value

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Statistics:
    def __init__(self):
        self.stat = ()

    def student(self, id, group, age):
        self.student = Student(id, group, age)

    def score(self, timp, eis, philosophy, english, sport):
        self.timp = Score(self.student, Subject(1, 'timp'), timp)
        self.eis = Score(self.student, Subject(2, 'eis'), eis)
        self.philosophy = Score(self.student, Subject(3, 'philosofy'), philosophy)
        self.english = Score(self.student,  Subject(4, 'english'), english)
        self.sport = Score(self.student, Subject(5, 'sport'), sport)

    def average(self):
        self.average = float(self.timp.value + self.eis.value + self.philosophy.value + self.english.value
                             + self.sport.value)/5.0


statis1 = Statistics()
statis1.student = Student(1, 743, 20)
statis1.student.fio = 'Иванов Алексей Олегович'
statis1.score(2, 3, 3, 3, 2)

statis2 = Statistics()
statis2.student = Student(2,743,19)
statis2.student.fio = 'Девятериков Дмитрий Константинович'
statis2.score(4,5,3,4,5)

statis3 = Statistics()
statis3.student = Student(3,723,19)
statis3.student.fio = 'Коновалов Алексей Олегович'
statis3.score(5,4,4,5,4)

statis4 = Statistics()
statis4.student = Student(4,773,20)
statis4.student.fio = 'Дьяконова Екатерина Сергеевна'
statis4.score(5,5,4,5,5)

statis5 = Statistics()
statis5.student = Student(5,723,20)
statis5.student.fio = 'Раднаев Виктор Алексеевич'
statis5.score(4,3,4,4,5)


for s in [statis1, statis2, statis3, statis4, statis5]:
    s.average()
    excellent = [s.student.fio for s in [statis1, statis2, statis3, statis4, statis5] if s.average >= 4.5]
    bad = [s.student.fio for s in [statis1, statis2, statis3, statis4, statis5] if s.average <= 3]
    excellent_students = ', '.join(excellent)
    bad_students = ', '.join(bad)

timp = 0
eis = 0
philosophy = 0
english = 0
sport = 0

for s in [statis1, statis2, statis3, statis4, statis5]:
    timp += s.timp.value/5.0
    eis += s.eis.value/5.0
    philosophy += s.philosophy.value/5.0
    english += s.english.value/5.0
    sport += s.sport.value/5.0

statsred = Statistics()
statsred.student = Student('', '', '')
statsred.student.fio = 'Средний балл'
statsred.score(timp, eis, philosophy, english, sport)

