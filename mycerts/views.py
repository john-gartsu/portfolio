from django.shortcuts import render
from django.views.generic import TemplateView
# from datetime import datetime

class MyCertsView(TemplateView):
    template_name = 'mycerts/mycerts.html'
   