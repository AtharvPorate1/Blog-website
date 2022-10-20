from logging.handlers import SYSLOG_UDP_PORT
from turtle import title
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100 )
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
        


