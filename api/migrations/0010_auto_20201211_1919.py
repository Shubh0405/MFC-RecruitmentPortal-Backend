# Generated by Django 3.1.3 on 2020-12-11 13:49

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201211_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, validators=[api.models.MyValidator()]),
        ),
    ]
