from django.shortcuts import render
from django.views import generic
from .models import Tool

class ToolList(generic.ListView):
    model = Tool
    queryset = Tool.objects.filter(published_status=1).order_by('-date_added')
    template_name = 'tools.html'
    paginate_by = 8

'''Renders a home page template'''

class HomePageView(generic.TemplateView):
    template_name = 'index.html'
