# Generated by Django 5.1.3 on 2024-11-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_events_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date_time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
