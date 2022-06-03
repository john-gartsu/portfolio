from django.shortcuts import render
from django.views.generic import TemplateView

class CompaniesView(TemplateView):
    template_name = 'companies/companies.html'
   