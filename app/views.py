from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from app.models import *
# Create your views here.
class home(TemplateView):
    template_name='app/home.html'

class school_list(ListView):
    model=School
    context_object_name='schools'