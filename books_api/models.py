from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    body =  models.TextField()
    auther =  models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

