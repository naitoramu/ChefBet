# Generated by Django 3.2.3 on 2021-05-31 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_types_odds'),
    ]

    operations = [
        migrations.AddField(
            model_name='types',
            name='parameters',
            field=models.JSONField(default='{}'),
        ),
    ]
