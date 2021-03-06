# Generated by Django 2.2.5 on 2019-09-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20190904_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='score',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='sentiment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='news',
            name='username',
            field=models.CharField(default='', max_length=250),
        ),
    ]
