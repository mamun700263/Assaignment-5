from django import forms
from accounts.models import Account

class DepositForm(forms.Form):
    amount = forms.IntegerField()



    def save(self,account,commit=False):
        amount = self.cleaned_data.get('amount')
        Account.deposit_money(account,amount)
        return amount 


    