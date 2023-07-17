from django.shortcuts import render
from .models import Profile
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"

class Projects(ListView):
    template_name = "projects.html"
    model = Profile

class Detailprojects(DetailView):
    template_name = "detailprojects.html"
    model = Profile