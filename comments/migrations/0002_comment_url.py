# Generated by Django 2.1 on 2018-09-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
