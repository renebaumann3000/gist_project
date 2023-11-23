from django.urls import path
from .views import (
    UserRegistrationView, 
    UserEditView,
    PasswordsChangeView,
    ProfilePageView,
    EditProfilePageView,
    CreateProfilePageView,
    member_profiles_view,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'), 

    path('edit_profile/', UserEditView.as_view(), name='edit_profile'), 

    path('password/', PasswordsChangeView.as_view(), name='change_password'),  

    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'), 

    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'), 

    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),

    path('members/', member_profiles_view, name='member_profiles'),

]
