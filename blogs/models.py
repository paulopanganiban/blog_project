from django.contrib.auth.models import User
# https://www.youtube.com/watch?v=aHC3uTkT9r8
from django.utils import timezone
from django.db import models
from django.db.models.fields import CharField


# pip install django-autoslug
from autoslug import AutoSlugField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #post model and user model will have a relationship, since user will author a post
    #use a FK

    def __str__(self):
        return self.title