from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):

    subject = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['contacts'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ContactModel
        fields = ['title', 'subject', 'email', 'contacts']
