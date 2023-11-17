from django.contrib import admin
from .models import BlogPost, Category, Profile, TreatmentLog # import BlogPost model

admin.site.register(BlogPost)  # Register the BlogPost model with the admin interface
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(TreatmentLog)