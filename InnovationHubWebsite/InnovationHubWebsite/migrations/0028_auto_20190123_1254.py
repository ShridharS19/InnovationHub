# Generated by Django 2.0.4 on 2019-01-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0027_job_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='file',
            field=models.FileField(upload_to='stl-uploads'),
        ),
    ]