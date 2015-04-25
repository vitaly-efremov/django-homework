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

subject_list = []

class Subject:
    def __init__(self, name):
        subject_list.append({
            'name': name,
            'id': (len(subject_list)+1)
        })



score_list = []

class Score:
    def __init__(self, id_student, id_subject, value):
        score_list.append({
            'id': id_student,
            'id_subject': id_subject,
            'value': value
        })

Subject('ТиМП')
Subject('ЭиС')
Subject('Философия')
Subject('Иностранный язык')
Subject('Физическая культура')
Subject('Дискретная математика')

Student('Гураков Иван', 723, 19)
Score(1, 1, 5)
Score(1, 2, 4)
Score(1, 3, 5)
Score(1, 4, 5)
Score(1, 5, 5)
Score(1, 6, 5)

Student('Муковкин Дмитрий', 723, 20)
Score(2, 1, 4)
Score(2, 2, 3)
Score(2, 3, 4)
Score(2, 4, 5)
Score(2, 5, 3)
Score(2, 6, 4)

Student('Иванов Евгений', 723, 23)
Score(3, 1, 2)
Score(3, 2, 3)
Score(3, 4, 3)
Score(3, 5, 2)
Score(3, 3, 3)
Score(3, 6, 4)

Student('Никитин Иван', 723, 20)
Score(4, 1, 4)
Score(4, 2, 3)
Score(4, 3, 4)
Score(4, 4, 4)
Score(4, 5, 3)
Score(4, 6, 2)

Student('Ондар Регина', 723, 23)
Score(5, 1, 2)
Score(5, 2, 3)
Score(5, 3, 1)
Score(5, 4, 4)
Score(5, 5, 2)
Score(5, 6, 2)

Student('Сагалакова Илона', 723, 20)
Score(6, 1, 5)
Score(6, 2, 4)
Score(6, 3, 5)
Score(6, 4, 5)
Score(6, 5, 5)
Score(6, 6, 4)

Student('Бровкин Никита', 723, 19)
Score(7, 1, 5)
Score(7, 2, 5)
Score(7, 3, 5)
Score(7, 4, 4)
Score(7, 5, 5)
Score(7, 6, 5)

Student('Харлам Михаил', 723, 19)
Score(8, 1, 4)
Score(8, 2, 3)
Score(8, 3, 4)
Score(8, 4, 3)
Score(8, 5, 4)
Score(8, 6, 5)

Student('Манов Виталий', 723, 20)
Score(9, 1, 5)
Score(9, 2, 5)
Score(9, 3, 5)
Score(9, 4, 5)
Score(9, 5, 5)
Score(9, 6, 5)

Student('Бикмухаметов Алексей', 723, 20)
Score(10, 1, 4)
Score(10, 2, 4)
Score(10, 3, 4)
Score(10, 4, 4)
Score(10, 5, 4)
Score(10, 6, 4)


sum = 0
for x in students_list:
    for y in score_list:
        if x['id'] == y['id']:
            mnoj = {str(y['id_subject']): y['value']}
            x.update(mnoj)
            sum += y['value']
    mnoj = {'average': float(sum)/len(subject_list)}
    x.update(mnoj)
    sum = 0

for x in subject_list:
    for y in score_list:
        if x['id'] == y['id_subject']:
            sum += y['value']
    mnoj = {'average': float(sum)/len(students_list)}
    x.update(mnoj)
    sum=0

exelent_students = [{'fio': x['fio']} for x in students_list if x['average'] > 4.5]

bad_students = [{'fio': x['fio']} for x in students_list if x['average'] < 3]


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_list,
                'subject_list': subject_list,
                'score_list': score_list,
                'exelent_students': exelent_students,
                'bad_students': bad_students
            }
        )
        return context

