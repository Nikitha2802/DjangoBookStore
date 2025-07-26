from django.db import models

class Book(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, default=False)
    follow_author = models.CharField(max_length=2083, blank=True)  
    book_available = models.BooleanField(default=False)

