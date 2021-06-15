from snacks.models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy


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


class SnackUpdateView(UpdateView):
    template_name = 'update.html'
    model = Snack
    fields = ["title","discribtion","purchaser"]


class SnackDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Snack
    success_url = reverse_lazy("home")
