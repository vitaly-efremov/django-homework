# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        listStudents = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 'Герасимов Вячеслав',
                          'Ерохин Евгений', 'Иванов Александр', 'Косаченко Татьяна', 'Кравченко Александр',
                          'Кузнецова Мария', 'Лозинг Варвара', 'Мартынов Роман', 'Машуков Никита',
                          'Мухин Алексей', 'Мякишева Эвелина', 'Пехова Анна', 'Сапунов Антон',
                          'Черемных Алексей', 'Шивцов Данил', 'Федурин Артем']
        listIDs = []
        listScores = []
        listAverage_scores = []
        listGood_students = []
        listBad_students = []
        listStatistics = []
        
        listIDs = Student.get_ids(listStudents)
        listScores = Score.get_scores(listStudents)
        for i in range(len(listStudents)):
            listAverage_scores.append(Average_Score.get_average(listScores[i]))
        listGood_students = Statistics.get_good_students(listAverage_scores,listStudents)
        listBad_students = Statistics.get_bad_students(listAverage_scores,listStudents)
        listStatistics = Statistics.get_statistics(listStudents,listIDs,listScores,listAverage_scores)
        context.update(
            {
                'students_statistics': listStatistics,
                'excellent_students': listGood_students,
                'bad_students': listBad_students
            }
        )
        return context


class Student:
    def get_ids(listStudents):
        listIDs = []
        for i in range(len(listStudents)):
            listIDs.append(i)
        return listIDs


class Score: #eis, fil, timp, eng, sport    
    def get_scores(listStudents):
        listProgramming = [random.randint(2,5) for i in range(len(listStudents))]
        listElectronics = [random.randint(2,5) for i in range(len(listStudents))]
        listPhilosophy = [random.randint(2,5) for i in range(len(listStudents))]
        listEnglish = [random.randint(2,5) for i in range(len(listStudents))]
        listPE = [random.randint(2,5) for i in range(len(listStudents))]
        listScores = []
        for i in range(len(listStudents)):
            listScores.append({'programming':listProgramming[i],
                            'electronics':listElectronics[i],
                            'philosophy':listPhilosophy[i],
                            'english':listEnglish[i],
                            'PE':listPE[i]})
        return listScores


class Average_Score:
    def get_average(scores_of_student):
        sum_of_scores = 0
        Average_score_of_student = 0
        listAverage_scores = []
        for i in scores_of_student.values():
            sum_of_scores += i
        Average_score_of_student = sum_of_scores/5
        return Average_score_of_student 


class Statistics: #badStudents, excStudents
    def get_statistics(listStudents,listIDs,listScores,listAverage_scores):
        listStatistics = []
        for i in range(len(listStudents)):
            listStatistics.append({'id': listIDs[i], 'fio': listStudents[i],
                                   'programming': listScores[i]['programming'], 'electronics': listScores[i]['electronics'],
                                   'philosophy': listScores[i]['philosophy'], 'english': listScores[i]['english'],
                                   'PE': listScores[i]['PE'], 'average': listAverage_scores[i]})
        return listStatistics
    
    def get_good_students(listAverage_scores,listStudents):
        listGood_students = []
        for i, avg in enumerate(listAverage_scores):
            if float(avg) >= 4.2:
                listGood_students.append(listStudents[i])
        return listGood_students

    def get_bad_students(listAverage_scores,listStudents):
        listBad_students = []
        for i, avg in enumerate (listAverage_scores):
            if float(avg) <= 2.7:
                listBad_students.append(listStudents[i])
        return listBad_students
