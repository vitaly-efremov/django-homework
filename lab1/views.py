# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistict_stud = []
        students = Student([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Иванов И. К.', 'Петров Е. Н.', 'Смирнов А. М.', 'Михайлов Н. А.', 'Никитина А. Ю.', 'Лисицына Ю. Г.', 'Голубев А. П.', 'Кузнецова Л. С.', 'Дёмкин И. Г.', 'Ревин С. Д.'])
        subject = Subject(['timp', 'eis', 'philosophy', 'english', 'PE'])
        score = Score([[5, 5, 5, 5, 5], [2, 3, 4, 5, 4], [3, 5, 2, 2, 5], [3, 5, 5, 2, 5], [3, 5, 2, 4, 5],
                   [2, 5, 2, 2, 5], [3, 5, 4, 4, 5], [3, 5, 2, 2, 2], [3, 5, 3, 3, 5], [3, 5, 4, 3, 5]],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        for i in range(1, 11):
            statistics = Statistics(score.get_grades(i))
            statistict_stud.append(statistics.format_record(i, students.get_fio(i), subject.get_subject()))
        bad_stud = ', '.join(students.get_fio(i) for i in score.bad_student())
        excellent_stud = ', '.join(students.get_fio(i) for i in score.excellent_student())
        context.update(
            {
                'students_statistics': statistict_stud,
                'excellent_students': excellent_stud,
                'bad_students': bad_stud
            }
        )
        return context


class Student(object):
    def __init__(self, student_id, fio):
        self.student = dict(zip(student_id, fio))
    def get_fio(self, student_id):
        return self.student.setdefault(student_id)

class Statistics(object):
    def __init__(self, grades):
        self.grades = grades

    def _average_grade(self):
        return sum(self.grades)/len(self.grades)

    def format_record(self, student_id, fio, subject):
        inform = {'id': student_id, 'fio': fio}
        tmp = dict(zip(subject, self.grades))
        inform.update(tmp)
        inform.update({'average': self._average_grade()})
        return inform

class Subject(object):
    def __init__(self, subject):
        self.subject = subject
    def get_subject(self):
        return self.subject


class Score(object):
    def __init__(self, grades, student_id):
        self.student_assessment = dict(zip(student_id, grades))
    def get_grades(self, student_id):
        return self.student_assessment.setdefault(student_id)
    def bad_student(self):
        return [i for i in range(1, 11) if Statistics(self.get_grades(i))._average_grade() < 3.5]
    def excellent_student(self):
        return [i for i in range(1, 11) if Statistics(self.get_grades(i))._average_grade() == 5]
