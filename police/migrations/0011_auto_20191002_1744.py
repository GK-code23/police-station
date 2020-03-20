# Generated by Django 2.2.5 on 2019-10-02 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0010_police_info_duty_cnt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police_info',
            name='duty_cnt',
        ),
        migrations.CreateModel(
            name='daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('pol_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police.police_info')),
            ],
        ),
    ]
