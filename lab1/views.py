# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        Subjects = [Subject(1, "timp")]
        Subject(2, "eis")
        Subject(3, "philosophy")
        Subject(4, "english")
        Subject(5, "sport")


        list_students = [
            Student(1, "surname1", name1, patronymic1, group1, 20),
            Student(2, surname2, name2, patronymic2, group2, 19),
            Student(3, surname3, name3, patronymic3, group1, 23),
            Student(4, surname4, name4, patronymic4, group2, 24),
            Student(5, surname5, name5, patronymic5, group1, 25),
            Student(6, surname6, name6, patronymic6, group2, 23),
            Student(7, surname7, name7, patronymic7, group3, 22),
            Student(8, surname8, name8, patronymic8, group3, 21),
            Student(9, surname9, name9, patronymic9, group2, 21),
            Student(10, surname10, name10, patronymic10, group2, 19)
        ]

        List_Score = Score()
        List_Score.add_fixed(1, 4, 5, 3, 4, 2)
        List_Score.add_fixed(2, 4, 5, 5, 5, 4)
        List_Score.add_fixed(3, 4, 5, 5, 5, 4)
        List_Score.add_fixed(4, 2, 3, 5, 5, 4)
        List_Score.add_fixed(5, 2, 2, 3, 3, 2)
        List_Score.add_fixed(6, 4, 5, 2, 5, 4)
        List_Score.add_fixed(7, 4, 5, 5, 5, 4)
        List_Score.add_fixed(8, 4, 5, 5, 3, 4)
        List_Score.add_fixed(9, 2, 5, 5, 5, 4)
        List_Score.add_fixed(10, 2, 1, 1, 1, 4)

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Someone',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.3,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Person:
    def __init__(self, familia, imya, otchestvo):
        self.familia = familia
        self.imya = imya
        self.otchestvo = otchestvo

class Student(Person):
    def __init__(self, id, familia, imya, otchestvo, group, age):
        self.id = id
        self.person = Person(familia, imya, otchestvo)
        self.group = group
        self.age = age

    def show(self):
        print self.id, self.group, self.age

class Subject:
    list = []
    def __init__(self, id, name):
        self.list.append((id, name))

    def show(self):
        print self.id, self.name

class Score:
    table = []
    def __init__(self):
        pass

    def add(self, st_id, su_id, value):
        self.table.append((st_id, su_id, value))

    def add_fixed(self, st_id, value1, value2, value3, value4, value5):
        self.table.append((st_id, 1, value1))
        self.table.append((st_id, 2, value2))
        self.table.append((st_id, 3, value3))
        self.table.append((st_id, 4, value4))
        self.table.append((st_id, 5, value5))

