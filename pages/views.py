from django.shortcuts import render
from django.views.generic.base import TemplateView #its class

class HomePageView(TemplateView):
    template_name = 'home.html'


