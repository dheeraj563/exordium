# Generated by Django 2.0.7 on 2018-10-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0008_auto_20181006_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='check'),
        ),
    ]
