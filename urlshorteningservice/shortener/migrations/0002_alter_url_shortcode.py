# Generated by Django 5.2 on 2025-06-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(blank=True, max_length=12, unique=True),
        ),
    ]
