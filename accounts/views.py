from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# import the user form
from .forms import UserCreationForm

# get the user model
User = get_user_model()

# Create your views here.
class SignUp(generic.CreateView):
    model = User
    template_name = 'accounts/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')


class Profile(LoginRequiredMixin, generic.TemplateView):
    """view for profile"""
    template_name = 'accounts/profile.html'


class ThanksPage(generic.TemplateView):
    """thanks page when the user logs out"""
    template_name = 'accounts/thanks.html'
    

    
