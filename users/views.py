from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm


class UserLogoutView(LogoutView):
    next_page = '/'


class UserRegistration(FormView):
    model = User
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        messages.error(request, 'Проверьте заполнение формы')
        return redirect(self.success_url)
