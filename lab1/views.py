# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'students_statistics': html_list, 'excellent_students': ', '.join(list_excellent_students),
                        'bad_students': ', '.join(list_bad_students), })
        return context


class Student:
    students = []
    students_id = {}
    id = 0

    def add_student(self, student_name):
        if student_name != "":
            self.students.append(student_name)
            self.students_id[self.id] = student_name
            self.id += 1
        else:
            self.students.append("noname")
            self.students_id[self.id] = "noname"
            self.id += 1


class Subject:
    subjects = []
    subjects_id = {}
    id = 0

    def add_subject(self, subject_name):
        if subject_name != "":
            self.subjects.append(subject_name)
            self.subjects_id[self.id] = subject_name
            self.id += 1
        else:
            self.subjects.append("noname")
            self.subjects_id[self.id] = "noname"
            self.id += 1


class Score:
    def __init__(self, students, subjects):
        self.scores = [[random.randint(2, 5) for j in range((len(subjects) + 1))] for i in range((len(students) + 1))]
        self.scores[0][0] = 0
        for j in range(1, len(subjects) + 1):
            self.scores[0][j] = j
        for i in range(1, len(students) + 1):
            self.scores[i][0] = i

    def change_score(self, student_name, subject_name, students_scores, students_id, subjects_id):
        students_dict = dict(map(lambda x: x[::-1], students_id.items()))
        subjects_dict = dict(map(lambda x: x[::-1], subjects_id.items()))
        if (students_scores >= 2) and (students_scores <= 5):
            self.scores[(students_dict[student_name] + 1)][(subjects_dict[subject_name] + 1)] = students_scores


class Statistics:
    def __init__(self, students, score_list, subjects):
        self.stat = [(sum(score_list[j]) - j) / len(subjects) for j in range(1, (len(students) + 1))]

    @staticmethod
    def get_excellent_students(stat, students_id):
        private_list_excellent_students = []
        for i in range(len(stat)):
            if stat[i] >= 4.0:
                private_list_excellent_students.append(students_id[i])
        return private_list_excellent_students

    @staticmethod
    def get_bad_students(stat, students_id):
        private_list_bad_students = []
        for i in range(len(stat)):
            if stat[i] < 3.0:
                private_list_bad_students.append(students_id[i])
        return private_list_bad_students

    @staticmethod
    def get_html_list(students_list, student_score, stat):
        my_html_list = []
        for i in range(1, (len(students_list) + 1)):
            my_html_list.append({'id': i, 'fio': students_list[i - 1], 'timp': student_score[i][1],
                                 'fdoik': student_score[i][2], 'philosophy': student_score[i][3],
                                 'english': student_score[i][4], 'sport': student_score[i][5],
                                 'average': stat[i - 1]})
        return my_html_list


student = Student()
student.add_student("Прокопьев Роман")
student.add_student("Газизов Рустам")
student.add_student("Пекарских Светлана")
student.add_student("Игорь Филимоненко")
student.add_student("Дмитрий Световец")
student.add_student("Анна Кузнецова")
student.add_student("Дмитрий Облаков")
student.add_student("Александр Пятков")
student.add_student("Павел Прокушев")
student.add_student("Юля Андреева")

subject = Subject()
subject.add_subject("ТиМП")
subject.add_subject("ФДОиК")
subject.add_subject("Философия")
subject.add_subject("Английский")
subject.add_subject("Физ-культура")

score = Score(student.students, subject.subjects)
score.change_score("Прокопьев Роман", "ТиМП", 5, student.students_id, subject.subjects_id)
score.change_score("Прокопьев Роман", "ФДОиК", 5, student.students_id, subject.subjects_id)
score.change_score("Прокопьев Роман", "Философия", 5, student.students_id, subject.subjects_id)
score.change_score("Прокопьев Роман", "Английский", 5, student.students_id, subject.subjects_id)
score.change_score("Прокопьев Роман", "Физ-культура", 5, student.students_id, subject.subjects_id)

statistics = Statistics(student.students, score.scores, subject.subjects)

list_excellent_students = statistics.get_excellent_students(statistics.stat, student.students_id)
list_bad_students = statistics.get_bad_students(statistics.stat, student.students_id)
html_list = statistics.get_html_list(student.students, score.scores, statistics.stat)
