from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import CreateUserForm


# Create your views here.


class LoginUserView(LoginView):
    template_name = "authentication/form.html"


class UserChangePaswordView(PasswordChangeView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('serviciu-all')


class CreateUserView(CreateView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('serviciu-all')
    form_class = CreateUserForm


class LogOutUserView(LogoutView):
    success_url = reverse_lazy('serviciu-all')


