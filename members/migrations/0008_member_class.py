# Generated by Django 5.0.1 on 2024-01-09 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_re_class_remove_member_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ClASS',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.re_class'),
        ),
    ]
