# Generated by Django 2.0.7 on 2018-10-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(max_length=6),
        ),
    ]