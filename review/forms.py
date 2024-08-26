from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ["rating","message"]
    message = forms.CharField(
            widget=forms.Textarea(attrs={
                'rows': 4, 
                'cols': 50, 
                'style': 'width: 300px; height: 100px;',
            })
        )