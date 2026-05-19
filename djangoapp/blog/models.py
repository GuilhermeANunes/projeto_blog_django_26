from django.db import models
from utils.rands import slugfy_new
from utils.image import resize_image
from django.contrib.auth.models import User


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

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True ,blank=True, default=None, null=True, max_length=55
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    content = models.TextField(null=True)
    cover = models.ImageField(upload_to='post/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text='Exibir a imagem de capa também no post?')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_created_by'
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category ,on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    tag = models.ManyToManyField(Tag, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.name, 5)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name
        
        if cover_changed:
            resize_image(self.cover, 900)

        return super_save
    
    def __str__(self):
        return self.title