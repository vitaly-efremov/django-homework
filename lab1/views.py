 #-*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistics_stud = []
        students = Student([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Артём', 'Данил', 'Пётр', 'Юля', 'Алиса', 'Ирина', 'Антон', 'Иван', 'Станислав', 'Владимир'])
        subject = Subject(['timp', 'eis', 'philosophy', 'english', 'sport'])
        score = Score([[5, 5, 5, 5, 5], [2, 3, 4, 4, 4], [5, 5, 3, 3, 5], [4, 5, 5, 4, 5], [3, 5, 3, 4, 5],
                   [4, 5, 4, 2, 5], [4, 5, 4, 4, 5], [3, 5, 3, 3, 5], [3, 5, 4, 4, 5], [5, 5, 4, 5, 5]],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        for i in range(1,11):
            statistics = Statistic(score.get_grades(i))
            statistics_stud.append(statistics.format_record(i, students.get_fio(i), subject.get_subject()))
        bad_stud = ', '.join(students.get_fio(i) for i in score.bad_student())
        excellent_stud = ', '.join(students.get_fio(i) for i in score.excellent_student())
        
        context.update(
            {
                'students_statistics': statistics_stud,
                'excellent_students': excellent_stud,
                'bad_students': bad_stud
            }
        )
        return context


class Student(object):
    def __init__(self, student_id, fio):
        self.students = dict(zip(student_id, fio))

    def get_fio(self, student_id):
        return self.students[student_id]


class Statistic(object):
    def __init__(self, grades):
        self.grades = grades

    def _average_grade(self):
        return float(sum(self.grades))/len(self.grades)

    def format_record(self, student_id, fio, subject):
        information = {'id':student_id, 'fio':fio}
        journal = dict(zip(subject, self.grades))
        information.update(journal)
        information.update({'average':self._average_grade()})
        return information


class Subject(object):
    def __init__(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject


class Score(object):
    def __init__(self, grades, student_id):
        self.student_grades = dict(zip(student_id, grades))

    def get_grades(self, student_id):
        return self.student_grades[student_id]

    def bad_student(self):
        tmp = self.student_grades.items()
        return [i[0] for i in tmp if i[1].count(2) or i[1].count(3)]

    def excellent_student(self):
        tmp = self.student_grades.items()
        return [i[0] for i in tmp if i[1].count(5) == len(i[1])]    
