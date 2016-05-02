# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class Student:
    def __init__(self, stud_id, fio, timp, eis, philosophy, english, sport):
        self.id = stud_id
        self.fio = fio
        self.timp = timp
        self.eis = eis
        self.philosophy = philosophy
        self.english = english
        self.sport = sport
        self.average = (timp+eis+philosophy+english+sport)/5

students = []
students.append(Student(1, "Антонова Мария Ивановна",
                          3, 4, 3, 4, 5))
students.append(Student(2, "Киселёв Александр Сергеевич",
                          4, 4, 4, 4, 3))
students.append(Student(3, "Иванов Иван Иванович",
                          3, 4, 4, 3, 5))
students.append(Student(4, "Моголь Ольга Дмитриевна",
                          5, 5, 5, 5, 5))
students.append(Student(5, "Амфибрахий Сергей Сергеевич",
                          2, 2, 2, 2, 2))

class IndexView(TemplateView):
    template_name = "index.html"
    global students
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students,
                'excellent_students': ", ".join([student.fio for student in students if student.average >= 4.8]),
                'bad_students': ", ".join([student.fio for student in students if student.average < 2.5])
            }
        )
        return context
