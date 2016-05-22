# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': studentsStatistics,
                'excellent_students': exellentStudents,
                'bad_students': badStudents,
            }
        )
        return context

class Students(object):
    students = {}
    ai = 1;
    
    def addStudent(self, fio):
        """ Добавление студента """
        self.students[self.ai] = fio
        self.ai+= 1


class Subjects(object):
    subjects = {}
    reverseSubjects = {}
    ai = 1;

    def addSubject(self, title):
        """ Добавление предмета """
        self.subjects[self.ai] = title
        self.reverseSubjects[title] = self.ai
        self.ai += 1

class Scores(object):
    scores = {}

    def addScore(self, studentId, subjectId, value):
        """ Добавление оценки """
        self.scores[studentId, subjectId] = value

    def getScore(self, studentId, subjectId):
        """ Возвращение оценки """
        return self.scores[studentId, subjectId]

    def getAverage(self, studentId):
        """ Возвращение среднего значения """
        average = 0.0
        for subjectId in range(1, len(Subjects.subjects) + 1, 1):
            average += self.scores[studentId, subjectId]
        return (average / len(Subjects.subjects))


class Statistics(object):
    def __init__(self, students, subjects, scores):
        """ Конструктор """
        self.students = students,
        self.subjects = subjects,
        self.scores = scores,

    def getStudentStatistics(self, id):
        """ Возвращение словаря значений """
        studentStatistics = {}
        studentStatistics['id'] = id
        studentStatistics['fio'] = Students.students.get(id)
        for subjectId in Subjects.subjects:
            studentStatistics[Subjects.subjects.get(subjectId)] = Scores.getScore(scores, id, Subjects.reverseSubjects.get(Subjects.subjects.get(subjectId)))
        studentStatistics['average'] = Scores.getAverage(scores, id)
        return studentStatistics

    def getExellentStudents(self, studentsStatistics):
        """ Возвращение списка преуспевающих студентов """
        exellentStudents = ",".join(student['fio'] for student in studentsStatistics if student['average'] >= 4.5)
        return exellentStudents

    def getBadStudents(self, studentsStatistics):
        """ Возвращение списка студентов на отчисление """
        badStudents = ",".join(student['fio'] for student in studentsStatistics if student['average'] <= 2.5)
        return badStudents

# Инициализируем класс студентов
students = Students()

# Заполняем словарь студентов
students.addStudent(u'Аримпилов Станислав Николаевич')
students.addStudent(u'Бомбов Антон Ярославович')
students.addStudent(u'Ковальчук Анастасия Олеговна')
students.addStudent(u'Ковчунов Петр Александрович')
students.addStudent(u'Крупина Алиса Александровна')
students.addStudent(u'Кучаев Николай Алексеевич')
students.addStudent(u'Лекаторчук Сергей Валерьевич')
students.addStudent(u'Лысак Ирина Юрьевна')
students.addStudent(u'Мусиенко Юрий Владимирович')
students.addStudent(u'Нестеров Никита Сергеевич')

# Инициализируем класс объектов
subjects = Subjects()

# Заполняем словарь объектов
subjects.addSubject(u'timp')
subjects.addSubject(u'eis')
subjects.addSubject(u'philosophy')
subjects.addSubject(u'english')
subjects.addSubject(u'sport')

# Инициализируем класс оценок
scores = Scores()

# Заполняем словарь оценок
for i in range(1, len(students.students) + 1, 1):
    for j in range(1, len(subjects.subjects) + 1, 1):
        scores.addScore(i, j, random.randint(2,5))

# Инициализируем класс статистики
statistics = Statistics(students, subjects, scores)

# Создаем список студентов
studentsStatistics = []
for i in range(1, len(students.students) + 1):
    studentsStatistics.append(statistics.getStudentStatistics(i))

# Создаем строки отличников и тех, кого необходимо отчислить
exellentStudents = statistics.getExellentStudents(studentsStatistics)
badStudents = statistics.getBadStudents(studentsStatistics)