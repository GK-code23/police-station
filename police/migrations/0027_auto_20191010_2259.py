# Generated by Django 2.2.5 on 2019-10-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0026_search_help_case_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='police_info',
            name='salary',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='search_help',
            name='ph',
            field=models.CharField(max_length=10),
        ),
    ]
