# Generated by Django 2.0.5 on 2018-06-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20180605_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emp_mobile',
            field=models.IntegerField(default=220),
        ),
    ]
