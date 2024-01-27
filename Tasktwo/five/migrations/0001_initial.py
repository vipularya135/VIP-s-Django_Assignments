# Generated by Django 5.0.1 on 2024-01-27 08:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(default=0, null=True)),
                ('gender', models.CharField(default='Not Specified', max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]