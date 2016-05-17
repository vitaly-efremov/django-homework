#-*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistict_stud = []
        students = Student([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Сидоров', 'Шишкин', 'Меньшиков', 'Сахаров', 'Филин', 'Арбузова', 'Белов', 'Вернадский', 'Демченко', 'Глазков'])
        subject = Subject(['s1', 's2', 's3', 's4', 's5'])
        score = Score([[3,4,5,4,5], [5,4,5,4,3], [5,5,5,4,4], [4,4,3,4,5], [2,3,4,4,4],
                   [4,4,3,5,5], [5,5,5,5,5], [5, 5, 5, 5, 5],[3, 2, 2, 2, 5], [3, 5, 4, 3, 5]],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        for i in range(1,11):
            statistics = Statistics(score.get_marks(i))
            statistict_stud.append(statistics.formatter(i, students.get_surname(i), subject.get_subject()))
        bad_stud = ', '.join(students.get_surname(i) for i in score.bad_student())
        excellent_stud = ', '.join(students.get_surname(i) for i in score.excellent_student())
        
        context.update(
            {
                'students_statistics': statistict_stud,
                'excellent_students': excellent_stud,
                'bad_students': bad_stud
            }
        )
        return context


class Student(object):
    def __init__(self, id, surname):
        self.student = dict(zip(id, surname))
    def get_surname(self, id):
        return self.student.setdefault(id)

class Subject(object):
    def __init__(self, subject):
        self.subject = subject
    def get_subject(self):
        return self.subject
    
class Score(object):
    def __init__(self, marks, id):
        self.student_marks = dict(zip(id, marks))
    def get_marks(self, id):
        return self.student_marks.setdefault(id)
    def bad_student(self):
        return [i[0] for i in self.student_marks.items() if float(sum(i[1])/len(i[1]))<3]
    def excellent_student(self):
        return [i[0] for i in self.student_marks.items() if float(sum(i[1])/len(i[1])) == 5]  

class Statistics(object):
    def __init__(self, marks):
        self.marks = marks
    def _average_grade(self):
        return float(sum(self.marks))/len(self.marks)
    def formatter(self, id, surname, subject):
        data = {'id':id, 'surname':surname}
        data.update(dict(zip(subject, self.marks)))
        data.update({'average':self._average_grade()})
        return data

  
