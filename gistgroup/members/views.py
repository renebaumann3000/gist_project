from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from blog.models import Profile

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        members = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_member = get_object_or_404(Profile, id=self.kwargs['pk'])


        context["page_member"] = page_member
        return context
