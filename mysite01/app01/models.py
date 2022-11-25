from django.db import models

# Create your models here.
class test02(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

class book_info(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating_nums = models.CharField(max_length=100)
    rating_people = models.CharField(max_length=100)
    press = models.CharField(max_length=100)
    publication_time = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    book_img = models.CharField(max_length=100)
    book_summary = models.CharField(max_length=300)
    book_target = models.CharField(max_length=50)