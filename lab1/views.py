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
                'students_statistics': all_students,
                'exc_students': exc_students,
                'bad_students': bad_students
            }
        )
        return context


class Student:
    def __init__(self,fio):
        self.id=id(self)-id(self)//10000*10000
        self.fio=fio
        self.state=dict()


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


names=['Alisa','Andrew','Ann','Bob','Britney','Bruce','Jonny','Lucida','Melisa','Pitt']
#пересортировали names в случайном порядке
names=sample(names,len(names))
all_students=[]
exc_students=[]
bad_students=[]
for i in range(len(names)):
    all_students.append(Student(names[i]))
    all_students[i].state['timp']=randint(1,5)
    all_students[i].state['eis']=randint(1,5)
    all_students[i].state['philosophy']=randint(1,5)
    all_students[i].state['english']=randint(1,5)
    all_students[i].state['sport']=randint(1,5)
    summ=0
    for e in all_students[i].state.values():
        summ+=e
    #вопрос: почему следующее присваивание корректно работает,
    #но если float будет на всё выражение, то будет округление к целому,
    #которое присваивает вещественная 'average'
    all_students[i].state['average']=float(summ)/len(all_students[i].state)
for i in all_students:
    if i.state['average']>=4.0:
        exc_students.append(i.fio)
    elif i.state['average']<3.0:
        bad_students.append(i.fio)
exc_students=', '.join(exc_students)
bad_students=', '.join(bad_students)