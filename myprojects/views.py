from django.shortcuts import render
from django.views.generic import TemplateView

class MyProjectsView(TemplateView):
    template_name = 'myprojects/myprojects.html'