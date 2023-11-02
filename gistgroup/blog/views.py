from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost

# def test(request):
#    return render(request, 'test.html')

class BlogPostListView(ListView):
    model = BlogPost  
    template_name = 'index.html'
    context_object_name = 'posts'

class BlogPostDetailView(DetailView):  # Create a detail view
    model = BlogPost
    template_name = 'post_detail.html'
    context_object_name = 'post'

class AddAdminPostView(CreateView):
    model = BlogPost  
    template_name = 'admin_post.html'
    fields = '__all__'

