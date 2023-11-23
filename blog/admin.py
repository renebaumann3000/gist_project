from django.contrib import admin
from .models import BlogPost, Category, Profile, TreatmentLog 

admin.site.register(BlogPost) 
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(TreatmentLog)