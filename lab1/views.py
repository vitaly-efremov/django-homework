# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        stdnts = [ 'Первый Первый ' , ' Второй Второй' , ' Третий Третий ' , ' Четвертый Четвертый ' , 
                    ' Пятый Пятый' , ' Шестой Шестой ' , ' Седьмой Седьмой ' , ' Восьмой Восьмой ' ,
                    ' Девятый Девятый ' , ' Десятый Десятый ']
        bstdnts = [] # bad student
        gstdnts = [] # Good student(point = 5)
        point = point.crt_point(stdnts) 
        P_id = sdnts.crt_id(stdnts)
        stts= [] # stdnts, points, P_ids
        subj= [ ' smthng1 ' , ' smthng2 ' , 'smthng3' , 'smthng4' , 'smthng5' ]
        
        for i in range(len(stdnts)):
            point=
        
        
        
        
        
        
        
        
        context.update(
            {
                'students_statistics': stdnts,
                'excellent_students': gstdnts,
                'bad_students': bsdtnts
            }
        )
        return context


class Student:
    def crt_id(stdnts)
        P_id=[]
        for i in range(len(stdnts)):
            p_id.append(i)
            return P_id


class Statistics:
    # student_id, [Scores]
    pass

class Subject:
    pass

class Score:
    # Subject, Student, value
    pass
