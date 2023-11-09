from django.urls import path
from .views import ( 
    UserRegistrationView, 
    UserEditView,
    PasswordsChangeView,
    ProfilePageView
  )

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='password_change'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
]    