# Generated by Django 5.1.4 on 2025-01-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingeventsmodel',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='events_images/'),
        ),
    ]
