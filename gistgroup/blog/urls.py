# from django.urls import path
# from . import views


# urlpatterns = [
#    path('test/', views.test, name='test'),
# ]

from django.urls import path
from .views import BlogPostListView  # Import the class-based view

urlpatterns = [
    path('', BlogPostListView.as_view(), name='test'),
]

