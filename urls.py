from django.conf.urls import url
from django.contrib import admin

from .views import IndexView
from .views import addWorkload, delWorkload, editWorkload
from .views import addSubject, delSubject, editSubject
from .views import addTeacher, delTeacher, editTeacher

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^addWorkload/$', addWorkload.as_view()),
    url(r'^delWorkload/(?P<pk>\d+)/$', delWorkload.as_view()),
    url(r'^editWorkload/(?P<pk>\d+)/$', editWorkload.as_view()),
    url(r'^addSubject/$', addSubject.as_view()),
    url(r'^delSubject/(?P<pk>\d+)/$', delSubject.as_view()),
    url(r'^editSubject/(?P<pk>\d+)/$', editSubject.as_view()),
    url(r'^addTeacher/$', addTeacher.as_view()),
    url(r'^delTeacher/(?P<pk>\d+)/$', delTeacher.as_view()),
    url(r'^editTeacher/(?P<pk>\d+)/$', editTeacher.as_view()),

]
