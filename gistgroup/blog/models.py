from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with User model
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])