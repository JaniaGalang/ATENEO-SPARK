# Generated by Django 5.0.7 on 2024-07-20 02:21

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0009_remove_reservation_estimated_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_reserved',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='plate_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.spot'),
        ),
    ]
