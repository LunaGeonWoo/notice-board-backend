# Generated by Django 5.0.7 on 2024-08-01 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 1, 11, 35, 13, 215677, tzinfo=datetime.timezone.utc)),
        ),
    ]
