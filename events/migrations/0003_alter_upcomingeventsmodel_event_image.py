# Generated by Django 5.1.4 on 2025-01-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_upcomingeventsmodel_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingeventsmodel',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/events_images'),
        ),
    ]
