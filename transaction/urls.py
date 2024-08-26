from django.urls import path
from .views import DepositView,borrow_book,return_book
from accounts.models import Account
urlpatterns = [
    path('deposit/',DepositView.as_view(),name='deposit'),
    path('borrow/<int:book_id>/',borrow_book,name='borrow'),
    path('return/<int:book_id>/',return_book,name='return'),
]
