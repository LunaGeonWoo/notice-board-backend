# Generated by Django 5.0.7 on 2024-07-31 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='updated_at',
            new_name='modified_at',
        ),
    ]
