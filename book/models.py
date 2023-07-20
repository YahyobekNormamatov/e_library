from django.db import models
from datetime import datetime
from author.models import AuthorModel
from django.contrib.auth.models import AbstractUser

from author.models import AuthorModel
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('A','Author'),
        ('b','Book')
    )
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class BookCategoryModel(models.Model):
    name = models.CharField(max_length=50, default='')
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'book_category'

class BookModel(models.Model):
    category =models.ForeignKey(BookCategoryModel,on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    page = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    year=models.DateTimeField(default=datetime.now)
    info=models.CharField(max_length=200,default='')
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'book'
