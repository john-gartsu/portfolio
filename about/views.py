from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

class AboutView(TemplateView):
    template_name = 'about/about.html'
    extra_context = {'today': datetime.today()}