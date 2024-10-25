from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #TYPE AND ID 
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE) 
    content_object_id = models.PositiveIntegerField() 
    content_object = GenericForeignKey('content_type', 'content_object_id') 