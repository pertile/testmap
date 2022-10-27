# Generated by Django 4.1.2 on 2022-10-26 14:05

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': ('view', 'change'),
            },
        ),
    ]
