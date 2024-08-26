from django.db import models
from django.contrib.auth.models import User
from books.models import Books

class Account(models.Model):
    """
    it will make a user with inbuild user along with balance and there will be a collection made with manytomany so that we can keep trak of already readen books
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    balance = models.IntegerField()
    borrowed_books = models.ManyToManyField(Books, related_name='borrowed_by', blank=True)

    def __str__(self):
        return self.user.username
    

    def deposit_money(self,amount):
        """
        recive the money first then add it here 
        
        """
        self.balance +=amount
        self.save()


    def buy_book(self,amount):
        """
        recive the money first then add it here 
        """
        if self.balance > amount:
            self.balance -= amount
            self.save()
            


