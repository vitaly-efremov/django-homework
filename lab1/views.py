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

Subject('ТиМП')
Subject('ЭиС')
Subject('Философия')
Subject('Иностранный язык')
Subject('Физическая культура')


score_list = []

class Score:
    def __init__(self, id_student, id_subject, value):
        score_list.append({
            'id': id_student,
            'id_subject': id_subject,
            'value': value
        })

Score(1,1,5)
Score(1,2,4)
Score(1,3,5)
Score(1,4,5)
Score(1,5,5)
Score(2,1,4)
Score(2,2,3)
Score(2,3,4)
Score(2,4,5)
Score(2,5,3)
Score(3,1,2)
Score(3,2,4)
Score(3,4,4)
Score(3,5,4)
Score(3,3,3)

# print score_list[0]['id']
sum = 0
for x in students_list:
    for y in score_list:
        if x['id'] == y['id']:
            mnoj = {str(y['id_subject']): y['value']}
            x.update(mnoj)
            sum += y['value']
    mnoj = {'average': float(sum)/len(subject_list)}
    print mnoj
    x.update(mnoj)
    sum=0

exelent_students = [{'fio': x['fio']} for x in students_list if x['average']>4.5]

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
                'bad_students': 'Student C, Student D'
            }
        )
        return context


