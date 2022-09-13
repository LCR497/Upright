from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subjects', 'message')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : "form-control rounded-0", 'placeholder' : 'Name'}),
            'email' : forms.EmailInput(attrs={'class' : "form-control rounded-0", 'placeholder' : 'Email'}),
            'subjects' : forms.Select(attrs={'class' : "form-control", 'placeholder' : 'Subjects'}),
            'message' : forms.Textarea(attrs={'class' : "form-control rounded-0", 'placeholder' : 'Message'}),
        }
        labels = {
           'name' : '',
           'email' : '',
           'subjects' : '',
           'message' : '',
        }