from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from blog.models import Profile

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# View for user registration
class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm  # Specifying the form class to use for registration
    template_name = 'registration/register.html'  # Template to render the registration form
    success_url = reverse_lazy('login')  # Redirect URL upon successful registration

# View for editing user profile
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm  # Form class to use for editing the user profile
    template_name = 'registration/edit_profile.html'  # Template to render the edit profile form
    success_url = reverse_lazy('index')  # Redirect URL upon successful profile update

    def get_object(self):
        return self.request.user  # Returns the current user object

# View for changing user password
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm  # Form class for changing password
    success_url = reverse_lazy('login')  # Redirect URL after password change

# View for displaying user profile
class ProfilePageView(DetailView):
    model = Profile  # The model associated with this view
    template_name = 'registration/user_profile.html'  # Template to render the user profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_member = get_object_or_404(Profile, id=self.kwargs['pk'])  # Get specific profile based on the primary key
        context["page_member"] = page_member  # Add the specific profile to the context
        return context

# View for editing user's profile page
class EditProfilePageView(generic.UpdateView):
    model = Profile  # The model associated with this view
    template_name = 'registration/edit_profile_page.html'  # Template to render the edit profile page form
    fields = ['bio, profile_pic, socialmedia_url']  # Fields to include in the form
    success_url = reverse_lazy('index')  # Redirect URL after successful profile update

