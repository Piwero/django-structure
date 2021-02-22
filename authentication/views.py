from django.shortcuts import render, redirect

# for basic signup form
from django.contrib.auth.forms import UserCreationForm

# for advanced signup form
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# for login required func
from django.contrib.auth.decorators import login_required

# for login required class
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {
        "form": form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page2.html'
