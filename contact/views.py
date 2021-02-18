from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from decouple import config
from .forms import ContactForm


# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST, request.FILES)

        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            upload = request.FILES.get("upload")
            content = f"Message from django-structure project,\
            The user with name {name}, with the email {email},\
             write the following: \n Subject: {subject}\n\n\n \
             Message: {message}"

            email_content= EmailMessage(
                subject=subject,
                body=content,
                from_email= "",
                to=[config('EMAIL_TO')],
                attachments=[(upload.name, upload.read(), upload.content_type)],
                reply_to=[email]
            )
            try:
                email_content.send()

                return redirect("/contact/?valid")

            except:
                return redirect("/contact/?invalid")

    return render(request, "contact.html", {"form": contact_form})
