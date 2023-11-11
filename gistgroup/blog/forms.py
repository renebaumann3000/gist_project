from django import forms
from .models import BlogPost, Category

# Retrieving all categories and converting them into a list of tuples
categories = Category.objects.all().values_list('name', 'name')

categories_list = []

# Appending each category tuple to the categories list
for item in categories:
    categories_list.append(item)

# Form for creating or editing a BlogPost
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # The model associated with this form
        # Fields to be included in the form
        fields = ['title', 'content', 'category', 'snippet', 'header_image'] 

        # Widgets to define HTML form input types and CSS classes
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            # Dropdown for selecting category, populated with categories_list
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),  # Author field (Note: This field is not listed in 'fields')
        }

# Form for creating or editing a Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # The model associated with this form
        fields = ['name']  # Field to be included in the form

