from django.db import models

# Create your models her.
class Item(models.Model):
    text = models.TextField(default='')