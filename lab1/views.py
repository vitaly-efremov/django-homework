# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_statistics,
                'excellent_students': excellent_students,
                'bad_students': bad_students,
            }
        )
        return context


class Student(object):
    students = {}
    id = 1

    def insert_student(self, student):
        self.students[self.id] = student
        self.id += 1


class Subject(object):
    subjects = {}
    reverse_subjects = {}
    id = 1

    def insert_subject(self, subject):
        self.subjects[self.id] = subject
        self.reverse_subjects[subject] = self.id
        self.id += 1


class Score(object):
    scores = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    def __init__(self, subject):
        self.subject = subject

    def insert_score(self, student, subject, value):
        self.scores[student - 1][subject - 1] = value

    def get_score(self, student, subject):
        return self.scores[student - 1][subject - 1]

    def get_average(self, student):
        average = 0.0
        for i in range(0, len(self.subject.subjects)):
            average += self.scores[student - 1][i]
        return average/len(self.subject.subjects)


class Statistics(object):
    def __init__(self, student, subject, score):
        self.student = student
        self.subject = subject
        self.score = score

    def student_statistics(self, id):
        student_statistics = {}
        student_statistics['id'] = id
        student_statistics['fio'] = self.student.students.get(id)
        student_statistics['timp'] = self.score.get_score(id, self.subject.reverse_subjects.get('timp'))
        student_statistics['eis'] = self.score.get_score(id, self.subject.reverse_subjects.get('eis'))
        student_statistics['philosophy'] = self.score.get_score(id, self.subject.reverse_subjects.get('philosophy'))
        student_statistics['english'] = self.score.get_score(id, self.subject.reverse_subjects.get('english'))
        student_statistics['sport'] = self.score.get_score(id, self.subject.reverse_subjects.get('sport'))
        student_statistics['average'] = self.score.get_average(id)
        return student_statistics

    def excellent_students(self, students_statistics):
        excellent_students = ",".join(student_statistics['fio'] for student_statistics in students_statistics if student_statistics['average'] >= 4.5)
        return excellent_students


    def bad_students(self, students_statistics):
        bad_students = ",".join(student_statistics['fio'] for student_statistics in students_statistics if student_statistics['average'] <= 2.5)
        return bad_students

student = Student()
student.insert_student("Боровков Сергей Станиславович ")
student.insert_student("Бусыгин Иван Владимирович ")
student.insert_student("Ворожцов Сергей Андреевич")
student.insert_student("Герасимов Вячеслав Андреевич")
student.insert_student("Иванов Александр Станиславович")
student.insert_student("Косаченко Татьяна Сергеевна")
student.insert_student("Кравченко Александр Васильевич")
student.insert_student("Кузнецова Мария Григорьевна ")
student.insert_student("Лозинг Варвара Романовна")
student.insert_student("Мартынов Роман Валерьевич ")

subject = Subject()
subject.insert_subject("fio")
subject.insert_subject("timp")
subject.insert_subject("eis")
subject.insert_subject("philosophy")
subject.insert_subject("english")
subject.insert_subject("sport")

score = Score(subject)
for i in student.students:
    for j in subject.subjects:
        score.insert_score(i, j, random.randint(2,5))

statistics = Statistics(student, subject, score)

students_statistics = []
for i in range(1, len(student.students)):
    students_statistics.append(statistics.student_statistics(i))

excellent_students = statistics.excellent_students(students_statistics)
bad_students = statistics.bad_students(students_statistics)