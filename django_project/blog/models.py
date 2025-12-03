'''
    import the reverse function from django.urls to generate URLs by their name
'''

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # create a get_absolute_url method to redirect to the post 
    # detail page after creating a new post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
