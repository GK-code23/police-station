# Generated by Django 2.2.5 on 2019-10-02 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0007_police_info_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='today',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_schedule', models.CharField(max_length=20)),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police.police_info')),
            ],
        ),
    ]
