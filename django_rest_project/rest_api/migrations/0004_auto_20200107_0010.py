# Generated by Django 3.0.2 on 2020-01-06 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0003_auto_20200107_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='blog_owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='bloglists', to=settings.AUTH_USER_MODEL),
        ),
    ]
