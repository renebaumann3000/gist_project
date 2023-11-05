from django.shortcuts import render
from django.views import View  # Import the View class
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
)
from django.utils.text import slugify
from .models import BlogPost, Category
from .forms import BlogPostForm, CategoryForm
from django.urls import reverse_lazy

# View for listing all blog posts.
class BlogPostListView(ListView):
    model = BlogPost  
    template_name = 'index.html'
    context_object_name = 'posts' # Specify the variable name in the template context for the list of posts.
    ordering = ['-publication_date']

# View for displaying a single blog post.
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    context_object_name = 'post' # Specify the variable name in the template context for the single post.

# View for adding a new admin blog post.
class AdminPostView(CreateView):
    model = BlogPost  
    form_class = BlogPostForm
    template_name = 'admin_post.html'

# View for adding a new category.
class AddCategoryView(CreateView):
    model = Category  
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = '/blog/'

class CategoryView(View):
    def get(self, request, section):
        category_posts = BlogPost.objects.filter(category=section.replace('-', ' '))
        return render(request, 'categories.html', {'section': section.title().replace('-', ' '), 'category_posts': category_posts})

#def CategoryView(request, section):
#    category_posts = BlogPost.objects.filter(category=section)
#    return render(request, 'categories.html', {'section': section, 'category_posts':category_posts})

# View for updating an existing blog post as admin.
class UpdatePostView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'admin_edit_post.html'

# View for deleting an existing blog post as admin.
class DeletePostView(DetailView):
   model = BlogPost
   template_name = 'admin_delete_post.html'
   context_object_name = 'post'
   success_url = reverse_lazy('index')


