from django.urls import path
from .views import ( 
    BlogPostListView, 
    BlogPostDetailView, 
    AdminPostView, 
    UpdatePostView, 
    DeletePostView,
    AddCategoryView,
    CategoryView
)

urlpatterns = [
    # Route for the home page displaying a list of all blog posts
    path('', BlogPostListView.as_view(), name='index'),

    # Route for deleting a specific blog post by admin, identified by its primary key (pk)
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='admin_delete_post'),

   # Route for editing a specific blog post by admin, identified by its primary key (pk)
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='admin_edit_post'),

    # Route for displaying a single blog post detail, identified by its primary key (pk)
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),


 
    # Route for an admin to add a new blog post
    path('admin_post/', AdminPostView.as_view(), name='admin_post'),

    # Route for adding a new category
    path('add_category/', AddCategoryView.as_view(), name='add_category'),

    # Route for displaying blog posts filtered by a category, specified by 'section'
    path('category/<str:section>/', CategoryView, name='category'),

    # The following paths are commented out and not active in the current configuration
    # path('category/<str:section>/', CategoryView, name='category'),
    # path('category/<str:section>/', CategoryView, name='category'),
]

