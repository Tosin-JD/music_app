from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError


# import the user form
from .forms import UserCreationForm, UserUpdateForm

# get the user model
User = get_user_model()

# Create your views here.
class SignUp(generic.CreateView):
    model = User
    template_name = 'accounts/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    
    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'A user with this email exists. ' + \
                                 'Please use a different email.')
        else:
            return render(request, 
                         template_name=self.template_name,
                         context=self.get_context_data())


class UserUpdateView(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = 'accounts/update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('accounts:profile')
    
    
class Profile(LoginRequiredMixin, generic.TemplateView):
    """view for profile"""
    model = User
    template_name = 'accounts/profile.html'


class ThanksPage(generic.TemplateView):
    """thanks page when the user logs out"""
    template_name = 'accounts/thanks.html'
    

    
