# Generated by Django 2.0.4 on 2018-04-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
