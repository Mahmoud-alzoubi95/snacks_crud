from snacks.models import Snack
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

class SnacksListView(ListView):
    template_name = 'List.html'
    model = Snack
