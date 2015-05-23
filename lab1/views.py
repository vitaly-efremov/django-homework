# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
students_list = []


class Student(object):
    id_student = 1

    def __init__(self, fio, group, age):
        self.id_student = Student.id_student
        students_list.append({
            'fio': fio,
            'group': group,
            'age': age,
            'id': Student.id_student
        })
        Student.id_student += 1


mark_list = []


class Mark(object):
    id_mark = 1

    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.id_mark = Mark.id_mark
        mark_list.append({
            's1': s1,
            's2': s2,
            's3': s3,
            's4': s4,
            's5': s5,
            's6': s6,
            'id':Mark.id_mark
        })
        Mark.id_mark +=1

Student('Иванов Иван', 743, 20)
Mark(5, 5, 5, 5, 5, 5)
Student('Петров Никита', 743, 20)
Mark(3, 2, 4, 5, 3, 4)
Student('Алексин Павел', 743, 20)
Mark(4, 4, 4, 4, 4, 4)
Student('Вершинин Артем',743, 20)
Mark(3, 3, 3, 3, 3, 3)
Student('Зарипов Данил', 743, 19)
Mark(4, 4, 4, 4, 4, 4)
Student('Звягинцев Евгений',743, 19)
Mark(2, 2, 2, 3, 2, 2)
Student('Кайзер Екатерина', 743, 20)
Mark(4, 4, 4, 3, 4, 4)
Student('Ковалев Вячеслав', 743, 20)
Mark(5, 5, 5, 5, 5, 4)
Student('Койшинов Тимур', 743, 20)
Mark(4, 4, 4, 4, 4, 4)
Student('Мингалев Кирилл', 743, 20)
Mark(3, 3, 3, 2, 3, 3)
Student('Минеева Татьяна', 743, 21)
Mark(3, 3, 3, 3, 4, 3)


class Statistics:
    # student_id, [Subjects]
    pass
memo = 0
for x in range(len(students_list)):
    mem=0
   # students_list[x].update({'s1':mark_list[x]['s1'], 's2':mark_list[x]['s2'], 's3':mark_list[x]['s3'],
                        #     's4':mark_list[x]['s4'], 's5':mark_list[x]['s5'], 's6':mark_list[x]['s6']})
    students_list[x].update({'s'+str(y): mark_list[x]['s'+str(y)] for y in range(1,7)})
    mem += mark_list[x]['s1'] + mark_list[x]['s2'] + mark_list[x]['s3'] + mark_list[x]['s4'] + \
           mark_list[x]['s5'] + mark_list[x]['s6']
    mem = float(mem)/6
    memo += mem
    students_list[x].update({'med':mem})
m1=0
m2=0
m3=0
m4=0
m5=0
m6=0
for x in range(len(students_list)):
    m1 += mark_list[x]['s1']
    m2 += mark_list[x]['s2']
    m3 += mark_list[x]['s3']
    m4 += mark_list[x]['s4']
    m5 += mark_list[x]['s5']
    m6 += mark_list[x]['s6']
exellent_students = [{'fio': x['fio']} for x in students_list if x['med'] > 4.5]
bad_students = [{'fio': x['fio']} for x in students_list if x['med'] < 3]
Student('статистика по предметам', ' ', ' ')

students_list[11].update({'s1':round((float(m1)/11),2), 's2':round((float(m2)/11),2), 's3':round((float(m3)/11),2),
                          's4':round((float(m4)/11),2), 's5':float(m5)/11, 's6':float(m6)/11, 'med':float(memo)/11})


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_list,
                'students_mark': mark_list,
                'exellent_students': exellent_students,
                'bad_students': bad_students
            }
        )
        return context
