from django import forms
from .models import BlogPost, Category

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'snippet', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'quill-editor'}), 
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
        }

    category = forms.ModelChoiceField(queryset=Category.objects.all())


# Form for creating or editing a Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  
        fields = ['name']  

