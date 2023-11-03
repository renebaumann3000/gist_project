from django.urls import path
from .views import ( 
    BlogPostListView, 
    BlogPostDetailView, 
    AdminPostView, 
    UpdatePostView, 
    DeletePostView,
    
  )

urlpatterns = [
    path('', BlogPostListView.as_view(), name='index'), # URL for listing all blog posts
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'), # URL for displaying a single blog post
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='admin_delete_post'), # URL for deleting a blog post as admin
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='admin_edit_post'), # URL for editing a blog post as admin
    path('admin_post/', AdminPostView.as_view(), name='admin_post') # URL for adding a new admin blog post
]    

    

