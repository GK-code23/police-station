# Generated by Django 2.2.5 on 2019-10-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0021_police_info_clas'),
    ]

    operations = [
        migrations.AddField(
            model_name='police_info',
            name='set',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
