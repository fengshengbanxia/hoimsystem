# Generated by Django 3.2.9 on 2022-12-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoimsystem', '0005_auto_20221211_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='prefer_time',
            field=models.CharField(max_length=5),
        ),
    ]
