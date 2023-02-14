from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MySignupView(CreateView):
    template_name = 'login/signup.html'
    form_class = SignupForm
    success_url = 'sc/'
    
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result

class MyLoginView(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm

class MyLogoutView(LogoutView):
    template_name = 'login/logout.html'

