from django.db import models

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   