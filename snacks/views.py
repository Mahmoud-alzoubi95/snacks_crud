from snacks.models import Snack
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

# from .models import Snack
# Create your views here.

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnacksDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "Create.html"
    model = Snack
    fields = ["title","discribtion","purchaser"]
