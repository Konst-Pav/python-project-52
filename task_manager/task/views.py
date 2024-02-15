from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from task_manager.task.models import Task
from task_manager.task.forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.utils import LoginRequiredMixinWithMessage
from task_manager.task.filters import TaskFilter
from django_filters.views import FilterView


class TaskIndexView(LoginRequiredMixinWithMessage, FilterView):
    filterset_class = TaskFilter
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    filterset_fields = ['executor', 'status', 'label']


class TaskCreateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TaskReadView(LoginRequiredMixinWithMessage, DetailView):
    model = Task
    template_name = 'task/read.html'
    login_url = reverse_lazy('login_view')
    context_object_name = 'task'


class TaskUpdateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/update.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно изменена'
    login_url = '/login/'


class TaskDeleteView(LoginRequiredMixinWithMessage, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно удалена'
    login_url = '/login/'
