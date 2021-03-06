# Generated by Django 3.2.4 on 2021-06-28 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_remove_coupon_enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    to_field='username'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    to_field='username'),
        ),
    ]
