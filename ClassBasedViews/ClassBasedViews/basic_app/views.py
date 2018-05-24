from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import (View, TemplateView, 
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from . import models


class SchoolListView(ListView):
    template_name = 'basic_app/school_list.html'
    model = models.School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')
    template_name = 'basic_app/new_school.html'


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')
    template_name = 'basic_app/new_school.html'


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
    template_name = 'basic_app/confirm_delete.html'