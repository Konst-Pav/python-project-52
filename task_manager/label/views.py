from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from task_manager.utils import LoginRequiredMixinWithMessage
from task_manager.label.models import Label
from task_manager.label.forms import LabelForm
from task_manager.task.models import Task
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class LabelIndexView(LoginRequiredMixinWithMessage, ListView):
    model = Label
    template_name = 'label/index.html'
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – list of labels')
        return context


class LabelCreateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'label/create.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('The label was created successfully')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – create a label')
        return context


class LabelUpdateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'label/update.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('The label has been successfully changed')
    login_url = reverse_lazy('login_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – change the label')
        return context


class LabelDeleteView(LoginRequiredMixinWithMessage, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('The label was successfully deleted')
    login_url = reverse_lazy('login_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – delete a label')
        body_title = _('Delete a label')
        body_subtitle = f"{_('Are you sure you want to delete the label')}: {context.get('label').name}"
        button_value = _('Yes, delete')
        context['body'] = {'title': body_title, 'subtitle': body_subtitle, 'button_value': button_value}
        return context

    def post(self, request, *args, **kwargs):
        tasks = Task.objects.filter(labels__id=kwargs['pk'])
        if list(tasks):
            messages.add_message(
                request,
                messages.ERROR,
                _('It is not possible to delete the label because it is being used'),
            )
            return redirect(reverse_lazy('labels_index'))
        return super().post(request, *args, **kwargs)
