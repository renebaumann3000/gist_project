from django import forms
from .models import BlogPost, Category

categories = Category.objects.all().values_list('name', 'name')

categories_list = []

for item in categories:
    categories_list.append(item)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'snippet', 'header_image'] #user restricition deleted author need to test
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
