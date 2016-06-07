# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

#ListStudent - список студентов
        ListStudent = ['Ажель Никита', 'Андреева Юлия','Бандеев Хашэгто','Власенко Анастасия','Газизов Рустам','Киселев Александр','Кудряшова Анастасия','Кузнецова Анна','Култаев Павел','Манаев Александр']
        #LS - список для класса Student
        LS = []
        for i in range(len(ListStudent)):
                LS.append(Student(i+1,ListStudent[i]))
        list_of_stats = []
        #excellentStudents - отличники
        excellentStudents = []
        #excellentStudents - студенты, которых нужно отчислить
        expelledStudents = []
        for i in range(len(ListStudent)):
            if LS[i].avg >= 4.5:
                excellentStudents.append(LS[i].nameS)
            elif LS[i].avg <=2.5:
                expelledStudents.append(LS[i].nameS)
            list_of_stats.append({'id': LS[i].id, 'fio': LS[i].nameS, 'timp': LS[i].score[0],
                                'eis': LS[i].score[1], 'philosophy': LS[i].score[2], 
                                'english': LS[i].score[3], 'sport': LS[i].score[4],
                                'average': LS[i].avg})

        context.update(
            {
                'students_statistics': list_of_stats,
                'excellent_students': excellentStudents,
                'bad_students': expelledStudents
            }
        )
        return context


class Student:
#class Student - служит для информации о студентах
#def __init___(self,idStudent, nameStudent) - конструктор класса для полной информации по студентам 
        def __init__(self,idStudent,nameStudent):
                self.nameS = nameStudent
                self.id = idStudent
                self.s = Subject().subjList
                self.score = Score(self.s).scoreList
                self.avg = Statistics.getAvg(self.score)

class Statistics:
#class Statistics - выделен под статистику ученика
#функция getAvg(scores) служит для подсчета среднего арифметического ученика
        def getAvg(scores):
                s=0
                n=0
                for i in scores:
                        s+=i
                        n+=1
                avg=s/n
                return avg

# __init__ - конструктор класса
# self - параметр, на место которого подставляется объект в момент его создания
class Subject:
# class Subject - выделен под предметы
#def __init__(self) - конструктор класса для предметов
    def __init__(self):
                self.subjList = ['timp','eis','philosophy','english','sport']
# Сменить конструктор на метод или организовать запрос баллов с его помощью

class Score:
#class Score - выделен под оценки учеников
#def __init__(self,subj) - конструктор класса под оценки
#генерирует случайным образом оценки от 1 до 5    
    def __init__(self,subj):
        self.scoreList=[]
        for n in subj:
            self.scoreList.append(random.randint(1,5))
        
