from django.shortcuts import render
from django.views import View  # Import the View class for creating views
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,  # Import generic views for common operations
)
from django.utils.text import slugify
from .models import BlogPost, Category  # Import the BlogPost and Category models
from .forms import BlogPostForm, CategoryForm  # Import forms for BlogPost and Category
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required # Import decorator for login requirement
from django.utils.decorators import method_decorator # Import decorator for method-level decorators

# View for listing all blog posts, inheriting from ListView
class BlogPostListView(ListView):
    model = BlogPost  # Specify the model to list
    template_name = 'index.html'  # Template to render the list
    context_object_name = 'posts'  # Context name to be used in the template
    ordering = ['-publication_date']  # Ordering of the posts

    # Add extra context data
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()  # Get all category objects
        context = super(BlogPostListView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu  # Add categories to the context
        return context

# View for displaying a single blog post, inheriting from DetailView
class BlogPostDetailView(DetailView):
    model = BlogPost  # Specify the model for detail view
    template_name = 'post_detail.html'  # Template for displaying the post
    context_object_name = 'post'  # Context name to be used in the template

# View for adding a new admin blog post, with login requirement
@method_decorator(login_required, name='dispatch')  # Require login for this view
class AdminPostView(CreateView):
    model = BlogPost  # Specify the model for creation
    form_class = BlogPostForm  # Form for creating a post
    template_name = 'admin_post.html'  # Template for the creation form

    # Validate the form
    def form_valid(self, form): 
        form.instance.author = self.request.user  # Set the author as the current user
        return super().form_valid(form)

# View for adding a new category
class AddCategoryView(CreateView):
    model = Category  # Specify the model for category creation
    form_class = CategoryForm  # Form for creating a category
    template_name = 'add_category.html'  # Template for the creation form
    success_url = '/blog/'  # URL to redirect after successful creation

# View for displaying posts by category
def CategoryView(request, section):
    cleanSection = section.lower().replace('-', ' ')
    results = BlogPost.objects.filter(category__icontains=cleanSection)
    #category_posts = BlogPost.objects.filter(category=section.replace('-', ''))
    category_posts = BlogPost.objects.filter(category=section)
    print('categorys', results)
    return render(request, 'categories.html', {'section': section.title().replace('-', ' '), 'category_posts': results})

# View for updating an existing blog post as admin
class UpdatePostView(UpdateView):
    model = BlogPost  # Specify the model for updating
    form_class = BlogPostForm  # Form for updating a post
    context_object_name = 'post'
    template_name = 'admin_edit_post.html'  # Template for the update form

# View for deleting an existing blog post as admin
class DeletePostView(DeleteView):
   model = BlogPost  # Specify the model for deletion
   template_name = 'admin_delete_post.html'  # Template for the delete confirmation
   context_object_name = 'post'  # Context name to be used in the template
   success_url = reverse_lazy('index')  # URL to redirect after successful deletion
