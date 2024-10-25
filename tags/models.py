from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)
    
class TaggedItem(models.Model):
    tag =  models.ForeignKey(Tag, on_delete=models.CASCADE)
    #GENERIC RELATIONSHIPS NEEDS TYPE && ID 
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object_id = models.PositiveIntegerField()
    content_object =GenericForeignKey('content_type', 'content_object_id')