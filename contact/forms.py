from django import forms
from contact.models import Document


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=30)
    email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Subject", required=True, max_length=50)
    message = forms.CharField(label="Message", widget=forms.Textarea)
    #upload = forms.FileField()

    class Meta:
        document = Document
        fields = ('description', 'document',)

