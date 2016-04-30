# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        stdnts = [ 'Первый Первый ' , ' Второй Второй' , ' Третий Третий ' , ' Четвертый Четвертый ' , 
                    ' Пятый Пятый' , ' Шестой Шестой ' , ' Седьмой Седьмой ' , ' Восьмой Восьмой ' ,
                    ' Девятый Девятый ' , ' Десятый Десятый ']
        bstdnts = sort.find(stdnts) 
        gstdnts = sort.find(stdnts) # Good student(point = 5)
        ss = score.crt_ss(stdnts) # 1st S-subject; 2nd S-score 
        p_id = ids.crt_id(stdnts)
        stts= sort.find(stdnts,ss,p_id) # stdnts, points, P_ids
        
        
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


class ids:
    def crt_id(stdnts)
        P_id=[]
        for i in range(len(stdnts)):
            p_id.append(i)
            return P_id


class sort: # sorting students on bad and good
def find(stdnts,ss,p_id)
for i in range(len(stdnts)):
   value = statistics.crt_value(stdnts[i])
   if value >=3.5:
       gstdnts.appen(stdnts[i])
    elif value <=3.5:
        bstdnts.append(stdnts[i])
stts.append({
    'student ' : stdnts, 
    ' id ' : p_id, 
    'ТиМП': ss[i]['эис']
    'ЭиС': ss[i]['Физика']
    'Философия': ss[i]['Програмирование']
    'Ин. Яз': ss[i]['МатАн']   
    'Физ-ра': ss[i]['Физ-ра']  
    'Средний бал': value
    }) 
   return stts
   

class score:
 def crt_ss(stdnts):
     ss= []
     for i in stdnts:
         ss.append({ ' ТиМП ':random.randint(0, 5) , ' ЭиС ':random.randint(0, 5) , 
         'Философия':random.randint(0, 5) , 'Ин. Яз':random.randint(0, 5) , 'Физ-ра':random.randint(0, 5) })
return ss


class Statistics:
   def crt_value(ss):
       v=0
       for score in ss.values():
           V += score 
           value = v/5
           return value
    
