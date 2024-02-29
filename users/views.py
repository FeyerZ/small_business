

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from users.forms import UserForm
from users.models import UserModel


class CreateUserView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')


# Create your views here.
class UsersListView(ListView):
    model = UserModel
    template_name = 'users/all.html'


class UsersUpdateView(UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')


class UsersDeleteView(DeleteView):
    model = UserModel
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users-all')


class UserDetailView(DetailView):
    model = UserModel
    template_name = 'users/detalii.html'
