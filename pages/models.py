from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class AboutUs(models.Model):
    whatis_runclub = RichTextField()
    our_mission = RichTextField()

class Sponsers(models.Model):
    # name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sponsers_image/')
    link = models.URLField(max_length=300)