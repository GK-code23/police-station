# Generated by Django 2.2.5 on 2019-10-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0025_search_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_help',
            name='case_id',
            field=models.CharField(default='null', max_length=10),
            preserve_default=False,
        ),
    ]