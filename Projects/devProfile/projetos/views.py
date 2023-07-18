from typing import Any, Dict
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

    def get_context_data(self, **kwargs):
        context = super(Detailprojects, self).get_context_data(**kwargs)
        other_projects = Profile.objects.filter(categoria=self.get_object().categoria)
        context["other_projects"] = other_projects
        return context