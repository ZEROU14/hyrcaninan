# Generated by Django 5.1.3 on 2024-11-18 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_event_signup_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_signup',
            name='phone_number',
            field=models.PositiveIntegerField(help_text='لطفاً شماره تلفن را بدون پیش\u200cشماره وارد کنید.', unique=True, validators=[django.core.validators.MinValueValidator(10000000000, message='شماره تلفن باید حداقل 10 رقم داشته باشد.'), django.core.validators.MaxValueValidator(99999999999, message='شماره تلفن نباید بیشتر از 10 رقم باشد.')], verbose_name='your Phone Number'),
        ),
    ]
