from django.db import models

# Create your models here.


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, default='')
    url = models.URLField(max_length=250, default='')
    score = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=250, default='')
    sentiment = models.CharField(max_length=100, default='')
    sentiment_confidence = models.DecimalField(max_digits=20, decimal_places=20, default=0)

    def __str__(self):
        return self.title
