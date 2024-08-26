from .models import Account,User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    balance = forms.IntegerField()
    """
    will initially take necessary informations along with a initial balance
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'balance', 'password1', 'password2']

    def save(self, commit=True):
        """
        this part actually creates the object
        """
        user = super().save(commit=False)
        if commit:
            user.save()
        Account.objects.create(
            user=user,  
            balance=self.cleaned_data.get('balance'),
        )
        return user
