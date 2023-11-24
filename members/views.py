from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ProfilePageForm, TreatmentLogForm
from blog.models import Profile

from blog.models import BlogPost

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

from blog.models import TreatmentLog


# View for user registration
class UserRegistrationView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm 
    template_name = 'registration/register.html'
    success_url = '/members/login/'
    success_message = "Your account was created successfully. You can now log in."


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_member_profile_page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return response

# View for editing user profile
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm  
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index') 

    def get_object(self):
        return self.request.user 

# View for changing user password
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm  
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('login') 

# View for displaying user profile
class ProfilePageView(DetailView):
    model = Profile 
    template_name = 'registration/user_profile.html' 

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_member = get_object_or_404(Profile, id=self.kwargs['pk'])  
        context["page_member"] = page_member 

        post = BlogPost.objects.filter(author=self.request.user).first()
        context["post"] = post 
        treatment_logs = TreatmentLog.objects.filter(user=self.request.user)
        context["treatment_logs"] = treatment_logs
        
        return context

# View for editing user's profile page
class EditProfilePageView(generic.UpdateView):
    model = Profile  
    template_name = 'registration/edit_profile_page.html' 
    fields = ['bio', 'profile_pic', 'socialmedia_url']  
    success_url = reverse_lazy('index') 

    def get_context_data(self, *args, **kwargs):
        print('this is the edit profile page view')
        context = super().get_context_data(*args, **kwargs)
        treatment_log_form = TreatmentLogForm()
        # Retrieve and pass the treatment logs for the user
        treatment_logs = TreatmentLog.objects.filter(user=self.request.user)
        context["treatment_logs"] = treatment_logs
        treatment_log_form = TreatmentLogForm()
        if treatment_logs:
            latest_log = treatment_logs.first()
            latest_log_content = {
                'treatment_date': latest_log.treatment_date,
                'medication_name': latest_log.medication_name,
                'dosage': latest_log.dosage,
                'side_effects': latest_log.side_effects
            }
            treatment_log_form = TreatmentLogForm(initial=latest_log_content, auto_id=False)
        context['treatment_log_form'] = treatment_log_form
        return context

    def form_valid(self, form):
        # Handle saving the treatment logs form
        treatment_log_form = TreatmentLogForm(self.request.POST)
        if treatment_log_form.is_valid():

            treatment_log = treatment_log_form.save(commit=False)
            treatment_log.user = self.request.user
            treatment_log.save()
        return super().form_valid(form)


def member_profiles_view(request):
    profiles = Profile.objects.all()  
    return render(request, 'members/profile_list.html', {'profiles': profiles})
