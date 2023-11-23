from django.shortcuts import render
from django.views import View 
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

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# View for listing all blog posts, inheriting from ListView
class BlogPostListView(ListView):
    model = BlogPost  
    template_name = 'index.html'  
    context_object_name = 'posts'  
    ordering = ['-publication_date']  

    # Add extra context data
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()  
        context = super(BlogPostListView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu  
        return context

# View for displaying a single blog post, inheriting from DetailView
class BlogPostDetailView(DetailView):
    model = BlogPost  
    template_name = 'post_detail.html' 
    context_object_name = 'post'  

# View for adding a new admin blog post, with login requirement
@method_decorator(login_required, name='dispatch') 
class AdminPostView(CreateView):
    model = BlogPost 
    form_class = BlogPostForm  
    template_name = 'admin_post.html'

    # Validate the form
    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super().form_valid(form)

# View for adding a new category
class AddCategoryView(CreateView):
    model = Category 
    form_class = CategoryForm  
    template_name = 'add_category.html' 
    success_url = reverse_lazy('index')  

# View for displaying posts by category
def CategoryView(request, section):
    cleanSection = section.lower().replace('-', ' ')
    results = BlogPost.objects.filter(category__icontains=cleanSection)

    category_posts = BlogPost.objects.filter(category=section)
    print('categorys', results)
    return render(request, 'categories.html', {'section': section.title().replace('-', ' '), 'category_posts': results})

# View for updating an existing blog post as admin
class UpdatePostView(UpdateView):
    model = BlogPost 
    form_class = BlogPostForm  
    context_object_name = 'post'
    template_name = 'admin_edit_post.html'  

# View for deleting an existing blog post as admin
class DeletePostView(DeleteView):
   model = BlogPost  
   template_name = 'admin_delete_post.html'  
   context_object_name = 'post'  
   success_url = reverse_lazy('index') 
