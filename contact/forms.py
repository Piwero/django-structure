from django import forms
from contact.models import Document


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=30)
    email = forms.EmailField(label="Email", required=True)
    CHOICES = (
        ('--------', (
            (1, '----------------------'),
        )),
        ('Error', (
            (11, 'System Error'),
            (12, 'Form Error'),
            (13, 'Payment Error'),
        )),
        ('Questions', (
            (21, 'Tutorial'),
            (22, 'Payments'),
        )),
        ('Other', (
            (31, 'Work with us'),
            (32, 'Marketing'),
            (33, 'Others')
        )),
    )
    subject = forms.ChoiceField(choices=CHOICES)
    message = forms.CharField(label="Message", widget=forms.Textarea)
    upload = forms.FileField()

    class Meta:
        document = Document
        fields = ('description', 'document',)

