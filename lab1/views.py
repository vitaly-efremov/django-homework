# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        list_of_students = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 'Герасимов Вячеслав',
                          'Ерохин Евгений', 'Иванов Александр', 'Косаченко Татьяна', 'Кравченко Александр',
                          'Кузнецова Мария', 'Лозинг Варвара', 'Мартынов Роман', 'Машуков Никита',
                          'Мухин Алексей', 'Мякишева Эвелина', 'Пехова Анна', 'Сапунов Антон',
                          'Черемных Алексей', 'Шивцов Данил', 'Федурин Артем']
        list_of_bad_students = [] #на отчисление
        list_of_good_students = [] #отличники
        list_of_stats = [] #список с оценками, фио, и идами
        list_of_ids = Student.get_ids(list_of_students)
        list_of_scores = Score.get_scores(list_of_students)
        for i in range(len(list_of_students)):
            average_score = Score.get_average(list_of_scores[i])
            if average_score >= 4.2:
                list_of_good_students.append(list_of_students[i])
            elif average_score <= 2.7:
                list_of_bad_students.append(list_of_students[i])
            list_of_stats.append({'id': list_of_ids[i], 'fio': list_of_students[i], 'timp': list_of_scores[i]['timp'],
                                'eis': list_of_scores[i]['eis'], 'philosophy': list_of_scores[i]['phil'], 
                                'english': list_of_scores[i]['eng'], 'sport': list_of_scores[i]['sport'],
                                'average': average_score})

        context.update(
            {
                'students_statistics': list_of_stats,
                'excellent_students': list_of_good_students,
                'bad_students': list_of_bad_students
            }
        )
        return context


class Student: 
    def get_ids(list_of_students):
        list_of_ids = [] 
        for i in range(len(list_of_students)):
            list_of_ids.append(i)
        return list_of_ids
        
class Statistics: #badStudents, excStudents
    pass


class Score: #eis, fil, timp, eng, sport
    def get_scores(list_of_students):
        list_of_scores = []
        sum_of_scores = 0
        #создается список, в котором каждый элемнет является словарем с оценками каждого студента
        for i in list_of_students:
            list_of_scores.append({'timp':random.randint(2, 5), 'eis':random.randint(2, 5), 
                                   'sport':random.randint(2, 5), 'phil':random.randint(2, 5), 
                                   'eng':random.randint(2, 5)})
        return list_of_scores
    
    def get_average(scores_of_student):
        sum_of_scores = 0
        # сумма оценок, чтобы найти потом среднее
        for score in scores_of_student.values():
             sum_of_scores += score
        average = sum_of_scores / 5  
        return average   