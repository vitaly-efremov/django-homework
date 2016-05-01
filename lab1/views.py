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
        self._subjects      = subjects
        self._students      = students
        self._scores        = scores
        self._statistics    = []
        self.update_statistics()
    def update_statistics(self):
        self._statistics = []
        for student in self._students.get_students():
            current_student = {
                "id": student.get_id(),
                "fn": student.get_fn(),
            }
            scores = self._scores.get_scores_by_student(student)
            total_score = sum(score for score in scores.values())
            current_student.update(scores)
            current_student['average'] = total_score/len(scores)
            self._statistics.append(current_student)
    def get_statistics(self):
        return self._statistics
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
        self._students = []
    def add(self, fn):
        current_student = Student(fn)
        self._students.append(current_student)
        return current_student
    def get_student_by_fn(self, fn):
        for student in self._students:
            if fn == student.get_fn():
                return student
        return None
    def get_students(self):
        return self._students

class Student:
    _inc = 1

    def __init__(self, fn):
        self._id    = Student._inc
        self._fn    = fn
        Student._inc += 1
    def get_id(self):
        return self._id
    def get_fn(self):
        return self._fn

class Subjects:
    def __init__(self):
        self._subjects = []
    def add(self, name):
        self._subjects.append(Subject(name))
    def get_subjects(self):
        return self._subjects
    def get_subject_by_name(self, name):
        for subject in self._subjects:
            if name == subject.get_name():
                return subject
        return None

class Subject:
    _inc = 1

    def __init__(self, name):
        self._id    = Subject._inc
        self._name  = name
        Subject._inc += 1
    def get_name(self):
        return self._name

class Scores:
    def __init__(self):
        self._scores = []
    def add(self, student, subject, score):
        self._scores.append(Score(student, subject, score))
    def get_scores_by_student(self, student):
        scores = {}
        for score in self._scores:
            if student.get_fn() == score.get_student().get_fn():
                scores[score.get_subject().get_name()] = score.get_score()
        return scores

class Score:
    _inc = 1

    def __init__(self, student, subject, score):
        self._id        = Score._inc
        self._student   = student
        self._subject   = subject
        self._score     = int(score)
        Score._inc += 1
    def get_student(self):
        return self._student
    def get_subject(self):
        return self._subject
    def get_score(self):
        return self._score

subjects    = Subjects()
students    = Students()
scores      = Scores()

datafile = os.path.join(os.path.dirname(__file__), 'data.json')
with open(datafile, 'r') as infile:
    data = infile.read()
print('\n---start data---\n',data,'\n---end data---\n')
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