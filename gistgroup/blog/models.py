from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)]) # URL for accessing the detail view of this blog post


class BlogPost(models.Model):
    title = models.CharField(max_length=200) # Title of the blog post
    content = models.TextField() # Content of the blog post
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey relationship with User model as the admin
    publication_date = models.DateField(auto_now_add=True) # Date the blog post was published
    category = models.CharField(max_length=200, default='News') # Category of the blog post

    def __str__(self):
        return self.title + ' | ' + str(self.author) # String representation of the blog post

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)]) # URL for accessing the detail view of this blog post