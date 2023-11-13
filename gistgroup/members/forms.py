from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile

from blog.models import TreatmentLog



class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'socialmedia_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'socialmedia_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Custom User Registration Form
class SignUpForm(UserCreationForm):
    # Email field with custom widget and CSS class
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # First name field with custom widget and CSS class
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Last name field with custom widget and CSS class
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Specifying the User model
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)  # Fields to be included in the form

    # Initializing the form with custom settings
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Customizing widget attributes for each field
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# Custom User Profile Edit Form
class EditProfileForm(UserChangeForm):
    # Email field with custom widget and CSS class
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # First name field with custom widget and CSS class
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Last name field with custom widget and CSS class
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Specifying the User model
        fields = ('username', 'first_name', 'last_name', 'email',)  # Fields to be included in the form



class TreatmentLogForm(forms.ModelForm):
    class Meta:
        model = TreatmentLog
        fields = ('treatment_date', 'medication_name', 'dosage', 'side_effects')

