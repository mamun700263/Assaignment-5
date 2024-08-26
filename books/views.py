from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView
from .models import Books
from accounts.models import Account
from transaction.models import TransactionReport
from review.forms import ReviewForm
from review.models import Review

class BookDetail(DetailView):
    model = Books
    template_name = 'books/detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        book = self.get_object()
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ReviewForm()
        context['comments'] = Review.objects.filter(book=book).order_by('-time')

        if self.request.user.is_authenticated:
            account = get_object_or_404(Account, user=self.request.user)
            transaction = TransactionReport.objects.filter(account=account, book=book, have_now=True).exists()
            context['have'] = transaction
            read = TransactionReport.objects.filter(account=account, book=book, read=True).exists()
            context['read'] = read
        else:
            context['have'] = False
            context['read'] = False
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid() and self.user_can_review():
            review = form.save(commit=False)
            review.account = get_object_or_404(Account, user=request.user)
            review.book = book
            review.save()
            return redirect(reverse('detail', kwargs={'pk': book.pk}))
        else:
            return self.render_to_response(self.get_context_data(comment_form=form))

    def user_can_review(self):
        if self.request.user.is_authenticated:
            account = get_object_or_404(Account, user=self.request.user)
            book = self.get_object()
            return TransactionReport.objects.filter(account=account, book=book, have_now=True).exists()
        return False
