# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Someone',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.7,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Person:
    fio = "Name Surname"
    def set_fio(self,f):
        self.fio = f
    def person(self):
        return self.fio

class Student(Person):
    id = "no id"
    person = "n/a"
    group = "n/a"
    age = "n/a"

    def set_person(self):
        self.person = Person.person(self)
    def set_id(self, id):
        self.id = id
    def set_group(self, g):
        self.group = g
    def set_age(self, a):
        self.age = a
    def student_desc(self):
        print("My ID: ", self.id)
        print("My name: ", self.person)
        print("My group: ", self.group)
        print("My age: ", self.age)

class Statistics:
    # student_id, [Subjects]
    pass

class Subject:
    pass

class Score:
    # Subject,
    pass

person1 = Student()
person1.set_fio("John Ivanov")
person1.set_person()
person1.set_id(1)
person1.set_age(20)
person1.set_group(743)