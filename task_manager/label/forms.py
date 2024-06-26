from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from task_manager.label.models import Label


class LabelForm(ModelForm):
    name = forms.CharField(label=_('Name'))

    class Meta:
        model = Label
        fields = ['name', ]
