from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
