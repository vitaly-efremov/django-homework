# -*- coding: utf-8 -*-
#импортируем методы рандомных последовательности и целого числа из random
from random import sample,randint
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': 
                [
                    {
                        'id': 1,
                        'fio': 'Julia',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.3,
                    },
                    {
                        'id': 2,
                        'fio': 'Bob',
                        'timp': 4,
                        'eis': 4,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 3,
                        'average': 2.3,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Student:
    def __init__(self,name):
        self.id=id(self)
        self.name=name
        state=dict()
    def set_rand_mark(self):
        pass



class Statistics:
    # student_id, [Subjects]
    def stud_rand():
        """
        в качестве параметров словарь фамилий
        в рандоме надо инициализировать список объектов 
        типа студент с присвоением фамилий
        """
        pass
    pass

class Subject:
    pass

class Score:
    # Subject,
    pass


"""
#возьмём список
a=['red','green','blue','violent','orange','purple','yellow','black']
#отсортируем его
a.sort()
#импортируем метод рандомной последовательности из random
from random import sample
b=sample(a,len(a))
#теперь можно посмотреть результат рандома
"""