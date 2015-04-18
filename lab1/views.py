# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


students_list = []

class Student:
    def __init__(self, fio, group, age):
        students_list.append({
            'fio': self.fio,
            'group': self.group,
            'age': self.age,
        })


Student('Gurakov Ivan', 723, 19)
Student('Mukovkin Dmitry',)




class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [{'age': x.id, 'fio': x.fio, 'age': x.age} for x in students_list],
                #     {
                #         'id': 1,
                #         'fio': 'Someone',
                #         'age': 18
                #         # 'timp': 2,
                #         # 'eis': 3,
                #         # 'philosophy': 4,
                #         # 'english': 5,
                #         # 'sport': 2.3,
                #         # 'average': 2.3,
                #     }
                #     ,
                #     {
                #         'id': 2,
                #         'fio': 'gia',
                #         'age': 20
                #         # 'timp': 4,
                #         # 'eis': 4,
                #         # 'philosophy': 4,
                #         # 'english': 4,
                #         # 'sport': 5,
                #         # 'average': 4.2,
                #     }
                # ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context




class Subject:
    pass

class Score:
    # Subject,
    pass