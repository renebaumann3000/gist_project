# from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

# def test(request):
#    return render(request, 'test.html')

class BlogPostListView(ListView):
    model = BlogPost  
    template_name = 'test.html'
    context_object_name = 'posts'
