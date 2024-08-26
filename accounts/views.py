import random
from django.shortcuts import render
# from .forms import AccountForm
from .forms import RegistrationForm
from .models import Account
from books.models import Books,Category
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,TemplateView,FormView,ListView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from .constants import quotes
from transaction.models import TransactionReport
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.





class RegistrationView(FormView):
    template_name = 'accounts/form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        mail_subject = "Deposit Message"
        message = render_to_string('accounts/registration_mail.html', {
            'user': self.request.user
        })
        recivers_mail = self.request.user.email
        email = EmailMessage(subject=mail_subject, body=message, to=[recivers_mail])
        email.content_subtype = "html"
        email.send()
        return super().form_valid(form)
    

class LoginPage(LoginView):
    template_name = 'accounts/form.html'
    form_class = AuthenticationForm
    success_url= reverse_lazy('profile')


    
    def get_context_data(self, **kwargs):
        """
        to know more about the form
        """
        context = super().get_context_data(**kwargs)
        context["form_type"] = 'Log In'
        return context
    

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    
    def get_object(self):
        return Account.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["account"] = Account.objects.get(user=self.request.user)
        context["transactions"] = TransactionReport.objects.filter(account__user=self.request.user)
        return context


class HomeView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'books'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
        if some one hits any brand that will triger the url in the action button and send the brand here 
        """
        context['quote'] = random.choice(quotes)
        cat = self.kwargs.get('cat')
        if cat :
            context['searched_category'] = Category.objects.get(id = cat)
            context['books'] = Books.objects.filter(categories__id=cat)
            context['search'] = context['books'].count()
        else:
            context['books'] = Books.objects.all()
        context["category"] =  Category.objects.all()
    
        return context


class CustomLogout(LoginRequiredMixin,LogoutView):
    next_page = reverse_lazy('login')