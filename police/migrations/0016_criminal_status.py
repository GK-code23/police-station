# Generated by Django 2.2.5 on 2019-10-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0015_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='status',
            field=models.CharField(default='---', max_length=20),
        ),
    ]
