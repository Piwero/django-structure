from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# for login required func
from django.contrib.auth.decorators import login_required

# for login required class
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin






# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {
        "form": form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page2.html'
