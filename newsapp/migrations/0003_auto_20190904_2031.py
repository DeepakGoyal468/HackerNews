# Generated by Django 2.2.5 on 2019-09-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_new_sentiment_confidence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
