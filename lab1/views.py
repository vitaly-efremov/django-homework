# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from random import random

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': statistics.get_statistics(),
                'excellent_students': statistics.get_excellent_students(),
                'bad_students': statistics.get_bad_students()
            }
        )
        return context


class Statistics:
    def __init__(self, subjects, students, scores):
        self.statistics = [{'id': student.get_id(), 'fio': student.get_fio()} for student in students]
        for score in scores:
            self.statistics[score.get_student().get_id()-1][score.get_subject().get_name()] = score.get_score()
        for i, student in enumerate(self.statistics):
            average = 0
            for subject in subjects:
                average += student[subject.get_name()]
            average /= len(subjects)
            self.statistics[i]['average'] = average
        self.excellent_students = ', '.join(student['fio'] for student in self.statistics if student['average'] >= 4)
        self.bad_students = ', '.join(student['fio'] for student in self.statistics if student['average'] < 2.5)
    def get_statistics(self):
        return self.statistics
    def get_excellent_students(self):
        return self.excellent_students
    def get_bad_students(self):
        return self.bad_students

class Student:
    def __init__(self, id, fio):
        self.id = id
        self.fio = fio
    def get_id(self):
        return self.id
    def get_fio(self):
        return self.fio

class Subject:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Score:
    def __init__(self, student, subject, score):
        self.student = student
        self.subject = subject
        self.score = score
    def get_student(self):
        return self.student
    def get_subject(self):
        return self.subject
    def get_score(self):
        return self.score

subjects = [
    Subject('timp'),
    Subject('eis'),
    Subject('philosophy'),
    Subject('english'),
    Subject('sport')
]

students = [
    Student(1 ,'Заммет Тобиас'),
    Student(2 ,'Гилмор Дэвид'),
    Student(3 ,'Мальмстин Ингви'),
    Student(4 ,'Хэтфилд Джеймс'),
    Student(5 ,'Турунен Тарья'),
    Student(6 ,'Осборн Оззи'),
    Student(7 ,'Плант Роберт'),
    Student(8 ,'Джонсон Брайан'),
    Student(9 ,'Фрипп Роберт'),
    Student(10 ,'Роуз Эксл'),
]

scores = [Score(student, subject, int(random()*5)+1) for subject in subjects for student in students]

statistics = Statistics(subjects, students, scores)