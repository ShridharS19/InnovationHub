# Generated by Django 2.0.4 on 2019-01-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0026_video_serial_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
