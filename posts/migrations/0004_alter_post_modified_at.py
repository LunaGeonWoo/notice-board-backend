# Generated by Django 5.0.7 on 2024-08-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_is_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
