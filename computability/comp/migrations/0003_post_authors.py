# Generated by Django 2.0.7 on 2018-07-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_post_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='authors',
            field=models.CharField(default='Author1, Author2', max_length=100),
        ),
    ]
