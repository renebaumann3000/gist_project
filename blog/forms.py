from django import forms
from .models import BlogPost, Category

# Appending each category tuple to the categories list

# Form for creating or editing a BlogPost (idea that no server restart is needed when addin a category)
#class BlogPostForm(forms.ModelForm):

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['category'] = forms.Select(choices=Category.objects.all().values_list('name', 'name'), attrs={'class': 'form-control'})

#    class Meta:
#        model = BlogPost  # The model associated with this form
        # Fields to be included in the form
#        fields = ['title', 'content', 'category', 'snippet', 'header_image'] 

        # Widgets to define HTML form input types and CSS classes
#        widgets = {
 #           'title': forms.TextInput(attrs={'class': 'form-control'}),
 #           'content': forms.Textarea(attrs={'class': 'form-control'}),
#            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            # Dropdown for selecting category, populated with categories_list
 #           'author': forms.Select(attrs={'class': 'form-control'}),  # Author field (Note: This field is not listed in 'fields')


 
 #       }
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'snippet', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
        }

    category = forms.ModelChoiceField(queryset=Category.objects.all())


# Form for creating or editing a Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # The model associated with this form
        fields = ['name']  # Field to be included in the form

