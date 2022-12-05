from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_ListView.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'Snack_DetailView.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'Snack_CreateView.html'
    model = Snack
    fields = ['title','purchaser','description']

class SnackUpdateView(UpdateView):
    template_name = 'Snack_UpdateView.html'
    model = Snack
    fields = ['title','purchaser','description']

class SnackDeleteView(DeleteView):
    template_name = 'Snack_DeleteView.html'
    model = Snack
    success_url = reverse_lazy('snack_listview')
