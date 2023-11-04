from django.contrib import admin
from .models import BlogPost, Category # import BlogPost model

admin.site.register(BlogPost)  # Register the BlogPost model with the admin interface
admin.site.register(Category)