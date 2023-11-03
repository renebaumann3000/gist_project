# from django.urls import path
# from . import views


# urlpatterns = [
#    path('test/', views.test, name='test'),
# ]

from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, AddAdminPostView, UpdatePostView, DeletePostView  # Import the class-based view

urlpatterns = [
    path('', BlogPostListView.as_view(), name='index'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='admin_delete_post'),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='admin_edit_post'),
    path('admin_post/', AddAdminPostView.as_view(), name='admin_post')
]    

    

