from django.forms import ModelForm
from .models import *


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class WorkloadForm(ModelForm):
    class Meta:
        model = Workload
        fields = '__all__'
