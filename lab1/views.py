# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from random import randint


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': main_stats,
                'excellent_students': ', '.join(Statistics.get_excellent_students(Student)),
                'bad_students': ', '.join(Statistics.get_bad_students(Student))
            }
        )
        return context


class Student:
    id = 1
    students = {}
    names = []
    ids = []

    def __init__(self, name):
        self.id = Student.id
        self.name = name
        Student.ids.append(self.id)
        Student.names.append(self.name)
        Student.id += 1

    def get_students(self):
        self.students = dict(zip(self.ids, self.names))


class Statistics:
    students_stats = []
    bad_students = []
    excellent_students = []

    def __init__(self, studentid):
        self.student_stats = {studentid: {Student.students.get(studentid): Score.scores[studentid - 1]}}
        self.students_stats.append(self.student_stats)

    def get_bad_students(self):
        return [(self.students.get(x+1)) for x in range(0, 10) if Score.average_scores[x] <= 2.5]

    def get_excellent_students(self):
        return [(self.students.get(x+1)) for x in range(0, 10) if Score.average_scores[x] >= 4.5]


class Subject:
    id = 1
    names = []
    ids = []
    subjects = {}
    rsubjects = {}

    def __init__(self, name):
        self.id = Subject.id
        self.name = name
        Subject.ids.append(self.id)
        Subject.names.append(self.name)
        Subject.id += 1

    def get_subjects(self):
        self.subjects = dict(zip(self.ids, self.names))

    def get_rsubjects(self):
        self.rsubjects = dict(zip(self.names, self.ids))


class Score:
    scores = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    average_scores = [0]*10

    def __init__(self, studentid, subjectid, mark):
        self.score = mark
        self.scores[studentid - 1][subjectid - 1] = self.score

    def get_average_scores(self):
        self.average_scores = [float(sum(self.scores[i])) / (len(self.scores[i])) for i in range(0, 10)]

# students:
student1 = Student("К П Р")
student2 = Student("Л К Д")
student3 = Student("ф Ы У")
student4 = Student("Й Щ О")
student5 = Student("Т Л К")
student6 = Student("М А К")
student7 = Student("С О Н")
student8 = Student("И Р О")
student9 = Student("М К А")
student10 = Student("Х С С")

# statistics:
stat1 = Statistics(1)
stat2 = Statistics(2)
stat3 = Statistics(3)
stat4 = Statistics(4)
stat5 = Statistics(5)
stat6 = Statistics(6)
stat7 = Statistics(7)
stat8 = Statistics(8)
stat9 = Statistics(9)
stat10 = Statistics(10)

# subjects:
subject1 = Subject('timp')
subject2 = Subject('eis')
subject3 = Subject('philosophy')
subject4 = Subject('english')
subject5 = Subject('sport')

# scores:
# student1
score1_1 = Score(1, 1, randint(1, 5))
score1_2 = Score(1, 2, randint(1, 5))
score1_3 = Score(1, 3, randint(1, 5))
score1_4 = Score(1, 4, randint(1, 5))
score1_5 = Score(1, 5, randint(1, 5))
# student2
score2_1 = Score(2, 1, randint(1, 5))
score2_3 = Score(2, 3, randint(1, 5))
score2_4 = Score(2, 4, randint(1, 5))
score2_5 = Score(2, 5, randint(1, 5))
score2_2 = Score(2, 2, randint(1, 5))
# student3
score3_1 = Score(3, 1, randint(1, 5))
score3_2 = Score(3, 2, randint(1, 5))
score3_3 = Score(3, 3, randint(1, 5))
score3_4 = Score(3, 4, randint(1, 5))
score3_5 = Score(3, 5, randint(1, 5))
# student 4
score4_1 = Score(4, 1, randint(1, 5))
score4_2 = Score(4, 2, randint(1, 5))
score4_3 = Score(4, 3, randint(1, 5))
score4_4 = Score(4, 4, randint(1, 5))
score4_5 = Score(4, 5, randint(1, 5))
# student 5
score5_1 = Score(5, 1, randint(1, 5))
score5_2 = Score(5, 2, randint(1, 5))
score5_3 = Score(5, 3, randint(1, 5))
score5_4 = Score(5, 4, randint(1, 5))
score5_5 = Score(5, 5, randint(1, 5))
# student 6
score6_1 = Score(6, 1, randint(1, 5))
score6_2 = Score(6, 2, randint(1, 5))
score6_3 = Score(6, 3, randint(1, 5))
score6_4 = Score(6, 4, randint(1, 5))
score6_5 = Score(6, 5, randint(1, 5))
# student 7
score7_1 = Score(7, 1, randint(1, 5))
score7_2 = Score(7, 2, randint(1, 5))
score7_3 = Score(7, 3, randint(1, 5))
score7_4 = Score(7, 4, randint(1, 5))
score7_5 = Score(7, 5, randint(1, 5))
# student 8
score8_1 = Score(8, 1, randint(1, 5))
score8_2 = Score(8, 2, randint(1, 5))
score8_3 = Score(8, 3, randint(1, 5))
score8_4 = Score(8, 4, randint(1, 5))
score8_5 = Score(8, 5, randint(1, 5))
# student 9
score9_1 = Score(9, 1, randint(1, 5))
score9_2 = Score(9, 2, randint(1, 5))
score9_3 = Score(9, 3, randint(1, 5))
score9_4 = Score(9, 4, randint(1, 5))
score9_5 = Score(9, 5, randint(1, 5))
# student 10
score10_1 = Score(10, 1, randint(1, 5))
score10_2 = Score(10, 2, randint(1, 5))
score10_3 = Score(10, 3, randint(1, 5))
score10_4 = Score(10, 4, randint(1, 5))
score10_5 = Score(10, 5, randint(1, 5))

# init:
Student.get_students(Student)
Subject.get_subjects(Subject)
Subject.get_rsubjects(Subject)
Score.get_average_scores(Score)
main_stats = [[], [], [], [], [], [], [], [], [], []]
for i in range(0, 10):
    main_stats[i] = {
        'id': i + 1,
        'fio': Student.students.get(i + 1),
        'timp': Score.scores[i][Subject.rsubjects.get('timp') - 1],
        'eis': Score.scores[i][Subject.rsubjects.get('eis') - 1],
        'philosophy': Score.scores[i][Subject.rsubjects.get('philosophy') - 1],
        'english': Score.scores[i][Subject.rsubjects.get('english') - 1],
        'sport': Score.scores[i][Subject.rsubjects.get('sport') - 1],
        'average': Score.average_scores[i]
    }
