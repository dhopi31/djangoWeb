from django.db import models
from django.utils.text import slugify

# Create your models here.
class PostProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(blank=True)    
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.name)
        super(PostProduct, self).save()

    def __str__(self):
        return self.name

class PostImageProduct(models.Model):
    post = models.ForeignKey(PostProduct, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to = 'product/%Y/%m')

    def __str__(self):
        return self.post.name   

