# Generated by Django 5.0.1 on 2024-01-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member_img_member_s_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ClASS',
            field=models.CharField(choices=[('rice', '飯'), ('noddles', '麵'), ('dessert', '甜點')], max_length=7, null=True),
        ),
    ]