from django.db import models

# Create your models here.

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')

