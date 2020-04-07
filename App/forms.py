from django.forms import ModelForm
from App.models import *

class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ['membres']
