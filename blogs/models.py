from django.db import models
from django.shortcuts import reverse

from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description =RichTextField()
    datetime_created = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    title_image = models.ImageField(upload_to='blogs_title/', )
    tag = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.pk])
    