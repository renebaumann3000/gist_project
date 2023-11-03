from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm
from django.urls import reverse_lazy

# def test(request):
#    return render(request, 'test.html')

class BlogPostListView(ListView):
    model = BlogPost  
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-publication_date']

class BlogPostDetailView(DetailView):  # Create a detail view
    model = BlogPost
    template_name = 'post_detail.html'
    context_object_name = 'post'

class AddAdminPostView(CreateView):
    model = BlogPost  
    form_class = BlogPostForm
    template_name = 'admin_post.html'
#    fields = '__all__'

class UpdatePostView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'admin_edit_post.html'
#    fields = ['title', 'content']

class DeletePostView(DetailView):
   model = BlogPost
   template_name = 'admin_delete_post.html'
   context_object_name = 'post'
   success_url = reverse_lazy('index')
