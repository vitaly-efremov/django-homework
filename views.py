from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *
import re


MANAGE_TEMPLATE_NAME = 'manage.html'

TABLES = [Teacher,
	Subject,
	Workload
	]



def get_table_name(model):
    return model.__name__


def get_edit_url(table_name, id):
    return '/edit{}/{}'.format(table_name, id)


def get_delete_url(table_name, id):
    return '/del{}/{}'.format(table_name, id)


def get_add_url(model):
    return '/add{}'.format(get_table_name(model))


def get_headers(model):
    return list(
        map(
            lambda x: re.sub('.*\.', '', str(x)),
            model._meta.fields
        )
    )


def get_content(model):
    res = list(
        map(
            lambda x: {
                'items': [getattr(
                    x,
                    re.sub('.*\.', '', str(field))
                ) for field in model._meta.fields],
                'url_edit': get_edit_url(
                    get_table_name(model),
                    getattr(x, 'id')
                ),
                'url_delete': get_delete_url(
                    get_table_name(model),
                    getattr(x, 'id')
                )
            },
            model.objects.all()
        )
    )
    return res


def get_table_info(table):
    return {
        'name': get_table_name(table),
        'url_add': get_add_url(table),
        'headers': get_headers(table),
        'content': get_content(table)
    }
	
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'tables': [get_table_info(table) for table in TABLES]
            }
        )
        return context
		
class addTeacher(CreateView):
    form_class = TeacherForm
    model = Teacher
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class delTeacher(DeleteView):
    form_class = TeacherForm
    model = Teacher
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class editTeacher(UpdateView):
    form_class = TeacherForm
    model = Teacher
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class addSubject(CreateView):
    form_class = SubjectForm
    model = Subject
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class delSubject(DeleteView):
    form_class = SubjectForm
    model = Subject
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class editSubject(UpdateView):
    form_class = SubjectForm
    model = Subject
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class addWorkload(CreateView):
    form_class = WorkloadForm
    model = Workload
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class delWorkload(DeleteView):
    form_class = WorkloadForm
    model = Workload
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"


class editWorkload(UpdateView):
    form_class = WorkloadForm
    model = Workload
    template_name = MANAGE_TEMPLATE_NAME
    success_url = "/"