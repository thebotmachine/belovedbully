from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


class AboutUsView(TemplateView):
    template_name = 'info/about.html'

