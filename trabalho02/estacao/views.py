from django.shortcuts import render
from django.views.generic import ListView

from .models import Data

class DataListView(ListView):
    model = Data
    template_name = 'estacao/data_list.html'
    context_object_name = 'estacao'
