from django.urls import path
from .views import (
    UserRegistrationView, 
    UserEditView,
    PasswordsChangeView,
    ProfilePageView,
    EditProfilePageView,
    CreateProfilePageView,
    member_profiles_view,
 #   TreatmentLogView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL pattern for user registration
    path('register/', UserRegistrationView.as_view(), name='register'),  # Maps to UserRegistrationView for handling registration

    # URL pattern for editing user profile
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),  # Maps to UserEditView for handling profile edits

    # URL pattern for changing password using custom view
    path('password/', PasswordsChangeView.as_view(), name='change_password'),  # Maps to PasswordsChangeView for password changes with a specific template

    # URL pattern for viewing a user's profile
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),  # Maps to ProfilePageView for displaying a specific user's profile, using user's primary key (pk)

    # URL pattern for editing a user's profile page
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),  # Maps to EditProfilePageView for editing a user's profile page, using user's primary key (pk)

    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),

    path('members/', member_profiles_view, name='member_profiles'),

  #  path('add_treatment_log/', TreatmentLogView.as_view(), name='add_treatment_log'),
]
