from django.contrib import admin
from .models import BlogPost # import BlogPost model

admin.site.register(BlogPost)  # Register the BlogPost model with the admin interface
