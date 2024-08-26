from django.db import models

# Create your models here.
from django.db import models
from accounts.models import Account
from books.models import Books
from django.contrib import messages
from .constant import RATING

class Review(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(choices=RATING)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.message
    
