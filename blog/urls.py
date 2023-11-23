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
    path('', BlogPostListView.as_view(), name='index'),

    path('post/<int:pk>/delete', DeletePostView.as_view(), name='admin_delete_post'),

    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='admin_edit_post'),

    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),

    path('admin_post/', AdminPostView.as_view(), name='admin_post'),

    path('add_category/', AddCategoryView.as_view(), name='add_category'),

    path('category/<str:section>/', CategoryView, name='category'),

]

