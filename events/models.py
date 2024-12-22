from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField

# models.py

from django.db import models
from django.core.validators import RegexValidator

# Validator for Iranian phone number
iran_phone_validator = RegexValidator(
    regex=r'^(\+98|0)?9\d{9}$',
    message=_("(Phone number must be entered in the format: '+989123456789' or '09123456789'. Up to 12 digits allowed.)")
)




# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField()
    time = models.TimeField()
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to='event_images/', )
    second_image = models.ImageField(upload_to='event_images/',)
    kilometers = models.IntegerField()
    gender = models.TextField(choices=[('Male', 'Male'), ('Memale', 'Female')])
    date_time_created = models.DateTimeField(default=timezone.now) 
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("events_detail", args=[self.pk])
    

class Event_SignUp(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100,verbose_name=_('first name'))
    last_name = models.CharField(max_length=100,verbose_name= _('Last Name'))
    Id_pic = models.ImageField(upload_to='Id_image/',verbose_name= _('Id Picture'))
    insurance_pic= models.ImageField(upload_to='insurance_image/',verbose_name=_('Insurance Picture'))
    paid_pic = models.ImageField(upload_to='paid_image/',verbose_name=_('عکس رسید'),blank=True)
    phone_number = models.CharField( max_length=12, verbose_name=_('Phone Number'), validators=[iran_phone_validator],unique=True )
    category = models.TextField(choices=[('زیر ۱۸', 'زیر ۱۸ ,  '), (_('18 ta 40'), _('18 ta 40')),(_('40 ta 45'), _('40 ta 45')),(_('45 bala'), _('45 bala'))], verbose_name=_('رده بندی'))
    # is_paid = mo
    
    
    def __str__(self):
        return (f"{self.name},,,{self.last_name},,,{self.event},,,")