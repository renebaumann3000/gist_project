from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

from ckeditor.fields import RichTextField  # Rich text editor field

# Model representing a category
class Category(models.Model):
    name = models.CharField(max_length=200)  # Name of the category

    def __str__(self):
        return self.name  # String representation of the category

    def get_absolute_url(self):
        # URL for accessing the detail view of a category
        return reverse('post_detail', args=[str(self.pk)])

# Model representing a user profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # One-to-one relationship with User model
    bio = models.TextField()  # Biography of the user
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/images/")  # Profile picture
    socialmedia_url = models.CharField(max_length=200, blank=True, null=True)  # Social media URL

    def __str__(self):
        return str(self.user)  # String representation of the user profile

# Model representing a blog post
class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")  # Header image of the blog post
    content = RichTextField(blank=True, null=True)  # Content of the blog post using a rich text editor
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the post, linked to User model
    publication_date = models.DateField(auto_now_add=True)  # Publication date of the post, automatically set
    category = models.CharField(max_length=200, default='news')  # Category of the blog post
    snippet = models.CharField(max_length=200)  # Short snippet or summary of the blog post

    def __str__(self):
        # String representation of the blog post
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # URL for accessing the detail view of this blog post
        return reverse('post_detail', args=[str(self.pk)])

