# Generated by Django 5.1 on 2024-09-10 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('pro_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prouser',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_service.subscription'),
        ),
    ]
