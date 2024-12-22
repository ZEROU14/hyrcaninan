# Generated by Django 5.1.3 on 2024-11-18 19:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_event_signup_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_signup',
            name='category',
            field=models.TextField(choices=[('zir_35', 'zir_35'), ('Female', 'Female')], verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='event_signup',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message="(Phone number must be entered in the format: '+989123456789' or '09123456789'. Up to 12 digits allowed.)", regex='^(\\+98|0)?9\\d{9}$')], verbose_name='Phone Number'),
        ),
    ]