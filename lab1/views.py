# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		students = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 
					'Герасимов Вячеслав', 'Иванов Александр', 'Ерохин Евгений', 'Кузнецова Мария', 
					'Лозинг Варвара', 'Пехова Анна', 'Машуков Никита']
		bad_students = []
		good_students = []
		spisok = []
		
		students_id = Student().create_id( students )
		students_score = Score().create_students_score( students )
		spisok = Statistics().create_spisok( students, students_score, good_students, bad_students, spisok, students_id)
		
		context.update(
			{
				'students_statistics': spisok,
				'excellent_students': good_students,
				'bad_students': bad_students
			}
		)
		return context


class Student:
	def create_id(self, students):
		return range(len(students))


class Statistics:
    # student_id, [Scores]
	def create_spisok(self, students, students_score, good_students, bad_students, spisok, students_id):
		for i in range(len(students)):
			if i <= len(students):
				value = Score().create_value( students_score[i])
				if value >= 4:
					good_students.append(students[i])
				elif value <=4:
					bad_students.append(students[i])
					
				spisok.append({
				'id':students_id[i]+1,
				'student': students[i],
				'ТиМП':students_score[i]['ТиМП'],
				'ЭиС': students_score[i]['ЭиС'],
				'Философия': students_score[i]['Философия'],
				'ИнЯз': students_score[i]['ИнЯз'],
				'Физра': students_score[i]['Физра'],
				'Среднийбалл': value})
		return spisok


class Score:
	def create_students_score(self, students):
		students_score = []
		for i in students:
			students_score.append({'ТиМП':random.randint(2,5),			'ЭиС':random.randint(2,5), 
									'Философия':random.randint(2,5),	'ИнЯз':random.randint(2,5),
									'Физра':random.randint(2,5)})
		return students_score
		
	def create_value(self, students_score):
		summa=0
		for score in students_score.values():
			summa += score
		value = summa / 5
		return value
	
    
