# Generated by Django 2.2.5 on 2019-10-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0027_auto_20191010_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
