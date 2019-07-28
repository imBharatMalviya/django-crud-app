from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=35)
    content = models.CharField(max_length=35)
    created_on = models.DateTimeField('date published')