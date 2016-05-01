# -*- coding: utf-8 -*-
import os
import json
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': statistics.get_statistics(),
                'excellent_students': statistics.get_excellent_students(),
                'bad_students': statistics.get_bad_students(),
            }
        )
        return context


class Statistics:

    def __init__(self, subjects, students, scores):
        self.__subjects = subjects
        self.__students = students
        self.__scores = scores
        self.__statistics = []
        self.update_statistics()

    def update_statistics(self):
        self.__statistics = []
        for student in self.__students.get_students():
            current_student = {
                "id": student.get_id(),
                "fn": student.get_fn(),
            }
            scores = self.__scores.get_scores_by_student(student)
            total_score = sum(score for score in scores.values())
            current_student.update(scores)
            current_student['average'] = total_score/len(scores)
            self.__statistics.append(current_student)

    def get_statistics(self):
        return self.__statistics

    def get_excellent_students(self):
        excellent_students = []
        for student in self.get_statistics():
            if student['average'] >= 4.5:
                excellent_students.append(student['fn'])
        return ', '.join(excellent_students)

    def get_bad_students(self):
        bad_students = []
        for student in self.get_statistics():
            if student['average'] <= 3:
                bad_students.append(student['fn'])
        return ', '.join(bad_students)


class Students:

    def __init__(self):
        self.__students = []

    def add(self, fn):
        current_student = Student(fn)
        self.__students.append(current_student)
        return current_student

    def get_student_by_fn(self, fn):
        for student in self.__students:
            if fn == student.get_fn():
                return student
        return None

    def get_students(self):
        return self.__students


class Student:
    __inc = 1

    def __init__(self, fn):
        self.__id = Student.__inc
        self.__fn = fn
        Student.__inc += 1

    def get_id(self):
        return self.__id

    def get_fn(self):
        return self.__fn


class Subjects:

    def __init__(self):
        self.__subjects = []

    def add(self, name):
        self.__subjects.append(Subject(name))

    def get_subjects(self):
        return self.__subjects

    def get_subject_by_name(self, name):
        for subject in self.__subjects:
            if name == subject.get_name():
                return subject
        return None


class Subject:
    __inc = 1

    def __init__(self, name):
        self.__id = Subject.__inc
        self.__name = name
        Subject.__inc += 1

    def get_name(self):
        return self.__name


class Scores:

    def __init__(self):
        self.__scores = []

    def add(self, student, subject, score):
        self.__scores.append(Score(student, subject, score))

    def get_scores_by_student(self, student):
        scores = {}
        for score in self.__scores:
            if student.get_fn() == score.get_student().get_fn():
                scores[score.get_subject().get_name()] = score.get_score()
        return scores


class Score:
    __inc = 1

    def __init__(self, student, subject, score):
        self.__id = Score.__inc
        self.__student = student
        self.__subject = subject
        self.__score = int(score)
        Score.__inc += 1

    def get_student(self):
        return self.__student

    def get_subject(self):
        return self.__subject

    def get_score(self):
        return self.__score

subjects = Subjects()
students = Students()
scores = Scores()

datafile = os.path.join(os.path.dirname(__file__), 'data.json')
with open(datafile, 'r') as infile:
    data = infile.read()
data = json.loads(data)

for subject in data['subjects']:
    subjects.add(subject)

for student in data['students']:
    current_student = students.add(student['fn'])
    for score in student['scores'].items():
        scores.add(
            current_student,
            subjects.get_subject_by_name(score[0]),
            score[1]
        )

statistics = Statistics(subjects, students, scores)
