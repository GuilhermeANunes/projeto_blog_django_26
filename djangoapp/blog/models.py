from django.db import models
from utils.rands import slugfy_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True ,blank=True, default=None, null=True, max_length=55
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.name, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True ,blank=True, default=None, null=True, max_length=55
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.name, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True ,blank=True, default=None, null=True, max_length=55
    )
    is_published = models.BooleanField(default=True)
    content = models.TextField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.name, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title