# Generated by Django 4.1.2 on 2022-10-26 14:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile2',
            new_name='UserProfile',
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
    ]