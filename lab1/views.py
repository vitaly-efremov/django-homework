# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


students_list = []

class Student:
    def __init__(self, fio, group, age):
        students_list.append({
            'fio': fio,
            'group': group,
            'age': age,
            'id': (len(students_list)+1)
        })

Student('Gurakov Ivan', 723, 19)
Student('Mukovkin Dmitry', 723, 20)
Student('Ivanov Evgeni', 723, 23)

subject_list = []

class Subject:
    def __init__(self, name):
        subject_list.append({
            'subject': name,
            'id': (len(subject_list)+1)
        })

Subject('Философия')
Subject('Английский')
Subject('Тер. Вер')
Subject('Программирование')

score_list = []

class Score:
    def __init__(self, id_student, id_subject, value):
        score_list.append({
            'id': id_student,
            'id_subject': id_subject,
            'value': value
        })



for x in score_list:
    for y in students_list:
        if x['id'] == y['id']:
            y.app({x['id_subject']: x['value']})

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_list,
                'subject_list': subject_list,
                'score_list': score_list,
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


