# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView # Обрабатывает заданный шаблон, используя контекст(context), содержащий параметры из URL.
import random


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)


        students = Student().students # получаем список студентов
        numbers = Student().id # получаем список номеров студентов
        subjects = Subject().subjects # получаем список предметов
        score = Score(students, subjects).get_scores # получаем список оценок
        statistic = Statistics(students, score, subjects).stat # получаем средние баллы студентов
        deduction = [] # на отчисление
        good_student = [] # хорошисты
        total = []


        for i in range(len(students)):

            if statistic[i] >= 4.0:
                good_student.append(students[i])
            elif statistic[i] < 3.0:
                deduction.append(students[i])


            total.append({'id': numbers[i], 'fio': students[i], 'timp': score[i][0],
                                'eis': score[i][1], 'philosophy': score[i][2],
                                'english': score[i][3], 'sport': score[i][4],
                                'average': statistic[i]})

        context.update(
            {
                'students_statistics': total,
                'excellent_students': good_student,
                'bad_students': deduction
            }
        )
        return context




class Student:
    def __init__(self):
        self.students = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 'Герасимов Вячеслав',
                         'Ерохин Евгений', 'Иванов Александр', 'Косаченко Татьяна', 'Кравченко Александр',
                         'Кузнецова Мария', 'Лозинг Варвара', 'Мартынов Роман', 'Машуков Никита',
                         'Мухин Алексей', 'Мякишева Эвелина', 'Пехова Анна', 'Сапунов Антон',
                         'Черемных Алексей', 'Шивцов Данил', 'Федурин Артем']
        self.id = []
        for i in range(len(self.students)): # получаем список номеров студентов
            self.id.append(i+1)
            print(self.id)




class Statistics:
    def __init__(self, students, score, subjects):
        self.stat = [(sum(score[i]))/len(subjects) for i in range(len(students))]


class Subject:
    def __init__(self):
        self.subjects = ['timp','eis','philosophy','english','sport']

class Score:
    def __init__(self, students, subjects):
        self.get_scores = [[random.randint(2, 5) for j in range(len(subjects))] for i in range(len(students))]
        # генератор матрицы, где кол-во студентов - строки, кол-во предметов - столбцы.