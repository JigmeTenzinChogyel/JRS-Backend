# Generated by Django 4.2.10 on 2024-02-25 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='user_id',
            new_name='user',
        ),
    ]
