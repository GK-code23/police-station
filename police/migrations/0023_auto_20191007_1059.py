# Generated by Django 2.2.5 on 2019-10-07 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0022_police_info_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='note',
            new_name='note1',
        ),
    ]