from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

from ckeditor.fields import RichTextField 




# Model representing a category
class Category(models.Model):
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name  

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

# Model representing a user profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    bio = models.TextField()  
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/images/")  
    socialmedia_url = models.CharField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return str(self.user) 

# Model representing a blog post
class BlogPost(models.Model):
    title = models.CharField(max_length=200)  
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") 
    content = RichTextField(blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    publication_date = models.DateField(auto_now_add=True)  
    category = models.CharField(max_length=200, default='news')  
    snippet = models.CharField(max_length=200) 

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


# Model representing a treatment log
class TreatmentLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment_date = models.DateField()
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    side_effects = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Treatment Log for {self.user.username} on {self.treatment_date}"


