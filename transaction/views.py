from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from .forms import DepositForm
from books.models import Books
from accounts.models import Account
from django.views.generic import FormView
from transaction.models import TransactionReport
from django.core.mail import message,EmailMessage
from django.template.loader import render_to_string
# Create your views here.

class DepositView(FormView):
    template_name = 'transaction/form.html'
    form_class = DepositForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        account = Account.objects.get(user=self.request.user)
        deposit_amount = form.save(account) 
        
        to = self.request.user.email
        subject = "Deposit Done"
        message = render_to_string('transaction/deposit_mail.html', {
            'user': self.request.user,
            'deposit_amount': deposit_amount,
        })
        email = EmailMessage(subject=subject, body=message, to=[to])
        email.content_subtype = "html"
        email.send() 
        
        return super().form_valid(form)   



def borrow_book(request, book_id):
    book = Books.objects.get(id=book_id)
    account = Account.objects.get(user=request.user)
    amount = book.price
    if account.balance<amount:
        messages.error(request,'You don\'t have Enough money. Deposit some money ' )
        return redirect(reverse_lazy('deposit'))
    else:
        TransactionReport.objects.create(
            book = book,
            account=account,
            have_now = True,
            read = True
        )

        account.buy_book(amount)
        account.borrowed_books.add(book)
        return redirect(reverse_lazy('profile'))


def return_book(request, book_id):
    print('return_book is ok')
    book = Books.objects.get(id=book_id)
    account = Account.objects.get(user=request.user) 
    transactions = TransactionReport.objects.filter(account=account, book=book, have_now=True,read = True)
    transaction = transactions.first()
    transaction.returner() 
    transaction.save()


    return redirect(reverse('profile'))

