from django.db import models
from accounts.models import Account
from books.models import Books

class TransactionReport(models.Model):
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    balance_then = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    have_now = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.name if self.book else 'Book Deleted'} - {self.account.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.pk: 
            self.balance_then = self.account.balance
        super().save(*args, **kwargs)
    
    def returner(self):
        self.have_now = False
        amount = self.book.price
        account = self.account
        Account.deposit_money(account, amount)
        self.save()
