# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

# Поменять list для изменения студентов

        list = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 'Герасимов Вячеслав','Ерохин Евгений', 'Иванов Александр', 'Косаченко Татьяна', 'Кравченко Александр','Кузнецова Мария', 'Лозинг Варвара']
        student = []
        for i in range(len(list)):
                student.append(Student(i,list[i]))
        list_of_stats = []
        badStudents = []
        goodStudents = []
        for i in range(len(list)):
            if student[i].avg >= 3.5:
                goodStudents.append(student[i].studentName)
            elif student[i].avg < 3.5:
                badStudents.append(student[i].studentName)
            list_of_stats.append({'id': student[i].id, 'fio': student[i].studentName, 'timp': student[i].score[0],
                                'eis': student[i].score[1], 'philosophy': student[i].score[2], 
                                'english': student[i].score[3], 'sport': student[i].score[4],
                                'average': student[i].avg})

        context.update(
            {
                'students_statistics': list_of_stats,
                'excellent_students': goodStudents,
                'bad_students': badStudents
            }
        )
        return context


class Student: 
        def __init__(self,num,name):
                self.studentName = name
                self.id = num
                self.s = Subject().subjList
                self.score = Score(self.s).scoreList
                self.avg = Statistics.getAvg(self.score)

# Поменять subjList для изменения предметов

class Subject:
        def __init__(self):
                self.subjList = ['timp','eis','philosophy','english','sport']

# Сменить конструктор на метод или организовать запрос баллов с его помощью

class Score:
        def __init__(self,subj):
                self.scoreList = []
                for n in subj:
                        self.scoreList.append(random.randint(2, 5))
        
class Statistics:
        def getAvg(sc):
                sum=0
                num=0
                for i in sc:
                        sum+=i
                        num+=1
                avg=sum/num
                return avg