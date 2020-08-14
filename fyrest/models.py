from django.db import models
##
from django.contrib.auth import get_user_model
from django.conf import settings
USER_MODEL = get_user_model()
# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class NewsContent(models.Model):
    reporter = models.ForeignKey(to=USER_MODEL,on_delete=models.CASCADE,related_name='news_contents')
    headline = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.headline
