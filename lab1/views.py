# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

t = 0
s = 0
b = 0
e = 0
p = 0
f = ''
students_stats = []
subject_stat = []
excellent_students = " "
bad_students = " "

def average(a, b, c, d, e):
    return ((a+b+c+d+e)/5.0)

class Person:
    def __init__(self, fio):
        global f
        f = fio
        students_stats.append(
            {
                'fio': fio
            }
        )
        f = fio

class Student(object):
    def __init__(self, id, person, group, age):
        students_stats[len(students_stats)-1].update(
            {
                'id': id,
                'person': person,
                'group': group,
                'age': age
            }
        )

class Subject(object):
    def __init__(self, id, name, rage):
        subject_stat.append(
            {
                'id': id,
                'name': name,
                'average': rage
            }
        )

class Score(object):
    def __init__(self, name ,student_id, timp, bsbd, philosophy, english, sport):
        global t, b, p, e, s , excellent_students, bad_students
        students_stats[len(students_stats)-1].update(
            {
                'student_id': id,
                'timp': timp,
                'bsbd': bsbd,
                'philosophy': philosophy,
                'english': english,
                'sport': sport,
                'average': average(timp, bsbd, philosophy, english, sport)
            }
        )
        if (timp + bsbd + philosophy + english + sport)/5.0 > 4.5:
            excellent_students = excellent_students + name + ', '
        if (timp + bsbd + philosophy + english + sport)/5.0 < 3.0:
            bad_students = bad_students + name + ', '

        t += timp
        b += bsbd
        p += philosophy
        e += english
        s += sport

Student(1, Person('Кузнецов Алексей Евгеньевич'), 743, 21)
Score('Кузнецов Алексей Евгеньевич', 1, 5, 4, 3, 2, 4)

Student(2, Person('Иванов Максим Викторович'), 743, 19)
Score('Иванов Максим Викторович', 2, 4, 5, 4, 3, 5)

Student(3, Person('Павлова Елена Михайловна'), 743, 19)
Score('Павлова Елена Михайловна',3, 5, 5, 5, 5, 5)

Student(4, Person('Сергеева Алена Дмитриевна'), 743, 20)
Score('Сергеева Алена Дмитриевна', 1, 4, 4, 4, 4, 4)

Student(5, Person('Дроздов Михаил Николаевич'), 743, 19)
Score('Дроздов Михаил Николаевич',1, 3, 2, 2, 3, 4)

Student(6, Person('Николаева Ирина Васильевна'), 743, 20)
Score('Николаева Ирина Васильевна', 6, 5, 5, 4, 5, 5)

Student(7, Person('Петров Олег Олегович'), 743, 19)
Score('Петров Олег Олегович', 7, 5, 4, 4, 3, 5)

Student(8, Person('Яблокова Юлия Вячеславовна'), 743, 21)
Score('Яблокова Юлия Вячеславовна', 1, 3, 5, 4, 5, 3)

Student(9, Person('Малкин Руслан Николаевич'), 743, 19)
Score('Малкин Руслан Николаевич', 1, 4, 5, 4, 5, 3)

Student(10, Person('Алексеева Екатерина Алексеевна'), 743, 18)
Score('Алексеева Екатерина Алексеевна', 1, 4, 3, 3, 2, 2)

Subject(1, "ТиМП", t/10.0)
Subject(2, "Базы данных", b/10.0)
Subject(3, "Философия", p/10.0)
Subject(4, "Иностранный язык", e/10.0)
Subject(5, "Физическая культура", s/10.0)

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_stats,
                'subject_stat': subject_stat,
                'excellent_students': excellent_students,
                'bad_students': bad_students
            }
        )
        return context

