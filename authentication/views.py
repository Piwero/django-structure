from django.shortcuts import render

# Create your views here.

def signup(request):
    render(request, "registration/signup.html")