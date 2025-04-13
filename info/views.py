from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


class AboutUsView(TemplateView):
    template_name = 'info/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Наша история"
        return context

