# Generated by Django 2.2.5 on 2019-09-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=250)),
                ('score', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=250)),
                ('sentiment', models.CharField(max_length=100)),
            ],
        ),
    ]
