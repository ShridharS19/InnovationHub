# Generated by Django 2.0.4 on 2018-12-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0023_statistic_month_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=500)),
                ('admin_only', models.BooleanField()),
            ],
        ),
    ]